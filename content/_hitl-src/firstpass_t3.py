#!/usr/bin/env python3
# TIER 3 - FIRST PASS, HUMAN FINISH, rebuilt to the WIRE-ITS-EYES bar: each panel a UNIQUE hand-built
# coded scene filling a clean rounded card, title + one-line caption, NO generic stat-chip strips,
# NO clip-path cuts, NO extruded walls. Overwrites models_clay/firstpass/*.png. Cost zero.
import importlib.util, os, math
from playwright.sync_api import sync_playwright
ROOT="/home/user/tiberiu-claude"
L=importlib.util.spec_from_file_location("L",f"{ROOT}/content/_hitl-src/clay3d_v4.py")
Lm=importlib.util.module_from_spec(L); L.loader.exec_module(Lm)
ACC="212,162,127"
BAD="200,70,35"
CARD='background:linear-gradient(165deg,#2b2b28,#1d1d1b);border:1px solid rgba(255,255,255,.07);border-radius:34px;box-shadow:0 42px 80px rgba(0,0,0,.55),0 16px 34px rgba(0,0,0,.44), inset 0 2.5px 3px rgba(255,255,255,.12), inset 0 -14px 30px rgba(0,0,0,.45)'
CARDIV='background:linear-gradient(160deg,#fdfbf6,#efe6d5 62%,#e6dac4);border:1px solid rgba(120,95,60,.16);border-radius:34px;box-shadow:0 40px 70px rgba(120,95,60,.20),0 14px 28px rgba(120,95,60,.14), inset 0 2px 3px rgba(255,255,255,.95), inset 0 -16px 34px rgba(150,120,80,.12)'
def htitle(t,tag,ink="#FAFAF7"): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:{ink}">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:rgb({ACC})">{tag}</span></div>')
def htitle_iv(t,tag): return (f'<div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:14px">'
    f'<span style="font-family:\'DM Sans\';font-weight:800;font-size:26px;color:#2a2016">{t}</span>'
    f'<span style="font-family:\'DM Mono\';font-size:13px;letter-spacing:.14em;color:#96562d">{tag}</span></div>')
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. CHATBOX - one lit typist seat + a 3x3 grid of empty role seats, a live chat input bar below
def chatbox():
    roles=["Researcher","Editor","Analyst","Deck builder","Outbound","Closer","Publisher","Legal","Skill maker"]
    seats=""
    for r in roles:
        seats+=(f'<div style="border:1.5px dashed rgba({BAD},.32);border-radius:16px;padding:16px 10px;'
          f'background:rgba({BAD},.04);display:flex;flex-direction:column;gap:8px;align-items:center">'
          f'<div style="width:36px;height:36px;border-radius:50%;background:rgba(250,250,247,.04);border:1px solid rgba(250,250,247,.10)"></div>'
          f'<span style="font-family:DM Sans;font-size:14px;color:#7a746a">{r}</span>'
          f'<span style="font-family:DM Mono;font-size:10px;letter-spacing:.16em;color:rgb({BAD})">EMPTY</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One typist, nine empty seats","CHAT BOX")}
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">{seats}</div>
      <div style="display:flex;align-items:center;gap:16px;margin-top:20px;background:#211d19;
        border:1px solid rgba(212,162,127,.34);border-radius:18px;padding:16px 20px">
        <div style="flex-shrink:0;width:44px;height:44px;border-radius:50%;background:radial-gradient(circle at 36% 30%,#f0c49e,rgb({ACC}) 58%,#7a4326);
          display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:15px;color:#1a0f0a">YOU</div>
        <span style="flex:1;font-family:DM Sans;font-size:19px;color:#c9c3b8">draft the outbound, then the deck, then the brief<span style="color:rgb({ACC})">|</span></span>
        <div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 55%,#9a5a35);
          display:flex;align-items:center;justify-content:center"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></div>
      </div>
      {cap("one prompt at a time, one person typing, nine roles nobody fills.")}</div>'''

# 2. ROSTER - IVORY directory of 10 installed skills, each a real job (org chart, not nicknames)
def roster():
    team=[("Researcher","profiles accounts"),("Editor","tightens every draft"),
          ("Analyst","reads the numbers"),("Deck builder","assembles slides"),
          ("Copywriter","writes in your voice"),("Outbound","runs the sequences"),
          ("Closer","handles objections"),("Publisher","schedules per channel"),
          ("Legal","flags contract risk"),("Skill maker","mints new skills")]
    rows=""
    for i,(nm,job) in enumerate(team):
        rows+=(f'<div style="display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.55);'
          f'border:1px solid rgba(150,120,80,.18);border-radius:14px;padding:13px 16px;box-shadow:0 6px 14px rgba(120,95,60,.10)">'
          f'<div style="flex-shrink:0;width:34px;height:34px;border-radius:10px;background:rgba(150,90,45,.12);border:1px solid rgba(150,90,45,.28);'
          f'display:flex;align-items:center;justify-content:center;font-family:DM Mono;font-weight:500;font-size:14px;color:#96562d">{i+1:02d}</div>'
          f'<div style="flex:1;min-width:0"><div style="font-family:DM Sans;font-weight:800;font-size:18px;color:#2a2016">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8a745a">{job}</div></div>'
          f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#96562d" stroke-width="3" style="flex-shrink:0"><path d="M20 6 9 17l-5-5"/></svg></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle_iv("Ten roles, ten real jobs","INSTALLED ROSTER")}
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">{rows}</div>
      {cap("each one an installed skill with a job, not a prompt with a nickname.","#8a745a")}</div>'''

# 3. SPLIT8 - split-screen: left DRAFTS machine spilling volume cards, right YOU decide (one check)
def split8():
    stack=""
    for i in range(4):
        stack+=(f'<div style="position:absolute;left:{i*10}px;top:{i*22}px;width:200px;height:60px;'
          f'background:linear-gradient(160deg,#3a3530,#241f1b);border:1px solid rgba(255,255,255,.10);border-radius:12px;'
          f'box-shadow:0 14px 26px rgba(0,0,0,.5);display:flex;align-items:center;padding:0 16px;gap:10px">'
          f'<div style="width:8px;height:8px;border-radius:50%;background:rgb({ACC})"></div>'
          f'<div style="flex:1"><div style="height:7px;width:70%;background:rgba(250,250,247,.24);border-radius:4px"></div>'
          f'<div style="height:6px;width:45%;background:rgba(250,250,247,.12);border-radius:4px;margin-top:6px"></div></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("It drafts. You decide.","VOLUME vs JUDGEMENT")}
      <div style="display:flex;align-items:stretch;gap:0;height:420px;border-radius:22px;overflow:hidden;border:1px solid rgba(255,255,255,.08)">
        <div style="flex:1.15;background:linear-gradient(180deg,#241f1b,#1a1613);padding:26px 28px;position:relative">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.16em;color:rgb({ACC})">FIRST PASS</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7;margin-top:4px">Drafts</div>
          <div style="font-family:DM Sans;font-size:15px;color:#8f8f85;margin-top:2px">reading &middot; sorting &middot; writing</div>
          <div style="position:absolute;left:34px;top:150px;width:240px;height:210px">{stack}</div>
          <div style="position:absolute;right:20px;bottom:22px;font-family:DM Sans;font-weight:900;font-size:52px;color:rgba(212,162,127,.9)">40</div>
          <div style="position:absolute;right:20px;bottom:14px;font-family:DM Mono;font-size:11px;color:#8f8f85;transform:translateY(0)">&nbsp;</div>
        </div>
        <div style="width:2px;background:linear-gradient(180deg,transparent,rgb({ACC}),transparent)"></div>
        <div style="flex:1;background:linear-gradient(180deg,#2f2a24,#211d18);padding:26px 28px;display:flex;flex-direction:column">
          <div style="font-family:DM Mono;font-size:13px;letter-spacing:.16em;color:rgb({ACC})">THE FINISH</div>
          <div style="font-family:DM Sans;font-weight:900;font-size:30px;color:#FAFAF7;margin-top:4px">You decide</div>
          <div style="font-family:DM Sans;font-size:15px;color:#8f8f85;margin-top:2px">taste &middot; risk &middot; the call</div>
          <div style="flex:1;display:flex;align-items:center;justify-content:center">
            <div style="width:118px;height:118px;border-radius:50%;background:radial-gradient(circle at 36% 30%,#f0c49e,rgb({ACC}) 58%,#7a4326);
              display:flex;align-items:center;justify-content:center;box-shadow:0 0 40px rgba(212,162,127,.4)">
              <svg width="60" height="60" viewBox="0 0 24 24" fill="none" stroke="#1a0f0a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg></div>
          </div>
          <div style="font-family:DM Sans;font-weight:800;font-size:17px;color:#e6d6c2;text-align:center">1 human call</div>
        </div>
      </div>
      {cap("the first pass is volume work. the finish is the one judgement only you make.")}</div>'''

# 4. MORNING - a 07:00 clock face beside a queue of 9 finished first passes waiting
def morning():
    items=[("12 briefs read","CORTEX"),("31 drafts ranked","PULSE"),("4 deck skeletons","AMPLIFY"),
           ("2 sequences staged","SPECTER"),("9 replies triaged","STRIKER")]
    rows=""
    for txt,tag in items:
        rows+=(f'<div style="display:flex;align-items:center;gap:14px;background:#211d19;border:1px solid rgba(255,255,255,.08);'
          f'border-radius:14px;padding:13px 16px">'
          f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" style="flex-shrink:0"><circle cx="12" cy="12" r="11" fill="rgba(212,162,127,.14)"/><path d="M7 12.5l3.2 3.2L17 8.5" stroke="rgb({ACC})" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:700;font-size:19px;color:#eae4d8">{txt}</span>'
          f'<span style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:#8f8f85">{tag}</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px;display:flex;align-items:center;gap:30px">
      <div style="flex-shrink:0;display:flex;flex-direction:column;align-items:center;gap:16px">
        <svg width="220" height="220" viewBox="0 0 220 220">
          <defs><radialGradient id="cl" cx="38%" cy="32%"><stop offset="0%" stop-color="#33302c"/><stop offset="100%" stop-color="#181614"/></radialGradient></defs>
          <circle cx="110" cy="110" r="100" fill="url(#cl)" stroke="rgba(212,162,127,.3)" stroke-width="2"/>
          {"".join(f'<line x1="{110+88*math.cos(math.radians(h*30-90)):.0f}" y1="{110+88*math.sin(math.radians(h*30-90)):.0f}" x2="{110+98*math.cos(math.radians(h*30-90)):.0f}" y2="{110+98*math.sin(math.radians(h*30-90)):.0f}" stroke="rgba(250,250,247,.24)" stroke-width="2"/>' for h in range(12))}
          <line x1="110" y1="110" x2="110" y2="52" stroke="rgb({ACC})" stroke-width="5" stroke-linecap="round"/>
          <line x1="110" y1="110" x2="158" y2="110" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round"/>
          <circle cx="110" cy="110" r="7" fill="rgb({ACC})"/>
        </svg>
        <div style="font-family:DM Sans;font-weight:900;font-size:40px;color:#FAFAF7;line-height:1">07:00</div>
        <div style="font-family:DM Mono;font-size:12px;letter-spacing:.16em;color:rgb({ACC})">9 PASSES READY</div>
      </div>
      <div style="flex:1">
        {htitle("Waiting before you wake","MORNING QUEUE")}
        <div style="display:flex;flex-direction:column;gap:10px">{rows}</div>
        {cap("your day starts at the decision layer, not the blank page.")}
      </div></div>'''

# 5. CRAFT - IVORY before/after: producing (struck) -> directing, two role transforms
def craft():
    rows=[("Editor","fixes typos","edits for taste"),
          ("Analyst","cleans spreadsheets","reads the meaning"),
          ("Researcher","copies pages","ranks what matters")]
    body=""
    for role,frm,to in rows:
        body+=(f'<div style="display:flex;align-items:center;gap:18px;background:rgba(255,255,255,.5);'
          f'border:1px solid rgba(150,120,80,.18);border-radius:16px;padding:16px 20px">'
          f'<span style="flex-shrink:0;width:110px;font-family:DM Mono;font-size:14px;letter-spacing:.1em;color:#96562d">{role.upper()}</span>'
          f'<span style="font-family:DM Sans;font-size:18px;color:#a08a68;text-decoration:line-through;text-decoration-color:rgba({BAD},.65)">{frm}</span>'
          f'<svg width="26" height="18" viewBox="0 0 26 18" style="flex-shrink:0"><path d="M2 9h20M16 3l6 6-6 6" fill="none" stroke="#96562d" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
          f'<span style="flex:1;font-family:DM Sans;font-weight:800;font-size:20px;color:#2a2016">{to}</span></div>')
    return f'''<div style="width:900px;{CARDIV};padding:34px 40px 34px">
      {htitle_iv("Producing becomes directing","THE LIFT")}
      <div style="display:flex;flex-direction:column;gap:14px">{body}</div>
      {cap("the machine takes the volume. your people keep the taste and the meaning.","#8a745a")}</div>'''

# 6. SKILLMAKER - a repeated job detected, minted into a fresh skill card on the org chart
def skillmaker():
    tally=""
    for i in range(5):
        tally+=f'<div style="width:44px;height:56px;border-radius:8px;background:linear-gradient(160deg,#3a3530,#241f1b);border:1px solid rgba(255,255,255,.10);box-shadow:0 8px 16px rgba(0,0,0,.45)"></div>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A skill that mints skills","SELF-BUILDING")}
      <div style="display:flex;align-items:center;gap:24px;margin-top:6px">
        <div style="flex-shrink:0;width:250px;background:#211d19;border:1px solid rgba(255,255,255,.08);border-radius:18px;padding:20px">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:#8f8f85">SPOTTED 5x THIS WEEK</div>
          <div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7;margin:8px 0 14px">"reprice the quote"</div>
          <div style="display:flex;gap:8px">{tally}</div>
        </div>
        <svg width="120" height="70" viewBox="0 0 120 70" style="flex-shrink:0">
          <defs><filter id="mg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="rgb({ACC})" flood-opacity="0.5"/></filter></defs>
          <path d="M6 35 H98" stroke="rgb({ACC})" stroke-width="4" stroke-dasharray="2 9" stroke-linecap="round"/>
          <path d="M92 24 L112 35 L92 46" fill="none" stroke="rgb({ACC})" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" filter="url(#mg)"/>
        </svg>
        <div style="flex:1;background:linear-gradient(160deg,#403a33,#241f1a);border:1.5px solid rgb({ACC});border-radius:18px;padding:22px;box-shadow:0 0 34px rgba(212,162,127,.22)">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px">
            <span style="font-family:DM Mono;font-size:12px;letter-spacing:.14em;color:rgb({ACC})">NEW SKILL</span>
            <span style="font-family:DM Mono;font-size:12px;color:#8f8f85">minted Fri</span></div>
          <div style="font-family:DM Sans;font-weight:900;font-size:24px;color:#FAFAF7">Requote</div>
          <div style="font-family:DM Sans;font-size:15px;color:#c9c3b8;margin-top:4px">reprices any quote from the last cost table</div>
          <div style="margin-top:14px;display:inline-flex;align-items:center;gap:8px;background:rgba(212,162,127,.14);border-radius:999px;padding:6px 14px">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="3"><path d="M20 6 9 17l-5-5"/></svg>
            <span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">ON THE ROSTER</span></div>
        </div>
      </div>
      {cap("spot a job you keep repeating, and it becomes role number eleven by friday.")}</div>'''

# 7. LINE8 - inside/outside boundary: free auto tasks inside, one human stamp before anything ships
def line8():
    inside=""
    for t in ["draft rewritten","deck restructured","brief re-ranked","numbers re-run"]:
        inside+=(f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">'
          f'<span style="width:8px;height:8px;border-radius:50%;background:rgb({ACC})"></span>'
          f'<span style="font-family:DM Sans;font-size:17px;color:#c9c3b8">{t}</span>'
          f'<span style="margin-left:auto;font-family:DM Mono;font-size:11px;color:#7fd39a">auto</span></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Free inside. Gated at the edge.","HUMAN FINISH")}
      <div style="display:flex;align-items:stretch;gap:0;height:400px">
        <div style="flex:1.25;background:#1c1916;border:1px solid rgba(255,255,255,.08);border-radius:20px 0 0 20px;padding:24px 26px;border-right:none">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.16em;color:#8f8f85;margin-bottom:16px">INSIDE &middot; RUNS FREE</div>
          {inside}
        </div>
        <div style="flex-shrink:0;width:150px;background:linear-gradient(180deg,#2f2a24,#211d18);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;border-top:1px solid rgba(212,162,127,.4);border-bottom:1px solid rgba(212,162,127,.4)">
          <div style="width:74px;height:74px;border-radius:18px;background:#201d19;border:2px solid rgb({ACC});display:flex;align-items:center;justify-content:center">
            <svg width="40" height="40" viewBox="0 0 60 60" fill="none" stroke="rgb({ACC})" stroke-width="5"><rect x="14" y="26" width="32" height="24" rx="6"/><path d="M20 26 V19 a10 10 0 0 1 20 0 v7"/></svg></div>
          <div style="font-family:DM Sans;font-weight:900;font-size:17px;color:#FAFAF7">YOUR TAP</div>
          <div style="font-family:DM Mono;font-size:11px;letter-spacing:.1em;color:rgb({ACC})">HUMAN GATE</div>
        </div>
        <div style="flex:1;background:linear-gradient(180deg,#241f1b,#1a1613);border:1px solid rgba(255,255,255,.08);border-radius:0 20px 20px 0;padding:24px 26px;border-left:none;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
          <div style="font-family:DM Mono;font-size:12px;letter-spacing:.16em;color:rgb({ACC})">OUTSIDE</div>
          <svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin:16px 0"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"/></svg>
          <div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#FAFAF7">ships to<br>the client</div>
        </div>
      </div>
      {cap("first passes run free inside the walls. the last touch out the door is always yours.")}</div>'''

# 8. RESULT8 - closing card: headcount bar flat, throughput bar 3x, side by side
def result8():
    return f'''<div style="width:900px;{CARD};padding:38px 44px 40px;text-align:center">
      {htitle("Same headcount. Triple the work.","THE OUTCOME")}
      <div style="display:flex;align-items:flex-end;justify-content:center;gap:80px;height:340px;margin-top:10px">
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%">
          <div style="display:flex;align-items:flex-end;gap:20px;height:170px">
            <div style="display:flex;flex-direction:column;align-items:center;gap:8px"><div style="width:72px;height:150px;border-radius:14px 14px 0 0;background:linear-gradient(180deg,#403a33,#2a2622);border:1px solid rgba(255,255,255,.10)"></div><span style="font-family:DM Mono;font-size:12px;color:#8f8f85">before</span></div>
            <div style="display:flex;flex-direction:column;align-items:center;gap:8px"><div style="width:72px;height:150px;border-radius:14px 14px 0 0;background:linear-gradient(180deg,#403a33,#2a2622);border:1px solid rgba(255,255,255,.10)"></div><span style="font-family:DM Mono;font-size:12px;color:#8f8f85">after</span></div>
          </div>
          <div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#e6d6c2;margin-top:18px">Headcount</div>
          <div style="font-family:DM Mono;font-size:14px;color:#8f8f85;margin-top:2px">5 &rarr; 5 &middot; flat</div>
        </div>
        <div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%">
          <div style="display:flex;align-items:flex-end;gap:20px;height:300px">
            <div style="display:flex;flex-direction:column;align-items:center;gap:8px"><div style="width:72px;height:96px;border-radius:14px 14px 0 0;background:linear-gradient(180deg,#403a33,#2a2622);border:1px solid rgba(255,255,255,.10)"></div><span style="font-family:DM Mono;font-size:12px;color:#8f8f85">before</span></div>
            <div style="display:flex;flex-direction:column;align-items:center;gap:8px"><div style="width:72px;height:288px;border-radius:14px 14px 0 0;background:linear-gradient(180deg,#f0c49e,rgb({ACC}) 55%,#8a4a2c);box-shadow:0 0 40px rgba(212,162,127,.35);display:flex;align-items:flex-start;justify-content:center;padding-top:12px"><span style="font-family:DM Sans;font-weight:900;font-size:26px;color:#1a0f0a">3x</span></div><span style="font-family:DM Mono;font-size:12px;color:rgb({ACC})">after</span></div>
          </div>
          <div style="font-family:DM Sans;font-weight:900;font-size:22px;color:#FAFAF7;margin-top:18px">Throughput</div>
          <div style="font-family:DM Mono;font-size:14px;color:rgb({ACC});margin-top:2px">1x &rarr; 3x</div>
        </div>
      </div>
      {cap("not replacement, elevation. the work everyone hated now does its own first pass.")}</div>'''

PANELS={"chatbox":chatbox(),"roster":roster(),"split8":split8(),"morning":morning(),
        "craft":craft(),"skillmaker":skillmaker(),"line8":line8(),"result8":result8()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/firstpass"; os.makedirs(outd,exist_ok=True)
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
