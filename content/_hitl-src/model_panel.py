#!/usr/bin/env python3
# ONE dense reference panel (operator: "fa mi model urgent ... foloseste toata capacitatea sa faci
# design, nu spatiu negru cu doua cuvinte"). Packed, real design, no dead black space.
import importlib.util
t=importlib.util.spec_from_file_location("B","/home/user/tiberiu-claude/content/_hitl-src/t3base.py")
B=importlib.util.module_from_spec(t); t.loader.exec_module(B)
MUT=B.MUT; DIM=B.DIM; CARD=B.CARD; A="204,120,92"

# a real, dense "signal lead" panel: 4 detected signals (left, each a row with source+value+bar),
# a 2-lane race (you-vs-VC) with milestones, and a head-start stat block. Every zone carries content.
SIGNALS=[("Funding","Series A term sheet drafted","94"),
         ("Hiring","3 senior eng reqs opened","81"),
         ("Stack","Switched to enterprise Snowflake","76"),
         ("Intent","Booked 2 competitor demos","69")]
def bar(v):
    return (f'<div style="height:8px;border-radius:5px;background:#201c19;overflow:hidden;margin-top:7px">'
            f'<div style="height:100%;width:{v}%;border-radius:5px;background:linear-gradient(90deg,rgba({A},.5),rgb({A}))"></div></div>')
rows="".join(
  f'<div style="padding:14px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
  f'<div style="display:flex;align-items:baseline;justify-content:space-between">'
  f'<span style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{n}</span>'
  f'<span style="font-family:DM Mono;font-size:15px;color:rgb({A})">{v}%</span></div>'
  f'<div style="font-family:DM Sans;font-size:15px;color:{MUT};margin-top:3px">{d}</div>{bar(v)}</div>'
  for n,d,v in SIGNALS)

def model():
    tl="".join(
      f'<div style="flex:1;text-align:center"><div style="width:10px;height:10px;border-radius:50%;'
      f'background:{"rgb("+A+")" if on else "#3a352f"};margin:0 auto 8px;{"box-shadow:0 0 12px rgb("+A+")" if on else ""}"></div>'
      f'<div style="font-family:DM Mono;font-size:12px;color:{"rgb("+A+")" if on else DIM}">{d}</div></div>'
      for d,on in [("Mon",1),("Tue",1),("Wed",1),("Thu",1),("Fri",1),("Sat",1),("Sun",1)])
    return f'''<div style="width:900px;{CARD};padding:34px 38px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:22px">
        <span style="font-family:DM Sans;font-weight:800;font-size:27px;color:#FAFAF7">It saw the round first</span>
        <span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:rgb({A})">SIGNAL LEAD</span></div>
      <div style="display:grid;grid-template-columns:1fr 1px 380px;gap:30px">
        <div>
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{DIM};margin-bottom:4px">4 SIGNALS IT CAUGHT</div>
          {rows}</div>
        <div style="background:rgba(255,255,255,.08)"></div>
        <div style="display:flex;flex-direction:column">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{DIM};margin-bottom:14px">WHO KNEW FIRST</div>
          <div style="background:#201c19;border-radius:16px;padding:20px 22px;margin-bottom:14px">
            <div style="display:flex;align-items:center;gap:12px"><div style="width:12px;height:12px;border-radius:50%;background:rgb({A});box-shadow:0 0 14px rgb({A})"></div>
              <span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">You + Ultron</span></div>
            <div style="font-family:DM Mono;font-size:14px;color:rgb({A});margin-top:8px">Tue 09:12 &middot; overnight scan</div></div>
          <div style="background:#201c19;border-radius:16px;padding:20px 22px">
            <div style="display:flex;align-items:center;gap:12px"><div style="width:12px;height:12px;border-radius:50%;background:#4a453f"></div>
              <span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#b9b2a7">The VC</span></div>
            <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:8px">Fri 15:40 &middot; press release</div></div>
          <div style="margin-top:auto;padding-top:16px;text-align:center">
            <div style="font-family:DM Sans;font-weight:900;font-size:58px;color:rgb({A});line-height:1">3 days</div>
            <div style="font-family:DM Sans;font-size:17px;color:{MUT}">of head start, every round</div></div>
        </div>
      </div>
      <div style="margin-top:26px;padding-top:22px;border-top:1px solid rgba(255,255,255,.08)">
        <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:{DIM};margin-bottom:14px">IT SCANNED, EVERY NIGHT THIS WEEK</div>
        <div style="display:flex;gap:8px">{tl}</div></div></div>'''

if __name__=="__main__":
    B.render("_model",{"model":model()})
    print("model rendered -> models_clay/_model/model.png")
