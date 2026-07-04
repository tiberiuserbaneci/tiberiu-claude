#!/usr/bin/env python3
# TIER 3 - IT REFUSES TO INVENT (grounded expert, zero hallucination), rebuilt to the WIRE-ITS-EYES
# bar: each panel a UNIQUE hand-built coded scene filling a clean rounded card, title + one-line
# caption, NO generic stat-chip strips. Warm palette only, muted red for the bad/ungrounded state.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
RED="rgb(200,70,35)"
IVACC="#96562d"; IVINK="#2a2016"; IVSUB="#8a745a"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def htiv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{IVINK}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{IVACC}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. LIAR - confidence ring pegged at 100% (RED), next to a fabricated answer stamped 0 sources
def liar():
    pct=100; r=76; circ=2*math.pi*r; dash=circ*pct/100
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It sounded certain","0 SOURCES")}
      <div style="display:flex;align-items:center;gap:40px;height:430px">
        <div style="flex-shrink:0;position:relative;width:212px;height:212px">
          <svg width="212" height="212" viewBox="0 0 212 212">
            <circle cx="106" cy="106" r="{r}" fill="none" stroke="rgba(200,70,35,.15)" stroke-width="16"/>
            <circle cx="106" cy="106" r="{r}" fill="none" stroke="{RED}" stroke-width="16" stroke-linecap="round" stroke-dasharray="{dash:.0f} {circ:.0f}" transform="rotate(-90 106 106)"/></svg>
          <div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center">
            <span style="font-family:DM Sans;font-weight:900;font-size:48px;color:#FAFAF7">{pct}%</span>
            <span style="font-family:DM Mono;font-size:12px;letter-spacing:.08em;color:{RED}">confidence</span></div></div>
        <div style="flex:1">
          <div style="background:#211d19;border:1px solid rgba(255,255,255,.09);border-radius:16px;padding:22px 24px;font-family:DM Sans;font-size:23px;color:#e7e2d8;line-height:1.4">"Your refund window is 45 days."</div>
          <div style="display:inline-flex;align-items:center;gap:10px;margin-top:18px;background:rgba(200,70,35,.12);border:1px solid rgba(200,70,35,.5);border-radius:999px;padding:10px 20px">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="{RED}" stroke-width="2.6"><circle cx="12" cy="12" r="9"/><path d="M15 9l-6 6M9 9l6 6"/></svg>
            <span style="font-family:DM Mono;font-size:14px;letter-spacing:.06em;color:{RED}">UNVERIFIED &middot; NOT IN YOUR DOCS</span></div>
          <div style="font-family:DM Sans;font-size:18px;color:#8f8f85;margin-top:18px">Your real policy says 30. It invented the rest.</div>
        </div></div>
      {cap("generic AI answers with total confidence and zero sources behind it.")}</div>'''

# 2. VAULT - IVORY: stack of your real source cards feeding one private vault box
def vault():
    srcs=[("PDF","product docs"),("ARTICLE","your blog"),("TRANSCRIPT","sales calls"),("REPLIES","past support")]
    rows=""
    for nm,sub in srcs:
        rows+=(f'<div style="background:linear-gradient(160deg,#fffdf8,#f1e8d8);border:1px solid rgba(120,95,60,.22);border-radius:15px;padding:15px 18px;margin-bottom:14px;box-shadow:0 14px 24px rgba(120,95,60,.14);display:flex;align-items:center;gap:15px">'
          f'<div style="flex-shrink:0;width:42px;height:42px;border-radius:11px;background:rgba(150,86,45,.12);border:1px solid rgba(150,86,45,.32);display:flex;align-items:center;justify-content:center"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="{IVACC}" stroke-width="2"><path d="M6 2h9l5 5v15H6z"/><path d="M14 2v6h6"/></svg></div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:12.5px;letter-spacing:.1em;color:{IVACC}">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:18px;color:{IVINK}">{sub}</div></div></div>')
    vaultbox=(f'<div style="flex-shrink:0;width:250px;background:linear-gradient(160deg,#a5643a,#7a4425);border-radius:22px;padding:26px 22px;box-shadow:0 30px 50px rgba(120,70,35,.4), inset 0 2px 3px rgba(255,255,255,.2);text-align:center">'
      f'<svg width="58" height="58" viewBox="0 0 24 24" fill="none" stroke="#fdf3e7" stroke-width="1.7" style="margin:2px auto 12px"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/></svg>'
      f'<div style="font-family:DM Sans;font-weight:900;font-size:24px;color:#fff6ec;letter-spacing:.02em">PRIVATE VAULT</div>'
      f'<div style="font-family:DM Mono;font-size:13px;color:#f2d9c2;margin-top:6px">your grounded truth</div></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htiv("Feed it your real sources","THE VAULT")}
      <div style="display:flex;align-items:center;gap:26px;height:400px">
        <div style="flex:1">{rows}</div>
        <svg width="52" height="34" viewBox="0 0 52 34"><path d="M2 17h44M36 6l12 11-12 11" fill="none" stroke="{IVACC}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg>
        {vaultbox}
      </div>
      {cap("PDFs, calls, docs and past replies. its truth, not the open web.",IVSUB)}</div>'''

# 3. GROUNDED - radial hub: one EXPERT core, spokes to your sources, every lifeline warm/intact
def grounded():
    cx,cy=214,214
    srcs=[("docs",-90),("blog",-30),("calls",30),("pricing",90),("FAQ",150),("replies",210)]
    lines=""; nodes=""
    for nm,a in srcs:
        x=cx+152*math.cos(math.radians(a)); y=cy+152*math.sin(math.radians(a))
        lines+=f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="rgba(212,162,127,.5)" stroke-width="3"/>'
        nodes+=(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="31" fill="#241f1a" stroke="rgba(212,162,127,.4)" stroke-width="2"/>'
          f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#cfc9bd">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:22px">
      <svg width="428" height="428" viewBox="0 0 428 428">
        <defs><radialGradient id="gc" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="gg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
        {lines}<g filter="url(#gg)"><circle cx="{cx}" cy="{cy}" r="58" fill="url(#gc)"/></g>
        <text x="{cx}" y="{cy-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">EXPERT</text>
        <text x="{cx}" y="{cy+18}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">grounded</text>
        {nodes}</svg>
      <div style="flex:1">
        {htitle("An expert on your world","BUILT ON YOU")}
        <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;line-height:1.45">It reads only what you fed the vault. Every spoke is a real source, nothing lives outside the ring.</div>
        {cap("built only on what you gave it. grounded, not guessing.")}</div></div>'''

# 4. CITE - IVORY ledger: answer with inline citation chips, mapped to real source rows
def cite():
    def chip(n): return f'<span style="display:inline-flex;align-items:center;justify-content:center;min-width:22px;height:22px;background:{IVACC};color:#fff6ec;font-family:DM Mono;font-size:12px;font-weight:500;border-radius:6px;padding:0 5px;vertical-align:2px;margin:0 2px">{n}</span>'
    ans=(f'<div style="background:rgba(255,255,255,.62);border-left:4px solid {IVACC};border-radius:12px;padding:20px 22px;font-family:DM Sans;font-size:21px;color:{IVINK};line-height:1.5">'
      f'Refunds run 30 days{chip(1)}, minus a 4% fee{chip(2)}, processed in your dashboard{chip(3)}.</div>')
    srcs=[("1","refund-policy.pdf","p.2, line 14"),("2","pricing.md","clause 3b"),("3","support-log.csv","row 812")]
    rows=""
    for n,f,loc in srcs:
        rows+=(f'<div style="display:flex;align-items:center;gap:14px;padding:13px 0;border-bottom:1px solid rgba(120,95,60,.16)">'
          f'<span style="display:inline-flex;align-items:center;justify-content:center;width:26px;height:26px;background:rgba(150,86,45,.14);border:1px solid rgba(150,86,45,.34);color:{IVACC};font-family:DM Mono;font-size:13px;border-radius:7px">{n}</span>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:18px;color:{IVINK}">{f}</span>'
          f'<span style="font-family:DM Mono;font-size:13px;color:{IVSUB}">{loc}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htiv("Every claim carries a source","CITED")}
      {ans}
      <div style="margin-top:20px">{rows}</div>
      {cap("click any sentence, see the exact line it came from. trace every word.",IVSUB)}</div>'''

# 5. DECLINE - routing fork: a query hits an in-sources gate, answers cited OR declines (RED)
def decline():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("No source, no answer","THE GUARDRAIL")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><filter id="dg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <rect x="16" y="182" width="150" height="56" rx="14" fill="#2a2724" stroke="rgba(255,255,255,.12)"/>
        <text x="91" y="208" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="16" fill="#e7e2d8">a question</text>
        <text x="91" y="228" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#8f8f85">comes in</text>
        <line x1="166" y1="210" x2="300" y2="210" stroke="rgba(212,162,127,.5)" stroke-width="3"/>
        <g filter="url(#dg)"><path d="M370 148 L438 210 L370 272 L302 210 Z" fill="#332c25" stroke="rgb({ACC})" stroke-width="2.5"/></g>
        <text x="370" y="205" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">in your</text>
        <text x="370" y="224" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="#FAFAF7">vault?</text>
        <path d="M438 195 C540 150,560 96,640 96" fill="none" stroke="rgb({ACC})" stroke-width="3.4"/>
        <text x="512" y="120" font-family="DM Mono" font-size="13" fill="rgb({ACC})">yes</text>
        <path d="M438 225 C540 270,560 324,640 324" fill="none" stroke="rgba(200,70,35,.7)" stroke-width="3.4" stroke-dasharray="4 8"/>
        <text x="512" y="316" font-family="DM Mono" font-size="13" fill="rgb(200,70,35)">no</text>
        <rect x="640" y="58" width="164" height="80" rx="16" fill="rgba(212,162,127,.1)" stroke="rgb({ACC})" stroke-width="2"/>
        <text x="722" y="94" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="rgb({ACC})">ANSWER</text>
        <text x="722" y="118" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">with citations</text>
        <rect x="640" y="286" width="164" height="80" rx="16" fill="rgba(200,70,35,.1)" stroke="rgb(200,70,35)" stroke-width="2"/>
        <text x="722" y="322" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="rgb(200,70,35)">DECLINE</text>
        <text x="722" y="346" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#b98a76">"not in your sources"</text>
      </svg>
      {cap("when the vault has no answer it says so, instead of inventing one.")}</div>'''

# 6. FIELD - dense dot field: a week of answers, all grounded, zero invented
def field():
    cols,rows_n=24,11; sp=32; dots=""
    for r in range(rows_n):
        for c in range(cols):
            x=8+c*sp; y=8+r*sp
            dots+=f'<circle cx="{x}" cy="{y}" r="8.5" fill="rgb({ACC})" opacity="{0.62+((c*7+r*3)%5)*0.075:.2f}"/>'
    w=8+(cols-1)*sp+9; h=8+(rows_n-1)*sp+9
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A week of answers","ALL GROUNDED")}
      <div style="display:flex;align-items:center;gap:34px;height:420px">
        <svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="flex-shrink:0">{dots}</svg>
        <div style="flex:1">
          <div style="font-family:DM Sans;font-weight:900;font-size:66px;color:rgb({ACC});line-height:.9">264</div>
          <div style="font-family:DM Sans;font-size:19px;color:#c9c3b8;margin-top:6px">answers shipped this week</div>
          <div style="height:1px;background:rgba(255,255,255,.1);margin:22px 0"></div>
          <div style="display:flex;align-items:baseline;gap:12px"><span style="font-family:DM Sans;font-weight:900;font-size:40px;color:#FAFAF7">0</span><span style="font-family:DM Sans;font-size:18px;color:#8f8f85">invented</span></div>
          <div style="font-family:DM Mono;font-size:13px;color:rgb({ACC});margin-top:6px">each traces to a real source line</div>
        </div></div>
      {cap("every reply this week traced back to a real line in your vault.")}</div>'''

# 7. EXPERTS - org tree: one vault root branching to the named expert agents
def experts():
    kids=[("CORTEX","research"),("SPECTER","outbound"),("STRIKER","deals"),("PULSE","content"),("COUNSEL","legal")]
    rootx,rooty=410,58; kw=140; centers=[92,251,410,569,728]; ky=300
    edges=""
    for (nm,role),kx in zip(kids,centers):
        edges+=f'<path d="M{rootx} 106 C{rootx} 210,{kx} 200,{kx} {ky-6}" fill="none" stroke="rgba(212,162,127,.4)" stroke-width="2.5"/>'
    kboxes=""
    for (nm,role),kx in zip(kids,centers):
        kboxes+=(f'<div style="position:absolute;left:{kx-kw/2:.0f}px;top:{ky}px;width:{kw}px;height:92px;background:linear-gradient(160deg,#332c25,#241f1a);border:1.5px solid rgba(212,162,127,.32);border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:0 18px 30px rgba(0,0,0,.4)">'
          f'<div style="font-family:DM Mono;font-size:13px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div>'
          f'<div style="font-family:DM Sans;font-weight:700;font-size:17px;color:#FAFAF7;margin-top:2px">{role}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One vault, every expert","THE ROSTER")}
      <div style="position:relative;height:412px">
        <svg width="820" height="412" viewBox="0 0 820 412" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="rt" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="rg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          {edges}
          <g filter="url(#rg)"><rect x="{rootx-96}" y="24" width="192" height="82" rx="20" fill="url(#rt)"/></g>
          <text x="{rootx}" y="60" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="20" fill="#2a160c">YOUR VAULT</text>
          <text x="{rootx}" y="84" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">one grounded core</text>
        </svg>
        {kboxes}
      </div>
      {cap("research, outbound, deals, content and legal all read the same truth.")}</div>'''

# 8. GATE - HUMAN GATE approval queue: cited actions park for your tap before they send
def gate():
    acts=[("SPECTER","send sequence &middot; 40 contacts","tap",True),("PULSE","publish the post","queued",False),("STRIKER","send the proposal","queued",False)]
    rows=""
    for nm,txt,st,live in acts:
        if live:
            pill=f'<div style="flex-shrink:0;display:flex;align-items:center;gap:9px;background:rgb({ACC});color:#1a0f0a;font-family:DM Sans;font-weight:900;font-size:15px;padding:11px 20px;border-radius:999px;box-shadow:0 10px 22px rgba(212,162,127,.4)"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.8"><path d="M6 12.5l3.5 3.5L18 7.5"/></svg>tap to send</div>'
            bd=f"rgba(212,162,127,.5)"; glow="box-shadow:0 22px 40px rgba(0,0,0,.5), 0 0 0 1px rgba(212,162,127,.25)"
        else:
            pill=f'<div style="flex-shrink:0;display:flex;align-items:center;gap:8px;background:#221f1b;border:1px solid rgba(255,255,255,.12);color:#8f8f85;font-family:DM Mono;font-size:13px;padding:11px 18px;border-radius:999px"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#8f8f85" stroke-width="2.4"><circle cx="12" cy="12" r="9"/><path d="M12 8v4l3 2"/></svg>{st}</div>'
            bd="rgba(255,255,255,.1)"; glow="box-shadow:0 16px 28px rgba(0,0,0,.4)"
        rows+=(f'<div style="display:flex;align-items:center;gap:18px;background:linear-gradient(160deg,#2c2723,#211d19);border:1.5px solid {bd};border-radius:18px;padding:19px 22px;margin-bottom:16px;{glow}">'
          f'<div style="flex-shrink:0;width:46px;height:46px;border-radius:12px;background:rgba(212,162,127,.13);border:1px solid rgba(212,162,127,.32);display:flex;align-items:center;justify-content:center;font-family:DM Mono;font-size:11px;letter-spacing:.06em;color:rgb({ACC})">{nm[:3]}</div>'
          f'<div style="flex:1"><div style="font-family:DM Mono;font-size:12px;letter-spacing:.12em;color:rgb({ACC})">{nm}</div><div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7">{txt}</div></div>'
          f'{pill}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Cited and ready. Your call.","HUMAN GATE")}
      <div style="height:420px;display:flex;flex-direction:column;justify-content:center">{rows}
        <div style="font-family:DM Mono;font-size:13px;color:#8f8f85;text-align:center;margin-top:4px">nothing leaves the building without your tap</div>
      </div>
      {cap("every external move parks for your approval before it sends. never auto.")}</div>'''

PANELS={"liar":liar(),"vault":vault(),"grounded":grounded(),"cite":cite(),
        "decline":decline(),"field":field(),"experts":experts(),"gate":gate()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src20"; os.makedirs(outd,exist_ok=True)
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
