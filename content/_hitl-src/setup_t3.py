#!/usr/bin/env python3
# TIER 3 - 60 MINUTES TO AN OPERATOR. forms: stack-connect / business profile fill / voice waveform /
# permission toggles / first-task done / morning digest / wk1-vs-wk2 delta / one-hour->forever.
import importlib.util, math
t=importlib.util.spec_from_file_location("B","/home/user/tiberiu-claude/content/_hitl-src/t3base.py")
B=importlib.util.module_from_spec(t); t.loader.exec_module(B)
CARD=B.CARD; INK=B.INK; MUT=B.MUT; DIM=B.DIM
ACC="212,162,127"
def mh(rng,t,tag):
    return (f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:18px">'
      f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.12em;color:rgb({ACC});border:1px solid rgba(212,162,127,.4);border-radius:8px;padding:5px 10px">MIN {rng}</span>'
      f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:25px;color:#FAFAF7">{t}</span>'
      f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.12em;color:{MUT};margin-left:auto">{tag}</span></div>')

# 1. stack connects
def connect():
    tools=["Gmail","Calendar","CRM","Drive"]
    rows="".join(f'<div style="display:flex;align-items:center;gap:14px;padding:11px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
      f'<div style="width:40px;height:40px;border-radius:11px;background:#2a2723;border:1px solid rgba(255,255,255,.08)"></div>'
      f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:18px;color:#e9e3d7">{t}</span>'
      f'<span style="display:flex;align-items:center;gap:7px;font-family:DM Mono;font-size:13px;color:#7fd39a"><svg width="18" height="18" viewBox="0 0 24 24"><path d="M6 12.5l3.2 3.2L17 8.5" fill="none" stroke="#7fd39a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>connected</span></div>' for t in tools)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {mh("0-10","The stack clicks in","CONNECT")}{rows}
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:14px">four tools live in ten minutes, one auth each</div></div>'''

# 2. business profile filling in
def init():
    fields=[("Company","Ultron · GTM OS",True),("ICP","founders, 2-50, US/UK",True),("Offer","AI operator, cents/mo",True),("Voice","operator, no hedging","typing")]
    rows=""
    for k,v,st in fields:
        typing=st=="typing"
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
          f'<span style="width:110px;font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:{MUT}">{k}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:{700 if not typing else 600};font-size:18px;color:{"#FAFAF7" if not typing else "#cfc9bd"}">{v}{"<span style=color:rgb("+ACC+")>|</span>" if typing else ""}</span>'
          f'<span style="font-family:DM Mono;font-size:12px;color:{"#7fd39a" if not typing else "rgb("+ACC+")"}">{"saved" if not typing else "..."}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {mh("10-20","It learns my business","INIT")}{rows}
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:14px">one interview writes the memory every agent reads</div></div>'''

# 3. voice waveform
def voice():
    import math
    bars="".join(f'<rect x="{i*20}" y="{60-abs(math.sin(i*0.7))*50-6:.0f}" width="10" height="{abs(math.sin(i*0.7))*100+12:.0f}" rx="5" fill="rgb({ACC})" opacity="{0.5+abs(math.sin(i*0.7))*0.5:.2f}"/>' for i in range(34))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {mh("20-30","It sounds like me","VOICE")}
      <svg width="700" height="130" viewBox="0 0 700 130" style="width:100%;margin:6px 0">{bars}</svg>
      <div style="display:flex;align-items:center;gap:14px;margin-top:10px">
        <div style="display:flex;align-items:center;gap:8px;background:rgba(212,162,127,.10);border:1px solid rgba(212,162,127,.3);border-radius:999px;padding:9px 16px"><span style="width:9px;height:9px;border-radius:50%;background:#7fd39a"></span><span style="font-family:DM Sans;font-weight:700;font-size:15px;color:#e9e3d7">voice matched</span></div>
        <span style="font-family:DM Mono;font-size:14px;color:{MUT}">short lines, operator cadence, your phrases</span></div></div>'''

# 4. permission toggles - the handbrake
def permissions():
    perms=[("Send email","ask first"),("Post content","ask first"),("Spend budget","ask first"),("Read data","auto")]
    rows=""
    for nm,mode in perms:
        ask=mode=="ask first"
        knob="right:4px" if ask else "left:4px"
        tbg=f"rgba(212,162,127,.5)" if ask else "#33302b"
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:18px;color:#e9e3d7">{nm}</span>'
          f'<span style="font-family:DM Mono;font-size:13px;color:{f"rgb({ACC})" if ask else MUT};width:80px;text-align:right">{mode}</span>'
          f'<div style="position:relative;width:52px;height:28px;border-radius:14px;background:{tbg}"><div style="position:absolute;{knob};top:4px;width:20px;height:20px;border-radius:50%;background:#faf7f0"></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {mh("30-40","The handbrake is set","PERMISSIONS")}{rows}
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:14px">every outward move waits for your tap; reads run free</div></div>'''

# 5. first task done
def firsttask():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {mh("40-50","First job, done","FIRST TASK")}
      <div style="background:#191614;border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:20px 22px">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px">
          <svg width="26" height="26" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="rgba(127,211,154,.14)"/><path d="M7 12.5l3.2 3.2L17 8.5" fill="none" stroke="#7fd39a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
          <span style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">Draft 12 follow-ups</span>
          <span style="margin-left:auto;font-family:DM Mono;font-size:13px;color:#7fd39a">done · 40s</span></div>
        {"".join(f'<div style="display:flex;gap:10px;align-items:center;padding:7px 0"><span style="width:6px;height:6px;border-radius:50%;background:rgb({ACC})"></span><span style="font-family:DM Sans;font-size:16px;color:#cfc9bd">follow-up to {n}, cited, under 62 words</span></div>' for n in ["Acme","Globex","Northwind"])}
        <div style="height:8px;border-radius:4px;background:#2c2925;margin-top:12px;overflow:hidden"><div style="height:100%;width:100%;background:rgb({ACC})"></div></div></div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:14px">first real output before the hour is up</div></div>'''

# 6. morning digest
def digest():
    def sec(lbl,items):
        li="".join(f'<div style="font-family:DM Sans;font-size:15px;color:#cfc9bd;padding:4px 0">· {x}</div>' for x in items)
        return f'<div style="flex:1"><div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC});margin-bottom:8px">{lbl}</div>{li}</div>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 38px">
      {mh("50-60","The digest lands","DIGEST")}
      <div style="background:#191614;border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:22px 24px">
        <div style="display:flex;justify-content:space-between;margin-bottom:16px"><span style="font-family:DM Sans;font-weight:900;font-size:22px;color:#FAFAF7">Morning brief</span><span style="font-family:DM Mono;font-size:13px;color:{MUT}">one page · 4 min</span></div>
        <div style="display:flex;gap:24px">
          {sec("MARKET",["2 rivals moved","1 funding round"])}
          {sec("CONTENT",["3 posts drafted","1 crowned"])}
          {sec("PIPELINE",["4 replies in","$90k advanced"])}
        </div></div></div>'''

# 7. wk1 vs wk2 delta
def compound():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {mh("W2","Smarter than week one","THE COMPOUND")}
      <div style="display:flex;align-items:flex-end;gap:40px;height:210px;padding:0 40px 0 20px">
        <div style="flex:1;text-align:center;display:flex;flex-direction:column;justify-content:flex-end;height:100%">
          <div style="font-family:DM Sans;font-weight:900;font-size:26px;color:{MUT}">week 1</div>
          <div style="width:100%;background:#3a352f;border-radius:12px 12px 0 0;height:90px;margin-top:8px"></div>
          <div style="font-family:DM Sans;font-size:15px;color:{MUT};margin-top:8px">learns your patterns</div></div>
        <div style="flex-shrink:0;align-self:center"><svg width="40" height="30" viewBox="0 0 40 30"><path d="M4 22 L20 6 L36 22" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <div style="flex:1;text-align:center;display:flex;flex-direction:column;justify-content:flex-end;height:100%">
          <div style="font-family:DM Sans;font-weight:900;font-size:26px;color:rgb({ACC})">week 2</div>
          <div style="width:100%;background:linear-gradient(180deg,#e6b48f,rgb({ACC}));border-radius:12px 12px 0 0;height:180px;margin-top:8px;box-shadow:0 0 34px rgba(212,162,127,.18)"></div>
          <div style="font-family:DM Sans;font-size:15px;color:#e9e3d7;margin-top:8px">anticipates them</div></div>
      </div></div>'''

# 8. one hour -> forever
def operator():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 44px;display:flex;align-items:center;gap:34px">
      <div style="flex-shrink:0;text-align:center">
        <div style="width:150px;height:150px;border-radius:50%;background:linear-gradient(160deg,#2a2723,#171512);border:2px solid rgba(212,162,127,.4);display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 16px 30px rgba(0,0,0,.5)">
          <span style="font-family:DM Sans;font-weight:900;font-size:40px;color:#FAFAF7">1</span>
          <span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb({ACC})">HOUR · ONCE</span></div></div>
      <svg width="70" height="40" viewBox="0 0 70 40" style="flex-shrink:0"><path d="M4 20 H52 M42 9 L60 20 L42 31" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <div style="flex:1">
        <div style="font-family:'DM Sans';font-weight:900;font-size:60px;color:rgb({ACC});line-height:.9">∞</div>
        <div style="font-family:'DM Sans';font-weight:900;font-size:30px;color:#FAFAF7;margin-top:8px">leverage, forever</div>
        <div style="font-family:'DM Sans';font-size:18px;color:{MUT};margin-top:8px">one hour of setup buys a coworker that compounds every day after</div></div></div>'''

PANELS={"connect":connect(),"init":init(),"voice":voice(),"permissions":permissions(),
        "firsttask":firsttask(),"digest":digest(),"compound":compound(),"operator":operator()}
if __name__=="__main__":
    print("setup t3:"); B.render("setup",PANELS)
