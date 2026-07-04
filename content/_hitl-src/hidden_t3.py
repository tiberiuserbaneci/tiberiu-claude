#!/usr/bin/env python3
# TIER 3 - THE HIDDEN SKILLS. forms: myth strikeout / proposal deck / cited sheet /
# redlined contract / visuals grid(822) / connector map / answer-vs-execution / dual-speed gate.
import importlib.util, math
t=importlib.util.spec_from_file_location("B","/home/user/tiberiu-claude/content/_hitl-src/t3base.py")
B=importlib.util.module_from_spec(t); t.loader.exec_module(B)
CARD=B.CARD; INK=B.INK; MUT=B.MUT; DIM=B.DIM
ACC="212,162,127"
def head(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#FAFAF7">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')

# 1. myth strikeout
def myth():
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:40px 40px 42px;text-align:center">
      <div style="font-family:'DM Mono';font-size:14px;letter-spacing:.16em;color:{MUT};margin-bottom:18px">THE MYTH</div>
      <div style="position:relative;display:inline-block;margin-bottom:8px">
        <span style="font-family:'DM Sans';font-weight:900;font-size:58px;color:{DIM}">prompt engineering</span>
        <div style="position:absolute;left:-10px;right:-10px;top:52%;height:5px;background:rgb({ACC});border-radius:3px;transform:rotate(-3deg);box-shadow:0 0 20px rgba(212,162,127,.4)"></div></div>
      <div style="font-family:'DM Sans';font-weight:800;font-size:30px;color:#FAFAF7;margin-top:16px">was the tutorial level.</div>
      <div style="font-family:'DM Sans';font-size:19px;color:{MUT};margin-top:12px">re-wording a request is not a skill. What it can DO is.</div></div>'''

# 2. proposal deck auto-built, you add the price
def decks():
    slides="".join(f'<div style="width:150px;height:96px;border-radius:10px;background:linear-gradient(160deg,#302c27,#211d19);border:1px solid rgba(255,255,255,.08);padding:12px"><div style="height:8px;width:70%;background:rgba(212,162,127,.5);border-radius:4px"></div><div style="height:6px;width:90%;background:#3a352f;border-radius:3px;margin-top:8px"></div><div style="height:6px;width:60%;background:#3a352f;border-radius:3px;margin-top:6px"></div><div style="font-family:DM Mono;font-size:11px;color:{MUT};margin-top:14px">0{i+1}</div></div>' for i in range(3))
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 40px">
      {head("The proposal built itself","DECKS")}
      <div style="display:flex;gap:16px;margin-bottom:18px">{slides}</div>
      <div style="display:flex;align-items:center;gap:16px;background:linear-gradient(160deg,rgba(212,162,127,.14),rgba(212,162,127,.04));border:1px solid rgba(212,162,127,.34);border-radius:14px;padding:16px 20px;box-shadow:0 0 40px rgba(212,162,127,.1)">
        <div style="flex:1"><div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:{MUT}">SLIDE 04 · PRICING</div>
        <div style="font-family:DM Sans;font-weight:900;font-size:28px;color:#FAFAF7">$24,000 <span style="font-size:16px;color:rgb({ACC});font-weight:600">/ engagement</span></div></div>
        <div style="font-family:DM Mono;font-size:13px;color:rgb({ACC});border:1px solid rgba(212,162,127,.4);border-radius:999px;padding:7px 14px">you added this</div></div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:16px">structure, copy, layout: done. you set one number.</div></div>'''

# 3. cited sheet
def sheets():
    rows=[("Q3 revenue","$482,000","stripe · 2026-06-30"),("Runway","14 months","board deck · p.12"),("CAC","$310","hubspot · live"),("Churn","1.8%","analytics · 2026-06")]
    tr="".join(f'<div style="display:grid;grid-template-columns:1fr 150px 1fr;gap:12px;align-items:center;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
      f'<span style="font-family:DM Sans;font-size:17px;color:#d7d1c6">{a}</span>'
      f'<span style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7;text-align:right">{b}</span>'
      f'<span style="font-family:DM Mono;font-size:12px;color:rgb({ACC});text-align:right;display:flex;align-items:center;justify-content:flex-end;gap:6px"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.5"><path d="M9 18l6-6-6-6"/></svg>{c}</span></div>' for a,b,c in rows)
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 36px">
      {head("Numbers with receipts","SHEETS")}
      <div style="display:grid;grid-template-columns:1fr 150px 1fr;gap:12px;padding-bottom:8px;border-bottom:1px solid rgba(255,255,255,.12)">
        <span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:{DIM}">METRIC</span>
        <span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:{DIM};text-align:right">VALUE</span>
        <span style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:{DIM};text-align:right">SOURCE</span></div>{tr}</div>'''

# 4. redlined contract
def contracts():
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 38px">
      {head("The NDA came back redlined","CONTRACTS")}
      <div style="background:linear-gradient(160deg,#faf7f0,#efe7d8);border-radius:14px;padding:24px 28px;box-shadow:0 20px 40px rgba(0,0,0,.4)">
        <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:#8a745a;margin-bottom:14px">MUTUAL NDA · v2 (auto-redline)</div>
        <div style="font-family:DM Sans;font-size:17px;color:#2a2016;line-height:1.9">
          Confidential info shall be retained for <span style="text-decoration:line-through;color:#b04a2a">5 years</span> <span style="background:rgba(200,70,35,.14);color:#b04a2a;font-weight:700;padding:0 4px;border-radius:3px">3 years</span> from disclosure. Governing law: <span style="text-decoration:line-through;color:#b04a2a">Delaware</span> <span style="background:rgba(200,70,35,.14);color:#b04a2a;font-weight:700;padding:0 4px;border-radius:3px">England &amp; Wales</span>. Add <span style="background:rgba(60,120,90,.16);color:#3c785c;font-weight:700;padding:0 4px;border-radius:3px">mutual non-solicit, 12 mo</span>.</div>
      </div>
      <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:16px">3 risk edits flagged and drafted before it hit your inbox</div></div>'''

# 5. visuals grid, 822 count
def visuals():
    tiles=""
    pals=["rgba(212,162,127,","rgba(204,120,92,","rgba(180,140,110,"]
    for i in range(18):
        p=pals[i%3]; op=0.3+ (i%5)*0.12
        tiles+=f'<div style="padding-top:100%;border-radius:8px;background:{p}{op:.2f})"></div>'
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 38px;display:flex;align-items:center;gap:34px">
      <div style="flex:1;display:grid;grid-template-columns:repeat(6,1fr);gap:8px">{tiles}</div>
      <div style="flex-shrink:0;text-align:right">
        <div style="font-family:DM Sans;font-weight:900;font-size:70px;color:rgb({ACC});line-height:.9">822</div>
        <div style="font-family:DM Sans;font-weight:700;font-size:18px;color:#FAFAF7;margin-top:4px">assets shipped</div>
        <div style="font-family:DM Mono;font-size:14px;color:{MUT};margin-top:6px">zero design queue</div></div></div>'''

# 6. connector map - acts INSIDE the tools
def connectors():
    cx,cy=180,180; tools=[("Gmail",-90),("Notion",-18),("CRM",54),("Slack",126),("Drive",198)]; import math
    lines=""; nodes=""
    for nm,a in tools:
        x=cx+140*math.cos(math.radians(a)); y=cy+140*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#2a2723" stroke="rgba(255,255,255,.12)"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:30px 40px 34px;display:flex;align-items:center;gap:26px">
      <svg width="360" height="360" viewBox="0 0 360 360">
        <defs><radialGradient id="hub" cx="38%" cy="32%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4a2c"/></radialGradient>
        <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}<g filter="url(#hg)"><circle cx="{cx}" cy="{cy}" r="44" fill="url(#hub)"/></g>
        <text x="{cx}" y="{cy+5}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">ULTRON</text>{nodes}</svg>
      <div style="flex:1">
        <div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7;line-height:1.1">It acts inside your tools</div>
        <div style="font-family:DM Sans;font-size:19px;color:{MUT};margin-top:10px;line-height:1.45">Not a chat that tells you what to click. It moves the record, sends the mail, updates the deal.</div>
        <div style="font-family:DM Mono;font-size:14px;color:rgb({ACC});margin-top:16px">inside the tools, not beside them</div></div></div>'''

# 7. answer vs execution
def result():
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 40px">
      {head("Answers are cheap","EXECUTION IS THE PRODUCT")}
      <div style="display:flex;align-items:stretch;gap:20px;margin-top:6px">
        <div style="flex:1;background:#211d19;border:1px dashed rgba(255,255,255,.14);border-radius:16px;padding:20px;opacity:.7">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:{MUT};margin-bottom:10px">AN ANSWER</div>
          <div style="font-family:DM Sans;font-size:18px;color:#bdb7ab;line-height:1.4">"Here is how you could write a follow-up sequence..."</div>
          <div style="font-family:DM Mono;font-size:13px;color:{DIM};margin-top:14px">costs a fraction of a cent · does nothing</div></div>
        <div style="flex-shrink:0;align-self:center"><svg width="46" height="24" viewBox="0 0 46 24"><path d="M2 12 H36 M28 5 L44 12 L28 19" fill="none" stroke="rgb({ACC})" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <div style="flex:1;background:linear-gradient(160deg,rgba(212,162,127,.16),rgba(212,162,127,.05));border:1px solid rgba(212,162,127,.4);border-radius:16px;padding:20px;box-shadow:0 0 40px rgba(212,162,127,.12)">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC});margin-bottom:10px">EXECUTION</div>
          <div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7;line-height:1.4">240 sequences written, cited, queued, gated for your send.</div>
          <div style="font-family:DM Mono;font-size:13px;color:rgb({ACC});margin-top:14px">this is what you actually pay for</div></div>
      </div></div>'''

# 8. dual-speed gate
def gate():
    def dial(label,pct,col,note):
        import math
        a=180*pct/100; x=110+90*math.cos(math.radians(180-a)); y=120-90*math.sin(math.radians(180-a))
        return (f'<div style="flex:1;text-align:center"><svg width="220" height="140" viewBox="0 0 220 140">'
          f'<path d="M20 120 A90 90 0 0 1 200 120" fill="none" stroke="#2c2925" stroke-width="14" stroke-linecap="round"/>'
          f'<path d="M20 120 A90 90 0 0 1 200 120" fill="none" stroke="{col}" stroke-width="14" stroke-linecap="round" stroke-dasharray="{math.pi*90*pct/100:.0f} {math.pi*90:.0f}"/>'
          f'<line x1="110" y1="120" x2="{x:.0f}" y2="{y:.0f}" stroke="{col}" stroke-width="4" stroke-linecap="round"/><circle cx="110" cy="120" r="7" fill="{col}"/></svg>'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">{label}</div>'
          f'<div style="font-family:DM Mono;font-size:13px;color:{MUT}">{note}</div></div>')
    return f'''<div style="width:900px;{CARD};min-height:740px;display:flex;flex-direction:column;justify-content:space-between;padding:34px 40px 38px">
      {head("Executes fast. Sends at your speed.","DUAL SPEED")}
      <div style="display:flex;gap:20px;margin-top:6px">
        {dial("Execute",100,f"rgb({ACC})","machine speed")}
        {dial("Send",0,DIM,"your tap")}
      </div></div>'''

PANELS={"myth":myth(),"decks":decks(),"sheets":sheets(),"contracts":contracts(),
        "visuals":visuals(),"connectors":connectors(),"result":result(),"gate":gate()}
if __name__=="__main__":
    print("hidden t3:"); B.render("hidden",PANELS)
