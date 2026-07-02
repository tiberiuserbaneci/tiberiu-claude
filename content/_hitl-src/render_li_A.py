#!/usr/bin/env python3
# LinkedIn v6 FORMAT A - LINE-FREE GROUP MAP (operator: connector lines were incoherent -> replaced
# with closed GROUP PANELS: header chip + rows inside one bordered container; hierarchy by nesting,
# not by wires). Dense rows, hairline separators, zero floating elements. Emits li-01 + li-04.
import os

CSS="""
@import 'https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700;9..40,800;9..40,900&family=DM+Mono:wght@400;500&display=swap';
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#d9d2c4;display:flex;justify-content:center;padding:24px 0;font-family:'DM Sans',sans-serif;-webkit-font-smoothing:antialiased;}
.frame{width:1080px;height:1450px;background:#F2EBDF;position:relative;overflow:hidden;color:#17150F;display:flex;flex-direction:column;padding:26px 40px 0;}
.frame::before{content:'';position:absolute;inset:0;pointer-events:none;background-image:radial-gradient(rgba(23,21,15,.045) 1.2px,transparent 1.3px);background-size:26px 26px;}
.frame>*{position:relative;}
.mast{flex-shrink:0;display:flex;justify-content:space-between;align-items:center;padding-bottom:10px;border-bottom:2px solid #17150F;font-family:'DM Mono',monospace;font-size:12px;font-weight:500;letter-spacing:.16em;text-transform:uppercase;color:#8d8371;}
.mast em{color:#A85B38;font-style:normal;}
.hook{margin-top:14px;font-weight:900;font-size:55px;letter-spacing:-2.2px;line-height:1.0;color:#17150F;}
.hook em{color:#A85B38;font-style:normal;}
.subl{margin-top:9px;font-size:18.5px;font-weight:600;color:#5d564a;}
.subl b{color:#17150F;}

.cols{flex:1;min-height:0;margin-top:14px;display:flex;gap:13px;}
.colL,.colR{flex:1;display:flex;flex-direction:column;gap:13px;min-width:0;}
.grp{border:2px solid #17150F;border-radius:16px;background:#FBF7EE;box-shadow:0 4px 0 rgba(23,21,15,.14);overflow:hidden;display:flex;flex-direction:column;}
.grp .gh{display:flex;align-items:center;justify-content:space-between;padding:10px 16px;border-bottom:2px solid #17150F;}
.grp .gh .n{font-weight:900;font-size:20px;letter-spacing:-.4px;}
.grp .gh .m{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:#8d8371;}
.grp.terra .gh{background:#D29A79;}
.grp.dark .gh{background:#211F1A;}.grp.dark .gh .n{color:#F7F1E6;}.grp.dark .gh .m{color:rgba(247,241,230,.6);}
.grp.grow{flex:1;}
.row{display:flex;gap:11px;padding:9px 16px;border-top:1px solid #e5dbc6;align-items:flex-start;}
.row:first-of-type{border-top:none;}
.row .nm{width:118px;flex-shrink:0;font-weight:900;font-size:16px;letter-spacing:-.2px;padding-top:1px;}
.row .nm small{display:block;font-family:'DM Mono',monospace;font-weight:500;font-size:10px;letter-spacing:.1em;color:#A85B38;margin-top:2px;text-transform:uppercase;}
.row .ds{flex:1;font-size:13.5px;line-height:1.32;color:#57503f;}
.row .ds b{color:#17150F;}
.row.hot{background:#F6E7DB;}
.grp.grow .rows{flex:1;display:flex;flex-direction:column;}
.grp.grow .rows .row{flex:1;align-items:center;}
.mono4{display:flex;flex-wrap:wrap;gap:8px;padding:11px 16px;}
.mchip{font-family:'DM Mono',monospace;font-size:14px;background:#F2EBDF;border:1.5px solid #17150F;border-radius:9px;padding:7px 13px;}
.mchip b{color:#A85B38;font-weight:500;}
.ctab{flex-shrink:0;margin:13px 0 0;background:#211F1A;border-radius:14px;display:flex;align-items:center;justify-content:space-between;padding:12px 20px;box-shadow:0 4px 0 rgba(23,21,15,.2);}
.ctab .l{font-size:18px;font-weight:700;color:#F7F1E6;}.ctab .l b{color:#E5A183;font-weight:900;}
.ctab .r{background:#F7F1E6;color:#17150F;border-radius:999px;padding:8px 18px;font-weight:900;font-size:15px;}
.ftr{flex-shrink:0;height:50px;margin:11px -40px 0;border-top:2px solid #17150F;background:#F2EBDF;display:flex;align-items:center;justify-content:space-between;padding:0 56px;}
.ftr .l{font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#8d8371;}
.ftr .r{display:flex;align-items:center;gap:10px;font-size:16.5px;font-weight:600;color:#3d3427;}
.ftr .r img{width:26px;height:26px;border-radius:50%;}
.ftr .r b{font-weight:900;color:#A85B38;}
"""

SPARK='<svg class="spark" viewBox="0 0 100 100"><g fill="#C87B57"><path d="M50 4 L56 38 L50 50 L44 38 Z"/><path d="M50 96 L56 62 L50 50 L44 62 Z"/><path d="M4 50 L38 44 L50 50 L38 56 Z"/><path d="M96 50 L62 44 L50 50 L62 56 Z"/><path d="M17 17 L44 40 L50 50 L38 46 Z"/><path d="M83 83 L56 60 L50 50 L62 54 Z"/><path d="M83 17 L60 44 L50 50 L54 38 Z"/><path d="M17 83 L40 56 L50 50 L46 62 Z"/></g></svg>'

def grp(cls,name,meta,rows_html,grow=False):
    return f'<div class="grp {cls}{" grow" if grow else ""}"><div class="gh"><span class="n">{name}</span><span class="m">{meta}</span></div><div class="rows">{rows_html}</div></div>'
def row(nm,tag,ds,hot=False):
    small=f'<small>{tag}</small>' if tag else ''
    return f'<div class="row{" hot" if hot else ""}"><span class="nm">{nm}{small}</span><span class="ds">{ds}</span></div>'

def emit(fn,title,sub,left,right,kw,asset,mastl="ULTRON <em>&middot;</em> THE OPERATING MAP",mastr="SAVE THIS"):
    html=f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>{CSS}</style></head><body>
<div class="frame" id="artifact">
<div class="mast"><span>{mastl}</span><span>{mastr}</span></div><div class="hook">{title}</div><div class="subl">{sub}</div>
<div class="cols"><div class="colL">{left}</div><div class="colR">{right}</div></div>
<div class="ctab"><span class="l">Comment <b>{kw}</b> and I will DM you {asset}</span><span class="r">{kw} &rarr;</span></div>
<div class="ftr"><span class="l">AI OPERATOR FOR FOUNDERS</span><span class="r"><img src="__LOGO__"><span><b>ULTRON</b> &middot; 51ultron.com</span></span></div>
</div></body></html>"""
    open(fn,"w").write(html); print("wrote",fn)

os.makedirs("content/howto2",exist_ok=True)

# ================= li-01: THE AGENT MAP (line-free groups) =================
L=(grp("terra","The seven agents","ONE CHAT BOX",
   row("CORTEX","research","Profiles people, companies and markets into <b>one ranked brief</b>: funding, size, stack, intent, 40 signals a page.")
  +row("SPECTER","outbound","Cold emails and <b>multi-step sequences</b>: one trigger per email, 62 words a step, personalised from the brief.")
  +row("STRIKER","deals","Qualification, discovery, <b>objection handling</b>, proposals, close plans. Reads your CRM before it answers.")
  +row("PULSE","content","Posts, launches and newsletters <b>in your voice</b>, from the stored sample. Hook first, no fluff.")
  +row("SENTINEL","code","Reads, writes, tests and <b>ships from Crescendo</b>: 822 components, 30+ kits. Opens the PR, waits for you.",True)
  +row("AMPLIFY","publishing","Formats and schedules every asset <b>per channel and timezone</b>. 10:00 local, ramped volume.")
  +row("COUNSEL","legal","NDAs, MSAs, term sheets. <b>Flags the risk lines</b> and drafts the redlines in minutes."),grow=True))
R=(grp("dark","The router picks the tier","YOU NEVER CHOOSE",
   row("Lite","haiku","Lookups, digests, classifications. The <b>cheap gear</b> for high-volume work.")
  +row("Smart","sonnet","The <b>default operator</b> for briefs, sequences and posts. Your daily driver.")
  +row("Deep","opus","Hard judgement only: objections, code, legal. <b>Paid where it pays.</b>")
  +row("The bill","cents","Pay per token through one subscription. A full day of agent work costs <b>cents, not seats</b>.",True))
+grp("dark","The human gate","NOTHING SENDS ALONE",
   row("Your tap","1 click","Every email, post, PR and contract <b>parks on HOLD</b>. You read, you tap, then it moves. Zero external accidents."))
+grp("terra","Wired into your stack","IT ACTS, NOT ANSWERS",
   row("CRM + mail","live","Reads deals and threads before answering. <b>Writes stages back</b> as replies land.")
  +row("Calendar","auto","Replies become <b>booked calls</b> on their own, timezone-correct.")
  +row("Crescendo","822 parts","The build library: kits, sections, dashboards. <b>Sites ship from chat.</b>",True))
+grp("","You just type","PLAIN ENGLISH",
   '<div class="mono4"><span class="mchip"><b>&gt;</b> source 200 founders</span><span class="mchip"><b>&gt;</b> audit my GTM</span><span class="mchip"><b>&gt;</b> build my landing page</span><span class="mchip"><b>&gt;</b> review this NDA</span></div>'))
emit("content/howto2/li-01.html",
 'You hired tools.<br>I hired <em>seven agents</em>.',
 "The full Ultron map on one image: agents, tiers, gate, wiring. Save it.",
 L,R,"ROUTER","the full agent map + the docs link")

# ================= li-04: THE BRAIN MAP (line-free groups) =================
L=(grp("terra","Who you sell to","LOADED IN EVERY RUN",
   row("Your ICP","filter","Founder / CEO, 2-50 employees, IT services and software, US + UK. <b>Every agent filters by it</b>: CORTEX sources inside it, STRIKER scores against it, SPECTER never writes outside it. Set it once and the whole pipeline stays on-profile.")
  +row("Named accounts","200","Your target list with <b>one-page briefs attached</b>: champion, signals, opener angle, next step. Briefs refresh the morning of every call, so nothing you read is stale by the time you dial.")
  +row("Deal stages","pipeline","Your stages, your close plan, your champions. STRIKER <b>never asks where a deal is</b>, and every reply lands in the right stage without you dragging a card."),grow=True)
+grp("","How you sound","EVERY DRAFT",
   row("Voice sample","pulse","How you actually write. PULSE drafts <b>in it</b>, not in AI-speak.")
  +row("Banned words","clean","The hedging and the fluff it <b>never uses</b>. Your no-list is enforced.")
  +row("Brand system","tokens","Colors, formats, rules. <b>Crescendo builds inherit them</b>, so even your site sounds like you.",True)))
R=(grp("dark","What you charge","QUOTED RIGHT",
   row("Pricing","3 tiers","Starter free, Max $19, Enterprise $297. <b>Quoted correctly every time</b>, no accidental discount.")
  +row("Objection bank","learned","What worked and what died, <b>per objection</b>. Every close feeds it back.")
  +row("Cost rules","cents","Cents per run. Deep tier <b>only where it pays</b>: objections, code, legal."))
+grp("terra","What it wires","EVIDENCE, NOT VIBES",
   row("CRM + inbox","live","Reads deals and threads <b>before answering</b>. Your pipeline is context, not a screenshot.")
  +row("Send logs","2,140","Every claim it makes carries <b>evidence from your own sends</b>, stamped with run IDs.")
  +row("Calendar","week","Knows your week <b>before it schedules</b> anything on it."),grow=True)
+grp("dark","Why it matters","THE COMPOUND",
   row("Elsewhere","15 min","Every other chat forgets this at close. You re-brief <b>15 minutes per session, forever</b>.")
  +row("Here","rules","Every correction becomes a rule. It sounds <b>more like you every month</b>.",True))
+grp("","Seed it once","THREE LINES",
   '<div class="mono4"><span class="mchip"><b>&gt;</b> /init my business</span><span class="mchip"><b>&gt;</b> remember: no discounts</span><span class="mchip"><b>&gt;</b> what do you know about me?</span></div>'))
emit("content/howto2/li-04.html",
 'You brief your AI every day.<br><em>I briefed mine once.</em>',
 "The brain map: what Ultron memorises about your business, and where it pays you back.",
 L,R,"BRAIN","the brain setup + the BCP link")
