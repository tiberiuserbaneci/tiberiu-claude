#!/usr/bin/env python3
# LinkedIn v4 FORMAT C - cream "CLEARLY EXPLAINED" (reference: Charlie Hills "Loop Engineering").
# Top: 4 era mini-cards. Main: 6 numbered color-coded cards (2 cols) w/ icon flows, mono chip, WHY
# line + central vertical loop spine with stops and the Ultron mark. Emits li-05, li-08, li-09.
import os

CSS="""
@import 'https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700;9..40,800;9..40,900&family=DM+Mono:wght@400;500&display=swap';
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#d9d2c4;display:flex;justify-content:center;padding:24px 0;font-family:'DM Sans',sans-serif;-webkit-font-smoothing:antialiased;color:#17150F;}
.frame{width:1080px;height:1450px;background:#F5F0E6;position:relative;overflow:hidden;display:flex;flex-direction:column;padding:30px 34px 0;}
.frame::before{content:'';position:absolute;inset:0;pointer-events:none;background-image:linear-gradient(rgba(23,21,15,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(23,21,15,.05) 1px,transparent 1px);background-size:38px 38px;}
.frame>*{position:relative;}
.hdr{flex-shrink:0;display:flex;align-items:center;gap:14px;}
.hdr svg{width:52px;height:52px;flex-shrink:0;}
.hdr .t{font-weight:900;font-size:45px;letter-spacing:-1.7px;}
.hdr .t em{font-style:normal;color:#C84623;}
.sub{flex-shrink:0;margin:6px 0 0 66px;font-size:17.5px;font-weight:600;color:#5d564a;}
.sub b{color:#C84623;}
.eras{flex-shrink:0;display:flex;gap:10px;margin-top:12px;}
.era{flex:1;background:#FDFAF3;border:1.5px solid #d8cdb8;border-radius:12px;padding:9px 12px;}
.era .k{font-family:'DM Mono',monospace;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:#8d8371;}
.era .n{font-weight:900;font-size:18px;margin-top:2px;}
.era .d{font-size:12px;color:#6b6357;margin-top:2px;line-height:1.25;}
.grid{flex:1;min-height:0;margin-top:12px;display:flex;gap:88px;position:relative;}
.gcol{flex:1;display:flex;flex-direction:column;gap:11px;min-width:0;}
.spine{position:absolute;left:50%;top:8px;bottom:8px;transform:translateX(-50%);width:64px;}
.spine .rail{position:absolute;left:50%;top:0;bottom:0;width:38px;transform:translateX(-50%);border:3px solid #C84623;border-radius:22px;background:transparent;}
.spine .lbl{position:absolute;top:-4px;left:50%;transform:translateX(-50%);background:#F5F0E6;padding:0 6px;font-family:'DM Mono',monospace;font-size:10px;letter-spacing:.13em;color:#8d8371;white-space:nowrap;}
.sstop{position:absolute;left:50%;transform:translateX(-50%);background:#FDFAF3;border:2px solid #17150F;border-radius:999px;padding:4px 10px;font-family:'DM Mono',monospace;font-size:11px;white-space:nowrap;display:flex;align-items:center;gap:6px;}
.sstop i{width:8px;height:8px;border-radius:50%;flex-shrink:0;}
.sorb{position:absolute;left:50%;top:47%;transform:translate(-50%,-50%);width:96px;height:96px;border-radius:50%;background:#FDFAF3;border:3px solid #C84623;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 0 rgba(200,70,35,.16);}
.sorb img{width:64px;height:64px;border-radius:50%;}
.kard{flex:1;background:#FDFAF3;border:2px solid var(--bc);border-radius:14px;padding:11px 14px;display:flex;flex-direction:column;box-shadow:0 3px 0 rgba(23,21,15,.1);}
.kard .top{display:flex;align-items:center;gap:9px;}
.kard .num{width:26px;height:26px;border-radius:8px;background:var(--bc);color:#fff;font-weight:900;font-size:15px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.kard .sec{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--bc);font-weight:500;}
.kard .tag{margin-left:auto;font-family:'DM Mono',monospace;font-size:10.5px;color:#8d8371;background:#F0E9DA;border-radius:6px;padding:2px 8px;white-space:nowrap;}
.kard .tt{margin-top:5px;font-weight:900;font-size:21px;letter-spacing:-.4px;}
.kard .bd{margin-top:3px;font-size:13px;color:#57503f;line-height:1.3;}
.kard .bd b{color:#17150F;}
.flow{margin-top:8px;display:flex;align-items:center;gap:6px;}
.fstep{flex:1;display:flex;flex-direction:column;align-items:center;gap:3px;min-width:0;}
.fico{width:40px;height:40px;border-radius:10px;background:#F0E9DA;border:1.5px solid #d8cdb8;display:flex;align-items:center;justify-content:center;}
.fico svg{width:20px;height:20px;stroke:#17150F;stroke-width:2;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.fico.hot{background:var(--bc);border-color:var(--bc);}
.fico.hot svg{stroke:#fff;}
.fstep .fl{font-size:10.5px;font-weight:700;color:#57503f;white-space:nowrap;}
.farr{flex-shrink:0;display:flex;flex-direction:column;align-items:center;margin-top:-12px;}
.farr .al{font-family:'DM Mono',monospace;font-size:8.5px;letter-spacing:.08em;color:#8d8371;text-transform:uppercase;}
.farr svg{width:22px;height:10px;stroke:#8d8371;stroke-width:2;fill:none;stroke-linecap:round;}
.chip{margin-top:8px;background:#F0E9DA;border:1.5px solid #d8cdb8;border-radius:8px;padding:6px 10px;font-family:'DM Mono',monospace;font-size:12.5px;color:#17150F;}
.chip b{color:#C84623;font-weight:500;}
.why{margin-top:7px;display:flex;gap:8px;font-size:12px;color:#57503f;line-height:1.3;}
.why b{font-family:'DM Mono',monospace;font-size:10px;letter-spacing:.14em;color:var(--bc);flex-shrink:0;margin-top:1px;}
.ftr{flex-shrink:0;height:52px;margin:12px -34px 0;background:#17150F;display:flex;align-items:center;justify-content:center;gap:12px;color:#F5F0E6;}
.ftr img{width:26px;height:26px;border-radius:50%;}
.ftr .a{font-weight:900;font-size:15.5px;}.ftr .b{font-size:14.5px;color:rgba(245,240,230,.6);}
.ftr .kw{font-family:'DM Mono',monospace;font-size:13px;color:#E8A17F;}
"""

SPARK='<svg viewBox="0 0 100 100"><g fill="#C84623"><path d="M50 4 L56 38 L50 50 L44 38 Z"/><path d="M50 96 L56 62 L50 50 L44 62 Z"/><path d="M4 50 L38 44 L50 50 L38 56 Z"/><path d="M96 50 L62 44 L50 50 L62 56 Z"/><path d="M17 17 L44 40 L50 50 L38 46 Z"/><path d="M83 83 L56 60 L50 50 L62 54 Z"/><path d="M83 17 L60 44 L50 50 L54 38 Z"/><path d="M17 83 L40 56 L50 50 L46 62 Z"/></g></svg>'
IC={
"chat":'<svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/></svg>',
"doc":'<svg viewBox="0 0 24 24"><path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4M9 12h7M9 16h5"/></svg>',
"bolt":'<svg viewBox="0 0 24 24"><path d="M13 2 5 13h6l-1 9 8-11h-6z"/></svg>',
"check":'<svg viewBox="0 0 24 24"><path d="M4 12l5 5L20 7"/></svg>',
"mag":'<svg viewBox="0 0 24 24"><circle cx="10" cy="10" r="6"/><path d="M15 15l6 6"/></svg>',
"person":'<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/></svg>',
"coin":'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><path d="M12 7v10M9.5 9.5c0-1 1-1.7 2.5-1.7s2.5.7 2.5 1.7-1 1.6-2.5 1.9-2.5 1-2.5 2 1 1.8 2.5 1.8 2.5-.8 2.5-1.8"/></svg>',
"clock":'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><path d="M12 7v5l4 3"/></svg>',
"link":'<svg viewBox="0 0 24 24"><path d="M9 15l6-6M8 12l-2.5 2.5a4 4 0 105.6 5.6L13.6 17.6M16 12l2.5-2.5a4 4 0 10-5.6-5.6L10.4 6.4"/></svg>',
"gear":'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.4"/><path d="M12 2.8v3M12 18.2v3M2.8 12h3M18.2 12h3M5.4 5.4l2.1 2.1M16.5 16.5l2.1 2.1M18.6 5.4l-2.1 2.1M7.5 16.5l-2.1 2.1"/></svg>',
"send":'<svg viewBox="0 0 24 24"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"/></svg>',
"cal":'<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
"shield":'<svg viewBox="0 0 24 24"><path d="M12 2l8 3v6c0 5-3.5 8.7-8 11-4.5-2.3-8-6-8-11V5z"/><path d="M8.5 12l2.5 2.5 4.5-4.5"/></svg>',
"chart":'<svg viewBox="0 0 24 24"><path d="M4 20V9M10 20V4M16 20v-8M22 20H2"/></svg>',
"loop":'<svg viewBox="0 0 24 24"><path d="M4 12a8 8 0 0114-5M20 12a8 8 0 01-14 5"/><path d="M18 3v4h-4M6 21v-4h4"/></svg>',
}
ARR='<svg viewBox="0 0 24 10"><path d="M0 5h20M17 1.5 21 5l-4 3.5"/></svg>'

def flow(steps):
    out=[]
    for i,(ic,lb,al,hot) in enumerate(steps):
        if i: out.append(f'<span class="farr"><span class="al">{al}</span>{ARR}</span>')
        out.append(f'<span class="fstep"><span class="fico{" hot" if hot else ""}">{IC[ic]}</span><span class="fl">{lb}</span></span>')
    return '<div class="flow">'+"".join(out)+'</div>'

def kard(color,num,sec,tag,tt,bd,fl,chip,why):
    return (f'<div class="kard" style="--bc:{color}"><div class="top"><span class="num">{num}</span><span class="sec">{sec}</span><span class="tag">{tag}</span></div>'
            f'<div class="tt">{tt}</div><div class="bd">{bd}</div>{fl}'
            f'<div class="chip">{chip}</div><div class="why"><b>WHY</b><span>{why}</span></div></div>')

def emit(fn,title,sub,eras,cardsL,cardsR,spine_lbl,stops,kw):
    er="".join(f'<div class="era"><div class="k">{k}</div><div class="n">{n}</div><div class="d">{d}</div></div>' for k,n,d in eras)
    st="".join(f'<span class="sstop" style="top:{p}%"><i style="background:{c}"></i>{t}</span>' for p,c,t in stops)
    html=f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>{CSS}</style></head><body>
<div class="frame" id="artifact">
<div class="hdr">{SPARK}<span class="t">{title}</span></div>
<div class="sub">{sub}</div>
<div class="eras">{er}</div>
<div class="grid"><div class="gcol">{cardsL}</div>
<div class="spine"><span class="rail"></span><span class="lbl">{spine_lbl}</span>{st}<span class="sorb"><img src="__LOGO__"></span></div>
<div class="gcol">{cardsR}</div></div>
<div class="ftr"><img src="__LOGO__"><span class="a">ULTRON</span><span class="b">&middot; AI operator for founders &middot; 51ultron.com &middot;</span><span class="kw">comment {kw}</span></div>
</div></body></html>"""
    open(fn,"w").write(html); print("wrote",fn)

os.makedirs("content/howto2",exist_ok=True)
TER="#C84623"; KRA="#B98A5F"; GRN="#4d8b6a"; BLK="#211F1A"

# ---------------- li-05 AUDIT ----------------
eras=[("HOW IT WAS","Gut feel","You ship and hope. No score, no fixes."),
("2023","Dashboards","Numbers you stare at. No verdicts."),
("2024","Consultants","Three weeks, five figures, one deck."),
("NOW","One sentence","&gt; audit my GTM. Scored teardown out.")]
cL=(kard(TER,1,"THE CHECK","score 44","Outbound","Openers are generic. Winners carry <b>one trigger</b> and 62 words.",
 flow([("mag","Scan sends","READS",0),("chart","Score 44","GRADES",1),("bolt","Fix cadence","SHIPS",0)]),
 "<b>/audit</b> outbound &middot; scored vs 2,140 sends","Copy quality was never the problem. The trigger was.")
+kard(KRA,3,"THE CHECK","score 58","ICP match","<b>31% of the pipeline</b> sits outside the 2-50 band you set.",
 flow([("mag","Scan CRM","214 DEALS",0),("person","Flag misfits","31%",1),("check","Requalify","CLEAN",0)]),
 "<b>/audit</b> icp &middot; scored vs your CRM","Misfit deals eat the weeks your ICP deserves.")
+kard(GRN,5,"THE CHECK","score 83","Deliverability","Domains warm, <b>99.2% inboxing</b>. Keep the ramp exactly as is.",
 flow([("send","4 domains","WARM",0),("chart","99.2%","INBOX",1),("check","Keep","AS IS",0)]),
 "<b>/audit</b> domains &middot; verdict: KEEP","The one green light. Everything else routes through it."))
cR=(kard(BLK,2,"THE CHECK","score 39","Follow-up","<b>68% of threads die</b> after touch one. The cadence never fires.",
 flow([("doc","Threads","90 DAYS",0),("clock","Die at T+1","68%",1),("loop","Cadence on","AUTO",0)]),
 "<b>/audit</b> followup &middot; worst score of the 8","Meetings live in touch 2. Nobody sends touch 2.")
+kard(TER,4,"THE CHECK","score 51","Pipeline hygiene","<b>14 deals stale</b> past 30 days. Kill them or revive them.",
 flow([("mag","Scan stages","LIVE",0),("clock","14 stale","30D+",1),("bolt","Kill / revive","TODAY",0)]),
 "<b>/audit</b> pipeline &middot; decay curve attached","Stale deals die at day 34. Yours are at 31.")
+kard(KRA,6,"THE VERDICT","61 / 100","The score","3 keep, 5 fix, each with the exact move. Re-run <b>every Monday</b>.",
 flow([("chart","61/100","TODAY",1),("bolt","5 fixes","THIS WK",0),("loop","Re-run","MONDAY",0)]),
 "<b>&gt; audit my GTM</b> &middot; three words, whole teardown","A score you re-run beats a deck you shelve."))
emit("content/howto2/li-05.html",'GTM Audits, <em>Clearly Explained</em>.',
 'Stop guessing what is broken. One sentence scores your whole funnel. <b>Six of the 8 checks below.</b>',
 eras,cL,cR,"THE AUDIT LOOP",
 [(6,TER,"Scan"),(30,KRA,"Score"),(62,"#4d8b6a","Fix"),(88,TER,"Re-run")],"AUDIT")

# ---------------- li-08 PROOF ----------------
eras=[("HOW IT WAS","Screenshots","30 crops pasted into chat. Zero sources."),
("THEN","Slide decks","Pretty, stale in a week, unverifiable."),
("THEN","Notion dumps","A wall of text nobody re-opens."),
("NOW","One live link","Every claim clicks to its source run.")]
cL=(kard(TER,1,"THE CLAIM","conf 98%","Reply timing","US + UK founders reply <b>3.1x more</b> at 10:00 local time.",
 flow([("doc","2,140 sends","LOGS",0),("chart","3.1x lift","MEASURED",1),("link","Run ID","STAMPED",0)]),
 "send logs &middot; n=2,140 &middot; <b>run #4411</b>","Timing beat copy in every cohort we ran.")
+kard(KRA,3,"THE CLAIM","conf 96%","One-trigger openers","Beat template openers <b>4.4x</b> on booked calls.",
 flow([("send","201 A/B","10 DAYS",0),("chart","4.4x","WINNER",1),("link","Source","1 CLICK",0)]),
 "A/B set &middot; 201 sends &middot; <b>run #4390</b>","The trigger does the work the adjectives cannot.")
+kard(GRN,5,"THE SHARE","zero decks","The link","<b>work.51ultron.com/brief/q3</b>. One URL replaces the deck, the dump and the debate.",
 flow([("doc","Brief","8 CLAIMS",0),("link","Live link","SHARED",1),("person","Co-founder","CONVINCED",0)]),
 "<b>&gt; share the brief</b> &middot; expires never","He challenged claim 4. The link settled it in one click."))
cR=(kard(BLK,2,"THE CLAIM","conf 99%","ICP drift","<b>31% of pipeline</b> was outside the ICP. CRM scan, not opinion.",
 flow([("mag","CRM scan","214 DEALS",0),("person","Misfits","31%",1),("link","Evidence","ROW LEVEL",0)]),
 "CRM scan &middot; 214 deals &middot; <b>run #4402</b>","Opinions argue. Row-level evidence closes the thread.")
+kard(TER,4,"THE CLAIM","conf 94%","Follow-up wins","Touch 2 books <b>58% of all meetings</b>. Most threads never get it.",
 flow([("doc","90d threads","READ",0),("chart","58% at T2","FOUND",1),("link","Thread IDs","LISTED",0)]),
 "thread analysis &middot; 90 days &middot; <b>run #4407</b>","The meeting was one send away the whole time.")
+kard(KRA,6,"THE HABIT","every claim","Stamp it","Every number in every brief carries <b>source + run ID + confidence</b>.",
 flow([("doc","Claim","WRITTEN",0),("gear","Auto-stamp","RUN ID",1),("check","Trusted","DEFAULT",0)]),
 "<b>/brief</b> &middot; stamping is automatic","Proof by default beats proof on demand."))
emit("content/howto2/li-08.html",'Research Proof, <em>Clearly Explained</em>.',
 'Three weeks of research, defended in one link. <b>No screenshots, no decks.</b>',
 eras,cL,cR,"THE EVIDENCE LOOP",
 [(6,TER,"Claim"),(30,KRA,"Source"),(62,"#4d8b6a","Stamp"),(88,TER,"Share")],"PROOF")

# ---------------- li-09 RESUME ----------------
eras=[("HOW IT WAS","New chat daily","Yesterday died at midnight."),
("THEN","Scroll-up dig","Ten minutes of archaeology per session."),
("THEN","Paste summary","You write memos to your own AI."),
("NOW","Two words","&gt; resume northwind. Everything is back.")]
cL=(kard(TER,1,"CARRIES OVER","deal state","The stage","Northwind at <b>proposal</b>, champion Sarah, close plan loaded.",
 flow([("doc","Monday 16:12","CLOSED",0),("clock","2 days","AWAY",0),("bolt","Wed 09:01","BACK",1)]),
 "<b>&gt; resume northwind</b> &middot; two words","You continue the deal, not the document hunt.")
+kard(KRA,3,"CARRIES OVER","v3 not v1","The draft","The proposal draft comes back at <b>version 3</b>, mid-edit, cursor warm.",
 flow([("doc","Draft v3","SAVED",0),("loop","Recalled","AS-IS",1),("send","Sent 09:11","DONE",0)]),
 "no re-paste &middot; no v1 regression","Redoing v1 twice is how founders lose Wednesdays.")
+kard(GRN,5,"CARRIES OVER","the thread","The objection","The open <b>too-expensive</b> thread resumes exactly where it stopped.",
 flow([("chat","Objection","OPEN",0),("bolt","STRIKER","FINISHES",1),("check","Rebuttal","OUT",0)]),
 "mid-negotiation &middot; nothing lost","Deals die in the gaps between sessions. This one had no gap.")
)
cR=(kard(BLK,2,"CARRIES OVER","zero re-brief","The context","ICP, pricing, voice: <b>0 minutes</b> re-explaining who you are.",
 flow([("person","Your brain","STORED",0),("loop","Auto-load","EVERY RUN",1),("check","0 re-brief","ALWAYS",0)]),
 "the brain loads before the session does","15 minutes per session, refunded every day.")
+kard(TER,4,"CARRIES OVER","numbers","The pricing","The quote already on the table stays quoted. <b>No accidental discount.</b>",
 flow([("coin","$ quoted","LOCKED",0),("doc","In draft","V3",0),("shield","Consistent","SAFE",1)]),
 "quoted once &middot; consistent forever","Re-quoting from memory is how margins leak.")
+kard(KRA,6,"THE RESULT","10 minutes","Reopen to sent","Two words in, proposal out the door by <b>09:11</b>.",
 flow([("bolt","Resume","09:01",1),("doc","Finish v3","09:03",0),("send","Proposal","09:11",0)]),
 "<b>&gt; resume</b> &middot; the whole ceremony","The fastest morning is the one that starts mid-stride."))
emit("content/howto2/li-09.html",'Sessions That Resume, <em>Clearly Explained</em>.',
 'Closed the laptop mid-negotiation Monday. Typed two words Wednesday. <b>Nothing was lost.</b>',
 eras,cL,cR,"THE SESSION LOOP",
 [(6,TER,"Work"),(30,KRA,"Close"),(62,"#4d8b6a","Resume"),(88,TER,"Continue")],"RESUME")
