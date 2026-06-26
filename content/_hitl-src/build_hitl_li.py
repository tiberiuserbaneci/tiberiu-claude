#!/usr/bin/env python3
# HUMAN GATE - LinkedIn dense infographic (Dark Ultron, 1080x1450).
# Flex-column layout (header/body/footer can't overlap). Capture-two density:
# packed cards/tables, tiny mono text, color-coded icons, ZERO dead space.
import base64
from playwright.sync_api import sync_playwright
TE="/tmp/claude-0/-home-user-tiberiu-claude/27326f10-40bf-555b-a3d3-cdb5d2e54cdb/scratchpad/te-gen"
REPO="/home/user/tiberiu-claude"
OUT=f"{REPO}/content/hitl-linkedin.html"; PNG=f"{REPO}/content/hitl-linkedin.png"
LOGO=f"{REPO}/content/ultron-logo.png"
logo_b64="data:image/png;base64,"+base64.b64encode(open(LOGO,"rb").read()).decode()
GOOGLE='<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700;9..40,800;9..40,900&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">'
LOCAL=("<style>@font-face{font-family:'DM Sans';src:url('file://"+TE+"/DMSans-VF.ttf');font-weight:100 900;}"
       "@font-face{font-family:'DM Mono';src:url('file://"+TE+"/DMMono-Medium.ttf');font-weight:400 500;}</style>")

CSS=r"""
*{margin:0;padding:0;box-sizing:border-box;}
html,body{background:#0c0c0c;font-family:'DM Sans',sans-serif;}
#artifact{width:1080px;height:1450px;background:#191919;position:relative;overflow:hidden;color:#FAFAF7;display:flex;flex-direction:column;padding:30px 34px 22px;}
#artifact::before{content:'';position:absolute;inset:0;pointer-events:none;z-index:0;background-image:radial-gradient(rgba(204,120,92,.05) 1.2px,transparent 1.3px);background-size:26px 26px;}
.atm{position:absolute;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse 58% 34% at 92% 0%,rgba(204,120,92,.15) 0%,transparent 60%),radial-gradient(ellipse 40% 26% at 4% 99%,rgba(212,162,127,.07) 0%,transparent 60%);}
/* header */
.hd{flex:none;display:flex;gap:22px;align-items:stretch;padding-bottom:15px;border-bottom:1px solid rgba(250,250,247,.10);position:relative;z-index:2;}
.hook{flex:1;min-width:0;display:flex;flex-direction:column;justify-content:center;}
.eye{font-family:'DM Mono',monospace;font-weight:500;font-size:12.5px;letter-spacing:.24em;text-transform:uppercase;color:#9a958c;}
.eye b{color:#CC785C;font-weight:500;}
.h1{font-weight:900;font-size:61px;line-height:1.01;letter-spacing:-2.2px;margin-top:11px;}
.h1 .o{color:#C84623;}
.desc{margin-top:12px;font-weight:400;font-size:15px;line-height:1.45;color:rgba(250,250,247,.66);max-width:610px;}
.desc b{color:#FAFAF7;font-weight:600;}
.tiles{flex:none;width:292px;display:flex;flex-direction:column;gap:8px;justify-content:center;}
.tile{border:1px solid rgba(250,250,247,.10);border-radius:11px;padding:12px 15px;background:#211f1e;}
.tile .l{font-family:'DM Mono',monospace;font-weight:500;font-size:9.5px;letter-spacing:.16em;text-transform:uppercase;color:#8d887f;}
.tile .v{font-weight:800;font-size:19px;letter-spacing:-.5px;margin-top:6px;line-height:1;}
.tile .v.o{color:#CC785C;}
.tile .s{font-family:'DM Mono',monospace;font-size:9.5px;letter-spacing:.02em;color:#83817b;margin-top:6px;}
/* body */
.body{flex:1;display:flex;gap:13px;min-height:0;margin:13px 0;position:relative;z-index:2;}
.col{flex:1;display:flex;flex-direction:column;gap:10px;min-width:0;}
.card{border:1px solid rgba(250,250,247,.09);border-radius:13px;background:#1c1b19;padding:11px 15px;}
.card.hero{border:1px solid rgba(204,120,92,.42);background:rgba(204,120,92,.055);}
.card.fill{flex:1;display:flex;flex-direction:column;}
.ch{display:flex;align-items:baseline;justify-content:space-between;gap:10px;padding-bottom:8px;margin-bottom:7px;border-bottom:1px solid rgba(250,250,247,.08);}
.ct{font-weight:800;font-size:16.5px;letter-spacing:-.3px;color:#FAFAF7;}
.ctag{font-family:'DM Mono',monospace;font-weight:500;font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;color:#83817b;white-space:nowrap;}
.ctag.o{color:#CC785C;}
/* rows */
.r{display:flex;align-items:center;gap:9px;padding:4px 0;}
.r+.r{border-top:1px solid rgba(250,250,247,.05);}
.ic{width:25px;height:25px;border-radius:7px;background:rgba(204,120,92,.12);border:1px solid rgba(204,120,92,.28);display:flex;align-items:center;justify-content:center;flex:none;}
.ic svg{width:14px;height:14px;stroke:#CC785C;stroke-width:2;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.rn{font-weight:600;font-size:14px;color:#e9e7e1;letter-spacing:-.2px;white-space:nowrap;flex:none;}
.dash{flex:1;border-bottom:1.5px dotted rgba(250,250,247,.14);margin:0 9px;min-width:10px;height:1px;}
.rv{font-family:'DM Mono',monospace;font-size:12px;color:#8d887f;flex:none;letter-spacing:.01em;white-space:nowrap;}
.rv.o{color:#CC785C;}
/* hero */
.bigact{font-weight:800;font-size:22px;line-height:1.16;letter-spacing:-.5px;color:#FAFAF7;}
.meta{margin-top:8px;font-size:12.5px;line-height:1.4;color:rgba(250,250,247,.6);}
.meta b{color:#FAFAF7;font-weight:700;}
.btns{display:flex;gap:9px;margin-top:12px;}
.btn{flex:1;text-align:center;border-radius:9px;padding:10px 0;font-weight:800;font-size:13.5px;letter-spacing:-.2px;}
.ba{background:#CC785C;color:#1a0f0a;box-shadow:0 0 26px rgba(204,120,92,.3);}
.bn{background:transparent;color:#9a958c;border:1px solid rgba(250,250,247,.15);}
.be{background:transparent;color:#D4A27F;border:1px solid rgba(212,162,127,.32);flex:.62;}
/* bullets */
.bl{display:flex;gap:9px;align-items:flex-start;padding:4px 0;}
.bl .d{width:6px;height:6px;border-radius:50%;background:#CC785C;flex:none;margin-top:7px;}
.bt{font-weight:500;font-size:13.5px;line-height:1.3;color:#d8d6cf;letter-spacing:-.1px;}
.bt b{color:#FAFAF7;font-weight:700;}
/* flow */
.flow{display:flex;align-items:center;gap:7px;}
.node{flex:1;text-align:center;background:#26241f;border:1px solid rgba(250,250,247,.1);border-radius:11px;padding:13px 4px;font-weight:800;font-size:16px;color:#cfcdc7;letter-spacing:-.3px;}
.node.on{background:rgba(204,120,92,.16);border-color:#CC785C;color:#FAFAF7;box-shadow:inset 0 0 0 1px rgba(204,120,92,.4);}
.ar{color:#CC785C;font-size:19px;font-weight:700;flex:none;}
.fcap{margin-top:10px;font-size:12.5px;line-height:1.4;color:#8d887f;}
.fcap b{color:#CC785C;font-weight:600;}
/* edit input */
.was{font-size:12.5px;color:#8d887f;margin-bottom:8px;line-height:1.35;}.was b{color:#d8d6cf;font-weight:600;}
.inp{background:#26241f;border:1px solid rgba(204,120,92,.4);border-radius:10px;padding:12px 14px;font-family:'DM Mono',monospace;font-size:15px;color:#FAFAF7;display:flex;align-items:center;}
.inp .cur{display:inline-block;width:2px;height:17px;background:#CC785C;margin-left:3px;}
/* compare */
.cmp{display:grid;grid-template-columns:72px 1fr 1fr;align-items:center;}
.cmp>div{padding:6px 4px;}
.cmp .hl{}
.cmp .hr{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.06em;text-transform:uppercase;font-weight:500;}
.cmp .hr.n{color:#8d887f;}.cmp .hr.g{color:#CC785C;}
.cmp .k{font-family:'DM Mono',monospace;font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:#9a958c;}
.cmp .v{font-size:13px;color:#cdcbc4;font-weight:500;}
.cmp .v.g{color:#FAFAF7;font-weight:600;}
.cmp .rowline{border-top:1px solid rgba(250,250,247,.05);}
/* glossary - inline full width */
.g{display:flex;align-items:baseline;gap:8px;padding:6px 0;}
.g+.g{border-top:1px solid rgba(250,250,247,.05);}
.gt{font-weight:700;font-size:13px;color:#FAFAF7;letter-spacing:-.2px;white-space:nowrap;flex:none;}
.gdash{flex:1;border-bottom:1.5px dotted rgba(250,250,247,.14);height:1px;min-width:10px;}
.gd{font-size:12px;color:#8d887f;flex:none;white-space:nowrap;}
.gmono{margin-top:9px;font-family:'DM Mono',monospace;font-size:10.5px;letter-spacing:.04em;color:#6f6a62;border-top:1px solid rgba(250,250,247,.06);padding-top:8px;line-height:1.4;}
/* bottom */
.bot{flex:none;position:relative;z-index:2;}
.follow{font-weight:700;font-size:14.5px;letter-spacing:-.2px;color:#FAFAF7;margin-bottom:9px;}
.bar{display:flex;align-items:center;gap:11px;background:#211f1e;border:1px solid rgba(204,120,92,.36);border-radius:13px;padding:9px 9px 9px 19px;box-shadow:0 12px 30px rgba(0,0,0,.38);}
.bar .ph{flex:1;font-family:'DM Mono',monospace;font-weight:500;font-size:17px;color:#CC785C;letter-spacing:-.2px;}
.bar .ph .cur{display:inline-block;width:2px;height:18px;background:#CC785C;margin-left:3px;transform:translateY(3px);}
.send{width:46px;height:46px;border-radius:11px;background:#CC785C;display:flex;align-items:center;justify-content:center;flex:none;box-shadow:0 0 24px rgba(204,120,92,.38);}
.send svg{width:22px;height:22px;stroke:#1a0f0a;stroke-width:2;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.foot{display:flex;align-items:center;justify-content:space-between;gap:14px;margin-top:11px;}
.foot .fl{display:flex;align-items:center;gap:11px;min-width:0;}
.foot .ulogo{width:29px;height:29px;border-radius:50%;object-fit:cover;flex:none;}
.foot .br{font-family:'DM Mono',monospace;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:#83817b;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}
.foot .br b{color:#FAFAF7;font-weight:500;}
.foot .url{font-weight:900;font-size:16px;letter-spacing:-.4px;color:#FAFAF7;flex:none;}
.foot .url em{color:#CC785C;font-style:normal;}
"""

def ic(p): return f'<span class="ic"><svg viewBox="0 0 24 24">{p}</svg></span>'
SENT='<path d="M3 5h18v14H3z"/><path d="M3 6l9 7 9-7"/>'
CARD='<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>'
PUB='<path d="M4 4h16v12H4z"/><path d="M8 20h8"/>'
DEL='<path d="M3 6h18"/><path d="M8 6V4h8v2"/><path d="M6 6l1 14h10l1-14"/>'
CAL='<rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/>'
SIGN='<path d="M5 21V5a2 2 0 0 1 2-2h7l5 5v13z"/><path d="M9 13l2 2 4-4"/>'
PLUG='<path d="M8 12a4 4 0 0 1 4-4h3a4 4 0 0 1 0 8h-1"/><path d="M16 12a4 4 0 0 1-4 4H9a4 4 0 0 1 0-8h1"/>'
MONEY='<circle cx="12" cy="12" r="9"/><path d="M12 7v10M9.5 9.5h4a1.8 1.8 0 0 1 0 3.6h-3a1.8 1.8 0 0 0 0 3.6h4"/>'
CLOCK='<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'
SEND2='<path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4z"/>'

def tile(l,v,s,o=False): return f'<div class="tile"><div class="l">{l}</div><div class="v{" o" if o else ""}">{v}</div><div class="s">{s}</div></div>'
def card(t,tag,inner,cls="",tago=False): return f'<div class="card {cls}"><div class="ch"><span class="ct">{t}</span><span class="ctag{" o" if tago else ""}">{tag}</span></div>{inner}</div>'
def girow(svg,nm,conseq,acc=False): return f'<div class="r">{ic(svg)}<span class="rn">{nm}</span><span class="dash"></span><span class="rv{" o" if acc else ""}">{conseq}</span></div>'
def frow(nm,val): return f'<div class="r"><span class="rn">{nm}</span><span class="dash"></span><span class="rv">{val}</span></div>'
def bull(t): return f'<div class="bl"><span class="d"></span><span class="bt">{t}</span></div>'
def glo(t,d): return f'<div class="g"><span class="gt">{t}</span><span class="gdash"></span><span class="gd">{d}</span></div>'

# header
TILES=(tile("Default","Paused","on any risk move")
      +tile("Scope","Irreversible","send, charge, delete",True)
      +tile("Trail","Logged","who, what, when"))
HEAD=(f'<div class="hd"><div class="hook">'
 f'<div class="eye"><b>Ultron</b> &middot; Human gate &middot; Approval layer</div>'
 f'<div class="h1">AI agents act<br>on their own.<br><span class="o">Mine asks first.</span></div>'
 f'<div class="desc">The approval layer between your autonomous AI agents and the outside world. '
 f'Research and drafting run free. <b>Every irreversible move waits for one human yes.</b></div></div>'
 f'<div class="tiles">{TILES}</div></div>')

# left column
hero=card("The approval card","paused",
  '<div class="bigact">Send 240 cold emails to the Q3 list</div>'
  '<div class="meta">Drafted by your outbound agent. <b>Cannot be unsent.</b> 240 founders, US and UK.</div>'
  '<div class="btns"><span class="btn ba">Approve</span><span class="btn bn">Decline</span><span class="btn be">Edit</span></div>',
  cls="hero",tago=True)
stops=card("What stops at the gate","9 moves",
  girow(SENT,"Send a campaign","cannot unsend")+girow(CARD,"Charge a card","real money")
  +girow(PUB,"Publish a post","goes public")+girow(DEL,"Delete records","no recovery",True)
  +girow(CAL,"Schedule a meeting","blocks time")+girow(SIGN,"Sign an agreement","binding")
  +girow(PLUG,"Connect a tool","new access")+girow(MONEY,"Move money out","leaves account",True)
  +girow(CLOCK,"Run on a timer","fires later"),
  tago=True)
free=card("What runs free","no gate",
  frow("Research an account","reads only")+frow("Draft an email","nothing sent")
  +frow("Score a lead","internal")+frow("Build a target list","internal"))
why=card("Why a gate at all","the logic",
  bull("One bad <b>autonomous send</b> burns the domain")
  +bull("A wrong charge is a refund and a chargeback")
  +bull("A deleted record may never come back")
  +bull("Speed with no gate is just faster mistakes")
  +bull("The gate sits <b>before</b> the step, never after")
  +bull("You stay the operator, the AI stays the engine"),
  cls="fill")
COLL=f'<div class="col">{hero}{stops}{free}{why}</div>'

# right column
flow=card("The flow","locked order",
  '<div class="flow"><span class="node">Draft</span><span class="ar">&rarr;</span><span class="node on">Gate</span><span class="ar">&rarr;</span><span class="node">Ship</span></div>'
  '<div class="fcap">Drafting runs free. The gate sits <b>before the irreversible step</b>, every time, never after the fact.</div>')
edit=card("Edit before it ships","example",
  '<div class="was">Was: <b>send to all 240.</b> You change it to:</div>'
  '<div class="inp">Send to the top 80 by score<span class="cur"></span></div>')
cmp=card("Gate vs no gate","compare",
  '<div class="cmp">'
  '<div class="hl"></div><div class="hr n">No gate</div><div class="hr g">Human gate</div>'
  '<div class="k rowline">State</div><div class="v rowline">ships now</div><div class="v g rowline">pauses on risk</div>'
  '<div class="k rowline">Risk</div><div class="v rowline">unbounded</div><div class="v g rowline">contained</div>'
  '<div class="k rowline">Undo</div><div class="v rowline">none</div><div class="v g rowline">decline first</div>'
  '<div class="k rowline">Trail</div><div class="v rowline">none</div><div class="v g rowline">every decision</div>'
  '</div>')
log=card("The decision log","audit",
  frow("Approved &middot; Q3 campaign","you &middot; 2h")+frow("Edited &middot; invoice 4,200 to 3,800","you &middot; 1d")
  +frow("Declined &middot; delete 1,204 rows","you &middot; 3d"))
gloss=card("Glossary","plain words",
  glo("Human gate","the approval layer for AI agents")
  +glo("Irreversible","cannot be undone once it leaves")
  +glo("Approve","one yes, the turn resumes")
  +glo("Decline","it stops, nothing ships")
  +glo("Audit trail","every yes, no and edit, logged")
  +'<div class="gmono">the approval layer between autonomous AI agents and the outside world</div>',
  cls="fill")
COLR=f'<div class="col">{flow}{edit}{cmp}{log}{gloss}</div>'

BODY=f'<div class="body">{COLL}{COLR}</div>'
BOT=(f'<div class="bot"><div class="follow">Follow for one AI system for founders every day.</div>'
 f'<div class="bar"><div class="ph">Comment GATE for the exact human-gate setup<span class="cur"></span></div>'
 f'<div class="send"><svg viewBox="0 0 24 24">{SEND2}</svg></div></div>'
 f'<div class="foot"><div class="fl"><img class="ulogo" src="__LOGO__"><span class="br"><b>ULTRON</b> &middot; AI operator for founders &middot; Human gate</span></div>'
 f'<span class="url">51ultron<em>.</em>com</span></div></div>')

ART=f'<div class="atm"></div>{HEAD}{BODY}{BOT}'
def page(fonts,logo):
    return ("<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\">"+fonts+
            "<style>"+CSS+"</style></head><body><div id=\"artifact\">"+ART.replace("__LOGO__",logo)+"</div></body></html>")

open(OUT,"w").write(page(GOOGLE,logo_b64))
rp=f"{TE}/_hitl_li_render.html"; open(rp,"w").write(page(LOCAL,logo_b64))
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1080,"height":1450},device_scale_factor=2)
    pg.goto(f"file://{rp}"); pg.wait_for_timeout(700)
    meas=pg.evaluate("""()=>{const q=s=>document.querySelector(s).getBoundingClientRect();
      const body=q('.body'),cols=document.querySelectorAll('.col');
      const g=[...cols].map(c=>{const last=c.lastElementChild.getBoundingClientRect();return Math.round(body.bottom-last.bottom);});
      return {art:Math.round(q('#artifact').height),hd:Math.round(q('.hd').height),bodyH:Math.round(body.bottom-body.top),botH:Math.round(q('.bot').height),gaps:g};}""")
    print("ART",meas["art"],"HD",meas["hd"],"BODY",meas["bodyH"],"BOT",meas["botH"],"GAPS",meas["gaps"])
    pg.locator("#artifact").screenshot(path=PNG)
    b.close()
print("wrote",OUT)
