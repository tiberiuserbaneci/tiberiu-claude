#!/usr/bin/env python3
# TIER 3 - THE CAROUSEL COMMAND. forms: week+revision timeline / interview->build / brand tokens /
# 10-slide filmstrip / caption-kit doc / stopwatch+coffee / review-tap-post flow / retainer->runway.
import importlib.util, math
t=importlib.util.spec_from_file_location("B","/home/user/tiberiu-claude/content/_hitl-src/t3base.py")
B=importlib.util.module_from_spec(t); t.loader.exec_module(B)
CARD=B.CARD; INK=B.INK; MUT=B.MUT; DIM=B.DIM
ACC="200,70,35"
def foot(items):
    chips="".join(f'<div style="flex:1;text-align:center;padding:18px 8px;background:#191614;border:1px solid rgba(255,255,255,.06);border-radius:14px"><div style="font-family:DM Sans;font-weight:900;font-size:28px;color:rgb({ACC});line-height:1">{b}</div><div style="font-family:DM Mono;font-size:11.5px;letter-spacing:.08em;color:{MUT};margin-top:7px">{s}</div></div>' for b,s in items)
    return f'<div style="display:flex;gap:12px;margin-top:22px">{chips}</div>'
def head(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#FAFAF7">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')

# 1. old bill: a week consumed + revision rounds
def oldbill():
    days="".join(f'<div style="flex:1;height:60px;border-radius:8px;background:#33302b;border:1px solid rgba(255,255,255,.05);display:flex;align-items:flex-end;justify-content:center;padding-bottom:6px;font-family:DM Mono;font-size:12px;color:{MUT}">D{i+1}</div>' for i in range(7))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {head("A week per deck","THE OLD BILL")}
      <div style="display:flex;gap:8px;margin-bottom:20px">{days}</div>
      <div style="display:flex;align-items:center;gap:14px">
        <div style="font-family:DM Mono;font-size:13px;color:{MUT}">+ revision rounds</div>
        <div style="display:flex;gap:8px">{"".join(f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC});border:1px solid rgba(200,70,35,.4);border-radius:999px;padding:5px 12px">round {i+1}</span>' for i in range(3))}</div>
      </div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:18px">seven days and three back-and-forths for one carousel</div>
      {foot([("7","DAYS GONE"),("3","REVISION ROUNDS"),("1","CAROUSEL")])}</div>'''

# 2. interview -> build
def command():
    qa=[("Ultron","Who is this for, and what is the one takeaway?"),("You","Founders. Loops beat prompts."),("Ultron","Tone, length, keyword?"),("You","Operator. 10 slides. BUILDER.")]
    rows=""
    for who,txt in qa:
        me=who=="You"
        rows+=(f'<div style="display:flex;{"justify-content:flex-end" if me else ""};margin-bottom:10px">'
          f'<div style="max-width:74%;background:{f"rgb({ACC})" if me else "#2a2723"};color:{"#1a0f0a" if me else "#e9e3d7"};border-radius:14px;padding:11px 16px;font-family:DM Sans;font-size:16px">{txt}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 38px">
      {head("It interviews me, then builds","THE COMMAND")}
      {rows}
      <div style="display:flex;align-items:center;gap:12px;margin-top:8px;background:#191614;border:1px solid rgba(200,70,35,.24);border-radius:12px;padding:14px 18px">
        <svg width="20" height="20" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" fill="none" stroke="rgb({ACC})" stroke-width="2.5" stroke-dasharray="30 12"/></svg>
        <span style="font-family:DM Mono;font-size:14px;color:#e9e3d7">building 10 slides · your voice · your tokens...</span></div>
      {foot([("4","QUESTIONS"),("10","SLIDES OUT"),("0","BLANK PAGE")])}</div>'''

# 3. brand tokens
def visuals():
    sw=[("#191919","slate"),("#c84623","book"),("#d4a27f","kraft"),("#faf af7","ivory")]
    sw=[("#191919","slate"),("#c84623","book"),("#d4a27f","kraft"),("#fafaf7","ivory")]
    chips="".join(f'<div style="text-align:center"><div style="width:80px;height:80px;border-radius:16px;background:{h};border:1px solid rgba(255,255,255,.12)"></div><div style="font-family:DM Mono;font-size:12px;color:{MUT};margin-top:8px">{nm}</div></div>' for h,nm in sw)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {head("My tokens, my type","NO TEMPLATE SMELL")}
      <div style="display:flex;gap:20px;margin-bottom:22px">{chips}</div>
      <div style="display:flex;gap:30px;align-items:flex-end;border-top:1px solid rgba(255,255,255,.08);padding-top:20px">
        <div><div style="font-family:'DM Sans';font-weight:900;font-size:40px;color:#FAFAF7">DM Sans</div><div style="font-family:DM Mono;font-size:12px;color:{MUT}">headlines · 900/800</div></div>
        <div><div style="font-family:'DM Mono';font-weight:500;font-size:30px;color:#e9e3d7">DM Mono</div><div style="font-family:DM Mono;font-size:12px;color:{MUT}">labels · meta</div></div></div>
      {foot([("4","BRAND COLORS"),("2","TYPEFACES"),("0","TEMPLATE SMELL")])}</div>'''

# 4. 10-slide filmstrip on proven bones
def slides():
    frames="".join(f'<div style="flex-shrink:0;width:66px;height:96px;border-radius:8px;background:linear-gradient(160deg,#302c27,#211d19);border:1px solid rgba(255,255,255,.08);padding:8px"><div style="height:6px;width:70%;background:rgba(200,70,35,.5);border-radius:3px"></div><div style="height:4px;width:90%;background:#3a352f;border-radius:2px;margin-top:6px"></div><div style="height:4px;width:60%;background:#3a352f;border-radius:2px;margin-top:4px"></div><div style="font-family:DM Mono;font-size:9px;color:{MUT};margin-top:auto;position:relative;top:44px">{i+1:02d}</div></div>' for i in range(10))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      {head("Ten pages, proven bones","THE SLIDES")}
      <div style="display:flex;gap:8px;overflow:hidden;padding-bottom:8px">{frames}</div>
      <div style="height:3px;background:linear-gradient(90deg,rgb({ACC}),transparent);border-radius:2px;margin-top:6px"></div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:14px">cover · hook · proof · steps · CTA: the structure that already works</div>
      {foot([("10","PAGES"),("5","PROVEN BEATS"),("1","STRUCTURE")])}</div>'''

# 5. caption kit doc
def captions():
    def sect(lbl,body): return f'<div style="margin-bottom:14px"><div style="font-family:DM Mono;font-size:11px;letter-spacing:.14em;color:rgb({ACC});margin-bottom:6px">{lbl}</div><div style="font-family:DM Sans;font-size:16px;color:#d7d1c6;line-height:1.4">{body}</div></div>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {head("The caption kit writes itself in","CAPTIONS")}
      <div style="background:#191614;border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:20px 24px">
        {sect("CAPTION","Comment BUILDER for the carousel command. Save this so you do not lose it.")}
        {sect("FIRST COMMENT","Drop BUILDER below and I will send it, I read every comment.")}
        {sect("HASHTAGS","#claude #ai #founder #startup #buildinpublic")}
      </div>
      {foot([("3","BLOCKS"),("BUILDER","THE KEYWORD"),("0","COPY LEFT")])}</div>'''

# 6. stopwatch + coffee
def clock():
    import math
    pct=0.55; a=360*pct; x=110+80*math.sin(math.radians(a)); y=110-80*math.cos(math.radians(a))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 40px">
      <div style="display:flex;align-items:center;gap:40px">
      <svg width="220" height="220" viewBox="0 0 220 220">
        <circle cx="110" cy="110" r="80" fill="#1a1815" stroke="#2c2925" stroke-width="10"/>
        <path d="M110 30 A80 80 0 {1 if pct>0.5 else 0} 1 {x:.0f} {y:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="10" stroke-linecap="round"/>
        <rect x="102" y="16" width="16" height="10" rx="3" fill="rgb({ACC})"/>
        <text x="110" y="104" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="42" fill="#FAFAF7">6</text>
        <text x="110" y="132" text-anchor="middle" font-family="DM Mono" font-size="14" fill="rgb({ACC})">MINUTES</text></svg>
      <div style="flex:1">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:10px">
          <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="1.8"><path d="M18 8h1a3 3 0 0 1 0 6h-1"/><path d="M3 8h15v5a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5Z"/><path d="M6 2v2M10 2v2M14 2v2"/></svg>
          <span style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7">Coffee brewed.</span></div>
        <div style="font-family:DM Sans;font-size:20px;color:{MUT};line-height:1.4">Deck done before the cup was cool. Six minutes, ten slides, ready for one tap.</div></div></div>
      {foot([("6 min","START TO DONE"),("10","SLIDES"),("1","COFFEE")])}</div>'''

# 7. review -> tap -> post flow
def gate():
    steps=[("Review","scan 10 slides",False),("Your tap","approve",True),("Posted","10:00 local",False)]
    lock=f'<svg width="32" height="32" viewBox="0 0 24 24"><path d="M6 11V8a6 6 0 0 1 12 0v3" fill="none" stroke="rgb({ACC})" stroke-width="2"/><rect x="4" y="11" width="16" height="10" rx="2.5" fill="none" stroke="rgb({ACC})" stroke-width="2"/></svg>'
    blk=f'<div style="width:26px;height:26px;border-radius:7px;background:{DIM}"></div>'
    nodes=""
    for i,(nm,sub,on) in enumerate(steps):
        cbg="linear-gradient(160deg,rgba(200,70,35,.18),rgba(200,70,35,.05))" if on else "#221f1b"
        cbd="rgba(200,70,35,.4)" if on else "rgba(255,255,255,.08)"
        csh="box-shadow:0 0 34px rgba(200,70,35,.16)" if on else ""
        ic=lock if on else blk
        tc="#FAFAF7" if on else "#bdb7ab"
        nodes+=(f'<div style="flex:1;text-align:center">'
          f'<div style="width:70px;height:70px;margin:0 auto 12px;border-radius:20px;background:{cbg};border:1px solid {cbd};display:flex;align-items:center;justify-content:center;{csh}">{ic}</div>'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:19px;color:{tc}">{nm}</div>'
          f'<div style="font-family:DM Mono;font-size:12px;color:{MUT};margin-top:2px">{sub}</div></div>')
        if i<2: nodes+=f'<div style="flex-shrink:0;align-self:flex-start;margin-top:24px"><svg width="46" height="22" viewBox="0 0 46 22"><path d="M2 11 H36 M28 4 L44 11 L28 18" fill="none" stroke="{DIM}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></div>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 42px">
      {head("One review. One tap. Then it posts.","GATED PUBLISH")}
      <div style="display:flex;align-items:flex-start;gap:6px;margin-top:12px">{nodes}</div>
      {foot([("1","YOUR TAP"),("10:00","LOCAL POST"),("0","AUTO-SEND")])}</div>'''

# 8. retainer -> runway
def math_():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 42px">
      {head("Retainer money became runway","THE MATH")}
      <div style="display:flex;align-items:center;gap:20px;margin-top:10px">
        <div style="flex-shrink:0;text-align:center">
          <div style="font-family:DM Sans;font-weight:900;font-size:34px;color:{DIM}">$6,000</div>
          <div style="font-family:DM Sans;font-size:15px;color:{MUT};margin-top:4px">agency / mo</div></div>
        <svg width="70" height="40" viewBox="0 0 70 40" style="flex-shrink:0"><path d="M4 20 H52 M42 9 L60 20 L42 31" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <div style="flex:1;background:linear-gradient(160deg,rgba(200,70,35,.16),rgba(200,70,35,.05));border:1px solid rgba(200,70,35,.4);border-radius:18px;padding:22px 26px;box-shadow:0 0 44px rgba(200,70,35,.12)">
          <div style="font-family:DM Sans;font-weight:900;font-size:44px;color:#FAFAF7;line-height:1">+3.2 months</div>
          <div style="font-family:DM Sans;font-size:17px;color:rgb({ACC});margin-top:4px">of runway, per year kept</div></div>
      </div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:20px">the desk runs on cents; the retainer stays in the bank</div>
      {foot([("$6k","AGENCY / MO"),("cents","THE DESK"),("+3.2mo","RUNWAY / YR")])}</div>'''

PANELS={"oldbill":oldbill(),"command":command(),"visuals":visuals(),"slides":slides(),
        "captions":captions(),"clock":clock(),"gate":gate(),"math":math_()}
if __name__=="__main__":
    print("carouselcmd t3:"); B.render("carouselcmd",PANELS)
