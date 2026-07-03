#!/usr/bin/env python3
# TIER 3 - 5 SIGNS YOU NEED AI NOW. five distinct diagnostic visuals + verdict + leak-plug + veto.
# forms: duplication row / manual transfer / bottleneck queue / lead-cooling gradient /
#        month-end calendar drain / verdict tally / leak plug / veto card.
import importlib.util
t=importlib.util.spec_from_file_location("B","/home/user/tiberiu-claude/content/_hitl-src/t3base.py")
B=importlib.util.module_from_spec(t); t.loader.exec_module(B)
CARD=B.CARD; INK=B.INK; MUT=B.MUT; DIM=B.DIM
ACC="204,120,92"
def qhead(q,t):
    return (f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:18px">'
      f'<span style="font-family:\'DM Sans\';font-weight:900;font-size:24px;color:rgb({ACC})">{q}</span>'
      f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:25px;color:#FAFAF7">{t}</span></div>')

# 1. duplication row + x40/wk counter
def sign1():
    chips="".join(f'<div style="width:150px;flex-shrink:0;background:#2a2723;border:1px solid rgba(255,255,255,.08);border-radius:12px;padding:12px 14px;opacity:{1-i*0.16}"><div style="font-family:DM Mono;font-size:12px;color:{MUT}">Re: pricing</div><div style="font-family:DM Sans;font-size:14px;color:#cfc9bd;margin-top:4px">"Here is how it..."</div></div>' for i in range(4))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {qhead("Q1","Same answer, on repeat")}
      <div style="display:flex;align-items:center;gap:26px">
        <div style="display:flex;gap:12px;overflow:hidden;flex:1">{chips}</div>
        <div style="flex-shrink:0;text-align:right"><div style="font-family:DM Sans;font-weight:900;font-size:70px;color:rgb({ACC});line-height:.9">40<span style="font-size:30px">×</span></div><div style="font-family:DM Mono;font-size:14px;color:{MUT}">every week</div></div>
      </div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:22px">if you type the same reply again and again → that is a skill, not a job</div></div>'''

# 2. manual transfer between two sheets
def sign2():
    def grid(active):
        cells="".join(f'<div style="height:16px;border-radius:3px;background:{("rgba(204,120,92,.5)" if (active and i==4) else "#2f2c27")}"></div>' for i in range(9))
        return f'<div style="display:grid;grid-template-columns:repeat(3,44px);gap:5px">{cells}</div>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 42px">
      {qhead("Q2","Payroll moves data by hand")}
      <div style="display:flex;align-items:center;justify-content:center;gap:30px;margin:10px 0">
        <div style="text-align:center"><div style="font-family:DM Mono;font-size:12px;color:{MUT};margin-bottom:8px">SOURCE</div>{grid(True)}</div>
        <div style="text-align:center">
          <svg width="90" height="50" viewBox="0 0 90 50"><path d="M6 25 H70 M60 14 L78 25 L60 36" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <div style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">copy · paste</div></div>
        <div style="text-align:center"><div style="font-family:DM Mono;font-size:12px;color:{MUT};margin-bottom:8px">SHEET</div>{grid(False)}</div>
        <div style="flex-shrink:0;margin-left:10px"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="1.8"><path d="M6 12 v-4 a1.6 1.6 0 0 1 3.2 0 M9.2 8 v-2 a1.6 1.6 0 0 1 3.2 0 v2 M12.4 7 a1.6 1.6 0 0 1 3.2 0 v5 M6 12 v4 a5 5 0 0 0 9.6 2 v-6"/></svg></div>
      </div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};text-align:center;margin-top:14px">a human moving rows between tabs is an integration waiting to happen</div></div>'''

# 3. bottleneck queue backing up behind your thumbs
def sign3():
    q="".join(f'<div style="width:120px;height:34px;border-radius:8px;background:#2c2925;border:1px solid rgba(255,255,255,.07);opacity:{1-i*0.12};display:flex;align-items:center;padding-left:12px;font-family:DM Sans;font-size:13px;color:{MUT}">task {i+1}</div>' for i in range(5))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 42px">
      {qhead("Q3","Work queues behind you")}
      <div style="display:flex;align-items:center;gap:16px;margin:8px 0">
        <div style="display:flex;flex-direction:column;gap:8px;flex:1">{q}</div>
        <div style="flex-shrink:0;width:20px;height:150px;background:linear-gradient(180deg,rgb({ACC}),#7a4326);border-radius:6px;box-shadow:0 0 30px rgba(204,120,92,.3)"></div>
        <div style="flex-shrink:0;width:130px;text-align:center">
          <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="1.8"><path d="M9 11V6a2 2 0 0 1 4 0v5 M13 11V4a2 2 0 0 1 4 0v9 a6 6 0 0 1-6 6 h-1 a5 5 0 0 1-4-2 l-3-4 a2 2 0 0 1 3-2 l2 2"/></svg>
          <div style="font-family:DM Sans;font-weight:800;font-size:17px;color:#FAFAF7;margin-top:6px">your thumbs</div>
          <div style="font-family:DM Mono;font-size:12px;color:{MUT}">the bottleneck</div></div>
      </div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};text-align:center">if everything waits on your two hands, your hands are the cap</div></div>'''

# 4. lead cooling gradient
def sign4():
    dots="".join(f'<circle cx="{60+i*88}" cy="40" r="{20-i*1.5}" fill="rgb({",".join(str(int(v)) for v in (204-(204-95)*i/7,120-(120-100)*i/7,92-(92-120)*i/7))})" opacity="{1-i*0.08}"/>' for i in range(8))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 42px">
      {qhead("Q4","Leads cool in your inbox")}
      <svg width="800" height="90" viewBox="0 0 800 90" style="width:100%">{dots}</svg>
      <div style="display:flex;justify-content:space-between;margin-top:6px">
        <div style="font-family:DM Sans;font-weight:800;font-size:18px;color:rgb({ACC})">hot · just replied</div>
        <div style="font-family:DM Sans;font-weight:700;font-size:18px;color:{DIM}">cold · forgotten</div></div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};text-align:center;margin-top:18px">every hour unanswered halves the odds; the inbox is where deals go to freeze</div></div>'''

# 5. month-end calendar drain (last 3 days lost)
def sign5():
    cells=""
    for i in range(30):
        lost=i>=27
        cells+=f'<div style="width:100%;padding-top:100%;position:relative;border-radius:5px;background:{("rgb("+ACC+")" if lost else "#2c2925")};{"box-shadow:0 0 14px rgba(204,120,92,.4)" if lost else ""}"></div>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {qhead("Q5","Month-end eats three days")}
      <div style="display:grid;grid-template-columns:repeat(15,1fr);gap:7px;margin:8px 0 14px">{cells}</div>
      <div style="display:flex;align-items:center;gap:12px">
        <span style="width:16px;height:16px;border-radius:4px;background:rgb({ACC})"></span>
        <span style="font-family:DM Sans;font-size:17px;color:#e9e3d7">3 days gone to reconciliation, every single month</span></div></div>'''

# 6. verdict tally: 3 of 5 -> you are the system
def test():
    boxes=""
    check=f'<svg width="20" height="20" viewBox="0 0 24 24"><path d="M6 12.5l3.2 3.2L17 8.5" fill="none" stroke="rgb({ACC})" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    for i in range(5):
        on=i<3
        bxbg="rgba(204,120,92,.18)" if on else "transparent"
        bxbd=f"rgb({ACC})" if on else DIM
        mark=check if on else ""
        txtc="#e9e3d7" if on else DIM
        boxes+=(f'<div style="display:flex;align-items:center;gap:12px">'
          f'<div style="width:34px;height:34px;border-radius:9px;background:{bxbg};border:2px solid {bxbd};display:flex;align-items:center;justify-content:center">{mark}</div>'
          f'<span style="font-family:DM Sans;font-size:17px;color:{txtc}">Sign {i+1}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 42px;display:flex;align-items:center;gap:40px">
      <div style="display:flex;flex-direction:column;gap:14px">{boxes}</div>
      <div style="width:1px;height:210px;background:rgba(255,255,255,.10)"></div>
      <div style="flex:1">
        <div style="font-family:DM Sans;font-weight:900;font-size:60px;color:rgb({ACC});line-height:.9">3<span style="font-size:30px;color:{MUT}"> / 5</span></div>
        <div style="font-family:DM Sans;font-weight:900;font-size:34px;color:#FAFAF7;margin-top:14px;line-height:1.05">You are the system.</div>
        <div style="font-family:DM Sans;font-size:18px;color:{MUT};margin-top:8px">three yes or more and the manual layer is you</div></div></div>'''

# 7. leak plug: one fix stops the worst drain
def fix():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 44px">
      {qhead("→","Plug the worst leak first")}
      <div style="display:flex;align-items:center;gap:20px;margin:10px 0">
        <div style="flex:1;height:26px;border-radius:13px;background:linear-gradient(90deg,#2c2925,#2c2925);position:relative;overflow:visible">
          <div style="position:absolute;left:0;top:0;bottom:0;width:64%;border-radius:13px;background:rgb({ACC})"></div>
          <div style="position:absolute;left:64%;top:-6px;width:38px;height:38px;border-radius:10px;background:linear-gradient(160deg,#e6b48f,rgb({ACC}));box-shadow:0 6px 16px rgba(0,0,0,.5),0 0 24px rgba(204,120,92,.4);display:flex;align-items:center;justify-content:center;transform:translateX(-50%)">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.4"><path d="M14 4l6 6-9 9H5v-6z"/></svg></div>
        </div>
      </div>
      <div style="display:flex;gap:20px;margin-top:22px">
        <div style="flex:1;background:#191614;border:1px solid rgba(255,255,255,.07);border-radius:12px;padding:16px 18px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:{MUT};margin-bottom:6px">ONE SENTENCE</div>
          <div style="font-family:DM Sans;font-size:18px;color:#e9e3d7">"Draft every follow-up the moment a lead replies."</div></div>
        <div style="flex-shrink:0;text-align:center;align-self:center">
          <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:rgb({ACC})">1</div>
          <div style="font-family:DM Mono;font-size:13px;color:{MUT}">leak, sealed</div></div>
      </div></div>'''

# 8. veto card: action pending your approval
def gate():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 42px">
      {qhead("✓","Automate work. Keep the veto.")}
      <div style="background:#191614;border:1px solid rgba(204,120,92,.28);border-radius:16px;padding:22px 24px;box-shadow:inset 0 2px 3px rgba(255,255,255,.05)">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">
          <div><div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">Send 240 follow-ups</div>
          <div style="font-family:DM Sans;font-size:15px;color:{MUT}">drafted · cited · ready</div></div>
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({ACC});border:1px solid rgba(204,120,92,.4);border-radius:999px;padding:7px 15px">PENDING YOU</div></div>
        <div style="display:flex;gap:14px">
          <div style="flex:1;background:rgb({ACC});border-radius:12px;padding:15px;text-align:center;font-family:DM Sans;font-weight:900;font-size:19px;color:#1a0f0a;box-shadow:0 0 30px rgba(204,120,92,.3)">Approve ✓</div>
          <div style="flex:1;background:transparent;border:1.5px solid {DIM};border-radius:12px;padding:15px;text-align:center;font-family:DM Sans;font-weight:800;font-size:19px;color:{MUT}">Hold</div></div>
      </div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};text-align:center;margin-top:18px">it does the work at machine speed and stops at your one tap</div></div>'''

PANELS={"sign1":sign1(),"sign2":sign2(),"sign3":sign3(),"sign4":sign4(),"sign5":sign5(),
        "test":test(),"fix":fix(),"gate":gate()}
if __name__=="__main__":
    print("fivesigns t3:"); B.render("fivesigns",PANELS)
