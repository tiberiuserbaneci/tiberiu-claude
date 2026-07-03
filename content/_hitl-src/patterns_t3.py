#!/usr/bin/env python3
# TIER 3 - HOW REAL AGENTS ARE BUILT. forms: react trace / merge card / plan->run handoff /
# version iteration / 7-specialists-vs-giant / 5-layer stack / trigger control / same-model outcome.
import importlib.util, math
t=importlib.util.spec_from_file_location("B","/home/user/tiberiu-claude/content/_hitl-src/t3base.py")
B=importlib.util.module_from_spec(t); t.loader.exec_module(B)
CARD=B.CARD; INK=B.INK; MUT=B.MUT; DIM=B.DIM
ACC="204,120,92"
def head(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#FAFAF7">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')

# 1. react trace with feedback loop
def react():
    steps=["THINK","ACT","LOOK"]
    nodes=""
    for i,s in enumerate(steps):
        x=90+i*230
        nodes+=(f'<g transform="translate({x},120)"><rect x="-70" y="-40" width="140" height="80" rx="16" fill="#2a2723" stroke="rgba(204,120,92,.4)" stroke-width="1.5"/>'
          f'<text x="0" y="7" text-anchor="middle" font-family="DM Mono" font-size="18" letter-spacing="2" fill="#e9e3d7">{s}</text></g>')
        if i<2: nodes+=f'<path d="M{x+72} 120 H{x+156}" stroke="rgb({ACC})" stroke-width="3"/><path d="M{x+150} 113 L{x+162} 120 L{x+150} 127" fill="rgb({ACC})"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 38px">
      {head("Think. Act. Look. Repeat.","PATTERN 1 · ReAct")}
      <svg width="760" height="220" viewBox="0 0 760 220" style="width:100%">
        {nodes}
        <path d="M560 160 C560 210, 90 210, 90 165" fill="none" stroke="rgba(204,120,92,.55)" stroke-width="3" stroke-dasharray="3 8"/>
        <path d="M96 175 L90 160 L82 173" fill="rgb({ACC})"/>
        <text x="325" y="205" text-anchor="middle" font-family="DM Mono" font-size="13" fill="{MUT}">observe → reason again, until it is right</text>
      </svg></div>'''

# 2. merge card (code action, product-UI)
def codeact():
    files=[("auth/login.ts","+42 −8"),("api/session.ts","+15 −3"),("tests/login.test.ts","+30 −0")]
    rows="".join(f'<div style="display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid rgba(255,255,255,.06)"><span style="font-family:DM Mono;font-size:15px;color:#cfc9bd">{f}</span><span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">{d}</span></div>' for f,d in files)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 38px">
      {head("It does not describe fixes","PATTERN 2 · CodeAct")}
      <div style="background:#191614;border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:20px 22px">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px"><span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">fix/login-bug</span><span style="font-family:DM Mono;font-size:12px;color:{MUT}">3 files</span>
        <span style="margin-left:auto;display:flex;align-items:center;gap:7px;font-family:DM Mono;font-size:13px;color:#7fd39a"><span style="width:9px;height:9px;border-radius:50%;background:#7fd39a"></span>tests pass</span></div>
        {rows}
        <div style="display:flex;align-items:center;gap:12px;margin-top:16px"><div style="background:rgb({ACC});border-radius:10px;padding:11px 22px;font-family:DM Sans;font-weight:900;font-size:17px;color:#1a0f0a">Merged ✓</div><span style="font-family:DM Mono;font-size:13px;color:{MUT}">it acts on the repo, not on a suggestion</span></div></div></div>'''

# 3. plan -> run handoff (big brain plans, cheap runs)
def plan():
    steps=["pull leads","score fit","draft replies","queue sends"]
    chips="".join(f'<div style="display:flex;align-items:center;gap:10px;padding:8px 0"><span style="font-family:DM Mono;font-size:13px;color:rgb({ACC})">{i+1}</span><span style="font-family:DM Sans;font-size:16px;color:#d7d1c6">{s}</span></div>' for i,s in enumerate(steps))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 38px">
      {head("Plan big. Run cheap.","PATTERN 3 · PLANNER")}
      <div style="display:flex;align-items:stretch;gap:20px">
        <div style="flex:1;background:linear-gradient(160deg,rgba(204,120,92,.14),rgba(204,120,92,.04));border:1px solid rgba(204,120,92,.34);border-radius:16px;padding:18px 20px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC});margin-bottom:8px">PLAN · DEEP MODEL</div>
          <div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7;margin-bottom:8px">builds the plan once</div>{chips}
          <div style="font-family:DM Mono;font-size:12px;color:{MUT};margin-top:6px">~1 call · pennies</div></div>
        <div style="flex-shrink:0;align-self:center"><svg width="46" height="24" viewBox="0 0 46 24"><path d="M2 12 H36 M28 5 L44 12 L28 19" fill="none" stroke="rgb({ACC})" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <div style="flex:1;background:#221f1b;border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:18px 20px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:{MUT};margin-bottom:8px">RUN · LITE MODEL</div>
          <div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7;margin-bottom:10px">executes each step</div>
          {"".join(f'<div style="height:12px;border-radius:6px;background:rgba(204,120,92,{0.5-i*0.1});margin-bottom:8px"></div>' for i in range(4))}
          <div style="font-family:DM Mono;font-size:12px;color:{MUT};margin-top:2px">240 runs · cents total</div></div>
      </div></div>'''

# 4. version iteration v1->v3
def reflect():
    vs=[("v1","first attempt","discarded",False),("v2","self-critiqued","discarded",False),("v3","delivered to you","shipped",True)]
    rows=""
    for v,note,tag,on in vs:
        rows+=(f'<div style="display:flex;align-items:center;gap:18px;background:{"linear-gradient(160deg,rgba(204,120,92,.14),rgba(204,120,92,.04))" if on else "#221f1b"};border:1px solid {"rgba(204,120,92,.4)" if on else "rgba(255,255,255,.06)"};border-radius:14px;padding:16px 20px;margin-bottom:10px;{"box-shadow:0 0 34px rgba(204,120,92,.12)" if on else "opacity:.6"}">'
          f'<span style="font-family:DM Sans;font-weight:900;font-size:30px;color:{f"rgb({ACC})" if on else DIM};width:60px">{v}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:{800 if on else 500};font-size:19px;color:{"#FAFAF7" if on else "#9a9488"}">{note}</span>'
          f'<span style="font-family:DM Mono;font-size:13px;color:{f"rgb({ACC})" if on else DIM}">{tag}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {head("v1 never reaches you","PATTERN 4 · REFLECT")}{rows}</div>'''

# 5. seven specialists vs one giant
def multi():
    specs=["Research","Outbound","Deals","Content","Code","Publish","Legal"]
    chips="".join(f'<div style="background:#2a2723;border:1px solid rgba(204,120,92,.24);border-radius:10px;padding:10px 8px;text-align:center;font-family:DM Sans;font-weight:700;font-size:14px;color:#e9e3d7">{s}</div>' for s in specs)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 38px">
      {head("Seven specialists beat one giant","PATTERN 5 · MULTI")}
      <div style="display:flex;align-items:center;gap:30px">
        <div style="flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:10px">{chips}
          <div style="background:rgb({ACC});border-radius:10px;padding:10px 8px;text-align:center;font-family:DM Sans;font-weight:900;font-size:14px;color:#1a0f0a">+ orchestrator</div></div>
        <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:rgb({ACC})">&gt;</div>
        <div style="flex-shrink:0;width:150px;text-align:center;opacity:.55">
          <div style="width:120px;height:120px;margin:0 auto;border-radius:50%;background:#33302b;border:1px dashed {DIM};display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:700;font-size:15px;color:{MUT}">one<br>giant</div>
          <div style="font-family:DM Mono;font-size:12px;color:{DIM};margin-top:8px">jack of all</div></div>
      </div></div>'''

# 6. five-layer stack
def stack():
    layers=[("MULTI","specialists + orchestrator"),("REFLECT","v3, not v1"),("PLAN · RUN","deep plans, lite runs"),("CodeAct","acts, not describes"),("ReAct","think · act · look")]
    rows=""
    for i,(nm,sub) in enumerate(layers):
        w=100-i*7
        rows+=(f'<div style="width:{w}%;margin:0 auto 8px;background:linear-gradient(160deg,rgba(204,120,92,{0.20-i*0.03}),rgba(204,120,92,.04));border:1px solid rgba(204,120,92,.28);border-radius:12px;padding:13px 20px;display:flex;justify-content:space-between;align-items:center">'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:13px;color:{MUT}">{sub}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {head("Real systems stack all five","THE STACK")}{rows}</div>'''

# 7. trigger control - human on the trigger
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 42px">
      {head("A human on the trigger","PATTERN 6 · GATE")}
      <div style="display:flex;align-items:center;gap:36px;margin-top:6px">
        <div style="flex:1">
          <div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7;margin-bottom:12px">loaded &amp; ready</div>
          {"".join(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:10px"><span style="width:9px;height:9px;border-radius:50%;background:rgb({ACC})"></span><span style="font-family:DM Sans;font-size:17px;color:#cfc9bd">{x}</span></div>' for x in ["plan built","240 actions staged","all cited"])}
          <div style="font-family:DM Mono;font-size:13px;color:{MUT};margin-top:6px">safe until you fire it</div></div>
        <div style="flex-shrink:0;text-align:center">
          <div style="width:150px;height:150px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#e6b48f,rgb({ACC}) 55%,#7a4326);box-shadow:0 20px 40px rgba(0,0,0,.5),0 0 50px rgba(204,120,92,.3),inset 0 4px 6px rgba(255,255,255,.4);display:flex;align-items:center;justify-content:center">
            <svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="#2a160c" stroke-width="1.8"><path d="M6 12 v4 a5 5 0 0 0 9.6 2 v-6 M6 12 v-4 a1.6 1.6 0 0 1 3.2 0 M9.2 8 v-2 a1.6 1.6 0 0 1 3.2 0 v2 M12.4 7 a1.6 1.6 0 0 1 3.2 0 v5"/></svg></div>
          <div style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7;margin-top:12px">your finger</div></div>
      </div></div>'''

# 8. same model, different outcome
def operator():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {head("Same models. Different companies.","THE OPERATOR")}
      <div style="display:flex;align-items:center;justify-content:center;gap:20px;margin:6px 0 8px">
        <div style="background:#221f1b;border:1px solid rgba(255,255,255,.1);border-radius:14px;padding:16px 22px;font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">Same model</div>
      </div>
      <div style="display:flex;gap:20px;margin-top:10px">
        <div style="flex:1;background:#211d19;border:1px dashed rgba(255,255,255,.14);border-radius:16px;padding:20px;opacity:.7">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:{MUT};margin-bottom:8px">NO PATTERNS</div>
          <div style="font-family:DM Sans;font-weight:700;font-size:20px;color:#bdb7ab">still prompting</div>
          <div style="font-family:DM Sans;font-size:15px;color:{DIM};margin-top:6px">chat in, copy out, repeat</div></div>
        <div style="flex:1;background:linear-gradient(160deg,rgba(204,120,92,.16),rgba(204,120,92,.05));border:1px solid rgba(204,120,92,.4);border-radius:16px;padding:20px;box-shadow:0 0 40px rgba(204,120,92,.12)">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC});margin-bottom:8px">FIVE PATTERNS</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:20px;color:#FAFAF7">a shipping company</div>
          <div style="font-family:DM Sans;font-size:15px;color:rgb({ACC});margin-top:6px">systems that run without you</div></div>
      </div></div>'''

PANELS={"react":react(),"codeact":codeact(),"plan":plan(),"reflect":reflect(),
        "multi":multi(),"stack":stack(),"gate":gate(),"operator":operator()}
if __name__=="__main__":
    print("patterns t3:"); B.render("patterns",PANELS)
