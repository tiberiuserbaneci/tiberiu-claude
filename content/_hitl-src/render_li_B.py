#!/usr/bin/env python3
# LinkedIn v4 FORMAT B - dark BLUEPRINT cheat-sheet (reference: Charlie Hills "Run Claude Code for Free").
# Grid texture, numbered center spine, section cards w/ mono corner tags, terminal boxes w/ send arrow,
# badge lists, checklists, bottom cheat-sheet strip. Emits li-02, li-03, li-06, li-07, li-10.
import os

CSS="""
@import 'https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700;9..40,800;9..40,900&family=DM+Mono:wght@400;500&display=swap';
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#0a0a09;display:flex;justify-content:center;padding:24px 0;font-family:'DM Sans',sans-serif;-webkit-font-smoothing:antialiased;color:#F6F1E7;}
.frame{width:1080px;height:1450px;background:#171716;position:relative;overflow:hidden;display:flex;flex-direction:column;padding:30px 36px 0;}
.frame::before{content:'';position:absolute;inset:0;pointer-events:none;z-index:0;
background-image:linear-gradient(rgba(250,250,247,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(250,250,247,.05) 1px,transparent 1px);
background-size:36px 36px;}
.frame::after{content:'';position:absolute;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse 70% 34% at 50% -6%,rgba(200,70,35,.22),transparent 62%);}
.frame>*{position:relative;z-index:2;}
.hdr{flex-shrink:0;display:flex;align-items:center;gap:18px;justify-content:center;}
.hdr img{width:54px;height:54px;border-radius:12px;}
.hdr .t{font-weight:900;font-size:47px;letter-spacing:-1.8px;}
.hdr .t em{font-style:normal;color:#E8845F;text-shadow:0 0 34px rgba(232,132,95,.55);}
.sub{flex-shrink:0;text-align:center;margin-top:8px;font-size:17.5px;font-weight:600;color:rgba(246,241,231,.66);}
.sub b{color:#E8A17F;font-weight:700;}
.start{flex-shrink:0;align-self:center;margin-top:12px;border:1.5px solid rgba(232,132,95,.55);background:rgba(200,70,35,.10);border-radius:999px;padding:8px 22px;display:flex;gap:14px;align-items:center;}
.start .a{font-family:'DM Mono',monospace;font-size:13px;letter-spacing:.16em;color:#E8845F;}
.start .b{font-weight:800;font-size:15.5px;color:#F6F1E7;}
.cols{flex:1;min-height:0;margin-top:16px;display:flex;gap:56px;position:relative;}
.col{flex:1;display:flex;flex-direction:column;gap:12px;min-width:0;}
.spine{position:absolute;left:50%;top:0;bottom:0;width:0;transform:translateX(-50%);}
.spine .bar{position:absolute;left:-2px;top:6px;bottom:6px;width:4px;border-radius:2px;background:linear-gradient(#E8845F,#C84623 55%,#D4A27F);box-shadow:0 0 18px rgba(200,70,35,.6);}
.stop{position:absolute;left:50%;transform:translate(-50%,-50%);width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'DM Mono',monospace;font-weight:500;font-size:18px;border:3px solid #171716;box-shadow:0 0 0 2px rgba(232,132,95,.5),0 0 22px rgba(200,70,35,.5);background:#C84623;color:#fff;}
.stop.k{background:#D4A27F;color:#211505;}.stop.w{background:#F6F1E7;color:#1b140e;}
.card{background:rgba(25,25,24,.92);border:1px solid rgba(250,250,247,.11);border-radius:14px;padding:13px 16px;box-shadow:0 12px 34px rgba(0,0,0,.45);}
.card .hd{display:flex;align-items:baseline;justify-content:space-between;gap:10px;margin-bottom:8px;}
.card .hd .t{font-weight:900;font-size:20.5px;letter-spacing:-.4px;}
.card .hd .tag{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.15em;color:#D4A27F;text-transform:uppercase;flex-shrink:0;}
.card p{font-size:14px;color:rgba(246,241,231,.72);line-height:1.32;}
.card p b{color:#F6F1E7;}
.term{margin-top:8px;background:#0d0d0c;border:1px solid rgba(250,250,247,.10);border-radius:10px;padding:10px 12px;display:flex;align-items:center;gap:10px;}
.term .c{flex:1;font-family:'DM Mono',monospace;font-size:14.5px;color:#F0C9AF;}
.term .go{width:26px;height:26px;border-radius:50%;background:#C84623;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.term .go svg{width:13px;height:13px;stroke:#fff;stroke-width:3;fill:none;stroke-linecap:round;}
.row{display:flex;align-items:center;gap:10px;padding:6.5px 0;border-top:1px solid rgba(250,250,247,.07);}
.row:first-of-type{border-top:none;}
.row .n{font-weight:800;font-size:15.5px;flex-shrink:0;}
.row .d{flex:1;font-size:13px;color:rgba(246,241,231,.6);}
.row .bg{flex-shrink:0;font-family:'DM Mono',monospace;font-size:12px;background:#C84623;color:#fff;border-radius:7px;padding:3px 10px;font-weight:500;}
.row .bg.k{background:#3a2c20;color:#E8A17F;border:1px solid rgba(232,132,95,.4);}
.chk{display:flex;gap:10px;align-items:flex-start;padding:5.5px 0;font-size:14.5px;color:rgba(246,241,231,.82);}
.chk b{color:#F6F1E7;}
.chk .bx{width:19px;height:19px;border-radius:5px;background:#2e7d54;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px;}
.chk .bx svg{width:11px;height:11px;stroke:#fff;stroke-width:3.4;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.chk.x .bx{background:#8a3category;background:#8a3520;}
.cheat{flex-shrink:0;margin:14px 0 0;background:rgba(15,15,14,.94);border:1px solid rgba(250,250,247,.10);border-radius:14px 14px 0 0;padding:13px 20px 12px;}
.cheat .hd{display:flex;justify-content:space-between;margin-bottom:9px;}
.cheat .hd .t{font-weight:900;font-size:17px;}
.cheat .hd .tag{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.15em;color:rgba(246,241,231,.4);text-transform:uppercase;}
.cheat .gridc{display:grid;grid-template-columns:1fr 1fr 1fr;gap:7px 22px;}
.ci{display:flex;align-items:center;gap:9px;font-size:13px;color:rgba(246,241,231,.62);}
.ci b{font-family:'DM Mono',monospace;font-weight:500;font-size:13px;color:#E8A17F;background:rgba(200,70,35,.13);border:1px solid rgba(232,132,95,.32);border-radius:6px;padding:2.5px 9px;white-space:nowrap;}
.ftr{flex-shrink:0;height:52px;margin:0 -36px;background:#0c0c0b;border-top:1px solid rgba(250,250,247,.1);display:flex;align-items:center;justify-content:center;gap:12px;}
.ftr img{width:26px;height:26px;border-radius:50%;}
.ftr .a{font-weight:900;font-size:15.5px;}.ftr .b{font-size:14.5px;color:rgba(246,241,231,.55);}
.ftr .kw{font-family:'DM Mono',monospace;font-size:13px;color:#E8A17F;}
"""

GO='<span class="go"><svg viewBox="0 0 24 24"><path d="M12 19V5M6 11l6-6 6 6"/></svg></span>'
CK='<span class="bx"><svg viewBox="0 0 24 24"><path d="M4 12l5 5L20 7"/></svg></span>'
XX='<span class="bx"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg></span>'

def bcard(t,tag,inner): return f'<div class="card"><div class="hd"><span class="t">{t}</span><span class="tag">{tag}</span></div>{inner}</div>'
def term(c): return f'<div class="term"><span class="c">{c}</span>{GO}</div>'
def rows(rr): return "".join(f'<div class="row"><span class="n">{n}</span><span class="d">{d}</span><span class="bg{" k" if k else ""}">{b}</span></div>' for n,d,b,k in rr)
def checks(cc,x=False): return "".join(f'<div class="chk{" x" if x else ""}">{XX if x else CK}<span>{c}</span></div>' for c in cc)
def cheat(t,tag,items): return ('<div class="cheat"><div class="hd"><span class="t">'+t+'</span><span class="tag">'+tag+'</span></div><div class="gridc">'
    +"".join(f'<span class="ci"><b>{a}</b>{b}</span>' for a,b in items)+'</div></div>')

def emit(fn,title,sub,start_a,start_b,left,right,nstops,cheat_html,kw):
    stops="".join(f'<span class="stop{[" "," k"," w"][i%3]}" style="top:{int((i+0.5)*100/nstops)}%">{i+1}</span>' for i in range(nstops))
    html=f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>{CSS}</style></head><body>
<div class="frame" id="artifact">
<div class="hdr"><img src="__LOGO__"><span class="t">{title}</span></div>
<div class="sub">{sub}</div>
<div class="start"><span class="a">{start_a}</span><span class="b">{start_b}</span></div>
<div class="cols"><div class="col">{left}</div><div class="spine"><span class="bar"></span>{stops}</div><div class="col">{right}</div></div>
{cheat_html}
<div class="ftr"><img src="__LOGO__"><span class="a">ULTRON</span><span class="b">&middot; AI operator for founders &middot; 51ultron.com &middot;</span><span class="kw">comment {kw}</span></div>
</div></body></html>"""
    open(fn,"w").write(html); print("wrote",fn)

os.makedirs("content/howto2",exist_ok=True)

# ---------------- li-03 SOURCE ----------------
L=(bcard("Type the sentence","THE INPUT",term("&gt; source 200 founders matching my ICP")+'<p style="margin-top:8px">Plain English. The router reads the job and hires <b>CORTEX</b>. No menus, no setup.</p>')
+bcard("The ICP filter","SET ONCE",rows([("Founder / CEO","the buyer it hunts","WHO",0),("2-50 seats","the size band","SIZE",1),("IT services / software","the niche","WHAT",1),("US + UK","the geo","WHERE",1)]))
+bcard("SPECTER picks it up","AUTO HANDOFF",term("&gt; draft 200 openers, one trigger each")+'<p style="margin-top:8px">62 words a step, personalised from each brief. <b>No mail-merge smell.</b></p>')
+bcard("What you get","THE PAYOFF",checks(["<b>200 briefs</b>, one page each","<b>200 openers</b> queued at 10:00 local","<b>37 accounts</b> flagged deal-ready","You only tap <b>approve</b>"])))
R=(bcard("CORTEX runs","LIVE DATA",rows([("Pulled","companies matching the niche","1,284",0),("Net-new","deduped against your CRM","902",1),("Scored","pass the full ICP filter","471",1),("Exported","ranked, with 1-page briefs","200",0)]))
+bcard("The gate holds","NO ACCIDENTS",'<p><b>240 sends parked on HOLD.</b> Nothing external fires until you approve. Read 12, spot-check the rest, one tap.</p>')
+bcard("The clock","REAL TIMING",rows([("09:14","you type the sentence","IN",1),("09:33","top 200 exported","+19 MIN",1),("09:47","queue ready, gate holds","47 MIN",0)])+'<p style="margin-top:8px">The laptop was closed for <b>46 of the 47 minutes</b>.</p>'))
CH=cheat("Handy commands","CHEAT SHEET",[("/cortex","profile + source"),("/specter","openers + sequences"),("/amplify","10:00 local queue"),("/striker","triage the replies"),("approve","release the queue"),("/brief","one-page account brief")])
emit("content/howto2/li-03.html",'Source <em>200 founders</em> from one sentence.',
 'The unedited run from this morning. One line in, briefed pipeline out. <b>47 minutes.</b>',
 "START HERE","one sentence &middot; laptop closed &middot; 47 min",L,R,6,CH,"SOURCE")

# ---------------- li-02 TABS ----------------
L=(bcard("The stack you pay for","$129 / MO",rows([("ChatGPT","answers, no memory of you","$20",0),("Claude","same, second tab","$20",0),("Perplexity","research only","$20",1),("Jasper","copy only","$49",1),("Midjourney","images only","$10",1),("Notion AI","notes only","$10",1)]))
+bcard("What actually breaks","THE TAB TAX",checks(["Context dies inside <b>every tab</b>","You re-paste your ICP <b>all day</b>","<b>You</b> are the router between them","Answers instead of <b>finished work</b>"],x=True)))
R=(bcard("One box instead","THE SWAP",term("&gt; write the cold sequence")+term("&gt; audit my GTM")+'<p style="margin-top:8px">The router reads each job, hires the agent, picks the model tier. <b>You never choose.</b></p>')
+bcard("One context","THE BRAIN",rows([("Your ICP","loaded in every job","SET",0),("Your voice","under every draft","SET",1),("Your pipeline","live in every answer","LIVE",1)]))
+bcard("What you keep","THE PAYOFF",checks(["One login, one history, <b>one bill</b>","Work lands <b>done</b>: briefs, sends, PRs","A day of work costs <b>cents</b>, not seats"])))
CH=cheat("The agents inside","ONE SUBSCRIPTION",[("/cortex","research"),("/specter","outbound"),("/striker","deals"),("/pulse","content"),("/sentinel","code"),("/amplify","publishing")])
emit("content/howto2/li-02.html",'Replace <em>six AI tabs</em> with one box.',
 'Six subscriptions, six logins, six dead contexts. Here is the whole swap, priced.',
 "THE MATH","$129/mo of tabs &rarr; cents per day",L,R,4,CH,"TABS")

# ---------------- li-06 SHIP ----------------
L=(bcard("Report the bug","PLAIN ENGLISH",term("&gt; the pricing toggle is broken on mobile")+'<p style="margin-top:8px">That is the whole ticket. <b>08:02</b>, first coffee poured.</p>')
+bcard("SENTINEL traces","08:04",rows([("12 files","read and traced","REPO",1),("Toggle.tsx","root cause found","FIX",0)]))
+bcard("The patch","08:09",rows([("+38 / -11","across 3 files","DIFF",1),("House style","matches your codebase","CLEAN",1)])))
R=(bcard("Tests run","08:12",checks(["<b>42 passed</b>, 0 failed","Mobile screenshot attached","No regressions flagged"]))
+bcard("The PR opens","08:14",rows([("PR #214","summary + risk notes","OPEN",0),("Rollback","plan included","SAFE",1)]))
+bcard("You merge it","THE GATE",'<p>The <b>only click you make</b>. Nothing lands on main without your yes.</p>'+term("&gt; merge it")+'<p style="margin-top:8px"><b>08:17.</b> Coffee still hot.</p>'))
CH=cheat("SENTINEL commands","CHEAT SHEET",[("/sentinel fix","bug to patch"),("/sentinel test","run the suite"),("/sentinel pr","open + describe"),("/rewind","undo a change"),("/deploy","ship to prod"),("merge","your one click")])
emit("content/howto2/li-06.html",'Ship a fix before your <em>coffee goes cold</em>.',
 'Bug at 08:02, merged PR at 08:17. You never open the editor.',
 "THE RUN","bug &rarr; patch &rarr; tests &rarr; PR &rarr; merge &middot; 15 min",L,R,6,CH,"SHIP")

# ---------------- li-07 GATE ----------------
L=(bcard("SPECTER writes","09:38",rows([("240 emails","4-step sequence","62W",0),("One trigger each","from the account brief","REAL",1)]))
+bcard("The queue","SPREAD",rows([("10:00 local","per prospect timezone","AUTO",1),("4 days","ramped, not blasted","SAFE",1)]))
+bcard("After the send","REPLIES",'<p>Every reply routes to <b>STRIKER</b>: qualify, handle the objection, book the call. You see a digest.</p>'))
R=(bcard("THE GATE: your tap","1 CLICK",'<p>All 240 wait here. You read 12, spot-check the rest.</p><div style="display:flex;gap:8px;margin:9px 0 2px"><span style="background:#2e7d54;color:#fff;border-radius:999px;padding:6px 15px;font-family:DM Mono,monospace;font-size:12.5px">Approve all</span><span style="border:1.5px solid rgba(246,241,231,.3);color:rgba(246,241,231,.75);border-radius:999px;padding:6px 15px;font-family:DM Mono,monospace;font-size:12.5px">Hold</span><span style="border:1.5px solid rgba(246,241,231,.3);color:rgba(246,241,231,.75);border-radius:999px;padding:6px 15px;font-family:DM Mono,monospace;font-size:12.5px">Edit 3</span></div>')
+bcard("What the gate caught","SAVED YOU",checks(["Tone drift on <b>3 drafts</b>","Wrong tier CC'd on one thread","A broken merge field"],x=True))
+bcard("The send fires","10:00",checks(["<b>99.2%</b> landed in the inbox","Warm domains, ramped volume","<b>0</b> emails sent without you"])))
CH=cheat("Gate rules","HOW IT HOLDS",[("external","never fires alone"),("approve","releases the queue"),("hold","parks it, no loss"),("edit","fix inline, resend"),("log","every send stamped"),("digest","replies summarised")])
emit("content/howto2/li-07.html",'Let AI write <em>240 emails</em>. Approve every one.',
 'Outbound at AI speed without AI accidents. The gate is the whole trick.',
 "THE DEAL","AI writes &middot; you approve &middot; then it sends",L,R,5,CH,"GATE")

# ---------------- li-10 INDEX ----------------
L=(bcard("The list, ranked","TOP 8 OF 40",rows([("Northwind","IT services &middot; 34 ppl","86",0),("Globex","software &middot; 22 ppl","81",0),("Initech","consulting &middot; 41 ppl","74",1),("Stark Labs","software &middot; 12 ppl","70",1),("Umbrella","IT services &middot; 48 ppl","63",1),("Hooli","agency &middot; 19 ppl","52",1),("Wayne Co","consulting &middot; 26 ppl","41",1),("Oscorp","hardware &middot; 44 ppl","28",1)])))
R=(bcard("The signals it reads","PUBLIC DATA",checks(["Hiring for <b>ops / RevOps</b>","Stack has <b>no AI layer</b> yet","Founder posts about <b>scaling pain</b>","Raised in the last <b>18 months</b>","Sits in the <b>2-50 seat</b> ICP band"]))
+bcard("The verdicts","SO WHAT",rows([("CALL NOW","86 + 81: ready to buy","2",0),("WARM","nurture, re-score weekly","3",1),("SKIP","not this quarter","3",1)]))
+bcard("Week 3, in hour 1","THE POINT",'<p>These two call-now accounts were <b>invisible</b> in my CRM. Manual research finds them in week 3. The index found them <b>before lunch</b>.</p>'))
CH=cheat("Run it yourself","ONE SENTENCE",[("&gt; score my list","40 accounts in"),("/cortex index","the readiness run"),("weekly","auto re-score"),("call-now","sorted first"),("brief","attached per account"),("gate","before any outreach")])
emit("content/howto2/li-10.html",'Score <em>40 companies</em> on AI-readiness.',
 'Stop guessing who is ready to buy. One run reads the public signals and ranks your list.',
 "ONE RUN","40 accounts &middot; 62 minutes &middot; call-now first",L,R,4,CH,"INDEX")
