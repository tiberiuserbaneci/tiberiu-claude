#!/usr/bin/env python3
# TIER 3 - FIVE ASSISTANTS, NO MEMORY, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"       # warm accent
IV="#96562d"            # ivory-card accent
BAD="200,70,35"         # muted red, only for bad/disconnected
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def htitleiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{IV}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. LIST7 - DISCONNECTED-TOOLS scene: 5 separate app-tool islands, each its own little window,
# scattered with gaps, each stamped with a red "no link" tab -> a specialist for every slice.
def list7():
    tools=[("Inbox","47 unread",56,26),("Calendar","3 meetings",352,10),
           ("Meetings","notes only",648,44),("Notes","no context",150,214),("Tasks","12 due",470,232)]
    islands=""
    for nm,sub,x,y in tools:
        islands+=(f'<div style="position:absolute;left:{x}px;top:{y}px;width:210px;'
          f'background:linear-gradient(158deg,#37332e,#211e1a);border:1px solid rgba(255,255,255,.10);'
          f'border-radius:16px;padding:16px 18px;box-shadow:0 22px 34px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<div style="display:flex;align-items:center;gap:12px">'
          f'<div style="width:38px;height:38px;border-radius:11px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.30);'
          f'display:flex;align-items:center;justify-content:center;font-family:\'DM Sans\';font-weight:900;font-size:18px;color:rgb({ACC})">{nm[0]}</div>'
          f'<div><div style="font-family:\'DM Sans\';font-weight:800;font-size:19px;color:#FAFAF7">{nm}</div>'
          f'<div style="font-family:\'DM Sans\';font-size:13px;color:#8f8f85">{sub}</div></div></div>'
          f'<div style="margin-top:12px;display:flex;align-items:center;gap:7px">'
          f'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="rgb({BAD})" stroke-width="2.6" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
          f'<span style="font-family:\'DM Mono\';font-size:11px;letter-spacing:.10em;color:rgb({BAD})">NO LINK</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A tool for every slice","5 SUBSCRIPTIONS")}
      <div style="position:relative;height:470px">{islands}</div>
      {cap("inbox tool, calendar tool, meeting tool, note tool. five logins, five silos.")}</div>'''

# 2. SEAMS - NODE GRAPH with SEVERED edges: 5 peer nodes in a pentagon, the links that SHOULD join
# them drawn as red dashed cut lines with a break mark -> none of them know the others exist.
def seams():
    cx,cy,R=290,240,180
    names=["Inbox","Calendar","Meetings","Pipeline","Notes"]
    pts=[(cx+R*math.cos(math.radians(-90+i*72)),cy+R*math.sin(math.radians(-90+i*72))) for i in range(5)]
    edges=""
    for i in range(5):
        for j in range(i+1,5):
            x1,y1=pts[i]; x2,y2=pts[j]; mx,my=(x1+x2)/2,(y1+y2)/2
            edges+=(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="rgba(200,70,35,.30)" stroke-width="1.6" stroke-dasharray="4 8"/>'
              f'<line x1="{mx-7:.0f}" y1="{my-7:.0f}" x2="{mx+7:.0f}" y2="{my+7:.0f}" stroke="rgb({BAD})" stroke-width="2.4"/>'
              f'<line x1="{mx+7:.0f}" y1="{my-7:.0f}" x2="{mx-7:.0f}" y2="{my+7:.0f}" stroke="rgb({BAD})" stroke-width="2.4"/>')
    nodes=""
    for (x,y),nm in zip(pts,names):
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="46" fill="#241f1a" stroke="rgba(255,255,255,.14)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:20px">
      <svg width="580" height="480" viewBox="0 0 580 480">{edges}{nodes}</svg>
      <div style="flex:1">
        {htitle("None know the others","NO SHARED STATE")}
        <div style="font-family:'DM Sans';font-size:19px;color:#c9c3b8;line-height:1.45">The inbox tool cannot see the deal. The meeting tool never met your pipeline. Every link that should exist is cut.</div>
        {cap("ten seams between five tools, every one of them severed.")}</div></div>'''

# 3. COST7 - MEMORY CORE, fragmented: a dim central core with 5 memory shards drifting off, each a
# context piece, links broken -> five memories means no memory.
def cost7():
    cx,cy=290,232
    shards=[("ICP",118,96,-20),("pipeline",470,120,14),("pricing",96,300,-12),
            ("your docs",448,332,10),("last call",300,392,6)]
    frag=""
    for nm,x,y,rot in shards:
        frag+=(f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="rgba(200,70,35,.28)" stroke-width="1.6" stroke-dasharray="3 10"/>')
    for nm,x,y,rot in shards:
        frag+=(f'<g transform="translate({x},{y}) rotate({rot})">'
          f'<rect x="-64" y="-30" width="128" height="60" rx="12" fill="rgba(45,40,35,.9)" stroke="rgba(212,162,127,.22)" stroke-width="1.5"/>'
          f'<text x="0" y="-4" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="#c9c3b8">{nm}</text>'
          f'<text x="0" y="17" text-anchor="middle" font-family="DM Mono" font-size="10.5" letter-spacing=".10em" fill="rgb({BAD})">orphaned</text></g>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Five memories, no memory","CONTEXT NOWHERE")}
      <svg width="580" height="466" viewBox="0 0 580 466" style="display:block;margin:0 auto">
        <defs><radialGradient id="dim" cx="42%" cy="36%"><stop offset="0%" stop-color="rgba(212,162,127,.30)"/><stop offset="70%" stop-color="rgba(212,162,127,.06)"/><stop offset="100%" stop-color="rgba(212,162,127,0)"/></radialGradient></defs>
        <circle cx="{cx}" cy="{cy}" r="120" fill="url(#dim)"/>
        {frag}
        <circle cx="{cx}" cy="{cy}" r="60" fill="#211d19" stroke="rgba(212,162,127,.22)" stroke-width="2" stroke-dasharray="6 9"/>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#6f6a60">0</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="11" letter-spacing=".12em" fill="#6f6a60">SHARED</text>
      </svg>
      {cap("your context lives nowhere, so you re-explain yourself to software all day.")}</div>'''

# 4. DESK7b - RADIAL HUB (IVORY): one desk at the centre, 3 solid glowing spokes to inbox / calendar
# / pipeline, all fed by one memory underneath.
def desk7b():
    cx,cy,R=232,230,150
    spokes=[("Inbox","47 read",-90),("Calendar","3 booked",30),("Pipeline","12 drafted",150)]
    arms=""; chips=""
    for nm,sub,a in spokes:
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        arms+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{IV}" stroke-width="5" stroke-linecap="round"/>'
        arms+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="44" fill="#fbf5ea" stroke="rgba(150,90,45,.28)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y-2:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#2a2016">{nm}</text>'
          f'<text x="{x:.0f}" y="{y+16:.0f}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="{IV}">{sub}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px;display:flex;align-items:center;gap:24px">
      <svg width="464" height="464" viewBox="0 0 464 464">
        <defs><radialGradient id="hubi" cx="38%" cy="32%"><stop offset="0%" stop-color="#e6b48f"/><stop offset="55%" stop-color="{IV}"/><stop offset="100%" stop-color="#5f3216"/></radialGradient>
        <filter id="hig" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="rgba(150,90,45,.35)"/></filter></defs>
        {arms}
        <g filter="url(#hig)"><circle cx="{cx}" cy="{cy}" r="74" fill="url(#hubi)"/></g>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#fdf7ee">ONE</text>
        <text x="{cx}" y="{cy+20}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#fdf7ee">DESK</text>
      </svg>
      <div style="flex:1">
        {htitleiv("One desk holds it all","ONE MEMORY")}
        <div style="font-family:'DM Sans';font-size:19px;color:#4a3a2a;line-height:1.45">Mail read, meetings booked, follow-ups drafted. Inbox, calendar and pipeline all sit on one memory underneath.</div>
        {cap("three surfaces, one context. nothing re-explained.","#8a745a")}</div></div>'''

# 5. COMPOUND7 - ISO STACK: a thread of reference cards, each layer referencing the one below
# (follow-up -> call -> deal -> history) rendered as an isometric stack.
def compound7():
    steps=[("FOLLOW-UP","references the call",0),("THE CALL","references the deal",1),
           ("THE DEAL","references the history",2),("HISTORY","the first email, Mar 4",3)]
    cards=""
    for nm,sub,i in steps:
        y=i*112
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:18px 24px;box-shadow:0 28px 42px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:13px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center">'
          f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M8 6v8a4 4 0 0 0 8 0M8 6l-4 4M8 6l4 4"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("The desk knows the thread","ONE THREAD")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:448px;position:relative">{cards}</div></div>
      {cap("the follow-up carries the whole history. five tools would have carried none.")}</div>'''

# 6. SLEEP7 - TIMELINE: a night shift line, 3 timed stops, moon-to-sun arc above it.
def sleep7():
    W,H=780,300
    stops=[("23:00","Triage","47 threads sorted",70),("06:00","Drafts","12 replies ready",390),("07:00","Digest","1 brief, your voice",700)]
    line=f'<line x1="70" y1="210" x2="700" y2="210" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
    marks=""
    for t,lab,sub,x in stops:
        marks+=(f'<line x1="{x}" y1="60" x2="{x}" y2="210" stroke="rgba(212,162,127,.18)" stroke-width="1.4" stroke-dasharray="3 7"/>'
          f'<circle cx="{x}" cy="210" r="13" fill="rgb({ACC})" filter="url(#sg)"/>'
          f'<text x="{x}" y="248" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#FAFAF7">{t}</text>'
          f'<text x="{x}" y="272" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="rgb({ACC})">{lab}</text>'
          f'<text x="{x}" y="46" text-anchor="middle" font-family="DM Sans" font-size="15" fill="#c9c3b8">{sub}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It works the night shift","WHILE YOU SLEEP")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:6px auto 0">
        <defs><filter id="sg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="7" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        <path d="M70 148 A360 360 0 0 1 700 148" fill="none" stroke="rgba(212,162,127,.22)" stroke-width="1.6" stroke-dasharray="2 9"/>
        <path d="M52 132 a18 18 0 1 0 20 22 a14 14 0 0 1 -20 -22Z" fill="rgb({ACC})" opacity="0.85"/>
        <circle cx="700" cy="140" r="15" fill="rgb({ACC})" filter="url(#sg)"/>
        {line}{marks}
      </svg>
      {cap("triage at 23:00, drafts by 06:00, digest at 07:00. in your voice, parked for your tap.")}</div>'''

# 7. PRICE7 - GAUGE (IVORY): a meter needle swung from an expensive 5-seat stack (competitor, crossed)
# down to cents per run. High $ only ever a competitor cost; Ultron reads in cents.
def price7():
    cx,cy,R=232,258,168
    a0,a1=180,360
    def pt(a,r): return (cx+r*math.cos(math.radians(a)),cy+r*math.sin(math.radians(a)))
    x0,y0=pt(a0,R); x1,y1=pt(a1,R)
    ticks=""
    for k in range(0,11):
        a=a0+(a1-a0)*k/10; ix,iy=pt(a,R-4); ox,oy=pt(a,R-20)
        ticks+=f'<line x1="{ix:.0f}" y1="{iy:.0f}" x2="{ox:.0f}" y2="{oy:.0f}" stroke="rgba(150,90,45,.45)" stroke-width="2"/>'
    na=a0+(a1-a0)*0.90  # needle near the cheap end
    nx,ny=pt(na,R-30)
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px;display:flex;align-items:center;gap:26px">
      <svg width="464" height="300" viewBox="0 0 464 300">
        <path d="M{x0:.0f} {y0:.0f} A{R} {R} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="rgba(150,90,45,.20)" stroke-width="20" stroke-linecap="round"/>
        <path d="M{x0:.0f} {y0:.0f} A{R} {R} 0 0 1 {pt(a0+(a1-a0)*0.30,R)[0]:.0f} {pt(a0+(a1-a0)*0.30,R)[1]:.0f}" fill="none" stroke="rgba(200,70,35,.5)" stroke-width="20" stroke-linecap="round"/>
        <path d="M{pt(a0+(a1-a0)*0.72,R)[0]:.0f} {pt(a0+(a1-a0)*0.72,R)[1]:.0f} A{R} {R} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="{IV}" stroke-width="20" stroke-linecap="round"/>
        {ticks}
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="#2a2016" stroke-width="6" stroke-linecap="round"/>
        <circle cx="{cx}" cy="{cy}" r="12" fill="#2a2016"/>
        <text x="{cx-150}" y="{cy+30}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({BAD})">$168/mo</text>
        <text x="{cx+150}" y="{cy+30}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="{IV}">cents</text>
        <text x="{cx}" y="{cy-26}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="40" fill="#2a2016">~4c</text>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".12em" fill="{IV}">PER RUN</text>
      </svg>
      <div style="flex:1">
        {htitleiv("One meter, not a stack","PAY PER RUN")}
        <div style="font-family:'DM Sans';font-size:19px;color:#4a3a2a;line-height:1.45">Five seats billed a flat <span style="text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7)">$168 a month</span>. One desk bills cents for the runs you actually make.</div>
        {cap("subscriptions became a meter. you pay for work, not for logins.","#8a745a")}</div></div>'''

# 8. RULE7b - DOT FIELD: a field of candidate tools, the few that SHARE MEMORY lit warm and kept,
# the rest dimmed out by the single filter.
def rule7b():
    cols,rowsn=14,7
    keep={18,45,63,72}   # tools that share memory -> kept
    cell=44; gap=14
    dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in keep:
            dots+=(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="12" fill="rgb({ACC})" filter="url(#kg)"/>'
              f'<path d="M{x+13} {y+22}l7 7 12 -14" fill="none" stroke="#1a0f0a" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>')
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="12" fill="rgba(250,250,247,.055)" stroke="rgba(250,250,247,.05)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One filter kills the list","SHARE OR SKIP")}
      <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="display:block;margin:0 auto">
        <defs><filter id="kg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.9"/></filter></defs>
        {dots}</svg>
      <div style="display:flex;gap:26px;margin-top:18px">
        <div style="display:flex;align-items:center;gap:9px"><span style="width:15px;height:15px;border-radius:5px;background:rgb({ACC})"></span><span style="font-family:'DM Sans';font-size:15px;color:#d9d5cc">shares memory, kept</span></div>
        <div style="display:flex;align-items:center;gap:9px"><span style="width:15px;height:15px;border-radius:5px;background:rgba(250,250,247,.08)"></span><span style="font-family:'DM Sans';font-size:15px;color:#8f8f85">no memory, cut</span></div></div>
      {cap("never add a tool that cannot share memory. that one rule kills most of the listicle.")}</div>'''

PANELS={"list7":list7(),"seams":seams(),"cost7":cost7(),"desk7b":desk7b(),
        "compound7":compound7(),"sleep7":sleep7(),"price7":price7(),"rule7b":rule7b()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/onetool"; os.makedirs(outd,exist_ok=True)
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
