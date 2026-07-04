#!/usr/bin/env python3
# TIER 3 - LOW EFFORT, DONE RIGHT, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
# 8 distinct scene types: dot field / gauge / comparison / iso stack / timeline / effort-vs-output
# line chart / radial hub / node graph. Warm palette, Ultron prices in cents. Cost zero.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"; RED="200,70,35"; IVACC="#96562d"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=None): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc or f"rgb({ACC})"}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. PITCH - dot field: the feed drowning in recycled, near-identical low-effort content
def pitch():
    cols,rowsn=27,12; cell=17; gap=7
    red={31,58,113,140,167,229,256,283}   # the same recycled quote, cloned everywhere
    dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in red:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba({RED},.62)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba(250,250,247,.075)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The gurus sell effortless posting","TEN MINUTES A DAY")}
      <div style="display:flex;align-items:center;gap:34px">
        <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="flex-shrink:0">{dots}</svg>
        <div style="flex:1">
          <div style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#FAFAF7;line-height:1.08">A drowning<br>feed</div>
          <div style="margin-top:16px">
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px"><span style="width:11px;height:11px;border-radius:3px;background:rgba({RED},.62)"></span><span style="font-family:DM Sans;font-size:16px;color:#c9c3b8">the same recycled quote</span></div>
            <div style="display:flex;align-items:center;gap:10px"><span style="width:11px;height:11px;border-radius:3px;background:rgba(250,250,247,.12)"></span><span style="font-family:DM Sans;font-size:16px;color:#c9c3b8">faceless clip, again</span></div>
          </div>
        </div></div>
      {cap("faceless clips, recycled quotes, ten minutes a day - the feed drowns in it.")}</div>'''

# 2. CATCHG - twin gauges: effort IN near zero, value OUT near zero (recycled reach)
def gauge_svg(cx,cy,r,frac,col):
    def pt(a): return (cx+r*math.cos(math.radians(a)), cy+r*math.sin(math.radians(a)))
    x0,y0=pt(180); x1,y1=pt(360)
    ex,ey=pt(180+180*frac)
    bg=f'<path d="M{x0:.0f} {y0:.0f} A{r} {r} 0 0 1 {x1:.0f} {y1:.0f}" fill="none" stroke="rgba(250,250,247,.10)" stroke-width="16" stroke-linecap="round"/>'
    val=f'<path d="M{x0:.0f} {y0:.0f} A{r} {r} 0 0 1 {ex:.0f} {ey:.0f}" fill="none" stroke="{col}" stroke-width="16" stroke-linecap="round"/>'
    tick=f'<line x1="{cx}" y1="{cy}" x2="{ex:.0f}" y2="{ey:.0f}" stroke="{col}" stroke-width="4"/><circle cx="{cx}" cy="{cy}" r="7" fill="{col}"/>'
    return bg+val+tick
def catchg():
    g1=gauge_svg(140,170,105,0.08,f"rgb({ACC})")
    g2=gauge_svg(500,170,105,0.05,f"rgb({RED})")
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Zero effort in reads as zero out","RECYCLED REACH")}
      <svg width="700" height="250" viewBox="0 0 700 250" style="display:block;margin:6px auto 0">
        {g1}
        <text x="140" y="150" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="40" fill="#FAFAF7">8%</text>
        <text x="140" y="204" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="#9a9488">EFFORT IN</text>
        <text x="320" y="162" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="46" fill="rgba(250,250,247,.5)">=</text>
        {g2}
        <text x="500" y="150" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="40" fill="rgb({RED})">5%</text>
        <text x="500" y="204" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="#9a9488">VALUE OUT</text>
      </svg>
      {cap("audiences smell templates. recycled content earns recycled reach.")}</div>'''

# 3. REFRAME2 - IVORY comparison: light posting column vs heavy system column
def reframe2():
    def col(icon,label,word,ink,accent,heavy):
        wt = "900" if heavy else "500"
        return (f'<div style="flex:1;text-align:center;padding:8px 6px">'
          f'<div style="width:118px;height:118px;margin:0 auto;border-radius:26px;background:{"rgba(150,90,45,.10)" if heavy else "rgba(150,90,45,.05)"};'
          f'border:1.5px solid rgba(150,90,45,{".28" if heavy else ".16"});display:flex;align-items:center;justify-content:center;'
          f'box-shadow:{"0 18px 30px rgba(120,90,55,.22)" if heavy else "0 8px 16px rgba(120,90,55,.10)"}">{icon}</div>'
          f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:{accent};margin-top:18px">{label}</div>'
          f'<div style="font-family:DM Sans;font-weight:{wt};font-size:{34 if heavy else 30}px;color:{ink};margin-top:6px">{word}</div></div>')
    feather=f'<svg width="52" height="52" viewBox="0 0 24 24" fill="none" stroke="{IVACC}" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M20.24 12.24a6 6 0 0 0-8.49-8.49L5 10.5V19h8.5z"/><line x1="16" y1="8" x2="2" y2="22"/><line x1="17.5" y1="15" x2="9" y2="15"/></svg>'
    anvil=f'<svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="{IVACC}" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8h11a4 4 0 0 1-4 4H8l-1 3"/><path d="M14 8l5-1v3l-3 1"/><rect x="5" y="18" width="8" height="3" rx="1"/><line x1="9" y1="15" x2="9" y2="18"/></svg>'
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:22px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#17150F">Low effort is an output</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:{IVACC}">NOT AN INPUT</span></div>
      <div style="display:flex;align-items:stretch">
        {col(feather,"THE POSTING","light","#2a2016",IVACC,False)}
        <div style="width:1.5px;background:rgba(150,90,45,.22);margin:6px 6px"></div>
        {col(anvil,"THE SYSTEM","heavy","#2a2016",IVACC,True)}
      </div>
      {cap("the posting should be light. the system behind it should be heavy.","#8a745a")}</div>'''

# 4. HEAVY - isometric stack of the 3 build-once blocks (the real work, done up front)
def heavy():
    steps=[("VOICE","sampled from 40 posts",0),("HOOK BANK","120 angles stocked",1),("CADENCE","14 slots wired",2)]
    cards=""
    for nm,sub,i in steps:
        y=i*128
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#403a35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:50px;height:50px;border-radius:14px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:22px;color:rgb({ACC})">{i+1}</div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:14px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{sub}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("Build once: voice, bank, cadence","THE REAL WORK")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(20deg) rotateZ(-8deg);width:560px;height:430px;position:relative">{cards}
          <div style="position:absolute;left:150px;top:396px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:16px;padding:9px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)">Wired &#10003; one afternoon</div></div></div>
      {cap("your voice sampled, your hook bank stocked, your calendar wired - up front.")}</div>'''

# 5. LIGHT - horizontal timeline of the daily loop: plan -> draft -> queue 10:00 -> approve
def light():
    steps=[("09:58","desk plans the day"),("+0:20","drafts to your bar"),("10:00","queued to post"),("one tap","you approve")]
    W=760; y=118; x0=70; gapx=(W-2*x0)/(len(steps)-1)
    line=f'<line x1="{x0}" y1="{y}" x2="{W-x0}" y2="{y}" stroke="rgba(212,162,127,.28)" stroke-width="3"/>'
    fill=f'<line x1="{x0}" y1="{y}" x2="{W-x0}" y2="{y}" stroke="rgb({ACC})" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>'
    nodes=""
    for i,(t,s) in enumerate(steps):
        x=x0+gapx*i; last=(i==len(steps)-1)
        fillc=f"rgb({ACC})" if last else "#2a2724"
        nodes+=(f'<circle cx="{x:.0f}" cy="{y}" r="16" fill="{fillc}" stroke="rgb({ACC})" stroke-width="3"/>'
          + (f'<path d="M{x-7:.0f} {y} l4.5 4.5 l8.5 -9" fill="none" stroke="#1a0f0a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>' if last else f'<circle cx="{x:.0f}" cy="{y}" r="5" fill="rgb({ACC})"/>')
          + f'<text x="{x:.0f}" y="{y-34}" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="16" fill="rgb({ACC})">{t}</text>'
          + f'<text x="{x:.0f}" y="{y+46}" text-anchor="middle" font-family="DM Sans" font-size="16" fill="#d9d5cc">{s}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 36px">
      {htitle("Then daily is one line and one tap","ONE LINE, ONE TAP")}
      <div style="display:flex;align-items:center;justify-content:center;height:250px">
        <svg width="{W}" height="200" viewBox="0 0 {W} 200">{line}{fill}{nodes}</svg></div>
      {cap("the desk plans, drafts to your bar, queues at 10:00 - you approve on your phone.")}</div>'''

# 6. DIFFERENCE - effort-vs-output line chart: guru reach decays, system reach compounds
def difference():
    W,H=740,420; ox,oy=80,340; pw,ph=600,270
    weeks=6
    guru=[0.42,0.36,0.30,0.25,0.20,0.16]      # decays
    sysd=[0.20,0.30,0.44,0.60,0.80,1.00]      # compounds
    def px(i): return ox+pw*i/(weeks-1)
    def py(v): return oy-ph*v
    grid="".join(f'<line x1="{ox}" y1="{oy-ph*g/4:.0f}" x2="{ox+pw}" y2="{oy-ph*g/4:.0f}" stroke="rgba(250,250,247,.06)"/>' for g in range(5))
    def poly(data): return " ".join(f"{px(i):.0f},{py(v):.0f}" for i,v in enumerate(data))
    gpts=poly(guru); spts=poly(sysd)
    gdots="".join(f'<circle cx="{px(i):.0f}" cy="{py(v):.0f}" r="5" fill="rgb({RED})"/>' for i,v in enumerate(guru))
    sdots="".join(f'<circle cx="{px(i):.0f}" cy="{py(v):.0f}" r="5.5" fill="rgb({ACC})"/>' for i,v in enumerate(sysd))
    axis=f'<line x1="{ox}" y1="{oy}" x2="{ox+pw}" y2="{oy}" stroke="rgba(250,250,247,.25)" stroke-width="2"/><line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy-ph}" stroke="rgba(250,250,247,.25)" stroke-width="2"/>'
    wlab="".join(f'<text x="{px(i):.0f}" y="{oy+26}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">wk{i+1}</text>' for i in range(weeks))
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Guru skips work. System front-loads.","SAME MINUTES")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        {grid}{axis}
        <polyline points="{gpts}" fill="none" stroke="rgb({RED})" stroke-width="3.5" stroke-dasharray="7 6"/>{gdots}
        <polyline points="{spts}" fill="none" stroke="rgb({ACC})" stroke-width="4"/>{sdots}
        {wlab}
        <text x="{px(5)-6:.0f}" y="{py(guru[5])+26:.0f}" text-anchor="end" font-family="DM Sans" font-weight="700" font-size="16" fill="rgb({RED})">guru: fades</text>
        <text x="{px(5)-6:.0f}" y="{py(sysd[5])-14:.0f}" text-anchor="end" font-family="DM Sans" font-weight="800" font-size="16" fill="rgb({ACC})">system: compounds</text>
        <text x="{ox-10}" y="{oy-ph+4}" text-anchor="end" font-family="DM Mono" font-size="11" fill="#8f8f85">reach</text>
      </svg>
      {cap("same daily minutes, opposite outcomes. the system version compounds.")}</div>'''

# 7. RECEIPTS - IVORY radial hub: one planning line at centre, 14 posts radiating out
def receipts():
    cx,cy,R=250,220,168; n=14
    spokes=""; nodes=""
    for i in range(n):
        a=-90+360*i/n
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(150,90,45,.28)" stroke-width="1.6"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="19" fill="#fbf5ea" stroke="{IVACC}" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-weight="500" font-size="14" fill="{IVACC}">{i+1}</text>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px;display:flex;align-items:center;gap:24px">
      <svg width="500" height="440" viewBox="0 0 500 440" style="flex-shrink:0">
        <defs><radialGradient id="hub" cx="38%" cy="32%"><stop offset="0%" stop-color="#c98a5f"/><stop offset="100%" stop-color="{IVACC}"/></radialGradient></defs>
        {spokes}{nodes}
        <circle cx="{cx}" cy="{cy}" r="58" fill="url(#hub)"/>
        <text x="{cx}" y="{cy-4}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#fdf6ec">1 line</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#f4e3d2">planning</text>
      </svg>
      <div style="flex:1">
        <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">
          <span style="font-family:'DM Sans';font-weight:800;font-size:25px;color:#17150F">Fourteen a week</span>
          <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.12em;color:{IVACC}">ONE INPUT</span></div>
        <div style="font-family:DM Sans;font-size:19px;color:#3a2c1e;line-height:1.45">In my voice, on my niche, each one passing the boring test before I ever see it.</div>
        {cap("fourteen posts a week from one planning line.","#8a745a")}
      </div></div>'''

# 8. VERDICTL - node graph: one heavy BUILD node feeds a forever-trailing chain of light posts
def verdictl():
    W,H=760,400
    bx,by=150,200
    posts=[(370,120),(470,190),(560,150),(650,220),(720,175)]
    edges=""
    prev=(bx+92,by)
    for i,(x,y) in enumerate(posts):
        mx=(prev[0]+x)/2
        op=max(0.25,0.85-i*0.14)
        edges+=f'<path d="M{prev[0]:.0f} {prev[1]:.0f} C{mx:.0f} {prev[1]:.0f},{mx:.0f} {y},{x-26} {y}" fill="none" stroke="rgba(212,162,127,{op:.2f})" stroke-width="2.4"/>'
        prev=(x+26,y)
    nodes=""
    for i,(x,y) in enumerate(posts):
        op=max(0.4,1.0-i*0.13)
        nodes+=(f'<circle cx="{x}" cy="{y}" r="26" fill="#2a2724" stroke="rgba(212,162,127,{op:.2f})" stroke-width="2" opacity="{op:.2f}"/>'
          f'<path d="M{x-9} {y-3} h18 M{x-9} {y+4} h12" stroke="rgba(212,162,127,{op:.2f})" stroke-width="2.4" stroke-linecap="round"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Work hard once. Post easy forever.","THE HONEST VERSION")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><radialGradient id="bn" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="bng" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {edges}
        <g filter="url(#bng)"><circle cx="{bx}" cy="{by}" r="92" fill="url(#bn)"/></g>
        <text x="{bx}" y="{by-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="#2a160c">BUILD</text>
        <text x="{bx}" y="{by+26}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".14em" fill="#3a2010">ONCE</text>
        {nodes}
        <text x="545" y="330" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="#8f8f85">POST EASY, FOREVER</text>
      </svg>
      {cap("that is the honest low effort. everything else is a template farm.")}</div>'''

PANELS={"pitch":pitch(),"catchg":catchg(),"reframe2":reframe2(),"heavy":heavy(),
        "light":light(),"difference":difference(),"receipts":receipts(),"verdictl":verdictl()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/loweffort"; os.makedirs(outd,exist_ok=True)
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
