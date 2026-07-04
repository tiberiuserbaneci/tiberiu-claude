#!/usr/bin/env python3
# TIER 3 - THE MODEL OF THE WEEK, built to the WIRE-ITS-EYES / AIBODY bar: each of the 8 panels is a
# UNIQUE hand-coded scene on a clean rounded card (CARD dark or CARDIV ivory), htitle + one mono cap,
# NO stat-chip-strip template, NO clip-path cuts, NO extruded walls. Warm palette. Ultron = cents.
# Model tiers are abstracted to Lite / Smart / Deep (Ultron hides the vendor).
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"            # kraft accent
IVK="#96562d"               # ivory-slide accent
RED="200,70,35"            # muted red, BAD only
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7",tc=f"rgb({ACC})"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:{tc}">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:18px">{t}</div>'

# 1. CYCLE - three weekly leaderboards side by side, the crown keeps swapping model = reshuffle
def cycle():
    models={"K":"Model K","R":"Model R","V":"Model V"}
    weeks=[("TUE - WK 1",["K","R","V"],[91,89,88]),
           ("TUE - WK 2",["R","V","K"],[92,90,87]),
           ("TUE - WK 3",["V","K","R"],[93,90,88])]
    crown='<svg width="20" height="20" viewBox="0 0 24 24" style="flex-shrink:0"><path d="M3 8l4 4 5-8 5 8 4-4-2 12H5z" fill="#1a0f0a"/></svg>'
    cols=""
    for wk,order,scores in weeks:
        rows=""
        for j,mk in enumerate(order):
            top=(j==0)
            bg=f"linear-gradient(150deg,#e6b48f,rgb({ACC}) 60%,#a35e37)" if top else "linear-gradient(158deg,#332f2a,#221e1a)"
            bd=f"rgb({ACC})" if top else "rgba(255,255,255,.09)"
            rk=f"#1a0f0a" if top else "#8f8f85"; nmc="#1a0f0a" if top else "#e2dccf"; scc="#3a2010" if top else "rgb("+ACC+")"
            cr=crown if top else f'<span style="width:20px;flex-shrink:0"></span>'
            rows+=(f'<div style="display:flex;align-items:center;gap:10px;background:{bg};border:1.5px solid {bd};border-radius:14px;padding:12px 14px;'
                   f'box-shadow:0 10px 20px rgba(0,0,0,.4){", inset 0 2px 2px rgba(255,255,255,.35)" if top else ""}">'
                   f'{cr}<span style="font-family:DM Sans;font-weight:900;font-size:19px;color:{rk};width:16px">{j+1}</span>'
                   f'<span style="flex:1;font-family:DM Sans;font-weight:800;font-size:18px;color:{nmc}">{models[mk]}</span>'
                   f'<span style="font-family:DM Mono;font-size:14px;color:{scc}">{scores[j]}</span></div>')
        cols+=(f'<div style="flex:1;display:flex;flex-direction:column;gap:11px">'
               f'<div style="font-family:DM Mono;font-size:12px;letter-spacing:.16em;color:#9a9488;text-align:center;margin-bottom:3px">{wk}</div>{rows}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A new king every Tuesday","LEADERBOARD RESHUFFLE")}
      <div style="display:flex;gap:20px;align-items:stretch">{cols}</div>
      {cap("same three models, a different crown every week. the ranking is noise, not signal.")}</div>'''

# 2. SWITCHERS - a 4-hop migration path, each hop taxed with a red penalty, output flat unchanged
def switchers():
    W,H=820,430
    nodes=[("STACK A",90),("STACK B",283),("STACK C",476),("STACK D",670)]
    pen=["new quirks","re-prompts","new bugs"]
    ny=150; body=""
    for nm,x in nodes:
        body+=(f'<rect x="{x-64}" y="{ny-44}" width="128" height="88" rx="16" fill="url(#chip)" stroke="rgba(255,255,255,.10)"/>'
               f'<rect x="{x-40}" y="{ny-24}" width="24" height="24" rx="7" fill="rgba(212,162,127,.16)" stroke="rgba(212,162,127,.4)"/>'
               f'<circle cx="{x-28}" cy="{ny-12}" r="4" fill="rgb({ACC})"/>'
               f'<text x="{x+6}" y="{ny-6}" font-family="DM Mono" font-size="14" letter-spacing=".08em" fill="#e2dccf">{nm.split()[1]}</text>'
               f'<text x="{x}" y="{ny+30}" text-anchor="middle" font-family="DM Mono" font-size="11" letter-spacing=".1em" fill="#8f8f85">MODEL {"ABCD"[nodes.index((nm,x))]}</text>')
    for i in range(3):
        x0=nodes[i][1]+64; x1=nodes[i+1][1]-64; mx=(x0+x1)/2
        body+=(f'<path d="M{x0} {ny} H{x1-10}" stroke="rgba(212,162,127,.4)" stroke-width="2.5" fill="none"/>'
               f'<path d="M{x1-14} {ny-6} l10 6 l-10 6" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2.5"/>'
               f'<rect x="{mx-56}" y="{ny-92}" width="112" height="34" rx="9" fill="rgba(200,70,35,.12)" stroke="rgba(200,70,35,.5)"/>'
               f'<text x="{mx}" y="{ny-70}" text-anchor="middle" font-family="DM Mono" font-size="12.5" fill="rgb({RED})">+ {pen[i]}</text>'
               f'<path d="M{mx} {ny-58} V{ny-14}" stroke="rgba(200,70,35,.4)" stroke-width="1.5" stroke-dasharray="3 5"/>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("They switched stacks four times","MIGRATION TAX")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><linearGradient id="chip" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#201d1a"/></linearGradient></defs>
        {body}
        <rect x="60" y="300" width="700" height="82" rx="18" fill="#1c1a17" stroke="rgba(255,255,255,.08)"/>
        <text x="88" y="332" font-family="DM Mono" font-size="12" letter-spacing=".16em" fill="#7a746a">PIPELINE OUTPUT</text>
        <path d="M88 358 H720" stroke="rgba(212,162,127,.5)" stroke-width="3" stroke-linecap="round"/>
        <text x="410" y="380" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="16" fill="#c9c3b8">flat line - four migrations, zero difference at the customer</text>
      </svg>
      {cap("every hop bought new quirks and new bugs. the numbers that mattered never moved.")}</div>'''

# 3. TRUTH - IVORY benchmark chart: raw models converge (tight), systems do not (wide gap)
def truth():
    def bar(label,val,mx,col,vc="#2a2016",trk="rgba(150,90,45,.14)"):
        w=int(val/mx*100)
        return (f'<div style="display:flex;align-items:center;gap:16px;margin-bottom:12px">'
                f'<span style="width:132px;font-family:DM Sans;font-weight:600;font-size:17px;color:#4a3a28;text-align:right">{label}</span>'
                f'<div style="flex:1;height:26px;border-radius:8px;background:{trk};position:relative;overflow:hidden">'
                f'<div style="position:absolute;left:0;top:0;bottom:0;width:{w}%;border-radius:8px;background:{col}"></div></div>'
                f'<span style="width:44px;font-family:DM Mono;font-size:15px;color:{vc};text-align:left">{val}</span></div>')
    raw="".join(bar(l,v,100,"linear-gradient(90deg,#c89468,#96562d)") for l,v in [("Model K",90),("Model R",89),("Model V",88),("Model N",87)])
    sysrows=(bar("Naked model",41,100,"linear-gradient(90deg,#d98d72,rgb("+RED+"))",vc=f"rgb({RED})")
             +bar("On Ultron",94,100,"linear-gradient(90deg,#e6b48f,#96562d)"))
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("Models converged. Systems did not.","BENCHMARK","#2a2016",IVK)}
      <div style="display:flex;gap:26px;align-items:stretch">
        <div style="flex:1">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#96562d;margin-bottom:12px">RAW MODELS &middot; 3 PT SPREAD</div>
          {raw}
          <div style="font-family:DM Sans;font-size:14px;color:#8a745a;margin-top:6px">top four sit inside three points</div>
        </div>
        <div style="width:1px;background:rgba(150,90,45,.2)"></div>
        <div style="flex:1">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#96562d;margin-bottom:12px">SAME MODEL &middot; 53 PT SPREAD</div>
          {sysrows}
          <div style="font-family:DM Sans;font-size:14px;color:#8a745a;margin-top:6px">the wrapper is the whole gap</div>
        </div>
      </div>
      {cap("the leaderboard is a rounding error. the system around the model is the product.","#8a745a")}</div>'''

# 4. ROUTER - one goal token fans into 3 abstracted tiers, Smart picked, cents per tier
def router():
    tiers=[("LITE","quick lookups","0.02c",108,False),
           ("SMART","the daily work","0.11c",258,True),
           ("DEEP","hard judgement","0.40c",408,False)]
    hx,hy=150,208; W,H=820,470
    edges=""; cards=""
    for nm,role,cost,y,on in tiers:
        col=f"rgb({ACC})" if on else "rgba(212,162,127,.3)"; w=5 if on else 2.5
        edges+=f'<path d="M{hx+62} {hy} C300 {hy},310 {y},432 {y}" fill="none" stroke="{col}" stroke-width="{w}"/>'
        bg="linear-gradient(160deg,#403a33,#241f1a)" if on else "#221f1b"
        bd=f"rgb({ACC})" if on else "rgba(255,255,255,.09)"; glow="filter:drop-shadow(0 0 20px rgba(212,162,127,.3))" if on else ""
        pick=f'<span style="font-family:DM Mono;font-size:11px;color:rgb({ACC})">picked</span>' if on else '<span style="font-family:DM Mono;font-size:11px;color:#6f6a60">idle</span>'
        cards+=(f'<div style="position:absolute;left:432px;top:{y-42}px;width:330px;{glow}">'
                f'<div style="background:{bg};border:1.5px solid {bd};border-radius:16px;padding:14px 18px;display:flex;align-items:center;gap:16px">'
                f'<div style="flex:1"><div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:{"#FAFAF7" if on else "#9a9488"}">{nm}</span>{pick}</div>'
                f'<div style="font-family:DM Sans;font-size:14px;color:#8f8f85;margin-top:2px">{role}</div></div>'
                f'<div style="flex-shrink:0;text-align:right"><span style="font-family:DM Sans;font-weight:900;font-size:26px;color:{"rgb("+ACC+")" if on else "#b7b1a5"}">{cost}</span>'
                f'<div style="font-family:DM Mono;font-size:10px;letter-spacing:.1em;color:#7a746a">/ TURN</div></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One goal in, the right tier out","MODEL-BLIND ROUTER")}
      <div style="position:relative;height:{H}px">
        <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position:absolute;left:0;top:0">
          <defs><radialGradient id="hub" cx="36%" cy="30%"><stop offset="0%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="hg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.45"/></filter></defs>
          <rect x="8" y="{hy-30}" width="96" height="60" rx="13" fill="#2a2724" stroke="rgba(255,255,255,.1)"/>
          <text x="56" y="{hy-4}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">your</text>
          <text x="56" y="{hy+14}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">goal</text>
          {edges}
          <g filter="url(#hg)"><circle cx="{hx}" cy="{hy}" r="62" fill="url(#hub)"/></g>
          <text x="{hx}" y="{hy-6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="16" fill="#1a0f0a">ROUTER</text>
          <text x="{hx}" y="{hy+15}" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#3a2010">reads the job</text>
        </svg>
        {cards}
      </div>
      {cap("you never pick a model. the router reads the job and buys the cheapest tier that clears it.")}</div>'''

# 5. ASSETS - persistent asset slabs (iso), model-release date chips wash over them struck out
def assets():
    releases=["v-2026.03","v-2026.04","v-2026.05","v-2026.06","v-2026.07"]
    chips="".join(f'<div style="font-family:DM Mono;font-size:12px;color:#6f6a60;background:rgba(250,250,247,.03);border:1px solid rgba(250,250,247,.1);border-radius:8px;padding:6px 12px;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.6)">{r}</div>' for r in releases)
    slabs=[("MEMORY","ICP, pipeline, pricing",0),("SKILLS","your workflows, saved",1),("GATE","approval rules",2)]
    cards=""
    for nm,sub,i in slabs:
        y=i*118
        cards+=(f'<div style="position:absolute;left:0;top:{y}px;width:540px;background:linear-gradient(160deg,#403a35,#2a2622);border:1.5px solid rgba(212,162,127,.3);border-radius:18px;padding:18px 24px;box-shadow:0 30px 44px rgba(0,0,0,.55), inset 0 2px 2px rgba(255,255,255,.1);display:flex;align-items:center;gap:18px">'
                f'<div style="flex:1"><div style="font-family:DM Mono;font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{nm}</div>'
                f'<div style="font-family:DM Sans;font-weight:700;font-size:19px;color:#FAFAF7;margin-top:2px">{sub}</div></div>'
                f'<div style="flex-shrink:0;display:flex;align-items:center;gap:7px;background:rgba(212,162,127,.14);border:1px solid rgba(212,162,127,.36);border-radius:999px;padding:6px 14px">'
                f'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.8"><path d="M6 12.5l3.5 3.5L18 7.5"/></svg>'
                f'<span style="font-family:DM Mono;font-size:11px;letter-spacing:.08em;color:rgb({ACC})">NO EXPIRY</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Your assets outlive every release","PERSISTENT LAYER")}
      <div style="display:flex;flex-wrap:wrap;gap:9px;margin-bottom:14px;opacity:.85">
        <span style="font-family:DM Mono;font-size:11px;letter-spacing:.14em;color:#7a746a;align-self:center;margin-right:4px">RELEASES COME AND GO</span>{chips}</div>
      <div style="perspective:1800px;height:400px;display:flex;align-items:center;justify-content:center">
        <div style="transform-style:preserve-3d;transform:rotateX(19deg) rotateZ(-8deg);width:540px;height:360px;position:relative">{cards}</div></div>
      {cap("memory, skills and gate survive untouched. the model underneath can change nightly.")}</div>'''

# 6. UPGRADE - IVORY gauge: same shell, engine swapped, needle jumps old -> new
def upgrade():
    old,new,mx=62,89,100
    cx,cy,r=190,196,150
    def ang(v): return 180+180*v/mx
    def pt(v,rr):
        a=math.radians(ang(v)); return cx+rr*math.cos(a), cy+rr*math.sin(a)
    ax0,ay0=pt(0,r); ax1,ay1=pt(100,r)
    circ=math.pi*r; dash=circ*new/100
    ticks=""
    for v in range(0,101,25):
        tx0,ty0=pt(v,r+5); tx1,ty1=pt(v,r+19)
        ticks+=f'<line x1="{tx0:.1f}" y1="{ty0:.1f}" x2="{tx1:.1f}" y2="{ty1:.1f}" stroke="rgba(150,90,45,.4)" stroke-width="2.5"/>'
    ndx,ndy=pt(new,r-30); oldx,oldy=pt(old,r-30)
    return f'''<div style="width:900px;{CARDIV};padding:34px 42px 34px">
      {htitle("New model, same desk","ENGINE SWAP",'#2a2016',IVK)}
      <div style="display:flex;align-items:center;gap:38px">
        <div style="flex-shrink:0;position:relative;width:380px;height:230px">
          <svg width="380" height="230" viewBox="0 0 380 230">
            <path d="M{ax0:.1f} {ay0:.1f} A{r} {r} 0 0 0 {ax1:.1f} {ay1:.1f}" fill="none" stroke="rgba(150,90,45,.16)" stroke-width="20" stroke-linecap="round"/>
            <path d="M{ax0:.1f} {ay0:.1f} A{r} {r} 0 0 0 {ax1:.1f} {ay1:.1f}" fill="none" stroke="#96562d" stroke-width="20" stroke-linecap="round" stroke-dasharray="{dash:.1f} {circ:.1f}"/>
            {ticks}
            <line x1="{cx}" y1="{cy}" x2="{oldx:.1f}" y2="{oldy:.1f}" stroke="rgba(120,90,55,.45)" stroke-width="3" stroke-dasharray="4 6"/>
            <line x1="{cx}" y1="{cy}" x2="{ndx:.1f}" y2="{ndy:.1f}" stroke="#2a2016" stroke-width="6" stroke-linecap="round"/>
            <circle cx="{cx}" cy="{cy}" r="13" fill="#2a2016"/>
            <circle cx="{cx}" cy="{cy}" r="5" fill="#f5ece3"/>
            <text x="{cx}" y="{cy-46}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="46" fill="#2a2016">{new}</text>
            <text x="{cx}" y="{cy-22}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#96562d">throughput index</text>
          </svg>
        </div>
        <div style="flex:1">
          <div style="display:flex;align-items:baseline;gap:12px;margin-bottom:16px">
            <span style="font-family:DM Sans;font-weight:600;font-size:20px;color:#8a745a;text-decoration:line-through">{old}</span>
            <svg width="30" height="18" viewBox="0 0 30 18"><path d="M2 9h22M18 3l7 6-7 6" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>
            <span style="font-family:DM Sans;font-weight:900;font-size:30px;color:#2a2016">{new}</span>
            <span style="font-family:DM Mono;font-size:15px;color:#96562d">+{new-old}</span></div>
          <div style="display:flex;flex-direction:column;gap:11px">
            {"".join(f'<div style="display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.55);border-left:3px solid #96562d;border-radius:10px;padding:12px 16px"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M6 12.5l3.5 3.5L18 7.5"/></svg><span style="font-family:DM Sans;font-size:17px;color:#3a2c1c">{x}</span></div>' for x in ["same commands","same memory","zero migration"])}
          </div>
        </div>
      </div>
      {cap("the router adopts the new model under the hood. nothing on your desk changes but the output.","#8a745a")}</div>'''

# 7. COST - dark ledger of hours burned chasing models, all red, none touched revenue
def cost():
    items=[("Reinstalling &amp; re-testing",4),("Rewriting prompts",6),("Re-learning quirks",5),("Chasing benchmark threads",3)]
    total=sum(v for _,v in items); mx=max(v for _,v in items)
    rows=""
    for lbl,h in items:
        w=int(h/mx*100)
        rows+=(f'<div style="display:flex;align-items:center;gap:16px;padding:13px 0;border-bottom:1px solid rgba(255,255,255,.06)">'
               f'<span style="flex:1;font-family:DM Sans;font-weight:600;font-size:19px;color:#d9d5cc">{lbl}</span>'
               f'<div style="width:220px;height:14px;border-radius:7px;background:rgba(200,70,35,.12);position:relative;overflow:hidden">'
               f'<div style="position:absolute;left:0;top:0;bottom:0;width:{w}%;border-radius:7px;background:linear-gradient(90deg,rgba(200,70,35,.5),rgb({RED}))"></div></div>'
               f'<span style="width:56px;text-align:right;font-family:DM Mono;font-size:17px;color:rgb({RED})">{h}h</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 44px 36px">
      {htitle("Chasing models is a second job","MONTHLY LEDGER",'#FAFAF7','rgb('+RED+')')}
      <div>{rows}</div>
      <div style="display:flex;align-items:center;justify-content:space-between;margin-top:18px;padding-top:18px;border-top:2px solid rgba(200,70,35,.35)">
        <div><span style="font-family:DM Sans;font-weight:900;font-size:44px;color:rgb({RED})">{total}h</span>
        <span style="font-family:DM Sans;font-weight:700;font-size:19px;color:#c98a72;margin-left:12px">burned / month</span></div>
        <div style="text-align:right"><div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7">0h</div>
        <div style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:#8f8f85">touched revenue</div></div>
      </div>
      {cap("eighteen hours a month reinstalling and re-prompting. none of it shipped a single deal.")}</div>'''

# 8. POSITION - your layer sits ABOVE a scrum of clashing models, you win whoever wins
def position():
    W,H=820,430
    mods=[("Model K",150),("Model R",320),("Model V",490),("Model N",660)]
    scrum=""; feeds=""
    for nm,x in mods:
        scrum+=(f'<rect x="{x-70}" y="326" width="140" height="66" rx="14" fill="url(#mchip)" stroke="rgba(255,255,255,.09)"/>'
                f'<text x="{x}" y="356" text-anchor="middle" font-family="DM Mono" font-size="14" fill="#b7b1a5">{nm}</text>'
                f'<text x="{x}" y="378" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#7a746a">fighting for #1</text>'
                f'<path d="M{x} 326 V236" stroke="rgba(212,162,127,.4)" stroke-width="2" stroke-dasharray="3 6"/>'
                f'<path d="M{x-4} 250 l4 -10 l4 10" fill="none" stroke="rgba(212,162,127,.5)" stroke-width="2"/>')
    # clash sparks between models
    for i in range(3):
        cxp=(mods[i][1]+mods[i+1][1])/2
        scrum+=f'<path d="M{cxp-10} 348 l8 12 l-6 -3 l6 12" fill="none" stroke="rgb({RED})" stroke-width="2" stroke-linecap="round" opacity=".7"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Own the layer above the fight","POSITION")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="mchip" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#2c2925"/><stop offset="100%" stop-color="#1c1a17"/></linearGradient>
          <linearGradient id="plat" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e6b48f"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#9a5a35"/></linearGradient>
          <filter id="pg" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="10" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.35"/></filter>
        </defs>
        <g filter="url(#pg)"><rect x="150" y="70" width="520" height="120" rx="24" fill="url(#plat)"/></g>
        <rect x="168" y="86" width="484" height="88" rx="16" fill="none" stroke="rgba(255,255,255,.28)"/>
        <text x="410" y="128" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">YOUR SYSTEM</text>
        <text x="410" y="158" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="#3a2010">router &middot; memory &middot; gate</text>
        <text x="410" y="224" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".14em" fill="#8f8f85">WHOEVER WINS FEEDS UP</text>
        {scrum}
      </svg>
      {cap("let the labs fight for the crown. the layer above them gets stronger the same afternoon.")}</div>'''

PANELS={"cycle":cycle(),"switchers":switchers(),"truth":truth(),"router":router(),
        "assets":assets(),"upgrade":upgrade(),"cost":cost(),"position":position()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/modelwars"; os.makedirs(outd,exist_ok=True)
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
