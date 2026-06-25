#!/usr/bin/env python3
# Coded 9:16 carousel (docs-style) for OPERATOR STACK. Each slide = one HTML doc:
# small 3D sunburst mark + eyebrow + headline + a CODED UI card + description + progress/footer.
import os
from playwright.sync_api import sync_playwright
TE="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/te-gen"
OUT=f"{TE}/roll3/operator_docs"; os.makedirs(OUT,exist_ok=True)
F=f"file://{TE}"; ACCENT=f"file://{TE}/claude_logo_genuine.png"
CSS=f"""
@font-face{{font-family:'DMSans';src:url('{F}/DMSans-VF.ttf');font-weight:100 900;}}
@font-face{{font-family:'DMMono';src:url('{F}/DMMono-Medium.ttf');font-weight:500;}}
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{background:#0f0f0f;}}
#artifact{{width:1080px;height:1920px;background:#161514;position:relative;overflow:hidden;
 font-family:'DMSans',sans-serif;padding:215px 72px 200px;display:flex;flex-direction:column;justify-content:center;}}
#artifact::before{{content:'';position:absolute;inset:0;background-image:radial-gradient(rgba(200,100,63,.05) 1.1px,transparent 1.2px);background-size:32px 32px;opacity:.5;}}
.ghost{{position:absolute;top:60px;right:42px;font-family:'DMSans';font-weight:900;font-size:360px;color:#201e1c;line-height:1;z-index:0;}}
.mark{{width:92px;height:92px;margin-bottom:30px;position:relative;z-index:2;filter:drop-shadow(0 12px 22px rgba(0,0,0,.4));}}
.eyebrow{{position:relative;z-index:2;font-family:'DMMono';font-weight:500;font-size:27px;letter-spacing:.34em;text-transform:uppercase;color:#C8643F;}}
.head{{position:relative;z-index:2;font-weight:900;font-size:96px;line-height:1.02;letter-spacing:-2px;color:#FAFAF7;margin-top:24px;}}
.head .o{{color:#C8643F;}}
.desc{{position:relative;z-index:2;margin-top:46px;font-weight:400;font-size:34px;line-height:1.5;color:#9a988f;max-width:910px;}}
.desc b{{color:#FAFAF7;font-weight:700;}}
.card{{position:relative;z-index:2;margin-top:60px;background:#1d1c1a;border:1px solid rgba(250,250,247,.09);border-radius:24px;padding:26px;box-shadow:0 30px 70px rgba(0,0,0,.45);}}
.chead{{display:flex;align-items:center;justify-content:space-between;padding:4px 4px 19px;margin-bottom:6px;border-bottom:1px solid rgba(250,250,247,.07);}}
.chead .t{{display:flex;align-items:center;gap:13px;font-family:'DMSans';font-weight:700;font-size:27px;color:#FAFAF7;}}
.cdot{{width:11px;height:11px;border-radius:50%;background:#C8643F;flex:none;}}
.chead .m{{font-family:'DMMono';font-size:20px;color:#83817b;letter-spacing:.04em;}}
.tag{{font-family:'DMMono';font-weight:500;font-size:16px;letter-spacing:.12em;text-transform:uppercase;color:#94918a;background:rgba(250,250,247,.07);border-radius:6px;padding:6px 11px;}}
.tag.o{{color:#1a0f0a;background:#C8643F;}}
.row{{display:flex;align-items:center;justify-content:space-between;padding:18px;border-radius:12px;}}
.row .l{{display:flex;align-items:center;gap:16px;min-width:0;}}
.dot{{width:9px;height:9px;border-radius:50%;background:#5f5d57;flex:none;}}
.name{{font-family:'DMMono';font-weight:500;font-size:26px;color:#cfcdc7;letter-spacing:-.2px;}}
.sub{{font-family:'DMSans';font-weight:400;font-size:22px;color:#83817b;}}
.row.on{{background:rgba(200,100,63,.13);box-shadow:inset 3px 0 0 #C8643F;}}
.row.on .dot{{background:#C8643F;}}.row.on .name{{color:#FAFAF7;}}
.input{{display:flex;align-items:center;justify-content:space-between;background:#26241f;border:1px solid rgba(250,250,247,.08);border-radius:13px;padding:18px;margin:14px 0;}}
.input .l{{display:flex;align-items:center;gap:14px;}}
.slash{{width:38px;height:38px;border-radius:9px;background:rgba(200,100,63,.16);color:#C8643F;font-family:'DMMono';font-weight:500;font-size:22px;display:flex;align-items:center;justify-content:center;}}
.q{{font-family:'DMMono';font-weight:500;font-size:27px;color:#FAFAF7;}}.cur{{display:inline-block;width:2px;height:28px;background:#C8643F;margin-left:3px;transform:translateY(4px);}}
.enter{{font-family:'DMMono';font-size:19px;color:#7c7a74;}}
.av{{width:46px;height:46px;border-radius:50%;flex:none;background:linear-gradient(135deg,#3a3733,#2a2825);}}
.ck{{width:26px;height:26px;color:#C8643F;font-size:24px;flex:none;}}
.pbar{{flex:1;height:8px;border-radius:4px;background:#322f2b;overflow:hidden;margin:0 14px;}}
.pbar i{{display:block;height:100%;background:#C8643F;border-radius:4px;}}
.tog{{width:62px;height:34px;border-radius:17px;background:#C8643F;position:relative;flex:none;}}
.tog::after{{content:'';position:absolute;right:4px;top:4px;width:26px;height:26px;border-radius:50%;background:#fff;}}
.foot{{position:absolute;left:72px;right:72px;bottom:150px;z-index:2;display:flex;align-items:center;gap:22px;}}
.bar{{flex:1;height:7px;border-radius:4px;background:#322f2b;overflow:hidden;}}.bar i{{display:block;height:100%;background:#C8643F;border-radius:4px;}}
.pg{{font-family:'DMMono';font-size:26px;color:#83817b;letter-spacing:.06em;}}
.url{{font-family:'DMMono';font-weight:500;font-size:30px;color:#C8643F;letter-spacing:.02em;}}
.ulogo{{width:50px;height:50px;border-radius:50%;object-fit:cover;flex:none;}}
.cover-burst{{width:330px;height:330px;align-self:center;margin:64px 0 0;position:relative;z-index:2;filter:drop-shadow(0 30px 50px rgba(0,0,0,.5));}}
.swipe{{position:absolute;left:0;right:0;bottom:140px;display:flex;justify-content:center;z-index:3;}}
.swipe span{{display:inline-flex;align-items:center;gap:14px;background:#C8643F;color:#fff;font-weight:800;font-size:34px;
 padding:18px 40px;border-radius:40px;box-shadow:0 0 40px rgba(200,100,63,.4);}}
"""
def CK(): return '<span class="ck">&#10003;</span>'
def rows(items):
    h=""
    for it in items:
        on=" on" if it.get("on") else ""
        left=f'<span class="dot"></span>' if it.get("dot",True) else ''
        nm=f'<span class="name">{it["name"]}</span>'
        sub=f'<span class="sub">{it["sub"]}</span>' if it.get("sub") else ''
        tag=f'<span class="tag{" o" if it.get("ot") else ""}">{it["tag"]}</span>' if it.get("tag") else ''
        h+=f'<div class="row{on}"><div class="l">{left}{nm}{sub}</div>{tag}</div>'
    return h
def card(title,meta,body,mtag=None):
    mt=f'<span class="tag{" o" if False else ""}">{mtag}</span>' if mtag else (f'<span class="m">{meta}</span>' if meta else '')
    return f'<div class="card"><div class="chead"><div class="t"><span class="cdot"></span>{title}</div>{mt}</div>{body}</div>'

def c_slash():
    inp='<div class="input"><div class="l"><div class="slash">/</div><span class="q">cold</span><span class="cur"></span></div><span class="enter">enter &#8629;</span></div>'
    r=rows([{"name":"/competitive-analysis","tag":"Research"},{"name":"/cold-outreach","tag":"Sales","on":True,"ot":True},
            {"name":"/morning-briefing","tag":"Ops"},{"name":"/vc-prospector","tag":"Lead-gen"},{"name":"/quarterly-recap","tag":"Research"}])
    return card("Skills","71 available",inp+r)
def c_plan():
    b=('<div class="row"><div class="l">'+CK()+'<span class="name" style="color:#cfcdc7">Pull rivals + score positioning</span></div><span class="m" style="font-family:DMMono;color:#83817b;font-size:20px">2.1s</span></div>'
       '<div class="row on"><div class="l"><span class="dot"></span><span class="name">Draft outreach sequence</span></div><span class="m" style="font-family:DMMono;color:#C8643F;font-size:20px">running</span></div>'
       '<div class="row" style="padding-top:0"><div class="pbar"><i style="width:64%"></i></div></div>'
       '<div class="row"><div class="l"><span class="dot" style="background:#3a3a36"></span><span class="name" style="color:#7c7a74">Sync to CRM + notify human gate</span></div><span class="m" style="font-family:DMMono;color:#6b6963;font-size:20px">queued</span></div>')
    return card("Active plan","3 steps",b)
def c_agents():
    r=rows([{"name":"CORTEX","sub":"researches the account","tag":"Research"},
            {"name":"SPECTER","sub":"writes the outbound","tag":"Sales","on":True,"ot":True},
            {"name":"STRIKER","sub":"runs the deal","tag":"Deals"},
            {"name":"PULSE","sub":"writes in your voice","tag":"Content"},
            {"name":"SENTINEL","sub":"ships the code","tag":"Code"},
            {"name":"AMPLIFY","sub":"publishes per channel","tag":"Publish"},
            {"name":"COUNSEL","sub":"drafts the contract","tag":"Legal"}])
    return card("Agents","7 active",r)
def c_files():
    b=(rows([{"name":"skill.yaml","tag":"192 B","dot":False},{"name":"prompt.md","tag":"1.4 KB","dot":False},{"name":"tools.allow","tag":"86 B","dot":False}])
       .replace('<span class="dot"></span>','')
       +'<div class="row"><div class="l"><span class="dot"></span><span class="name" style="color:#C8643F">registry reload pending</span></div></div>')
    # add checks
    b=b.replace('<div class="l"><span class="name">skill.yaml','<div class="l">'+CK()+'<span class="name">skill.yaml')
    b=b.replace('<div class="l"><span class="name">prompt.md','<div class="l">'+CK()+'<span class="name">prompt.md')
    b=b.replace('<div class="l"><span class="name">tools.allow','<div class="l">'+CK()+'<span class="name">tools.allow')
    return card("quarterly-recap",None,b,mtag="Research")
def c_dash():
    r=rows([{"name":"Northwind Labs","sub":"Hiring 3 AEs","tag":"92","ot":True},
            {"name":"Belmont Freight","sub":"Series A, 14d ago","tag":"88","ot":True},
            {"name":"Carver Studios","sub":"Left a rival tool","tag":"81","ot":True},
            {"name":"Halden Group","sub":"Budget signal in 10-K","tag":"76","ot":True}])
    return card("Ranked accounts","by buying signal",r)
def c_routing():
    b=('<div class="row"><div class="l"><span class="name">Lite &middot; Haiku</span></div><div class="pbar" style="max-width:240px"><i style="width:30%"></i></div></div>'
       '<div class="row"><div class="l"><span class="name">Smart &middot; Sonnet</span></div><div class="pbar" style="max-width:240px"><i style="width:62%"></i></div></div>'
       '<div class="row"><div class="l"><span class="name">Deep &middot; Opus</span></div><div class="pbar" style="max-width:240px"><i style="width:85%"></i></div></div>'
       '<div class="row on"><div class="l"><span class="dot"></span><span class="name">Human gate</span></div><span class="tag o">ON</span></div>')
    return card("Model routing","auto",b)
def c_comment():
    b=('<div class="row"><div class="l"><span class="av"></span><div><div class="name" style="font-size:24px;color:#e6e4de">founder_mode</div><div class="sub">send me the setup</div></div></div></div>'
       '<div class="row"><div class="l"><span class="av"></span><div><div class="name" style="font-size:24px;color:#e6e4de">ops_anna</div><div class="sub">need this</div></div></div></div>'
       '<div class="input" style="margin-bottom:0"><div class="l"><span class="q" style="font-size:26px">OPERATOR</span><span class="cur"></span></div><span class="tag o" style="padding:9px 18px;font-size:18px">Post</span></div>')
    return card("Comments","2.4k",b)

SLIDES=[
 dict(n=1,role="cover",eb="The operator stack",head='I gave Ultron<br><span class="o">7 jobs.</span><br>It runs the company.',sub="One operator. 71 skills, 92 tools, one $19 plan.",burst=True),
 dict(n=2,role="mid",eb="Why it works",head='You don\'t need a team.<br><span class="o">You need an operator.</span>',card=c_plan(),desc='Ask in plain English. The operator drafts a plan, runs the skills, and <b>pauses at every step that leaves the building</b>.'),
 dict(n=3,role="mid",eb="The roster",head='7 agents.<br><span class="o">One per job.</span>',card=c_agents(),desc='Each agent owns a lane, hands off to the next, and shares the same memory of your business.'),
 dict(n=4,role="mid",eb="Run a skill",head='71 skills.<br><span class="o">One slash away.</span>',card=c_slash(),desc='Trigger any skill from chat with a slash command or plain language. Each loads <b>its model, its tools and its quality bar</b>.'),
 dict(n=5,role="mid",eb="Build a skill",head='Build one<br><span class="o">in minutes.</span>',card=c_files(),desc='A manifest, a tool allow-list and a model tier. Scaffold it once and it is <b>loaded on the next start</b>.'),
 dict(n=6,role="mid",eb="Agent 01 / research",head='Account research<br><span class="o">runs itself.</span>',card=c_dash(),desc='It reads the web, the funding and the hiring, then ranks every account so you call the right one first.'),
 dict(n=7,role="mid",eb="Routing + control",head='3 model tiers.<br><span class="o">1 human gate.</span>',card=c_routing(),desc='The router picks the cheapest model that can do the job, and <b>nothing irreversible ships without your yes</b>.'),
 dict(n=8,role="last",eb="Get the setup",head='Comment <span class="o">OPERATOR</span>.<br>I will send it.',card=c_comment(),desc='The exact operator setup I run my company on. Follow for one AI system for founders every day.'),
]
N=len(SLIDES)
def html(s):
    mark=f'<img class="mark" src="{ACCENT}">'
    ghost=f'<div class="ghost">{s["n"]:02d}</div>'
    body=mark+f'<div class="eyebrow">{s["eb"]}</div><div class="head">{s["head"]}</div>'
    if s.get("sub"): body+=f'<div class="desc" style="margin-top:30px">{s["sub"]}</div>'
    if s.get("burst"): body+=f'<img class="cover-burst" src="{ACCENT}">'
    if s.get("card"): body+=s["card"]
    if s.get("desc"): body+=f'<div class="desc">{s["desc"]}</div>'
    if s["role"]=="cover": body+='<div class="swipe"><span>Swipe &#8594;</span></div>'
    elif s["role"]=="last": body+=f'<div class="foot"><img class="ulogo" src="file:///home/user/tiberiu-claude/content/ultron-logo.png"><span class="url" style="margin-left:4px">51ultron.com</span><div style="flex:1"></div><span class="pg">{s["n"]:02d} / {N:02d}</span></div>'
    else: body+=f'<div class="foot"><div class="bar"><i style="width:{int(s["n"]/N*100)}%"></i></div><span class="pg">{s["n"]:02d} / {N:02d}</span></div>'
    # cover: hide the small top mark (use the big burst instead)
    if s.get("burst"): body=body.replace(mark,"",1)
    return f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="artifact">{ghost}{body}</div></body></html>'

with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920},device_scale_factor=2)
    for s in SLIDES:
        fp=f"{OUT}/s{s['n']}.html"; open(fp,"w").write(html(s))
        pg.goto(f"file://{fp}"); pg.wait_for_timeout(500)
        pg.locator("#artifact").screenshot(path=f"{OUT}/s{s['n']}.png")
        print("built",s["n"])
    b.close()
from PIL import Image
ims=[Image.open(f"{OUT}/s{i}.png") for i in range(1,N+1)]
cols=4;rows_=2;sc=300;sh=int(sc*1920/1080)
st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows_+8*(rows_+1)),(18,18,20))
for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
st.save(f"{TE}/operator_docs_montage.png"); print("montage saved")
