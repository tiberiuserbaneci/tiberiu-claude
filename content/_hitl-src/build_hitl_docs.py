#!/usr/bin/env python3
# TikTok 2D coded (Model A) - HUMAN GATE. Coded approval-card UIs at 1080x1920.
import os
from playwright.sync_api import sync_playwright
TE="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/te-gen"
OUT=f"{TE}/roll3/hitl_docs"; os.makedirs(OUT,exist_ok=True)
F=f"file://{TE}"; ACCENT=f"file://{TE}/claude_official.png"; ULOGO="file:///home/user/tiberiu-claude/content/ultron-logo.png"
CSS=f"""
@font-face{{font-family:'DMSans';src:url('{F}/DMSans-VF.ttf');font-weight:100 900;}}
@font-face{{font-family:'DMMono';src:url('{F}/DMMono-Medium.ttf');font-weight:500;}}
*{{margin:0;padding:0;box-sizing:border-box;}}html,body{{background:#0f0f0f;}}
#artifact{{width:1080px;height:1920px;background:#161514;position:relative;overflow:hidden;font-family:'DMSans',sans-serif;padding:300px 78px 470px;display:flex;flex-direction:column;justify-content:center;}}
#artifact::before{{content:'';position:absolute;inset:0;background-image:radial-gradient(rgba(204,120,92,.05) 1.1px,transparent 1.2px);background-size:32px 32px;opacity:.5;}}
.ghost{{position:absolute;top:308px;right:150px;font-family:'DMSans';font-weight:900;font-size:250px;color:#201e1c;line-height:1;z-index:0;}}
.mark{{width:66px;height:66px;margin-bottom:12px;position:relative;z-index:2;filter:drop-shadow(0 12px 22px rgba(0,0,0,.4));}}
.eyebrow{{position:relative;z-index:2;font-family:'DMMono';font-weight:500;font-size:26px;letter-spacing:.34em;text-transform:uppercase;color:#C8643F;}}
.head{{position:relative;z-index:2;font-weight:900;font-size:96px;line-height:1.02;letter-spacing:-2px;color:#FAFAF7;margin-top:20px;}}
.head.mid{{font-size:76px;letter-spacing:-1.5px;}}
.head .o{{color:#C8643F;}}
.desc{{position:relative;z-index:2;margin-top:30px;font-weight:400;font-size:31px;line-height:1.46;color:#9a988f;max-width:910px;}}
.desc b{{color:#FAFAF7;font-weight:700;}}
.desc .fl{{display:block;color:#FAFAF7;font-weight:700;margin-top:10px;}}
.card{{position:relative;z-index:2;margin-top:34px;background:#1d1c1a;border:1px solid rgba(250,250,247,.09);border-radius:22px;padding:22px 24px;box-shadow:0 30px 70px rgba(0,0,0,.45);}}
.chead{{display:flex;align-items:center;justify-content:space-between;padding:2px 4px 13px;margin-bottom:6px;border-bottom:1px solid rgba(250,250,247,.07);}}
.chead .t{{display:flex;align-items:center;gap:13px;font-family:'DMSans';font-weight:700;font-size:27px;color:#FAFAF7;}}
.cdot{{width:12px;height:12px;border-radius:50%;background:#C8643F;flex:none;box-shadow:0 0 14px #C8643F;}}
.chead .m{{font-family:'DMMono';font-size:20px;color:#83817b;letter-spacing:.04em;}}
.tag{{font-family:'DMMono';font-weight:500;font-size:16px;letter-spacing:.12em;text-transform:uppercase;color:#94918a;background:rgba(250,250,247,.07);border-radius:6px;padding:6px 11px;}}
.tag.o{{color:#1a0f0a;background:#C8643F;}}
.row{{display:flex;align-items:center;justify-content:space-between;padding:12px 8px;}}
.row+.row{{border-top:1px solid rgba(250,250,247,.05);}}
.row .l{{display:flex;align-items:center;gap:15px;min-width:0;}}
.ic{{width:37px;height:37px;border-radius:9px;background:rgba(200,100,63,.12);border:1px solid rgba(200,100,63,.3);display:flex;align-items:center;justify-content:center;flex:none;}}
.ic svg{{width:19px;height:19px;stroke:#C8643F;stroke-width:2;fill:none;stroke-linecap:round;stroke-linejoin:round;}}
.nm{{font-weight:700;font-size:25px;color:#eceae4;}}
.sub{{font-family:'DMSans';font-weight:400;font-size:21px;color:#83817b;margin-top:2px;}}
.apa{{font-weight:800;font-size:38px;color:#FAFAF7;letter-spacing:-.5px;line-height:1.12;margin-top:6px;}}
.apm{{margin-top:12px;font-size:23px;color:#9a988f;}}.apm b{{color:#D4A27F;font-weight:700;}}
.apb{{margin-top:24px;display:flex;gap:14px;}}
.btn{{flex:1;text-align:center;border-radius:12px;padding:18px 0;font-weight:800;font-size:26px;}}
.bo{{background:#C8643F;color:#1a0f0a;box-shadow:0 0 30px rgba(200,100,63,.35);}}
.bn{{background:transparent;color:#9a988f;border:1px solid rgba(250,250,247,.14);}}
.be{{background:transparent;color:#D4A27F;border:1px solid rgba(212,162,127,.3);flex:.6;}}
.inp{{margin-top:6px;background:#26241f;border:1px solid rgba(200,100,63,.4);border-radius:14px;padding:18px 20px;font-family:'DMMono';font-size:27px;color:#FAFAF7;display:flex;align-items:center;}}
.inp .cur{{display:inline-block;width:2px;height:30px;background:#C8643F;margin-left:3px;transform:translateY(4px);}}
.fl{{display:flex;align-items:center;justify-content:space-between;gap:10px;}}
.node{{flex:1;text-align:center;background:#26241f;border:1px solid rgba(250,250,247,.1);border-radius:14px;padding:22px 8px;font-weight:800;font-size:26px;color:#cfcdc7;}}
.node.on{{background:rgba(200,100,63,.16);border-color:#C8643F;color:#FAFAF7;box-shadow:inset 0 0 0 1px rgba(200,100,63,.4);}}
.arr{{color:#C8643F;font-size:30px;font-weight:700;flex:none;}}
.ck{{color:#C8643F;font-size:24px;flex:none;width:26px;}}
.av{{width:46px;height:46px;border-radius:50%;background:linear-gradient(135deg,#3a3733,#2a2825);flex:none;}}
.foot{{position:absolute;left:90px;right:150px;bottom:476px;z-index:2;display:flex;align-items:center;gap:20px;}}
.bar{{flex:1;height:7px;border-radius:4px;background:#322f2b;overflow:hidden;}}.bar i{{display:block;height:100%;background:#C8643F;border-radius:4px;}}
.pg{{font-family:'DMMono';font-size:26px;color:#83817b;letter-spacing:.06em;}}
.ulogo{{width:50px;height:50px;border-radius:50%;object-fit:cover;flex:none;}}
.url{{font-family:'DMMono';font-weight:500;font-size:30px;color:#C8643F;}}
.cover-burst{{width:330px;height:330px;align-self:center;margin:64px 0 0;position:relative;z-index:2;filter:drop-shadow(0 30px 50px rgba(0,0,0,.5));}}
.swipe{{position:absolute;left:0;right:0;bottom:472px;display:flex;justify-content:center;z-index:3;}}
.swipe span{{display:inline-flex;align-items:center;gap:14px;background:#C8643F;color:#fff;font-weight:800;font-size:34px;padding:18px 42px;border-radius:42px;box-shadow:0 0 40px rgba(200,100,63,.4);}}
"""
def ic(p): return f'<span class="ic"><svg viewBox="0 0 24 24">{p}</svg></span>'
SENT='<path d="M3 5h18v14H3z"/><path d="M3 6l9 7 9-7"/>'; CARD='<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>'
PUB='<path d="M4 4h16v12H4z"/><path d="M8 20h8"/>'; DEL='<path d="M3 6h18"/><path d="M8 6V4h8v2"/><path d="M6 6l1 14h10l1-14"/>'
CAL='<rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/>'; SIGN='<path d="M5 21V5a2 2 0 0 1 2-2h7l5 5v13z"/><path d="M9 13l2 2 4-4"/>'
PLUG='<path d="M8 12a4 4 0 0 1 4-4h3a4 4 0 0 1 0 8h-1"/><path d="M16 12a4 4 0 0 1-4 4H9a4 4 0 0 1 0-8h1"/>'
def card(title,meta,body): return f'<div class="card"><div class="chead"><div class="t"><span class="cdot"></span>{title}</div><span class="m">{meta}</span></div>{body}</div>'

def c_approval():
    b=('<div class="apa">Send 240 cold emails to the Q3 list</div>'
       '<div class="apm">Drafted by your outbound agent &middot; <b>cannot be unsent</b> &middot; 240 founders</div>'
       '<div class="apb"><span class="btn bo">Approve</span><span class="btn bn">Decline</span><span class="btn be">Edit</span></div>')
    return card("Approval required","paused",b)
def c_triggers():
    r=(f'<div class="row"><div class="l">{ic(SENT)}<span class="nm">Send a campaign</span></div><span class="tag">mail</span></div>'
       f'<div class="row"><div class="l">{ic(CARD)}<span class="nm">Charge a card</span></div><span class="tag">money</span></div>'
       f'<div class="row"><div class="l">{ic(PUB)}<span class="nm">Publish a post</span></div><span class="tag">public</span></div>'
       f'<div class="row"><div class="l">{ic(DEL)}<span class="nm">Delete records</span></div><span class="tag">data</span></div>'
       f'<div class="row"><div class="l">{ic(CAL)}<span class="nm">Schedule meetings</span></div><span class="tag">calendar</span></div>'
       f'<div class="row"><div class="l">{ic(SIGN)}<span class="nm">Sign an agreement</span></div><span class="tag o">legal</span></div>'
       f'<div class="row"><div class="l">{ic(PLUG)}<span class="nm">Connect an integration</span></div><span class="tag">access</span></div>')
    return card("Needs your yes","7 moves",r)
def c_decide():
    r=('<div class="row"><div class="l"><span class="nm">Approve / Decline</span></div><span class="sub">one tap</span></div>'
       '<div class="row"><div class="l"><span class="nm">Choose</span></div><span class="sub">pick a path</span></div>'
       '<div class="row"><div class="l"><span class="nm">Edit</span></div><span class="sub">tweak first</span></div>')
    return card("Clear the gate","3 ways",r)
def c_edit():
    b=('<div class="apm" style="margin-top:0;margin-bottom:14px">Was: Send to all 240 &middot; you edited it to:</div>'
       '<div class="inp">Send to the top 80 by score<span class="cur"></span></div>'
       '<div class="apb"><span class="btn bo">Approve edit</span><span class="btn bn">Cancel</span></div>')
    return card("Edit before it ships","draft",b)
def c_flow():
    b='<div class="fl"><span class="node">Draft</span><span class="arr">&rarr;</span><span class="node on">Gate</span><span class="arr">&rarr;</span><span class="node">Ship</span></div>'
    return card("The order","locked",b)
def c_audit():
    b=('<div class="row"><div class="l"><span class="ck">&#10003;</span><span class="nm" style="font-size:25px">Approved &middot; Q3 campaign</span></div><span class="sub">you &middot; 2h ago</span></div>'
       '<div class="row"><div class="l"><span class="ck">&#9998;</span><span class="nm" style="font-size:25px">Edited &middot; invoice 4,200 to 3,800</span></div><span class="sub">you &middot; 1d ago</span></div>'
       '<div class="row"><div class="l"><span class="ck" style="color:#9a988f">&#10005;</span><span class="nm" style="font-size:25px">Declined &middot; delete 1,204 rows</span></div><span class="sub">you &middot; 3d ago</span></div>')
    return card("Decision log","audit",b)
def c_comment():
    b=('<div class="row"><div class="l"><span class="av"></span><div><div class="nm" style="font-size:24px">founder_mode</div><div class="sub">send me the setup</div></div></div></div>'
       '<div class="row"><div class="l"><span class="av"></span><div><div class="nm" style="font-size:24px">ops_anna</div><div class="sub">need this</div></div></div></div>'
       '<div class="inp" style="margin-top:14px;justify-content:space-between"><span>GATE<span class="cur"></span></span><span class="tag o" style="padding:10px 20px;font-size:19px">Post</span></div>')
    return card("Comments","2.1k",b)

S=[
 dict(n=1,role="cover",eb=None,head='Your AI can send,<br>charge and delete.<br><span class="o">Mine asks first.</span>',sub="It runs the busywork. It stops before anything it cannot undo.",burst=True),
 dict(n=2,role="mid",eb="The gate",head='It stops before<br><span class="o">it ships.</span>',card=c_approval(),desc='It drafts the work and runs it, then <b>pauses at every step that leaves the building</b> and waits for you.'),
 dict(n=3,role="mid",eb="What needs a yes",head='7 moves that<br><span class="o">need your yes.</span>',card=c_triggers(),desc='Drafting and research run free. Only the irreversible moves park at the gate.'),
 dict(n=4,role="mid",eb="The decision",head='Approve, decline,<br><span class="o">or pick a path.</span>',card=c_decide(),desc='One card, one tap. Say yes, say no, or choose between the options it lays out.'),
 dict(n=5,role="mid",eb="Edit first",head='Change it before<br><span class="o">it ships.</span>',card=c_edit(),desc='Not happy with the draft? <b>Edit the action on the card</b>, then approve the version you actually want.'),
 dict(n=6,role="mid",eb="The rule",head='Before the action.<br><span class="o">Never after.</span>',card=c_flow(),desc='An approval after the fact is theatre. The gate sits before the irreversible step, every single time.'),
 dict(n=7,role="mid",eb="The record",head='Every yes<br><span class="o">is logged.</span>',card=c_audit(),desc='Who approved what, when, and any edit. A clean trail you can hand to anyone.'),
 dict(n=8,role="last",eb="Get the setup",head='Comment <span class="o">GATE</span>.<br>I will send it.',card=c_comment(),desc='The exact human-gate setup I run my company on.<span class="fl">Follow for one AI system for founders every day.</span>'),
]
N=len(S)
def html(s):
    g=f'<div class="ghost">{s["n"]:02d}</div>'; body=g
    # Claude logo only on the cover (big burst). Slides 2-8 carry no mark (operator).
    if s.get("eb"): body+=f'<div class="eyebrow">{s["eb"]}</div>'
    body+=f'<div class="head{"" if s.get("burst") else " mid"}">{s["head"]}</div>'
    if s.get("sub"): body+=f'<div class="desc" style="margin-top:30px">{s["sub"]}</div>'
    if s.get("burst"): body+=f'<img class="cover-burst" src="{ACCENT}">'
    if s.get("card"): body+=s["card"]
    if s.get("desc"): body+=f'<div class="desc">{s["desc"]}</div>'
    if s["role"]=="cover": body+='<div class="swipe"><span>Swipe &#8594;</span></div>'
    elif s["role"]=="last": body+=f'<div class="foot"><img class="ulogo" src="{ULOGO}"><span class="url" style="margin-left:4px">51ultron.com</span></div>'
    else: body+=f'<div class="foot"><div class="bar"><i style="width:{int(s["n"]/N*100)}%"></i></div></div>'
    return f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div id="artifact">{body}</div></body></html>'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1920},device_scale_factor=2)
    for s in S:
        fp=f"{OUT}/s{s['n']}.html"; open(fp,"w").write(html(s)); pg.goto(f"file://{fp}"); pg.wait_for_timeout(450)
        m=pg.evaluate("""()=>{const a=document.getElementById('artifact');let t=1e9,b=-1e9;for(const c of a.children){if(getComputedStyle(c).position==='absolute')continue;const r=c.getBoundingClientRect();if(r.height<2)continue;t=Math.min(t,r.top);b=Math.max(b,r.bottom);}return {t:Math.round(t),b:Math.round(b)};}""")
        flag="" if (m["t"]>=300 and m["b"]<=1450) else "  <-- OUT"
        print(f"s{s['n']} [{m['t']},{m['b']}] h={m['b']-m['t']}{flag}")
        pg.locator("#artifact").screenshot(path=f"{OUT}/s{s['n']}.png")
    b.close()
from PIL import Image
ims=[Image.open(f"{OUT}/s{i}.png") for i in range(1,N+1)]
cols=4;rows=2;sc=300;sh=int(sc*1920/1080)
st=Image.new("RGB",(sc*cols+8*(cols+1),sh*rows+8*(rows+1)),(18,18,20))
for k,im in enumerate(ims): st.paste(im.resize((sc,sh)),(8+(k%cols)*(sc+8),8+(k//cols)*(sh+8)))
st.save(f"{TE}/hitl_docs_montage.png"); print("montage saved")
