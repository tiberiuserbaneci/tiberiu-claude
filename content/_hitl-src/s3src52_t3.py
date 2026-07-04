#!/usr/bin/env python3
# TIER 3 - PLUG IN YOUR REAL APPS. The MCP CONNECTOR explainer: an MCP is a plug, your app is the
# socket, connecting your real tools gives the agent hands INSIDE the apps you already own. Each panel
# is a UNIQUE hand-built coded scene on a clean rounded card (WIRE-ITS-EYES bar). NO generic stat-chips.
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
def cap(t,c="#8f8f85"): return f'<div style="font-family:\'DM Mono\';font-size:14px;color:{c};margin-top:16px">{t}</div>'

# 1. GAP - the agent orb can only talk; a red no-bridge wall cuts it off from your dim apps
def gap():
    apps=[("Apollo",100),("Gmail",214),("Calendar",328)]
    tiles=""; reach=""
    for nm,y in apps:
        tiles+=(f'<g opacity="0.55"><rect x="560" y="{y-38}" width="222" height="76" rx="16" fill="#221f1b" stroke="rgba(255,255,255,.08)"/>'
          f'<rect x="588" y="{y-16}" width="32" height="32" rx="9" fill="#2c2824" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="640" y="{y+6}" font-family="DM Sans" font-weight="700" font-size="21" fill="#8f8f85">{nm}</text></g>')
        reach+=f'<path d="M262 214 C400 214,410 {y},548 {y}" fill="none" stroke="rgba(200,70,35,.42)" stroke-width="2.4" stroke-dasharray="4 8"/>'
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("A chat box has no hands","NO REACH")}
      <svg width="820" height="440" viewBox="0 0 820 440" style="display:block;margin:0 auto">
        <defs><radialGradient id="ag" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="agg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {reach}
        <g filter="url(#agg)"><circle cx="168" cy="214" r="86" fill="url(#ag)"/></g>
        <text x="168" y="209" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="23" fill="#2a160c">CHAT</text>
        <text x="168" y="236" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#3a2010">text only</text>
        <line x1="438" y1="46" x2="438" y2="398" stroke="rgba(200,70,35,.55)" stroke-width="2.5" stroke-dasharray="3 9"/>
        <text x="438" y="30" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".12em" fill="rgb(200,70,35)">NO BRIDGE</text>
        {tiles}
      </svg>
      {cap("it reads and writes words. it cannot open apollo, gmail or your calendar.")}</div>'''

# 2. PLUG - IVORY hero object: an MCP plug about to seat into your app's socket (the whole mechanic)
def plug():
    return f'''<div style="width:900px;{CARDIV};padding:38px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:8px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">One plug, one standard</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">WHAT IS AN MCP</span></div>
      <svg width="640" height="468" viewBox="0 0 640 468" style="display:block;margin:0 auto">
        <defs>
          <linearGradient id="plugb" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#e8b791"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#9a5a35"/></linearGradient>
          <linearGradient id="sockb" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#ffffff"/><stop offset="100%" stop-color="#e8dcc7"/></linearGradient>
          <radialGradient id="spark" cx="50%" cy="50%"><stop offset="0%" stop-color="rgba(204,120,92,.55)"/><stop offset="70%" stop-color="rgba(204,120,92,0)"/></radialGradient>
          <filter id="ds" x="-40%" y="-40%" width="180%" height="180%"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="rgba(120,90,55,.30)"/></filter>
        </defs>
        <circle cx="336" cy="234" r="128" fill="url(#spark)"/>
        <text x="150" y="150" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="#96562d">THE PLUG</text>
        <g filter="url(#ds)"><rect x="66" y="178" width="184" height="112" rx="26" fill="url(#plugb)"/></g>
        <text x="158" y="243" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="30" fill="#2a160c">MCP</text>
        <rect x="250" y="198" width="90" height="26" rx="8" fill="#caa06f"/>
        <rect x="250" y="246" width="90" height="26" rx="8" fill="#caa06f"/>
        <g filter="url(#ds)"><rect x="362" y="146" width="212" height="176" rx="30" fill="url(#sockb)" stroke="rgba(120,95,60,.22)"/></g>
        <rect x="356" y="198" width="54" height="26" rx="8" fill="#d8c8ad"/>
        <rect x="356" y="246" width="54" height="26" rx="8" fill="#d8c8ad"/>
        <text x="468" y="140" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="#96562d">YOUR APP</text>
        <text x="468" y="300" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="#2a2016">the socket</text>
      </svg>
      {cap("an mcp is a plug. your app is the socket. they just fit, no glue code.","#8a745a")}</div>'''

# 3. CONNECT - Ultron Settings > Connectors list: toggle a tool on, no scripts
def connect():
    rows=[("A","Apollo","find leads, enrich, sequence",True),
          ("M","Gmail","send and draft in your inbox",True),
          ("C","Calendar","hold and book real slots",True),
          ("H","CRM","log every deal automatically",False)]
    items=""
    for ic,nm,desc,on in rows:
        status=(f'<div style="display:flex;align-items:center;gap:8px;flex-shrink:0"><span style="width:9px;height:9px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 10px rgba({ACC},.8)"></span><span style="font-family:DM Mono;font-size:14px;color:rgb({ACC})">Connected</span></div>'
                if on else
                f'<div style="font-family:DM Mono;font-size:14px;color:#c9c3b8;border:1px solid rgba(212,162,127,.5);border-radius:999px;padding:6px 18px;flex-shrink:0">Connect</div>')
        items+=(f'<div style="display:flex;align-items:center;gap:18px;background:linear-gradient(158deg,#302c28,#211e1a);border:1px solid rgba(255,255,255,.09);border-radius:16px;padding:16px 20px">'
          f'<div style="flex-shrink:0;width:44px;height:44px;border-radius:12px;background:linear-gradient(160deg,#4a423a,#2a2622);display:flex;align-items:center;justify-content:center;font-family:DM Sans;font-weight:900;font-size:20px;color:rgb({ACC})">{ic}</div>'
          f'<div style="flex:1"><div style="font-family:DM Sans;font-weight:800;font-size:20px;color:#FAFAF7">{nm}</div>'
          f'<div style="font-family:DM Sans;font-size:15px;color:#8f8f85;margin-top:1px">{desc}</div></div>{status}</div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Flip a toggle, not a script","SETTINGS &middot; CONNECTORS")}
      <div style="display:flex;flex-direction:column;gap:13px">{items}</div>
      <div style="display:flex;align-items:center;gap:10px;margin-top:16px">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgb({ACC})" stroke-width="2.4"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>
        <span style="font-family:DM Mono;font-size:13px;letter-spacing:.06em;color:#8f8f85">Secure &middot; Private &middot; OAuth 2.0</span></div>
      {cap("connect the tools you already own. no api glue, no zapier, no code.")}</div>'''

# 4. GRID - board of your real apps, each a lit socket port marked PLUGGED
def grid():
    apps=[("Apollo","270M contacts"),("Gmail","your outreach"),("Calendar","real slots"),
          ("HubSpot","every deal"),("Slack","team pings"),("Notion","your docs")]
    cells=""
    for nm,sub in apps:
        cells+=(f'<div style="background:linear-gradient(160deg,#2f2b27,#201d1a);border:1px solid rgba(255,255,255,.09);border-radius:18px;padding:20px;display:flex;flex-direction:column;gap:13px;box-shadow:0 18px 30px rgba(0,0,0,.4), inset 0 2px 2px rgba(255,255,255,.06)">'
          f'<div style="display:flex;align-items:center;justify-content:space-between">'
          f'<span style="font-family:DM Sans;font-weight:800;font-size:21px;color:#FAFAF7">{nm}</span>'
          f'<svg width="36" height="27" viewBox="0 0 36 27"><rect x="1" y="1" width="34" height="25" rx="7" fill="#191713" stroke="rgba(212,162,127,.5)"/><rect x="10" y="8" width="6" height="11" rx="2" fill="rgb({ACC})"/><rect x="20" y="8" width="6" height="11" rx="2" fill="rgb({ACC})"/></svg></div>'
          f'<div style="font-family:DM Sans;font-size:14px;color:#8f8f85">{sub}</div>'
          f'<div style="display:flex;align-items:center;gap:7px;margin-top:auto"><span style="width:8px;height:8px;border-radius:50%;background:rgb({ACC});box-shadow:0 0 9px rgba({ACC},.8)"></span><span style="font-family:DM Mono;font-size:12px;letter-spacing:.1em;color:rgb({ACC})">PLUGGED</span></div></div>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("Every app you already own","THE SOCKETS")}
      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px">{cells}</div>
      {cap("each tool becomes a place the agent can actually reach and act.")}</div>'''

# 5. REACH - IVORY app window: the agent drafts INSIDE Gmail, the draft lands in your real inbox
def reach():
    return f'''<div style="width:900px;{CARDIV};padding:36px 42px 34px">
      <div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:18px">
        <span style="font-family:'DM Sans';font-weight:800;font-size:26px;color:#2a2016">It works inside the app</span>
        <span style="font-family:'DM Mono';font-size:13px;letter-spacing:.14em;color:#96562d">HANDS IN GMAIL</span></div>
      <div style="background:#ffffff;border:1px solid rgba(120,95,60,.18);border-radius:18px;overflow:hidden;box-shadow:0 26px 44px rgba(120,90,55,.22)">
        <div style="display:flex;align-items:center;gap:8px;background:linear-gradient(180deg,#f3ece0,#e9dfce);padding:14px 20px;border-bottom:1px solid rgba(120,95,60,.14)">
          <span style="width:12px;height:12px;border-radius:50%;background:#d8b48f"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#e0d2ba"></span>
          <span style="width:12px;height:12px;border-radius:50%;background:#e0d2ba"></span>
          <span style="font-family:DM Mono;font-size:14px;color:#8a745a;margin-left:12px">New Message</span>
          <span style="margin-left:auto;font-family:DM Mono;font-size:12px;color:#96562d">drafted by Ultron</span></div>
        <div style="padding:18px 24px;font-family:'DM Sans';color:#2a2016">
          <div style="display:flex;gap:10px;padding:9px 0;border-bottom:1px solid rgba(120,95,60,.14)"><span style="color:#a08a68;font-size:16px;width:74px">To</span><span style="font-size:16px">ops@northwind.io</span></div>
          <div style="display:flex;gap:10px;padding:9px 0;border-bottom:1px solid rgba(120,95,60,.14)"><span style="color:#a08a68;font-size:16px;width:74px">Subject</span><span style="font-size:16px;font-weight:700">Your 3 new ops hires</span></div>
          <div style="font-size:17px;line-height:1.5;color:#4a3f30;margin-top:14px">Saw you opened three ops roles this week. We cut onboarding time for teams your size. Worth 15 minutes on Thursday?</div>
          <div style="display:flex;align-items:center;gap:14px;margin-top:18px">
            <span style="background:linear-gradient(160deg,#e6b48f,rgb({ACC}) 60%,#9a5a35);color:#2a160c;font-family:DM Sans;font-weight:900;font-size:16px;padding:10px 26px;border-radius:999px">Send</span>
            <span style="font-family:DM Mono;font-size:13px;color:#96562d">waiting for your tap</span></div>
        </div>
      </div>
      {cap("the draft lands in your real inbox, not a copy-paste box you clean up.","#8a745a")}</div>'''

# 6. FLOW - one instruction crosses three connected apps in order (left to right pipeline)
def flow():
    tools=[("APOLLO","find the account"),("GMAIL","draft the note"),("CALENDAR","hold the slot")]
    xs=[240,470,700]; y=232; w=150; prev=150
    conns=""; nodes=""
    for i,(nm,verb) in enumerate(tools):
        x=xs[i]; left=x-w/2; right=x+w/2; mid=(prev+left)/2
        conns+=f'<path d="M{prev} {y} C{mid:.0f} {y},{mid:.0f} {y},{left:.0f} {y}" fill="none" stroke="rgb({ACC})" stroke-width="4"/>'
        conns+=f'<circle cx="{prev}" cy="{y}" r="4" fill="rgb({ACC})"/>'
        nodes+=(f'<g><rect x="{left:.0f}" y="{y-38}" width="{w}" height="76" rx="16" fill="#2b2723" stroke="rgba(212,162,127,.45)" stroke-width="1.5"/>'
          f'<text x="{x}" y="{y-52}" text-anchor="middle" font-family="DM Mono" font-size="12" letter-spacing=".1em" fill="rgb({ACC})">STEP {i+1}</text>'
          f'<text x="{x}" y="{y-4}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="17" fill="#FAFAF7">{nm}</text>'
          f'<text x="{x}" y="{y+18}" text-anchor="middle" font-family="DM Sans" font-size="12.5" fill="#8f8f85">{verb}</text></g>')
        prev=right
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One ask crosses three apps","ACROSS CONNECTORS")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="ask" cx="36%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="askg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="16" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g filter="url(#askg)"><circle cx="86" cy="{y}" r="62" fill="url(#ask)"/></g>
        <text x="86" y="{y-2}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="18" fill="#2a160c">ASK</text>
        <text x="86" y="{y+18}" text-anchor="middle" font-family="DM Mono" font-size="10.5" fill="#3a2010">one line</text>
        {conns}{nodes}
        <text x="775" y="{y+6}" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="26" fill="rgb({ACC})">&#10003;</text>
        <text x="410" y="360" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".06em" fill="#8f8f85">hands-free, socket to socket, in order</text>
      </svg>
      {cap("one instruction moves across every connected tool, no tab switching.")}</div>'''

# 7. AUTH - native OAuth lock seal; a crossed-out pasted API key left, a one-click Revoke right
def auth():
    return f'''<div style="width:900px;{CARD};padding:34px 40px 36px">
      {htitle("No keys on a sticky note","NATIVE OAUTH")}
      <svg width="820" height="420" viewBox="0 0 820 420" style="display:block;margin:0 auto">
        <defs><radialGradient id="lk" cx="38%" cy="30%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="55%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="lg2" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="20" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        <g opacity="0.92">
          <rect x="40" y="146" width="230" height="128" rx="20" fill="#241f1b" stroke="rgba(200,70,35,.5)"/>
          <text x="155" y="190" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".12em" fill="rgb(200,70,35)">PASTED API KEY</text>
          <text x="155" y="224" text-anchor="middle" font-family="DM Mono" font-size="17" fill="#8f8f85">sk-3f9a...b21</text>
          <line x1="62" y1="158" x2="248" y2="262" stroke="rgb(200,70,35)" stroke-width="4"/>
          <text x="155" y="256" text-anchor="middle" font-family="DM Sans" font-size="14" fill="rgb(200,70,35)">leaked, forgotten</text>
        </g>
        <g filter="url(#lg2)"><circle cx="470" cy="210" r="120" fill="url(#lk)"/></g>
        <g transform="translate(430,170)"><rect x="0" y="46" width="80" height="58" rx="12" fill="none" stroke="#2a160c" stroke-width="7"/><path d="M14 46 V31 a26 26 0 0 1 52 0 v15" fill="none" stroke="#2a160c" stroke-width="7"/></g>
        <text x="470" y="358" text-anchor="middle" font-family="DM Mono" font-size="14" letter-spacing=".16em" fill="rgb({ACC})">OAUTH 2.0</text>
        <rect x="618" y="176" width="172" height="72" rx="16" fill="#241f1b" stroke="rgba(255,255,255,.14)"/>
        <text x="704" y="208" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#FAFAF7">Revoke</text>
        <text x="704" y="230" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#8f8f85">one click, any time</text>
      </svg>
      {cap("native oauth grants the access and you pull it back whenever you want.")}</div>'''

# 8. OPERATOR - all your app sockets converge into one operator orb (brain, memory, hands)
def operator():
    scat=[("Apollo",78,84),("Gmail",78,190),("Calendar",78,296),("HubSpot",204,137),("Slack",204,243)]
    left=""
    for nm,x,y in scat:
        left+=(f'<path d="M{x+42} {y} C360 {y},390 210,478 210" fill="none" stroke="rgba(212,162,127,.32)" stroke-width="2"/>'
          f'<rect x="{x-42}" y="{y-22}" width="84" height="44" rx="12" fill="#221f1b" stroke="rgba(255,255,255,.10)"/>'
          f'<text x="{x}" y="{y+5}" text-anchor="middle" font-family="DM Mono" font-size="12" fill="#c9c3b8">{nm}</text>')
    return f'''<div style="width:900px;{CARD};padding:34px 40px 34px">
      {htitle("One operator, every socket","PLUGGED IN")}
      <svg width="820" height="430" viewBox="0 0 820 430" style="display:block;margin:0 auto">
        <defs><radialGradient id="op" cx="42%" cy="34%"><stop offset="0%" stop-color="#f0c49e"/><stop offset="52%" stop-color="rgb({ACC})"/><stop offset="100%" stop-color="#7a4326"/></radialGradient>
        <filter id="opg" x="-80%" y="-80%" width="260%" height="260%"><feDropShadow dx="0" dy="0" stdDeviation="26" flood-color="rgb({ACC})" flood-opacity="0.4"/></filter></defs>
        {left}
        <g filter="url(#opg)"><circle cx="600" cy="210" r="122" fill="url(#op)"/></g>
        <text x="600" y="198" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">ONE</text>
        <text x="600" y="228" text-anchor="middle" font-family="DM Sans" font-weight="900" font-size="24" fill="#2a160c">OPERATOR</text>
        <text x="600" y="366" text-anchor="middle" font-family="DM Mono" font-size="13" letter-spacing=".08em" fill="#8f8f85">brain &middot; memory &middot; hands</text>
      </svg>
      {cap("one chat, plugged into the real tools you already pay for.")}</div>'''

PANELS={"gap":gap(),"plug":plug(),"connect":connect(),"grid":grid(),
        "reach":reach(),"flow":flow(),"auth":auth(),"operator":operator()}
if __name__=="__main__":
    outd=f"{ROOT}/content/_hitl-src/models_clay/s3src52"; os.makedirs(outd,exist_ok=True)
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
