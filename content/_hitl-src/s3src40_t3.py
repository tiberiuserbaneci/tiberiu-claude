#!/usr/bin/env python3
# TIER 3 - ANATOMY OF A REPLY (s3src40). Angle: the OUTREACH MESSAGE COPY itself - what makes a
# cold message get a reply (trigger, one-line relevance, a question not a pitch, short), and SPECTER
# writing it in your voice. 8 unique hand-built coded scenes on clean CARD/CARDIV, warm palette.
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
def htitleIV(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:16px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'
RED="200,70,35"

# 1. DEADTEMPLATE - chat/message-request UI mockup: one generic opener, copy-pasted to a crowd,
# struck through, filed unread. Ghost duplicate bubbles behind imply the mass send.
def deadtemplate():
    ghosts=""
    for i,(dx,op) in enumerate([(46,.20),(24,.34)]):
        ghosts+=(f'<div style="position:absolute;right:{dx}px;top:{-14-i*10}px;width:520px;height:120px;'
          f'background:linear-gradient(160deg,#302c27,#221f1b);border:1px solid rgba(255,255,255,.06);'
          f'border-radius:22px 22px 6px 22px;opacity:{op}"></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It reads like a template","REQUESTS &middot; UNREAD")}
      <div style="background:#1a1816;border:1px solid rgba(255,255,255,.07);border-radius:22px;padding:24px 26px 26px">
        <div style="display:flex;align-items:center;gap:14px;padding-bottom:18px;border-bottom:1px solid rgba(255,255,255,.06)">
          <div style="width:46px;height:46px;border-radius:50%;background:linear-gradient(160deg,#3a352f,#241f1a);border:1px solid rgba(255,255,255,.08);flex-shrink:0"></div>
          <div><div style="font-family:'DM Sans';font-weight:700;font-size:18px;color:#cfc9bd">A name you never met</div>
          <div style="font-family:'DM Mono';font-size:12px;letter-spacing:.1em;color:#7a7468">MESSAGE REQUEST &middot; FILTERED</div></div>
          <div style="margin-left:auto;font-family:'DM Mono';font-size:12px;color:rgb({RED})">unread</div></div>
        <div style="position:relative;margin-top:38px;display:flex;justify-content:flex-end">
          {ghosts}
          <div style="position:relative;width:560px;background:linear-gradient(160deg,#37322c,#282420);border:1px solid rgba(255,255,255,.10);
            border-radius:22px 22px 6px 22px;padding:22px 24px;box-shadow:0 18px 34px rgba(0,0,0,.5)">
            <div style="font-family:'DM Sans';font-size:20px;line-height:1.5;color:#b3ada1;
              text-decoration:line-through;text-decoration-color:rgba({RED},.8);text-decoration-thickness:2px">
              Hi [first name], came across your profile and would love to connect and explore possible synergies. Open to a quick 15 min call this week?</div>
          </div>
        </div>
        <div style="display:flex;align-items:center;gap:10px;margin-top:20px">
          <span style="width:8px;height:8px;border-radius:50%;background:rgb({RED})"></span>
          <span style="font-family:'DM Mono';font-size:14px;color:#9a9488">copy-pasted to 340 names this week</span>
          <span style="margin-left:auto;font-family:'DM Sans';font-weight:900;font-size:22px;color:rgb({RED})">0 replies</span></div>
      </div>
      {cap("the same opener in 340 inboxes reads as a broadcast, and broadcasts get muted.")}</div>'''

# 2. ANATOMY - a message dissected into its 4 working parts along a spine: TRIGGER, RELEVANCE,
# QUESTION, SHORT. Each part = a numbered node on the spine + the real line + a mono part-label.
def anatomy():
    parts=[("01","TRIGGER","Saw you just closed your seed round."),
           ("02","RELEVANCE","We stand up the first 5 sales hires for post-raise teams."),
           ("03","QUESTION","Worth a look at your hiring plan?"),
           ("04","SHORT","Thirty-four words. Then I stop.")]
    rows=""
    for i,(n,lab,txt) in enumerate(parts):
        last=(i==3)
        rows+=(f'<div style="position:relative;display:flex;align-items:center;gap:20px;padding:16px 0">'
          f'<div style="position:relative;z-index:2;flex-shrink:0;width:52px;height:52px;border-radius:15px;'
          f'background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgba(212,162,127,.4);'
          f'display:flex;align-items:center;justify-content:center;font-family:\'DM Mono\';font-weight:500;font-size:17px;color:rgb({ACC})">{n}</div>'
          f'<div style="flex:1;background:linear-gradient(160deg,#312d28,#211e1a);border:1px solid rgba(255,255,255,.08);'
          f'border-radius:16px;padding:15px 20px;display:flex;align-items:center;gap:18px">'
          f'<span style="flex:1;font-family:\'DM Sans\';font-weight:600;font-size:19px;color:#eae4d8">{txt}</span>'
          f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:12px;letter-spacing:.14em;color:rgb({ACC});'
          f'background:rgba(212,162,127,.12);border:1px solid rgba(212,162,127,.3);border-radius:999px;padding:6px 12px">{lab}</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Four lines, nothing else","MESSAGE, DISSECTED")}
      <div style="position:relative">
        <div style="position:absolute;left:26px;top:36px;bottom:36px;width:2px;background:rgba(212,162,127,.28);z-index:1"></div>
        {rows}
      </div>
      {cap("trigger, one line of relevance, a question not a pitch, then stop.")}</div>'''

# 3. TRIGGER - horizontal event timeline; one recent event (Tue: raised $4M) glows and drops a
# connector into the opening line. Proof you actually looked, in the first six words.
def trigger():
    W,H=820,430
    axy=150
    evs=[("MON","product launch",150,False),("TUE","raised $4M",340,True),
         ("WED","hired a VP",530,False),("NOW","",700,False)]
    axis=f'<line x1="70" y1="{axy}" x2="740" y2="{axy}" stroke="rgba(212,162,127,.28)" stroke-width="2"/>'
    nodes=""; drop=""
    for day,txt,x,hot in evs:
        if day=="NOW":
            nodes+=(f'<line x1="{x}" y1="{axy-16}" x2="{x}" y2="{axy+16}" stroke="rgba(250,250,247,.35)" stroke-width="2"/>'
              f'<text x="{x}" y="{axy-28}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".12em" fill="#8f8f85">NOW</text>')
            continue
        if hot:
            nodes+=(f'<circle cx="{x}" cy="{axy}" r="15" fill="rgb({ACC})" filter="url(#tg)"/>'
              f'<text x="{x}" y="{axy-34}" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".1em" fill="rgb({ACC})">{day}</text>'
              f'<text x="{x}" y="{axy+44}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="19" fill="#FAFAF7">{txt}</text>')
            drop=(f'<path d="M{x} {axy+15} C{x} 250,410 250,410 300" fill="none" stroke="rgb({ACC})" stroke-width="2.5" stroke-dasharray="2 8" stroke-linecap="round"/>')
        else:
            nodes+=(f'<circle cx="{x}" cy="{axy}" r="9" fill="#2a2724" stroke="rgba(255,255,255,.18)" stroke-width="2"/>'
              f'<text x="{x}" y="{axy-30}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="#7a7468">{day}</text>'
              f'<text x="{x}" y="{axy+42}" text-anchor="middle" font-family="DM Sans" font-size="16" fill="#8f8f85">{txt}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Open on a real, recent event","THE FIRST SIX WORDS")}
      <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="display:block;margin:0 auto">
        <defs><filter id="tg" x="-200%" y="-200%" width="500%" height="500%"><feDropShadow dx="0" dy="0" stdDeviation="9" flood-color="rgb({ACC})" flood-opacity="0.85"/></filter></defs>
        {axis}{nodes}{drop}
        <rect x="150" y="300" width="520" height="86" rx="18" fill="#1a1816" stroke="rgba(212,162,127,.34)" stroke-width="1.5"/>
        <text x="180" y="335" font-family="DM Mono" font-size="12" letter-spacing=".14em" fill="rgb({ACC})">YOUR OPENING LINE</text>
        <text x="180" y="366" font-family="DM Sans" font-weight="700" font-size="21" fill="#FAFAF7">Saw you closed the $4M on Tuesday.</text>
      </svg>
      {cap("a funding round, a hire, a launch from last week - proof you actually looked.")}</div>'''

# 4. BRIDGE - relevance as ONE line joining two orbs (their event -> your value). A single beam,
# the one sentence riding above it; a faded struck brochure-stack beneath as the contrast.
def bridge():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One line ties them to you","THE BRIDGE")}
      <svg width="820" height="300" viewBox="0 0 820 300" style="display:block;margin:0 auto">
        <defs>
          <radialGradient id="oA" cx="38%" cy="32%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <radialGradient id="oB" cx="38%" cy="32%"><stop offset="0%" stop-color="#e6b48f"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
          <filter id="og" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.42"/></filter></defs>
        <rect x="150" y="176" width="520" height="8" rx="4" fill="rgb({ACC})" opacity="0.85" filter="url(#og)"/>
        <g filter="url(#og)"><circle cx="150" cy="180" r="62" fill="url(#oA)"/></g>
        <text x="150" y="175" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#2a160c">THEIR</text>
        <text x="150" y="193" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="17" fill="#2a160c">$4M</text>
        <g filter="url(#og)"><circle cx="670" cy="180" r="62" fill="url(#oB)"/></g>
        <text x="670" y="173" text-anchor="middle" font-family="DM Mono" font-size="11" fill="#2a160c">YOUR</text>
        <text x="670" y="191" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="15" fill="#2a160c">5 HIRES</text>
        <rect x="212" y="96" width="396" height="60" rx="16" fill="#211d19" stroke="rgba(212,162,127,.34)" stroke-width="1.5"/>
        <text x="410" y="132" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="18" fill="#FAFAF7">We staff post-raise sales teams.</text>
      </svg>
      <div style="display:flex;align-items:center;gap:14px;background:rgba(250,250,247,.03);border:1px dashed rgba(250,250,247,.14);border-radius:14px;padding:12px 18px;margin-top:8px;opacity:.72">
        <span style="font-family:'DM Mono';font-size:12px;letter-spacing:.12em;color:#7a7468;flex-shrink:0">INSTEAD OF</span>
        <span style="font-family:'DM Sans';font-size:17px;color:#8f8f85;text-decoration:line-through;text-decoration-color:rgba({RED},.7)">three paragraphs about our platform, mission and roadmap</span></div>
      {cap("their event, then the single sentence that makes your reach out obvious.")}</div>'''

# 5. ASK - split compare: a PITCH ending (struck, red, ignored) vs a QUESTION ending (lit, replied).
def ask():
    def sidecard(kind,txt,tag,good):
        acc=f"rgb({ACC})" if good else f"rgb({RED})"
        txtcol="#FAFAF7" if good else "#b3ada1"
        strike="" if good else f"text-decoration:line-through;text-decoration-color:rgba({RED},.75);text-decoration-thickness:2px"
        bg="linear-gradient(160deg,#332f29,#211e1a)" if good else "#201d1a"
        icon=('<path d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18Zm.2 4.4a1.7 1.7 0 0 1 1.7 2.5c-.3.6-1 .9-1.4 1.4-.3.4-.5.9-.5 1.5m0 3.2v.1" fill="none" stroke="'+acc+'" stroke-width="2.2" stroke-linecap="round"/>'
          if good else '<path d="M6 6l12 12M18 6L6 18" stroke="'+acc+'" stroke-width="2.4" stroke-linecap="round"/>')
        return (f'<div style="flex:1;background:{bg};border:1.5px solid {("rgba(212,162,127,.4)" if good else "rgba(200,70,35,.34)")};'
          f'border-radius:20px;padding:22px 24px;display:flex;flex-direction:column;'
          f'{"box-shadow:0 0 30px rgba(212,162,127,.16)" if good else ""}">'
          f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:14px">'
          f'<svg width="26" height="26" viewBox="0 0 24 24">{icon}</svg>'
          f'<span style="font-family:\'DM Mono\';font-size:12px;letter-spacing:.14em;color:{acc}">{kind}</span></div>'
          f'<div style="flex:1;font-family:\'DM Sans\';font-weight:600;font-size:21px;line-height:1.4;color:{txtcol};{strike}">{txt}</div>'
          f'<div style="margin-top:18px;font-family:\'DM Sans\';font-weight:900;font-size:16px;color:{acc}">{tag}</div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("End on a question, never a pitch","THE ASK")}
      <div style="display:flex;align-items:stretch;gap:20px;position:relative">
        {sidecard("THE PITCH","Can I book 15 minutes to walk you through our full platform?","asks them to work &middot; ignored",False)}
        <div style="align-self:center;flex-shrink:0;font-family:'DM Sans';font-weight:900;font-size:18px;color:#7a7468">VS</div>
        {sidecard("THE QUESTION","Are you even hiring for this yet?","asks them to reply &middot; answered",True)}
      </div>
      {cap("a pitch asks them to work. a short question just asks them to reply.")}</div>'''

# 6. LENGTH - radial half-gauge: the needle sits in the sweet zone at 34 words; a red overflow mark
# at the far end flags the 200+ word essay. Big center number.
def length():
    cx,cy,r=250,300,200
    def P(g,rad):
        a=math.radians(g); return (cx-rad*math.cos(a), cy-rad*math.sin(a))
    bg0=P(0,r); bg1=P(180,r)
    z0=P(30,r); z1=P(82,r)         # sweet zone 20..55 words
    ng=51                          # 34 words
    nx,ny=P(ng,r-34)
    ticks=""
    for g in range(0,181,18):
        t0=P(g,r); t1=P(g,r-16)
        ticks+=f'<line x1="{t0[0]:.0f}" y1="{t0[1]:.0f}" x2="{t1[0]:.0f}" y2="{t1[1]:.0f}" stroke="rgba(250,250,247,.18)" stroke-width="2"/>'
    rx,ry=P(172,r-16)
    return f'''<div style="width:900px;{CARD};padding:34px 40px 30px">
      {htitle("Forty words, then stop typing","THE LENGTH")}
      <svg width="500" height="330" viewBox="0 0 500 330" style="display:block;margin:0 auto">
        <defs><filter id="ng" x="-120%" y="-120%" width="340%" height="340%"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="rgb({ACC})" flood-opacity="0.7"/></filter></defs>
        <path d="M{bg0[0]:.0f} {bg0[1]:.0f} A{r} {r} 0 0 1 {bg1[0]:.0f} {bg1[1]:.0f}" fill="none" stroke="rgba(250,250,247,.10)" stroke-width="22" stroke-linecap="round"/>
        <path d="M{z0[0]:.0f} {z0[1]:.0f} A{r} {r} 0 0 1 {z1[0]:.0f} {z1[1]:.0f}" fill="none" stroke="rgb({ACC})" stroke-width="22" stroke-linecap="round"/>
        {ticks}
        <circle cx="{rx:.0f}" cy="{ry:.0f}" r="10" fill="rgb({RED})"/>
        <text x="{rx-6:.0f}" y="{ry-16:.0f}" text-anchor="end" font-family="DM Mono" font-size="12" fill="rgb({RED})">200+ essay</text>
        <line x1="{cx}" y1="{cy}" x2="{nx:.0f}" y2="{ny:.0f}" stroke="rgb({ACC})" stroke-width="6" stroke-linecap="round" filter="url(#ng)"/>
        <circle cx="{cx}" cy="{cy}" r="14" fill="rgb({ACC})"/>
        <text x="{cx}" y="{cy-46}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="66" fill="#FAFAF7">34</text>
        <text x="{cx}" y="{cy-16}" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".16em" fill="rgb({ACC})">WORDS SENT</text>
      </svg>
      {cap("long messages read as a mass send. under forty reads like a person wrote it.")}</div>'''

# 7. WRITER (IVORY hero) - SPECTER composes the assembled winning message in your voice: a light
# draft sheet, the 4 parts tagged inline, a byline + voice-match chip. The payoff panel.
def writer():
    lines=[("Saw you closed the seed round.","TRIGGER"),
           ("We staff post-raise sales teams.","RELEVANCE"),
           ("Worth a look at your hiring plan?","QUESTION")]
    body=""
    for txt,tag in lines:
        body+=(f'<div style="display:flex;align-items:center;gap:14px;padding:12px 0;border-bottom:1px solid rgba(150,120,80,.14)">'
          f'<span style="flex:1;font-family:\'DM Sans\';font-weight:600;font-size:21px;color:#2a2016">{txt}</span>'
          f'<span style="flex-shrink:0;font-family:\'DM Mono\';font-size:11px;letter-spacing:.12em;color:#96562d;'
          f'background:rgba(150,90,45,.10);border:1px solid rgba(150,90,45,.22);border-radius:999px;padding:5px 11px">{tag}</span></div>')
    chk="".join(f'<div style="display:flex;align-items:center;gap:8px"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="2.8"><path d="M20 6 9 17l-5-5"/></svg><span style="font-family:DM Sans;font-size:15px;color:#5a4634">{x}</span></div>' for x in ["your cadence","no hedging","34 words"])
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitleIV("SPECTER writes it in your voice","DRAFT &middot; READY")}
      <div style="background:rgba(255,255,255,.62);border-left:4px solid #96562d;border-radius:14px;padding:20px 24px 14px;
        box-shadow:0 10px 24px rgba(120,95,60,.12), inset 0 2px 3px rgba(255,255,255,.9)">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px">
          <div style="width:34px;height:34px;border-radius:10px;background:linear-gradient(160deg,#c98a5c,#8a4a2c);
            display:flex;align-items:center;justify-content:center;font-family:'DM Mono';font-weight:500;font-size:12px;color:#fff2e6">S</div>
          <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">SPECTER &middot; TO A FOUNDER</span>
          <span style="margin-left:auto;font-family:'DM Mono';font-size:12px;color:#a08a68">in your voice</span></div>
        {body}
      </div>
      <div style="display:flex;align-items:center;gap:22px;margin-top:18px">{chk}
        <span style="margin-left:auto;font-family:'DM Sans';font-weight:900;font-size:15px;color:#96562d">98% style match</span></div>
      {cap("trigger, relevance, question, short - assembled from your real cadence.","#8a745a")}</div>'''

# 8. REPLY (IVORY) - the thread lands: your short outgoing line, then an incoming reply bubble with
# a fresh reply badge. A cold name became a live conversation.
def reply():
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      {htitleIV("Sent once, answered in an hour","THE REPLY")}
      <div style="display:flex;flex-direction:column;gap:20px;padding:6px 0 2px">
        <div style="display:flex;justify-content:flex-end">
          <div style="max-width:560px;background:linear-gradient(160deg,#c98a5c,#a85c34);border-radius:20px 20px 6px 20px;
            padding:16px 20px;box-shadow:0 14px 26px rgba(150,90,45,.28)">
            <div style="font-family:'DM Sans';font-weight:600;font-size:20px;color:#fff6ec;line-height:1.45">Saw you closed the seed round. We staff post-raise sales teams. Worth a look at your hiring plan?</div>
            <div style="text-align:right;font-family:'DM Mono';font-size:11px;color:rgba(255,246,236,.7);margin-top:6px">you &middot; 09:12</div></div>
        </div>
        <div style="display:flex;justify-content:flex-start">
          <div style="max-width:520px;background:#ffffff;border:1px solid rgba(150,120,80,.16);border-radius:20px 20px 20px 6px;
            padding:16px 20px;box-shadow:0 14px 26px rgba(120,95,60,.14)">
            <div style="font-family:'DM Sans';font-weight:600;font-size:20px;color:#2a2016;line-height:1.45">Ha, yeah we are. Send me the details.</div>
            <div style="display:flex;align-items:center;gap:8px;margin-top:8px">
              <span style="width:7px;height:7px;border-radius:50%;background:#96562d"></span>
              <span style="font-family:'DM Mono';font-size:11px;letter-spacing:.08em;color:#96562d">REPLIED &middot; 1h later</span></div></div>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:14px;margin-top:20px;padding-top:16px;border-top:1px solid rgba(150,120,80,.18)">
        <span style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#2a2016">Cold name</span>
        <svg width="30" height="20" viewBox="0 0 30 20" fill="none" stroke="#96562d" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10h22M19 4l6 6-6 6"/></svg>
        <span style="font-family:'DM Sans';font-weight:900;font-size:26px;color:#96562d">live thread</span></div>
      {cap("the right four lines turn a name into a conversation - that is the whole game.","#8a745a")}</div>'''

PANELS={"deadtemplate":deadtemplate(),"anatomy":anatomy(),"trigger":trigger(),"bridge":bridge(),
        "ask":ask(),"length":length(),"writer":writer(),"reply":reply()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src40"; os.makedirs(outd,exist_ok=True)
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
