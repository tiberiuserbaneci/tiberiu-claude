#!/usr/bin/env python3
# LinkedIn v4 FORMAT A - cream MIND MAP (reference: Ruben Hassid "Claude is eating up everything").
# Center mark in a circle, hub pills, color-coded card groups (terracotta / black / outline),
# thin connectors with small square joints. Emits li-01 (agents map) + li-04 (brain map).
import os

CSS="""
@import 'https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700;9..40,800;9..40,900&family=DM+Mono:wght@400;500&display=swap';
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#d9d2c4;display:flex;justify-content:center;padding:24px 0;font-family:'DM Sans',sans-serif;-webkit-font-smoothing:antialiased;}
.frame{width:1080px;height:1450px;background:#F2EBDF;position:relative;overflow:hidden;color:#17150F;}
.frame::before{content:'';position:absolute;inset:0;pointer-events:none;background-image:radial-gradient(rgba(23,21,15,.045) 1.2px,transparent 1.3px);background-size:26px 26px;}
.spark{position:absolute;top:-38px;left:-30px;width:150px;height:150px;opacity:.5;transform:rotate(-14deg);}
.title{position:absolute;top:30px;left:60px;right:40px;font-weight:900;font-size:52px;letter-spacing:-2px;line-height:1.02;}
.title em{color:#C84623;font-style:normal;}
.title u{text-decoration-thickness:6px;text-decoration-color:#17150F;text-underline-offset:8px;}
.sub{position:absolute;top:146px;left:62px;right:60px;font-size:18.5px;font-weight:600;color:#5d564a;}
svg.wires{position:absolute;inset:0;pointer-events:none;}
.card{position:absolute;border-radius:12px;padding:12px 15px;box-shadow:0 3px 0 rgba(23,21,15,.14);}
.card .t{font-weight:900;font-size:19.5px;letter-spacing:-.3px;}
.card .d{margin-top:4px;font-size:13.5px;line-height:1.28;font-weight:500;}
.card.terra{background:#D29A79;border:2px solid #17150F;}
.card.terra .t{color:#17150F;}.card.terra .d{color:#3d2416;}
.card.black{background:#211F1A;border:2px solid #17150F;}
.card.black .t{color:#F7F1E6;}.card.black .d{color:rgba(247,241,230,.78);}
.card.line{background:#FBF7EE;border:2px solid #17150F;}
.card.line .t{color:#17150F;}.card.line .d{color:#57503f;}
.card.mono .t{font-family:'DM Mono',monospace;font-weight:500;font-size:16.5px;}
.hub{position:absolute;background:#FBF7EE;border:2.5px solid #17150F;border-radius:10px;padding:9px 14px;font-weight:900;font-size:19px;letter-spacing:-.3px;box-shadow:0 3px 0 rgba(23,21,15,.2);white-space:nowrap;}
.hub.dark{background:#211F1A;color:#F7F1E6;}
.hub.terra{background:#D29A79;}
.center{position:absolute;width:220px;height:220px;border-radius:50%;background:#FBF7EE;border:3px solid #C84623;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 0 rgba(200,70,35,.18);}
.center img{width:150px;height:150px;border-radius:50%;object-fit:cover;}
.ctab{position:absolute;left:40px;right:40px;bottom:74px;background:#211F1A;border-radius:14px;display:flex;align-items:center;justify-content:space-between;padding:12px 20px;box-shadow:0 4px 0 rgba(23,21,15,.2);}
.ctab .l{font-size:18px;font-weight:700;color:#F7F1E6;}.ctab .l b{color:#E5A183;font-weight:900;}
.ctab .r{background:#F7F1E6;color:#17150F;border-radius:999px;padding:8px 18px;font-weight:900;font-size:15px;}
.ftr{position:absolute;left:0;right:0;bottom:0;height:52px;border-top:2px solid #17150F;background:#F2EBDF;display:flex;align-items:center;justify-content:space-between;padding:0 60px;}
.ftr .l{font-size:16.5px;font-weight:600;color:#3d3427;}.ftr .l b{font-weight:900;color:#17150F;}
.ftr .r{display:flex;align-items:center;gap:10px;font-size:16.5px;font-weight:600;color:#3d3427;}
.ftr .r img{width:26px;height:26px;border-radius:50%;}
.ftr .r b{font-weight:900;color:#C84623;}
"""

SPARK='<svg class="spark" viewBox="0 0 100 100"><g fill="#C84623"><path d="M50 4 L56 38 L50 50 L44 38 Z"/><path d="M50 96 L56 62 L50 50 L44 62 Z"/><path d="M4 50 L38 44 L50 50 L38 56 Z"/><path d="M96 50 L62 44 L50 50 L62 56 Z"/><path d="M17 17 L44 40 L50 50 L38 46 Z"/><path d="M83 83 L56 60 L50 50 L62 54 Z"/><path d="M83 17 L60 44 L50 50 L54 38 Z"/><path d="M17 83 L40 56 L50 50 L46 62 Z"/></g></svg>'

def card(x,y,w,cls,t,d):
    dd=f'<div class="d">{d}</div>' if d else ''
    tt='<div class="t">'+t+'</div>'
    return f'<div class="card {cls}" style="left:{x}px;top:{y}px;width:{w}px">{tt}{dd}</div>'
def hub(x,y,cls,t): return f'<div class="hub {cls}" style="left:{x}px;top:{y}px">{t}</div>'
def wires(paths):
    seg="".join(f'<path d="{p}" fill="none" stroke="#8f8672" stroke-width="2"/>' for p in paths)
    joints="".join(f'<rect x="{x-4}" y="{y-4}" width="8" height="8" fill="#C84623"/>' for x,y in JOINTS)
    return f'<svg class="wires" viewBox="0 0 1080 1450">{seg}{joints}</svg>'

def emit(fn,title,sub,body,asset="the full map",pin="app.51ultron.com/docs"):
    html=f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>{CSS}</style></head><body>
<div class="frame" id="artifact">{SPARK}
<div class="title">{title}</div><div class="sub">{sub}</div>
{body}
<div class="ctab"><span class="l">Comment <b>__KW__</b> and I will DM you __ASSET__</span><span class="r">__KW__ &rarr;</span></div>
<div class="ftr"><span class="l">__PIN__</span><span class="r"><img src="__LOGO__"><span><b>ULTRON</b> &middot; 51ultron.com</span></span></div>
</div></body></html>"""
    html=html.replace("__ASSET__",asset).replace("__PIN__",pin)
    open(fn,"w").write(html); print("wrote",fn)

os.makedirs("content/howto2",exist_ok=True)

# ================= li-01: ULTRON AGENT MAP =================
JOINTS=[]
def J(x,y): JOINTS.append((x,y)); return ""
# left: 7 agents (terracotta). right: tiers(black), gate(black), integrations(terra). bottom: you type (mono outline)
agents=[("CORTEX","Research. Profiles people, companies and markets into one ranked brief."),
("SPECTER","Outbound. Cold emails, follow-ups and multi-step sequences."),
("STRIKER","Deals. Qualification, objections, proposals, close plans."),
("PULSE","Content. Posts, launches and newsletters in your voice."),
("SENTINEL","Code. Reads, writes, tests and ships. Opens the PR."),
("AMPLIFY","Publishing. Formats and schedules per channel and timezone."),
("COUNSEL","Legal. NDAs, MSAs, term sheets. Flags the risk.")]
B=[]
y=176
for t,d in agents:
    B.append(card(36,y,300,"terra",t,d)); y+=118
tiers=[("Lite &middot; Haiku","Quick lookups and digests. The cheap gear."),
("Smart &middot; Sonnet","The daily driver. Default for most jobs."),
("Deep &middot; Opus","Hard judgement: objections, code, legal.")]
y=176
for t,d in tiers:
    B.append(card(744,y,300,"black",t,d)); y+=124
B.append(card(744,568,300,"black","Human gate","Nothing sends until you tap approve. Every agent, every time."))
integ=[("CRM + Mail","It reads and writes your pipeline and inbox."),
("Calendar","Replies become booked calls on their own."),
("Your repo","SENTINEL ships from a real branch, with tests.")]
y=712
for t,d in integ:
    B.append(card(744,y,300,"terra",t,d)); y+=112
B.append(card(36,1058,300,"line","The brain","Your ICP, voice, pricing and deal stages. Briefed once, recalled in every run."))
B.append(card(36,1168,300,"line","The router","Reads the job, hires the agent, picks the tier. You never choose a model."))
# bottom mono strip: what you type
B.append(card(370,1108,224,"line mono","&gt; source 200 founders",""))
B.append(card(610,1108,190,"line mono","&gt; audit my GTM",""))
B.append(card(370,1182,224,"line mono","&gt; fix the pricing page",""))
B.append(card(610,1182,190,"line mono","&gt; review this NDA",""))
# hubs
B.append(hub(368,332,"terra","The Agents"))
B.append(hub(556,242,"dark","Model Tiers"))
B.append(hub(584,486,"dark","Human Gate"))
B.append(hub(566,862,"terra","Integrations"))
B.append(hub(392,1052,"","You just type"))
B.append('<div class="center" style="left:430px;top:560px"><img src="__LOGO__"></div>')
paths=[]
# agents col -> hub -> center
for i in range(7):
    yy=176+118*i+50; paths.append(f"M336 {yy} H400"); J(336,yy)
paths.append("M400 226 V1004"); paths.append("M400 700 H430"); J(400,378); J(400,700)
# tiers -> hub -> center
for i in range(3):
    yy=176+124*i+55; paths.append(f"M744 {yy} H700"); J(744,yy)
paths.append("M700 231 V266 H726"); J(700,266)
# gate
paths.append(f"M744 622 H712 V512 H744"); J(712,512)
# integrations -> hub
for i in range(3):
    yy=712+112*i+48; paths.append(f"M744 {yy} H716"); J(744,yy)
paths.append("M716 760 V886 H714"); J(716,886)

# center to hubs (short spokes)
paths+=["M540 560 V280","M540 780 V1046","M430 670 H408","M650 670 H690 V530"]
body1="".join(B)+wires(paths)
emit_args1=True
emit("content/howto2/li-01.html",
 'You hired tools. I hired <em>seven agents</em>.',
 "The full Ultron map: seven agents, three model tiers, one human gate. Save it.",
 body1,asset="the full agent map + the docs link",pin="PINPOINT: app.51ultron.com/docs")

# ================= li-04: THE BRAIN MAP =================
JOINTS=[]
B=[]
who=[("Your ICP","Founder / CEO, 2-50 employees, IT services, US + UK."),
("Named accounts","The 200 on your list, with briefs attached."),
("Deal stages","Your pipeline, your close plan, your champions.")]
y=176
for t,d in who: B.append(card(36,y,300,"terra",t,d)); y+=118
voice=[("Voice sample","How you actually write. PULSE drafts in it."),
("Banned words","The hedging and the fluff it never uses."),
("Brand system","Colors, formats, the rules of every asset.")]
y=560
for t,d in voice: B.append(card(36,y,300,"line",t,d)); y+=112
B.append(card(36,952,300,"black","What dies elsewhere","Every other chat forgets this at close. You re-brief 15 minutes per session, forever."))
B.append(card(36,1100,300,"black","Here it compounds","Every correction becomes a rule. It sounds more like you every month."))
money=[("Pricing","Starter free, Max $19, Enterprise $297. Quoted right, every time."),
("Objection bank","What worked, what died, per objection."),
("Cost rules","Cents per run. Deep tier only where it pays.")]
y=176
for t,d in money: B.append(card(744,y,300,"black",t,d)); y+=124
wired=[("CRM + inbox","Reads deals and threads before answering."),
("Send logs","2,140 sends of evidence behind every claim."),
("Calendar","Knows your week before it schedules.")]
y=628
for t,d in wired: B.append(card(744,y,300,"terra",t,d)); y+=112
B.append(card(744,1010,300,"line mono","&gt; /init my business",""))
B.append(card(744,1078,300,"line mono","&gt; remember: no discounts",""))
B.append(card(744,1146,300,"line mono","&gt; what do you know about me?",""))
B.append(hub(352,330,"terra","Who you sell to"))
B.append(hub(352,500,"","How you sound"))
B.append(hub(548,244,"dark","What you charge"))
B.append(hub(596,846,"terra","What it wires"))
B.append(hub(364,1012,"dark","Why it matters"))
B.append(hub(608,952,"","Seed it once"))
B.append('<div class="center" style="left:430px;top:560px"><img src="__LOGO__"></div>')
paths=[]
for i in range(3):
    yy=176+118*i+50; paths.append(f"M336 {yy} H402"); J(336,yy)
paths.append("M402 226 V330")
for i in range(3):
    yy=560+112*i+48; paths.append(f"M336 {yy} H402"); J(336,yy)
paths.append("M402 608 V546 H420"); J(402,546)
for i in range(3):
    yy=176+124*i+55; paths.append(f"M744 {yy} H700"); J(744,yy)
paths.append("M700 231 V268 H718"); J(700,268)
for i in range(3):
    yy=628+112*i+48; paths.append(f"M744 {yy} H700"); J(744,yy)
paths.append("M700 676 V870 H726"); J(700,870)
for i in range(3):
    yy=1010+74*i+26; paths.append(f"M744 {yy} H710"); J(744,yy)
paths.append("M710 1036 V984 H730"); J(710,984)
for i in range(2):
    yy=952+156*i+52; paths.append(f"M336 {yy} H392"); J(336,yy)
paths.append("M392 1004 V1036 H408"); J(392,1036)
paths+=["M540 560 V282","M540 780 V1006","M430 670 H406","M650 670 H700"]
body4="".join(B)+wires(paths)
emit("content/howto2/li-04.html",
 'You brief your AI every day. <em>I briefed mine once.</em>',
 "The brain map: what Ultron memorises about your business, and where it pays you back.",
 body4,asset="the brain setup + the BCP link",pin="PINPOINT: app.51ultron.com/bcp")
