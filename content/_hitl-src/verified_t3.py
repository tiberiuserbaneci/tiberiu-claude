#!/usr/bin/env python3
# TIER 3 - I CHECKED THE LISTS, built to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tagc=f"rgb({ACC})"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tagc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. FLOOD - a fanned hand of IDENTICAL repost cards pinned at the bottom (the same recycled list,
# on repeat), the front card stamped "0 RECEIPTS" in muted red. No verification anywhere.
def flood():
    reposts=[("@ai_daily","2d"),("@toolstack","3d"),("@promptclub","0d"),("@skillfeed","4d"),("@growth_x","5d")]
    n=len(reposts); mid=(n-1)/2
    cards=""
    for i,(acct,ago) in enumerate(reposts):
        rot=(i-mid)*11; front=(i==int(mid))
        bg="linear-gradient(160deg,#35312c,#221f1b)" if front else "linear-gradient(160deg,#2a2723,#1c1a17)"
        op=1 if front else .82
        cards+=(f'<div style="position:absolute;left:50%;bottom:0;width:430px;margin-left:-215px;'
          f'transform-origin:bottom center;transform:rotate({rot}deg);opacity:{op};'
          f'background:{bg};border:1px solid rgba(255,255,255,.10);border-radius:18px;padding:20px 22px;'
          f'box-shadow:0 26px 40px rgba(0,0,0,.5), inset 0 2px 2px rgba(255,255,255,.08)">'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#e9e3d6">TOP 50 AI SKILLS</div>'
          f'<div style="font-family:DM Mono;font-size:12px;color:#8f8f85;margin-top:4px">copy-paste list &middot; {acct} &middot; {ago}</div>'
          + "".join(f'<div style="height:7px;border-radius:4px;background:rgba(250,250,247,.08);margin-top:9px;width:{w}%"></div>' for w in (94,80,88))
          + '<div style="font-family:DM Mono;font-size:11px;letter-spacing:.14em;color:#7a746a;margin-top:12px">REPOSTED &middot; NO SOURCE</div>'
          + (f'<div style="position:absolute;top:72px;left:26px;font-family:DM Sans;font-weight:900;font-size:32px;letter-spacing:.06em;color:rgba(200,70,35,.9);transform:rotate(-11deg);border:3px solid rgba(200,70,35,.75);border-radius:10px;padding:4px 14px">0 RECEIPTS</div>' if front else '')
          + '</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("The same list, on repeat","RECYCLED FEED")}
      <div style="position:relative;height:470px">{cards}</div>
      {cap("fifty skills per card, reposted daily. nobody installs them, nobody verifies them.")}</div>'''

# 2. TEST - a 7-day timeline, every skill run on real work (briefs, drafts, builds, audits)
def test():
    days=[("MON","brief","cortex"),("TUE","draft","specter"),("WED","build","sentinel"),
          ("THU","audit","striker"),("FRI","draft","pulse"),("SAT","build","sentinel"),("SUN","audit","counsel")]
    W,H=820,430; x0=20; lane=(W-x0*2)/7
    lines=f'<line x1="{x0}" y1="70" x2="{W-x0}" y2="70" stroke="rgba(212,162,127,.35)" stroke-width="2"/>'
    cells=""
    for i,(d,job,who) in enumerate(days):
        cx=x0+lane*i+lane/2
        lines+=f'<circle cx="{cx:.0f}" cy="70" r="7" fill="rgb({ACC})"/><line x1="{cx:.0f}" y1="77" x2="{cx:.0f}" y2="118" stroke="rgba(212,162,127,.3)" stroke-width="2"/>'
        lines+=f'<text x="{cx:.0f}" y="46" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".1em" fill="#c9c3b8">{d}</text>'
        cells+=(f'<foreignObject x="{cx-lane/2+8:.0f}" y="120" width="{lane-16:.0f}" height="250">'
          f'<div xmlns="http://www.w3.org/1999/xhtml" style="background:linear-gradient(160deg,#37322c,#221f1b);border:1px solid rgba(255,255,255,.10);border-radius:14px;padding:14px 8px;height:100%;box-shadow:0 16px 28px rgba(0,0,0,.45), inset 0 2px 2px rgba(255,255,255,.07);display:flex;flex-direction:column;align-items:center;text-align:center">'
          f'<div style="width:36px;height:36px;border-radius:10px;background:rgba(212,162,127,.16);border:1px solid rgba(212,162,127,.34);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:17px;color:rgb({ACC})">{job[0].upper()}</div>'
          f'<div style="font-family:DM Sans;font-weight:800;font-size:18px;color:#FAFAF7;margin-top:12px">{job}</div>'
          f'<div style="font-family:DM Mono;font-size:11px;color:#8f8f85;margin-top:4px">{who}</div>'
          f'<div style="margin-top:auto;font-family:DM Mono;font-size:11px;letter-spacing:.08em;color:rgb({ACC})">RAN</div></div></foreignObject>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every skill, on real work","7 DAYS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">{lines}{cells}</svg>
      {cap("one week, each skill run on a live task: briefs, drafts, builds, audits.")}</div>'''

# 3. FAKES - a ring gauge, one third severed in muted red, three failure reasons beside it
def fakes():
    r=104; circ=2*math.pi*r; fake=circ/3
    reasons=[("Dead links","point at nothing"),("Renamed duplicates","one skill, five names"),("Answers, no action","talks instead of runs")]
    rows=""
    for t,s in reasons:
        rows+=(f'<div style="display:flex;align-items:flex-start;gap:14px;margin-bottom:18px">'
          f'<svg width="26" height="26" viewBox="0 0 24 24" style="flex-shrink:0;margin-top:2px"><circle cx="12" cy="12" r="11" fill="rgba(200,70,35,.14)"/><path d="M8 8l8 8M16 8l-8 8" stroke="rgb(200,70,35)" stroke-width="2.4" stroke-linecap="round"/></svg>'
          f'<div><div style="font-family:DM Sans;font-weight:800;font-size:19px;color:#FAFAF7">{t}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#8f8f85;margin-top:1px">{s}</div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:40px">
      <div style="flex-shrink:0;position:relative;width:250px;height:250px">
        <svg width="250" height="250" viewBox="0 0 250 250">
          <circle cx="125" cy="125" r="{r}" fill="none" stroke="rgb({ACC})" stroke-width="26"/>
          <circle cx="125" cy="125" r="{r}" fill="none" stroke="rgb(200,70,35)" stroke-width="26" stroke-linecap="butt" stroke-dasharray="{fake:.0f} {circ:.0f}" transform="rotate(-90 125 125)"/></svg>
        <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
          <span style="font-family:DM Sans;font-weight:900;font-size:54px;color:#FAFAF7;line-height:1">17</span>
          <span style="font-family:DM Mono;font-size:13px;letter-spacing:.1em;color:rgb(200,70,35)">OF 50 FAKE</span></div></div>
      <div style="flex:1">
        {htitle("A third were made up","FAILED CHECK")}
        {rows}
        {cap("dead links, renamed duplicates, skills that answer instead of execute.")}</div></div>'''

# 4. KEEPERS - IVORY isometric stack of the four survivor categories, each with a count
def keepers():
    steps=[("WRITING","posts, emails, replies","4"),("RESEARCH","icp, accounts, markets","3"),
           ("DESIGN","pages, decks, assets","3"),("BUILD","features, fixes, audits","2")]
    cards=""
    for i,(nm,sub,c) in enumerate(steps):
        y=i*118
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:560px;background:linear-gradient(160deg,#fffdf9,#efe4d1);border:1.5px solid rgba(120,95,60,.22);border-radius:18px;padding:18px 22px;box-shadow:0 28px 42px rgba(120,95,60,.28), inset 0 2px 2px rgba(255,255,255,.9);display:flex;align-items:center;gap:20px">'
          f'<div style="flex-shrink:0;width:52px;height:52px;border-radius:14px;background:#96562d;display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:24px;color:#fdf6ec;box-shadow:0 8px 16px rgba(150,86,45,.4)">{c}</div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:#96562d">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:20px;color:#2a2016;margin-top:2px">{sub}</div></div>'
          f'<svg width="26" height="26" viewBox="0 0 24 24" style="flex-shrink:0"><path d="M6 12.5l3.5 3.5L18 7.5" fill="none" stroke="#96562d" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("What survived earns its slot","SHORTLIST",ink="#2a2016",tagc="#96562d")}
      <div style="perspective:1900px;height:470px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(19deg) rotateZ(-8deg);width:560px;height:420px;position:relative">{cards}</div></div>
      {cap("writing, research, design, build: the twelve that actually finish work.","#8a745a")}</div>'''

# 5. SAFEST - radial trust order: an Anthropic first-party core, a verified community ring around it
def safest():
    cx,cy=306,225; R=158
    comm=["templates","review","summarize","extract","classify","convert"]
    nodes=""; lines=""
    for i,nm in enumerate(comm):
        a=-90+i*60
        x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="42" fill="#221f1b" stroke="rgba(212,162,127,.4)" stroke-width="1.6"/>'
          f'<text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("First-party core, then the rest","TRUST ORDER")}
      <svg width="612" height="470" viewBox="0 0 612 470" style="display:block;margin:0 auto">
        <defs><radialGradient id="core" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="cg" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        <circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="rgba(212,162,127,.12)" stroke-dasharray="4 9"/>
        {lines}{nodes}
        <g filter="url(#cg)"><circle cx="{cx}" cy="{cy}" r="78" fill="url(#core)"/></g>
        <text x="{cx}" y="{cy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">2</text>
        <text x="{cx}" y="{cy+22}" text-anchor="middle" font-family="DM Mono" font-size="12.5" letter-spacing=".1em" fill="#3a2010">ANTHROPIC</text>
      </svg>
      {cap("start with the two built by anthropic, then the verified community layer.")}</div>'''

# 6. CURATED - a verify pipeline: raw skills in, a VERIFY gate, out to the Ultron techniques shelf
def curated():
    W,H=820,430
    raw=[("random-skill",96),("dead-link",210),("dupe-v3",324)]
    inp=""; edges=""
    for nm,y in raw:
        edges+=f'<path d="M196 {y} C300 {y},300 215,368 215" fill="none" stroke="rgba(212,162,127,.35)" stroke-width="2.2"/>'
        inp+=(f'<rect x="24" y="{y-26}" width="172" height="52" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.09)"/>'
          f'<text x="110" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#9a9488">{nm}</text>')
    shelf=[("cold-email","tested"),("icp-research","tested"),("landing-page","tested")]
    rows=""
    for i,(nm,st) in enumerate(shelf):
        y=118+i*70
        rows+=(f'<rect x="590" y="{y}" width="206" height="54" rx="13" fill="#241f1a" stroke="rgba(212,162,127,.3)"/>'
          f'<text x="606" y="{y+34}" font-family="DM Sans" font-weight="700" font-size="17" fill="#FAFAF7">{nm}</text>'
          f'<circle cx="770" cy="{y+27}" r="6" fill="rgb({ACC})"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Curated before your desk","PRE-VERIFIED")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="gate" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#403a33"/><stop offset="100%" stop-color="#211e1a"/></linearGradient>
        <filter id="gg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.35"/></filter></defs>
        {edges}{inp}
        <g filter="url(#gg)"><rect x="368" y="120" width="150" height="190" rx="26" fill="url(#gate)" stroke="rgb({ACC})" stroke-width="2.5"/></g>
        <g transform="translate(420,178)"><path d="M9 20l7 7 15 -18" fill="none" stroke="rgb({ACC})" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>
        <text x="443" y="252" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#FAFAF7">VERIFY</text>
        <text x="443" y="280" text-anchor="middle" font-family="DM Mono" font-size="12" fill="rgb({ACC})">run + check</text>
        <rect x="518" y="211" width="52" height="8" rx="4" fill="rgb({ACC})" opacity="0.85"/>
        <text x="590" y="102" font-family="DM Mono" font-size="13" letter-spacing=".14em" fill="rgb({ACC})">ULTRON TECHNIQUES</text>
        {rows}
      </svg>
      {cap("the techniques library is curated and tested before it reaches your desk.")}</div>'''

# 7. RULE - IVORY split verdict: returns advice (a bookmark, dropped) vs finishes work (kept)
def rule():
    def col(head,line,foot,ok):
        ic=('<svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M6 12.5l3.5 3.5L18 7.5"/></svg>' if ok
            else '<svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="rgb(200,70,35)" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h12v18l-6-4-6 4z"/></svg>')
        tag=("KEEP" if ok else "DROP"); tagc=("#96562d" if ok else "rgb(200,70,35)")
        bg=("rgba(150,86,45,.10)" if ok else "rgba(200,70,35,.08)")
        bd=("rgba(150,86,45,.34)" if ok else "rgba(200,70,35,.32)")
        return (f'<div style="flex:1;background:{bg};border:1.5px solid {bd};border-radius:20px;padding:26px 24px;display:flex;flex-direction:column;align-items:flex-start">'
          f'<div style="display:flex;align-items:center;justify-content:space-between;width:100%">{ic}'
          f'<span style="font-family:DM Mono;font-size:13px;letter-spacing:.16em;color:{tagc}">{tag}</span></div>'
          f'<div style="font-family:DM Sans;font-weight:900;font-size:26px;color:#2a2016;margin-top:20px;line-height:1.15">{head}</div>'
          f'<div style="font-family:DM Sans;font-size:18px;color:#5a4634;margin-top:8px;line-height:1.4">{line}</div>'
          f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.08em;color:{tagc};margin-top:18px">{foot}</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("Advice is just a bookmark","EXECUTE TEST",ink="#2a2016",tagc="#96562d")}
      <div style="display:flex;align-items:stretch;gap:22px;height:410px">
        {col("Returns advice","It answers your question and stops. You still have to do the work.","0 work done",False)}
        {col("Finishes the work","It ships the draft, the page, the audit. The task is closed.","task closed",True)}
      </div>
      {cap("a skill that returns advice is a bookmark. keep the ones that finish work.","#8a745a")}</div>'''

# 8. DESK - a 12-tile survivor dashboard, every kept skill lit and named, running daily
def desk():
    skills=["cold-email","icp-research","deal-notes","landing-page","post-draft","doc-audit",
            "pricing-calc","seq-builder","brief-gen","pr-review","objections","close-plan"]
    tiles=""
    for nm in skills:
        tiles+=(f'<div style="background:linear-gradient(160deg,#37322c,#221f1b);border:1px solid rgba(212,162,127,.26);border-radius:16px;padding:16px 16px;display:flex;align-items:center;gap:12px;box-shadow:0 16px 28px rgba(0,0,0,.42), inset 0 2px 2px rgba(255,255,255,.07)">'
          f'<span style="flex-shrink:0;width:12px;height:12px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 12px rgba({ACC},.8)"></span>'
          f'<span style="font-family:DM Mono;font-size:15px;color:#eae4d8">{nm}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("My desk runs on survivors","12 LIVE")}
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;padding:8px 0 6px">{tiles}</div>
      {cap("twelve skills, each tested on my own pipeline, running daily.")}</div>'''

PANELS={"flood":flood(),"test":test(),"fakes":fakes(),"keepers":keepers(),
        "safest":safest(),"curated":curated(),"rule":rule(),"desk":desk()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/verified"; os.makedirs(outd,exist_ok=True)
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
