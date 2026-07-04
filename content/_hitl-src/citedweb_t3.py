#!/usr/bin/env python3
# TIER 3 - REPORTS THAT CITE TODAY, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips,
# NO clip-path cuts, NO extruded walls. Warm palette; muted red ONLY for stale/uncited bad states.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"      # warm kraft accent
RED="200,70,35"        # muted red, ONLY for stale / uncited bad states
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def ihead(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. STALE - TIMELINE: training cutoff -> today, an 18-month red "blind" gap it improvises across
def stale():
    x0,x1=54,742; cut=372; ax=232
    ticks=""
    for i in range(9):
        tx=x0+(x1-x0)*i/8
        ticks+=f'<line x1="{tx:.0f}" y1="{ax-7}" x2="{tx:.0f}" y2="{ax+7}" stroke="rgba(250,250,247,.16)" stroke-width="1.5"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Confident, and 18 months late","TRAINING CUTOFF")}
      <svg width="820" height="380" viewBox="0 0 820 380">
        <defs>
          <radialGradient id="tnow" cx="40%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="tg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.85"/></filter>
        </defs>
        <!-- red blind bracket over the gap -->
        <path d="M{cut} 120 V104 H720 V120" fill="none" stroke="rgba({RED},.6)" stroke-width="2"/>
        <text x="{(cut+720)//2}" y="94" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".06em" fill="rgb({RED})">18 MONTHS YOUR MARKET MOVED, THE MODEL DID NOT</text>
        <!-- axis -->
        <line x1="{x0}" y1="{ax}" x2="{cut}" y2="{ax}" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round"/>
        <line x1="{cut}" y1="{ax}" x2="720" y2="{ax}" stroke="rgba({RED},.7)" stroke-width="6" stroke-linecap="round" stroke-dasharray="3 12"/>
        {ticks}
        <!-- cutoff marker -->
        <line x1="{cut}" y1="150" x2="{cut}" y2="{ax}" stroke="rgba(255,255,255,.2)" stroke-width="1.5" stroke-dasharray="4 5"/>
        <circle cx="{cut}" cy="{ax}" r="9" fill="#2a2724" stroke="rgb({ACC})" stroke-width="3"/>
        <text x="{cut}" y="176" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="#cfc9bd">KNOWLEDGE ENDS</text>
        <text x="{cut}" y="{ax+26}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#a8a296">Jan 2024</text>
        <!-- today marker -->
        <circle cx="720" cy="{ax}" r="12" fill="url(#tnow)" filter="url(#tg)"/>
        <text x="720" y="176" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">TODAY</text>
        <text x="720" y="{ax+26}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="16" fill="#FAFAF7">Jul 2026</text>
        <!-- improvised claim chip -->
        <g transform="translate(54,286)">
          <rect x="0" y="0" width="712" height="62" rx="16" fill="rgba({RED},.06)" stroke="rgba({RED},.34)" stroke-width="1.5" stroke-dasharray="6 6"/>
          <text x="24" y="27" font-family="DM Mono" font-size="12" letter-spacing=".12em" fill="rgb({RED})">IMPROVISED</text>
          <text x="24" y="48" font-family="DM Sans" font-weight="700" font-size="19" fill="#b58a78" text-decoration="line-through">"they are still a 12-person team"</text>
          <text x="688" y="39" text-anchor="end" font-family="DM Mono" font-size="14" fill="rgb({RED})">now 41. no source.</text>
        </g>
      </svg>
      {cap("training data ends; your market does not. unwired AI narrates the gap.")}</div>'''

# 2. STANDARD - RECEIPT SCENE (ivory): three figures, each butting a source chip (domain + date + link)
def standard():
    rows=[("$4.2M","Series A, closed","crunchbase.com","2026-06-30"),
          ("41","headcount, up from 12","linkedin.com","2026-07-01"),
          ("+18%","pricing, raised MoM","g2.com","2026-06-24")]
    body=""
    for fig,lab,dom,date in rows:
        fav=dom[0].upper()
        body+=f'''<div style="display:flex;align-items:center;gap:22px;background:rgba(255,255,255,.55);border:1px solid rgba(120,95,60,.16);border-left:4px solid #96562d;border-radius:16px;padding:16px 20px">
          <div style="flex-shrink:0;width:120px;text-align:left"><span style="font-family:'DM Sans';font-weight:900;font-size:34px;color:#96562d">{fig}</span></div>
          <div style="flex:1;text-align:left"><span style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#2a2016">{lab}</span></div>
          <div style="flex-shrink:0;display:flex;align-items:center;gap:11px;background:rgba(150,86,45,.10);border:1px solid rgba(150,86,45,.22);border-radius:12px;padding:9px 14px">
            <div style="width:30px;height:30px;border-radius:9px;background:linear-gradient(160deg,#c98a5f,#96562d);display:flex;align-items:center;justify-content:center;font-family:'DM Sans';font-weight:900;font-size:15px;color:#fdf6ee">{fav}</div>
            <div style="text-align:left"><div style="font-family:'DM Mono';font-size:14px;color:#4a3524">{dom}</div><div style="font-family:'DM Mono';font-size:12px;color:#a08a68">{date}</div></div>
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M10 14L21 3M15 3h6v6M21 14v5a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5"/></svg>
          </div>
        </div>'''
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {ihead("Every figure traces to a source","SOURCED . DATED")}
      <div style="display:flex;flex-direction:column;gap:16px">{body}</div>
      {cap("reports on the desk carry the link and the date, named, not recalled.","#8a745a")}</div>'''

# 3. BRIEF10 - ISO STACK of account-brief cards, each a quoted line with its source line
def brief10():
    rows=[("hiring 3 ops roles","linkedin.com/jobs","2026-07-02"),
          ("closed Series A, $4.2M","crunchbase.com","2026-06-30"),
          ("shipped SOC 2 page","northwind.io/trust","2026-06-18")]
    cards=""
    for i,(q,src,date) in enumerate(rows):
        y=i*138
        cards+=f'''<div style="position:absolute;left:0;top:{y}px;width:600px;
          background:linear-gradient(160deg,#413b35,#2b2723);border:1.5px solid rgba(255,255,255,.14);border-radius:18px;padding:18px 22px;
          box-shadow:0 32px 48px rgba(0,0,0,.58), inset 0 2px 2px rgba(255,255,255,.1)">
          <div style="display:flex;align-items:baseline;gap:12px">
            <span style="font-family:'DM Sans';font-weight:800;font-size:23px;color:#FAFAF7;line-height:1.15">"{q}"</span></div>
          <div style="display:flex;align-items:center;gap:10px;margin-top:9px">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round"><path d="M9 17H7A5 5 0 0 1 7 7h2M15 7h2a5 5 0 0 1 0 10h-2M8 12h8"/></svg>
            <span style="font-family:'DM Mono';font-size:14px;color:rgb({ACC})">{src}</span>
            <span style="font-family:'DM Mono';font-size:13px;color:#8f8f85">. {date}</span></div>
        </div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 44px 34px">
      {htitle("The brief quotes, it does not recall","ACCOUNT BRIEF")}
      <div style="perspective:2000px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(21deg) rotateZ(-9deg);width:600px;height:440px;position:relative">{cards}</div></div>
      {cap("role, date and link land inside the brief, not a paraphrase of them.")}</div>'''

# 4. NUMBERS10 - GAUGE bank (ivory): three semicircle dials pulled live, each with its source, cents cost
def numbers10():
    r=104; full=math.pi*r
    dials=[("REVENUE","$182K","stripe",0.74),("PIPELINE","$540K","hubspot",0.61),("SPEND","$9.4K","mercury",0.38)]
    cxs=[172,410,648]; cy=176
    arcs=""
    for (lab,val,src,p),cx in zip(dials,cxs):
        d=f"M{cx-r} {cy} A{r} {r} 0 0 1 {cx+r} {cy}"
        arcs+=(f'<path d="{d}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="15" stroke-linecap="round"/>'
          f'<path d="{d}" fill="none" stroke="#96562d" stroke-width="15" stroke-linecap="round" stroke-dasharray="{full*p:.0f} {full:.0f}"/>'
          f'<text x="{cx}" y="{cy-30}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="34" fill="#2a2016">{val}</text>'
          f'<text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".08em" fill="#a08a68">{lab}</text>'
          f'<g transform="translate({cx},{cy+30})">'
          f'<rect x="-58" y="0" width="116" height="30" rx="9" fill="rgba(150,86,45,.10)" stroke="rgba(150,86,45,.22)"/>'
          f'<circle cx="-40" cy="15" r="4.5" fill="#96562d"/>'
          f'<text x="-26" y="20" font-family="DM Mono" font-size="13" fill="#4a3524">{src}, live</text></g>')
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {ihead("Month-end pulls live","LIVE . SOURCED")}
      <svg width="820" height="250" viewBox="0 0 820 250" style="display:block;margin:0 auto">{arcs}</svg>
      {cap("revenue, pipeline, spend: fetched fresh for 0.4c, source attached, zero whose-sheet meetings.","#8a745a")}</div>'''

# 5. RIVALS - CRAWL / bezier graph: competitor sources converge into one dated digest
def rivals():
    W,H=820,430
    src=[("crunchbase.com","funding",92),("g2.com","pricing +18%",188),("techcrunch.com","launch",284),("producthunt.com","new tier",380)]
    hubx,huby=628,236; edges=""; nodes=""
    for dom,move,y in src:
        mx=(180+hubx)/2
        edges+=f'<path d="M186 {y} C{mx:.0f} {y},{mx:.0f} {huby},{hubx-72} {huby}" stroke="rgba({ACC},.5)" stroke-width="2.5" fill="none"/>'
        nodes+=(f'<rect x="40" y="{y-28}" width="146" height="56" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>'
          f'<text x="52" y="{y-4}" font-family="DM Mono" font-size="14" fill="#e2dccf">{dom}</text>'
          f'<text x="52" y="{y+16}" font-family="DM Sans" font-weight="700" font-size="14" fill="rgb({ACC})">{move}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Rival moves, dated and linked","COMPETITOR DIGEST")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
        <defs><radialGradient id="hub" cx="35%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gh" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {edges}{nodes}
        <g filter="url(#gh)"><circle cx="{hubx}" cy="{huby}" r="74" fill="url(#hub)"/></g>
        <text x="{hubx}" y="{huby-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="22" fill="#1a0f0a">DIGEST</text>
        <text x="{hubx}" y="{huby+18}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2416">Mon 07:00</text>
      </svg>
      {cap("price changes and launches arrive with receipts, not rumors.")}</div>'''

# 6. TRUST10 - COMPARISON: a guess that stays on the desk vs a receipt that travels (delegable)
def trust10():
    def col(kind,head,line,foot,bad):
        c=RED if bad else ACC
        icon=('<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="rgb('+c+')" stroke-width="2.6" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>' if bad
              else '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="rgb('+c+')" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M6 12.5l3.5 3.5L18 7.5"/></svg>')
        return f'''<div style="flex:1;background:{"rgba("+RED+",.05)" if bad else "linear-gradient(160deg,#332f2a,#211e1a)"};
          border:1px solid {"rgba("+RED+",.3)" if bad else "rgba("+ACC+",.32)"};border-radius:22px;padding:26px 24px;text-align:left">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:16px">{icon}
            <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({c})">{kind}</span></div>
          <div style="font-family:'DM Sans';font-weight:900;font-size:26px;color:{"#b58a78" if bad else "#FAFAF7"};line-height:1.15">{head}</div>
          <div style="font-family:'DM Sans';font-size:18px;color:#a8a296;margin-top:10px;line-height:1.4">{line}</div>
          <div style="margin-top:20px;padding-top:16px;border-top:1px solid rgba(255,255,255,.09);font-family:'DM Mono';font-size:14px;color:rgb({c})">{foot}</div>
        </div>'''
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Cited output is delegable output","VERIFY . FORWARD")}
      <div style="display:flex;align-items:stretch;gap:20px">
        {col("UNCITED GUESS","Stays on your desk","No source to check, so nobody else can act on it.","you re-verify it yourself",True)}
        {col("SOURCED CLAIM","Travels to the team","Link and date attached, forward it and they run.","hand it off, it holds up",False)}
      </div>
      {cap("you can only delegate what someone else can verify; receipts travel, guesses do not.")}</div>'''

# 7. HABIT10 - RADIAL HUB: set the source rule ONCE (center), every later output cites forever
def habit10():
    cx,cy=410,222; R=158
    labels=["brief","email","report","memo","deck","recap"]
    spokes=""; nodes=""
    for i,nm in enumerate(labels):
        a=-90+i*60
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        spokes+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba({ACC},.4)" stroke-width="2.5"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#241f1a" stroke="rgba({ACC},.4)" stroke-width="1.5"/>'
          f'<svg x="{x-13:.0f}" y="{y-24:.0f}" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 12.5l3.5 3.5L16 7.5"/></svg>'
          f'<text x="{x:.0f}" y="{y+22:.0f}" text-anchor="middle" font-family="DM Mono" font-size="13" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Set the standard once","THEN FOREVER")}
      <svg width="820" height="450" viewBox="0 0 820 450" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
        {spokes}{nodes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="76" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">CITE THE</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#1a0f0a">SOURCE</text>
        <text x="{cx}" y="{cy+92}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="rgb({ACC})">asked one time</text>
      </svg>
      {cap("one instruction sets the rule; every later output carries a source without asking.")}</div>'''

# 8. LINE10 - DOT FIELD: knowledge with a date lit, undated facts flagged red (closing verdict)
def line10():
    cols,rowsn=26,9   # 234
    flagged={41,88,120,167,199,212}
    cell=17; gap=6
    dots=""
    for i in range(cols*rowsn):
        r,c=divmod(i,cols); x=c*(cell+gap); y=r*(cell+gap)
        if i in flagged:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgb({RED})" filter="url(#rg)"/>'
        else:
            dots+=f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="4" fill="rgba({ACC},.82)"/>'
    fw=cols*(cell+gap)-gap; fh=rowsn*(cell+gap)-gap
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:20px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#FAFAF7">If it cannot say when, it does not know</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:rgb({RED})">6 UNDATED</span></div>
      <div style="display:flex;align-items:center;gap:34px">
        <svg width="{fw}" height="{fh}" viewBox="0 0 {fw} {fh}" style="flex-shrink:0">
          <defs><filter id="rg" x="-300%" y="-300%" width="700%" height="700%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({RED})" flood-opacity="1"/></filter></defs>
          {dots}</svg>
        <div style="flex:1">
          <div style="font-family:'DM Sans';font-weight:900;font-size:52px;color:#FAFAF7;line-height:1">228</div>
          <div style="font-family:'DM Sans';font-weight:700;font-size:19px;color:#c9a583">facts on the desk, dated</div>
          <div style="display:flex;align-items:center;gap:12px;margin-top:18px">
            <span style="width:15px;height:15px;border-radius:4px;background:rgb({RED});box-shadow:0 0 12px rgba({RED},.8)"></span>
            <span style="font-family:'DM Sans';font-size:18px;color:#b58a78">6 undated, held back</span></div>
        </div>
      </div>
      {cap("undated knowledge is opinion wearing a suit; the desk flags it before you send.")}</div>'''

PANELS={"stale":stale(),"standard":standard(),"brief10":brief10(),"numbers10":numbers10(),
        "rivals":rivals(),"trust10":trust10(),"habit10":habit10(),"line10":line10()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/citedweb"; os.makedirs(outd,exist_ok=True)
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
