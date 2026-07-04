#!/usr/bin/env python3
# TIER 3 - THE NIGHT SHIFT (s2src37). 8 unique hand-built coded scenes, one overnight Ultron run.
# Each panel = a clean rounded CARD/CARDIV, htitle + one cap, no stat-chip strips, no cuts/walls.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def ihead(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. KICKOFF (IVORY) - the single plain-English instruction typed before bed + clock + crescent moon
def kickoff():
    return f'''<div style="width:900px;{CARDIV};padding:38px 42px 34px">
      {ihead("One line before bed","THE INSTRUCTION")}
      <div style="background:linear-gradient(160deg,#fffdf9,#f3ead9);border:1px solid rgba(150,90,45,.18);border-radius:22px;padding:28px 32px;box-shadow:inset 0 2px 4px rgba(255,255,255,.9),0 18px 30px rgba(120,95,60,.14)">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">
          <span style="font-family:'DM Mono';font-weight:500;font-size:16px;color:#96562d">ultron ~ %</span>
          <span style="width:9px;height:9px;border-radius:50%;background:#7fbf8f"></span>
          <span style="font-family:'DM Mono';font-size:12px;color:#a08a68;letter-spacing:.14em">SESSION 1</span></div>
        <div style="font-family:'DM Sans';font-weight:700;font-size:29px;color:#2a2016;line-height:1.42">
          <span style="color:#96562d">&gt;</span> Tonight: research 40 target accounts, draft the outreach, prep three posts.</div>
      </div>
      <div style="display:flex;align-items:center;gap:14px;margin-top:24px">
        <svg width="34" height="34" viewBox="0 0 24 24"><path d="M21 12.8A8.5 8.5 0 1 1 11.2 3a6.6 6.6 0 0 0 9.8 9.8Z" fill="#e6b48f" stroke="#96562d" stroke-width="1.2"/></svg>
        <span style="font-family:'DM Sans';font-weight:800;font-size:21px;color:#2a2016">11:47 PM</span>
        <span style="font-family:'DM Sans';font-size:18px;color:#8a745a">you go to sleep. the shift starts.</span>
      </div>
      {cap("no dashboards, no clicks. one sentence, then lights out.","#8a745a")}</div>'''

# 2. CREW - vertical shift-log timeline, spine with 7 agent nodes, each a done row w/ time + LED
def crew():
    agents=[("CORTEX","ranked 40 accounts","01:12"),
            ("SPECTER","wrote the sequence","02:40"),
            ("STRIKER","prepped 3 close plans","03:05"),
            ("PULSE","drafted 3 posts","03:58"),
            ("SENTINEL","shipped the landing fix","04:30"),
            ("AMPLIFY","scheduled the week","05:15"),
            ("COUNSEL","flagged 1 NDA clause","05:47")]
    rows=""
    for nm,task,t in agents:
        rows+=f'''<div style="display:flex;align-items:center;gap:20px">
          <div style="flex-shrink:0;width:15px;height:15px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 0 5px rgba(212,162,127,.12),0 0 14px rgba(212,162,127,.6);z-index:2"></div>
          <div style="flex:1;display:flex;align-items:center;gap:16px;background:linear-gradient(160deg,#302c28,#211e1a);border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:12px 20px;box-shadow:0 12px 22px rgba(0,0,0,.4)">
            <span style="font-family:'DM Mono';font-weight:500;font-size:16px;letter-spacing:.1em;color:#FAFAF7;width:120px">{nm}</span>
            <span style="flex:1;font-family:'DM Sans';font-size:17px;color:#a8a296">{task}</span>
            <span style="font-family:'DM Mono';font-size:14px;color:rgb({ACC})">{t}</span>
            <span style="flex-shrink:0;width:9px;height:9px;border-radius:50%;background:#7fd39a;box-shadow:0 0 10px rgba(127,211,154,.8)"></span>
          </div></div>'''
    return f'''<div style="width:900px;{CARD};padding:32px 40px 32px">
      {htitle("Seven agents clocked in","THE SHIFT LOG")}
      <div style="position:relative;padding-left:6px">
        <div style="position:absolute;left:13px;top:14px;bottom:14px;width:2px;background:linear-gradient(180deg,rgba(212,162,127,.55),rgba(212,162,127,.1))"></div>
        <div style="display:flex;flex-direction:column;gap:10px;position:relative">{rows}</div>
      </div>
      {cap("one instruction fanned out to the whole roster. each did its job by dawn.")}</div>'''

# 3. RESEARCH - horizontal fit-score leaderboard, top account lit in accent
def research():
    rows=[("Northwind Robotics",94,"hiring 3 ops roles"),
          ("Globex Systems",89,"raised $4M in May"),
          ("Umbrella SaaS",85,"switched CRM last week"),
          ("Initech",78,"no AI layer yet"),
          ("Soylent Cloud",71,"new VP of Sales")]
    bars=""
    for i,(nm,sc,note) in enumerate(rows):
        top=i==0
        barcol=f"linear-gradient(90deg,#e6b48f,rgb({ACC}))" if top else "linear-gradient(90deg,#3a342e,#6b5c4c)"
        sccol="#1a0f0a" if top else "#d9d5cc"
        bars+=f'''<div style="display:flex;align-items:center;gap:18px">
          <div style="width:238px;flex-shrink:0;text-align:right">
            <div style="font-family:'DM Sans';font-weight:{800 if top else 600};font-size:19px;color:{'#FAFAF7' if top else '#b8b2a6'}">{nm}</div>
            <div style="font-family:'DM Sans';font-size:13px;color:#8f8f85">{note}</div></div>
          <div style="flex:1;height:36px;background:rgba(250,250,247,.05);border-radius:9px;overflow:hidden;position:relative">
            <div style="height:100%;width:{sc}%;background:{barcol};border-radius:9px;box-shadow:{'0 0 20px rgba(212,162,127,.55)' if top else 'none'}"></div>
            <span style="position:absolute;right:14px;top:50%;transform:translateY(-50%);font-family:'DM Sans';font-weight:900;font-size:19px;color:{sccol}">{sc}</span></div>
        </div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It ranked 40 by 3 AM","FIT SCORE")}
      <div style="display:flex;flex-direction:column;gap:15px;margin:8px 0 2px">{bars}</div>
      {cap("scored on fit, timing and intent. the seven worth your morning float to the top.")}</div>'''

# 4. OUTBOUND - 3-step sequence, email preview cards connected by a dashed day-spine
def outbound():
    steps=[("1","The opener","Saw Northwind is hiring 3 ops roles. Usually means the founder is drowning in manual work."),
           ("3","The nudge","One question: who owns pipeline research while you scale the team?"),
           ("6","The close","A two-line teardown of your current stack, or I close the loop. Your call.")]
    cards=""
    for i,(day,subj,body) in enumerate(steps):
        spine='<div style="flex:1;width:2px;background:repeating-linear-gradient(180deg,rgba(212,162,127,.55) 0 6px,transparent 6px 12px);margin:4px 0"></div>' if i<2 else ''
        cards+=f'''<div style="display:flex;gap:20px;align-items:stretch">
          <div style="flex-shrink:0;width:56px;display:flex;flex-direction:column;align-items:center">
            <div style="width:54px;height:54px;border-radius:15px;background:linear-gradient(160deg,#403a33,#241f1a);border:1px solid rgba(212,162,127,.35);display:flex;flex-direction:column;align-items:center;justify-content:center">
              <span style="font-family:'DM Mono';font-size:10px;letter-spacing:.1em;color:#8f8f85">DAY</span>
              <span style="font-family:'DM Sans';font-weight:900;font-size:20px;color:rgb({ACC});line-height:1">{day}</span></div>
            {spine}
          </div>
          <div style="flex:1;background:linear-gradient(160deg,#2f2b27,#211e1a);border:1px solid rgba(255,255,255,.08);border-radius:16px;padding:15px 20px;box-shadow:0 14px 26px rgba(0,0,0,.4);margin-bottom:10px">
            <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px">
              <span style="font-family:'DM Sans';font-weight:800;font-size:19px;color:#FAFAF7">{subj}</span>
              <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.1em;color:rgb({ACC})">DRAFTED</span></div>
            <div style="font-family:'DM Sans';font-size:16px;color:#a8a296;line-height:1.42">{body}</div></div>
        </div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 28px">
      {htitle("A full sequence by dawn","SPECTER · OUTBOUND")}
      <div style="display:flex;flex-direction:column">{cards}</div>
      {cap("three touches, personalised per account, sitting in your drafts ready to send.")}</div>'''

# 5. COST (IVORY) - itemised receipt in cents, competitor retainer struck out
def cost():
    items=[("CORTEX","40 accounts researched","$0.03"),
           ("SPECTER","12 emails drafted","$0.04"),
           ("PULSE","3 posts written","$0.05")]
    lines=""
    for nm,desc,c in items:
        lines+=f'''<div style="display:flex;align-items:baseline;justify-content:space-between;padding:13px 0;border-bottom:1px dashed rgba(150,90,45,.22)">
          <div><span style="font-family:'DM Mono';font-weight:500;font-size:16px;color:#96562d;letter-spacing:.06em">{nm}</span>
          <span style="font-family:'DM Sans';font-size:16px;color:#6a5642;margin-left:12px">{desc}</span></div>
          <span style="font-family:'DM Sans';font-weight:800;font-size:19px;color:#2a2016">{c}</span></div>'''
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {ihead("The whole night, itemised","PAY PER TOKEN")}
      <div style="background:linear-gradient(160deg,#fffdf9,#f2e8d6);border:1px solid rgba(150,90,45,.16);border-radius:20px;padding:6px 26px 20px;box-shadow:inset 0 2px 4px rgba(255,255,255,.9)">
        {lines}
        <div style="display:flex;align-items:baseline;justify-content:space-between;padding-top:18px">
          <span style="font-family:'DM Sans';font-weight:900;font-size:23px;color:#2a2016">Total for the shift</span>
          <span style="font-family:'DM Sans';font-weight:900;font-size:40px;color:#96562d">$0.12</span></div>
      </div>
      <div style="display:flex;align-items:center;gap:14px;margin-top:20px">
        <span style="font-family:'DM Sans';font-size:18px;color:#8a745a">An agency to do the same:</span>
        <span style="font-family:'DM Sans';font-weight:800;font-size:22px;color:#8a745a;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.75)">$2,400/mo</span>
      </div>
      {cap("cents per run, not a retainer. the meter only moves when it produces.","#8a745a")}</div>'''

# 6. CONTENT - downward cascade of 3 draft post cards in your voice + match badge
def content():
    cards=[("-4deg","36px","2px","1","Most founders automate the wrong half of the funnel."),
           ("3deg","330px","150px",".97","Nine tools died last month. The survivor had no chat box."),
           ("-2deg","96px","294px","1","Your cold emails do not have a copy problem.")]
    stack=""
    for rot,left,top,op,txt in cards:
        stack+=f'''<div style="position:absolute;left:{left};top:{top};width:452px;transform:rotate({rot});opacity:{op};
          background:linear-gradient(160deg,#413b35,#2b2723);border:1px solid rgba(255,255,255,.13);border-radius:18px;padding:19px 22px;box-shadow:0 28px 46px rgba(0,0,0,.55)">
          <div style="display:flex;align-items:center;gap:10px;margin-bottom:11px">
            <div style="width:34px;height:34px;border-radius:50%;background:linear-gradient(160deg,#e6b48f,rgb({ACC}))"></div>
            <div><div style="font-family:'DM Sans';font-weight:700;font-size:14px;color:#FAFAF7">Tibi Serbaneci</div>
            <div style="font-family:'DM Mono';font-size:11px;color:#a08d76">draft &middot; in your voice</div></div></div>
          <div style="font-family:'DM Sans';font-weight:800;font-size:21px;color:#FAFAF7;line-height:1.3">{txt}</div>
        </div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Three posts, your voice","PULSE · CONTENT")}
      <div style="position:relative;height:452px">{stack}
        <div style="position:absolute;right:8px;top:64px;background:rgb({ACC});color:#1a0f0a;font-family:'DM Sans';font-weight:900;font-size:16px;padding:9px 18px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4);z-index:5">98% your voice</div>
      </div>
      {cap("sampled from your real posts. your cadence, your banned words, your takes.")}</div>'''

# 7. GATE - morning approval phone mockup: queue frozen, approve / kill per item (HUMAN GATE)
def gate():
    items=[("Outreach to Northwind","12 emails ready"),
           ("This week's 3 posts","scheduled Mon to Wed"),
           ("Landing page fix","PR #182, tests green")]
    rows=""
    for t,s in items:
        rows+=f'''<div style="display:flex;align-items:center;gap:12px;background:#211d19;border:1px solid rgba(255,255,255,.08);border-radius:14px;padding:13px 14px;margin-bottom:11px">
          <div style="flex:1;min-width:0"><div style="font-family:'DM Sans';font-weight:700;font-size:15px;color:#FAFAF7">{t}</div>
          <div style="font-family:'DM Sans';font-size:12px;color:#8f8f85">{s}</div></div>
          <div style="flex-shrink:0;width:36px;height:36px;border-radius:10px;background:rgb({ACC});display:flex;align-items:center;justify-content:center"><svg width="19" height="19" viewBox="0 0 24 24"><path d="M5 12.5l4 4L19 7" fill="none" stroke="#1a0f0a" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
          <div style="flex-shrink:0;width:36px;height:36px;border-radius:10px;background:rgba(200,70,35,.15);border:1px solid rgba(200,70,35,.5);display:flex;align-items:center;justify-content:center"><svg width="16" height="16" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18" stroke="rgb(200,70,35)" stroke-width="2.6" stroke-linecap="round"/></svg></div>
        </div>'''
    phone=f'''<div style="width:392px;background:linear-gradient(165deg,#26231f,#1a1815);border:2px solid rgba(255,255,255,.1);border-radius:38px;padding:24px 20px;box-shadow:0 40px 70px rgba(0,0,0,.6),inset 0 2px 3px rgba(255,255,255,.1)">
      <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:16px;padding:0 6px">
        <span style="font-family:'DM Sans';font-weight:900;font-size:20px;color:#FAFAF7">7:00 AM</span>
        <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.1em;color:rgb({ACC})">3 WAITING</span></div>
      {rows}</div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:34px">
      <div style="flex-shrink:0">{phone}</div>
      <div style="flex:1">
        {htitle("Nothing sent without you","HUMAN GATE")}
        <div style="font-family:'DM Sans';font-size:19px;color:#c9c3b8;line-height:1.5">The shift is done, but the queue stays frozen. One tap approves. One tap kills. Nothing leaves the building on its own.</div>
        {cap("augmented, never unsupervised. the reins stay in your hand.")}</div>
    </div>'''

# 8. SUMMARY - sunrise scene + morning readout of the night's output, for cents
def summary():
    cx,cy=260,150
    rays=""
    for a in range(180,361,20):
        x1=cx+72*math.cos(math.radians(a)); y1=cy+72*math.sin(math.radians(a))
        x2=cx+104*math.cos(math.radians(a)); y2=cy+104*math.sin(math.radians(a))
        rays+=f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(212,162,127,.6)" stroke-width="4" stroke-linecap="round"/>'
    stats=[("40","accounts ranked"),("12","emails drafted"),("3","posts written")]
    strip=""
    for i,(n,l) in enumerate(stats):
        strip+=f'''<div style="text-align:center;padding:0 30px;{'border-left:1px solid rgba(255,255,255,.12)' if i>0 else ''}">
          <div style="font-family:'DM Sans';font-weight:900;font-size:46px;color:rgb({ACC});line-height:1">{n}</div>
          <div style="font-family:'DM Sans';font-size:15px;color:#a8a296;margin-top:4px">{l}</div></div>'''
    return f'''<div style="width:900px;{CARD};padding:30px 40px 34px;text-align:center">
      {htitle("You woke up to it done","THE MORNING")}
      <svg width="520" height="180" viewBox="0 0 520 180" style="display:block;margin:2px auto 0">
        <defs>
          <radialGradient id="sun" cx="50%" cy="72%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#8a4a2c"/></radialGradient>
          <filter id="sg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="24" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter>
          <clipPath id="hz"><rect x="0" y="0" width="520" height="150"/></clipPath></defs>
        <g clip-path="url(#hz)">{rays}<g filter="url(#sg)"><circle cx="{cx}" cy="{cy}" r="56" fill="url(#sun)"/></g></g>
        <rect x="36" y="148" width="448" height="3" rx="1.5" fill="rgb({ACC})" opacity="0.7"/>
      </svg>
      <div style="display:flex;align-items:center;justify-content:center;margin:20px 0 6px">{strip}</div>
      <div style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#FAFAF7;margin-top:6px">All before your coffee. For <span style="color:rgb({ACC})">12 cents</span>.</div>
      {cap("the night shift never clocks out. one instruction, a finished morning.")}</div>'''

PANELS={"kickoff":kickoff(),"crew":crew(),"research":research(),"outbound":outbound(),
        "cost":cost(),"content":content(),"gate":gate(),"summary":summary()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s2src37"; os.makedirs(outd,exist_ok=True)
    with sync_playwright() as pw:
        b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium",args=["--no-sandbox","--no-proxy-server"])
        pg=b.new_page(viewport={"width":960,"height":900},device_scale_factor=2)
        for name,html in PANELS.items():
            full=f"<!DOCTYPE html><html><head><meta charset='utf-8'><style>{Lm.css(ACC)}</style></head><body style='padding:30px'>{html}</body></html>"
            pg.set_content(full); pg.wait_for_timeout(400)
            pg.screenshot(path=f"{outd}/{name}.png",omit_background=True,full_page=True)
            print("rendered",name)
        b.close()
    print("done")
