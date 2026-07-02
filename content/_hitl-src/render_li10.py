#!/usr/bin/env python3
# 10 LinkedIn posters, REBUILT: 5 distinct dense archetypes (command table / before-after split /
# run-trace terminal / flow rail / scorecard) x rotated accents. Fixes the "identical template x10"
# rejection: each poster has its OWN structure + focal element, central block HEAVY (§27.9).
# Emits content/howto2/li-NN.html (1080x1450). Export via scratchpad/export_li10.py.
import os
BOOK="#CC785C"; KRAFT="#D4A27F"; BDARK="#C84623"; OK="#5ea884"

BASE="""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
@import 'https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700;9..40,800;9..40,900&family=DM+Mono:wght@400;500&display=swap';
:root{--slate:#191919;--card:#1f1f1e;--card2:#262625;--ivory:#FAFAF7;--ink70:rgba(250,250,247,.70);--ink46:rgba(250,250,247,.44);
--rule:rgba(250,250,247,.08);--acc:__ACC__;--kraft:#D4A27F;--ok:#5ea884;--mut:#8b857d;}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#0d0d0d;display:flex;justify-content:center;padding:24px 0;font-family:'DM Sans',sans-serif;-webkit-font-smoothing:antialiased;color:var(--ivory);}
.frame{width:1080px;height:1450px;background:var(--slate);padding:32px 44px 20px;position:relative;overflow:hidden;display:flex;flex-direction:column;}
.frame::before{content:'';position:absolute;inset:0;pointer-events:none;z-index:0;background-image:radial-gradient(rgba(204,120,92,.06) 1.4px,transparent 1.5px);background-size:30px 30px;}
.atm{position:absolute;inset:0;pointer-events:none;z-index:1;background:radial-gradient(ellipse 54% 20% at 90% -2%,rgba(204,120,92,.16) 0%,transparent 60%);}
.frame>*{position:relative;z-index:2;}
.mast{flex-shrink:0;display:flex;align-items:center;justify-content:space-between;padding-bottom:11px;border-bottom:1px solid var(--rule);font-family:'DM Mono',monospace;font-size:12px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;}
.mast .ml{color:var(--ink46);}.mast .ml em{color:var(--acc);font-style:normal;}.mast .mr{color:var(--ink70);}
.hook{margin-top:16px;font-weight:900;font-size:54px;line-height:1.0;letter-spacing:-1.8px;flex-shrink:0;}.hook em{color:var(--acc);font-style:normal;}
.sub{margin-top:10px;font-size:19.5px;font-weight:500;line-height:1.3;color:var(--ink70);flex-shrink:0;}.sub b{color:var(--ivory);font-weight:700;}
.main{flex:1;min-height:0;margin-top:16px;display:flex;gap:14px;}
.cta{flex-shrink:0;margin-top:13px;display:flex;align-items:center;gap:16px;border:1.5px solid var(--acc);border-radius:16px;background:rgba(204,120,92,.08);padding:12px 12px 12px 24px;}
.cta .ph{flex:1;font-size:21px;font-weight:600;color:var(--ink70);}.cta .ph b{color:var(--acc);font-weight:900;}
.cta .send{width:50px;height:50px;border-radius:50%;background:var(--acc);flex-shrink:0;display:flex;align-items:center;justify-content:center;}
.cta .send svg{width:24px;height:24px;stroke:#1a0f0a;stroke-width:2.4;fill:none;stroke-linecap:round;stroke-linejoin:round;}
.ftr{flex-shrink:0;margin-top:11px;padding-top:10px;border-top:1px solid var(--rule);display:flex;align-items:center;justify-content:space-between;}
.fl{display:flex;align-items:center;gap:11px;}.flogo{width:28px;height:28px;border-radius:50%;object-fit:cover;}
.ftx{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--ink70);}.ftx b{color:var(--ivory);font-weight:500;}
.furl{font-weight:900;font-size:20px;letter-spacing:-.5px;}.furl em{color:var(--acc);font-style:normal;}
__EXTRA__
</style></head><body><div class="frame" id="artifact"><div class="atm"></div>
<div class="mast"><span class="ml">__MASTL__</span><span class="mr">__MASTR__</span></div>
<div class="hook">__HOOK__</div><div class="sub">__SUB__</div>
<div class="main">__MAIN__</div>
<div class="cta"><span class="ph">Comment <b>__KW__</b> __TAIL__</span><span class="send"><svg viewBox="0 0 24 24"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"/></svg></span></div>
<div class="ftr"><div class="fl"><img class="flogo" src="__LOGO__"><span class="ftx"><b>ULTRON</b> &middot; AI OPERATOR FOR FOUNDERS</span></div><span class="furl">51ultron<em>.</em>com</span></div>
</div></body></html>"""

def emit(n,acc,mastl,mastr,hook,sub,extra,main,kw,tail):
    h=(BASE.replace("__ACC__",acc).replace("__MASTL__",mastl).replace("__MASTR__",mastr)
        .replace("__HOOK__",hook).replace("__SUB__",sub).replace("__EXTRA__",extra)
        .replace("__MAIN__",main).replace("__KW__",kw).replace("__TAIL__",tail))
    os.makedirs("content/howto2",exist_ok=True)
    open(f"content/howto2/li-{n:02d}.html","w").write(h); print("wrote",n)

# ---------- P1 ROUTING: full-width COMMAND TABLE ----------
extra1="""
.tbl{flex:1;display:flex;flex-direction:column;border:1px solid var(--rule);border-radius:14px;overflow:hidden;background:var(--card);}
.thead{display:flex;background:var(--card2);font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink46);padding:11px 16px;gap:12px;}
.tr{display:flex;align-items:center;gap:12px;padding:0 16px;border-top:1px solid var(--rule);flex:1;}
.c1{width:305px;font-family:'DM Mono',monospace;font-size:16.5px;color:var(--ivory);}.c1 i{color:var(--acc);font-style:normal;}
.c2{width:132px;font-weight:800;font-size:16px;color:var(--acc);}
.c3{width:88px;font-family:'DM Mono',monospace;font-size:13px;color:var(--kraft);}
.c4{flex:1;font-size:15.5px;color:var(--ink70);line-height:1.22;}.c4 b{color:var(--ivory);}
.rail{width:236px;display:flex;flex-direction:column;gap:10px;}
.st{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:12px 15px;}
.st .v{font-size:34px;font-weight:900;color:var(--acc);letter-spacing:-1px;line-height:1;}
.st .k{margin-top:5px;font-size:13.5px;color:var(--ink70);line-height:1.2;}
.tier{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:12px 15px;flex:1;}
.tier .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:8px;}
.tier .row{display:flex;justify-content:space-between;font-size:14.5px;padding:6px 0;border-top:1px solid var(--rule);}
.tier .row b{color:var(--kraft);font-family:'DM Mono',monospace;font-weight:500;}
.gate{background:linear-gradient(180deg,rgba(94,168,132,.08),var(--card));border:1px solid rgba(94,168,132,.36);border-radius:12px;padding:12px 15px;}
.gate .h{display:flex;align-items:center;gap:8px;font-size:15px;font-weight:800;}
.gate .h i{width:9px;height:9px;border-radius:50%;background:var(--ok);box-shadow:0 0 8px rgba(94,168,132,.8);}
.gate .d{margin-top:5px;font-size:13px;color:var(--ink70);line-height:1.25;}
"""
rows1=[("profile this founder","CORTEX","SMART","ranked brief, <b>40 signals</b>, 1 page"),
("write the cold sequence","SPECTER","SMART","<b>4-step</b> sequence, 62 words a step"),
("handle this objection","STRIKER","DEEP","rebuttal + <b>close plan</b>, deal-aware"),
("draft the launch post","PULSE","SMART","post <b>in your voice</b>, hook first"),
("fix the pricing page","SENTINEL","DEEP","patch + tests + <b>PR opened</b>"),
("schedule this everywhere","AMPLIFY","LITE","per channel, <b>per timezone</b>"),
("review this NDA","COUNSEL","DEEP","<b>risk flags</b> + redlines in minutes"),
("what changed today","ROUTER","LITE","one-line digest, <b>every agent</b>")]
trs="".join(f'<div class="tr"><div class="c1"><i>&gt;</i> {a}</div><div class="c2">{b}</div><div class="c3">{c}</div><div class="c4">{d}</div></div>' for a,b,c,d in rows1)
main1=f'''<div class="tbl"><div class="thead"><span style="width:305px">You type</span><span style="width:132px">Routes to</span><span style="width:88px">Tier</span><span style="flex:1">What comes back</span></div>{trs}</div>
<div class="rail">
<div class="st"><div class="v">8</div><div class="k">jobs, one chat box, zero picking</div></div>
<div class="st"><div class="v">7+1</div><div class="k">agents + the router that reads the job</div></div>
<div class="tier"><div class="h">The router picks the tier</div>
<div class="row"><span>Lite &middot; lookups</span><b>Haiku</b></div>
<div class="row"><span>Smart &middot; default</span><b>Sonnet</b></div>
<div class="row"><span>Deep &middot; judgement</span><b>Opus</b></div>
<div class="row"><span>You pay</span><b>cents</b></div></div>
<div class="gate"><div class="h"><i></i>Human gate</div><div class="d">Anything that sends waits for your yes.</div></div>
</div>'''

# ---------- P2 TABS: BEFORE/AFTER split ----------
extra2="""
.col{flex:1;display:flex;flex-direction:column;border-radius:14px;border:1px solid var(--rule);background:var(--card);overflow:hidden;}
.col .hd{padding:13px 18px;background:var(--card2);display:flex;justify-content:space-between;align-items:baseline;}
.col .hd .t{font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);}
.col .hd .p{font-weight:900;font-size:22px;color:var(--ivory);}.col .hd .p.bad{color:var(--mut);text-decoration:line-through;text-decoration-color:rgba(200,70,35,.7);text-decoration-thickness:3px;}
.trow{flex:1;display:flex;align-items:center;justify-content:space-between;padding:0 18px;border-top:1px solid var(--rule);}
.trow .n{font-weight:700;font-size:18px;}.trow .m{font-family:'DM Mono',monospace;font-size:13.5px;color:var(--mut);}
.trow .pr{font-weight:800;font-size:17px;color:var(--ink70);}
.vs{align-self:center;font-weight:900;font-size:26px;color:var(--acc);flex-shrink:0;padding:0 2px;}
.one{flex:1.15;display:flex;flex-direction:column;border-radius:14px;border:1.5px solid var(--acc);background:linear-gradient(180deg,rgba(204,120,92,.10),var(--card));overflow:hidden;}
.one .hd{padding:13px 18px;display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid var(--rule);}
.one .hd .t{font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--acc);}
.one .hd .p{font-weight:900;font-size:22px;color:var(--acc);}
.feat{flex:1;display:flex;align-items:center;gap:12px;padding:0 18px;border-top:1px solid var(--rule);}
.feat i{width:8px;height:8px;border-radius:50%;background:var(--acc);flex-shrink:0;}
.feat .x{font-size:16.5px;color:var(--ink70);line-height:1.25;}.feat .x b{color:var(--ivory);}
.chips{display:flex;flex-wrap:wrap;gap:7px;padding:12px 18px;border-top:1px solid var(--rule);}
.chip{font-family:'DM Mono',monospace;font-size:12px;color:var(--acc);border:1px solid rgba(204,120,92,.34);background:rgba(204,120,92,.08);border-radius:7px;padding:4px 10px;}
"""
tabs=[("ChatGPT Plus","context dies per tab","$20"),("Claude Pro","re-paste everything","$20"),("Perplexity Pro","research only","$20"),
("Jasper","copy only","$49"),("Midjourney","images only","$10"),("Copy.ai","one more login","$49")]
tabrows="".join(f'<div class="trow"><span class="n">{n}</span><span class="m">{m}</span><span class="pr">{p}</span></div>' for n,m,p in tabs)
feats=[("One context. Your ICP, voice and pipeline <b>live in every job</b>."),
("The router reads the task and <b>picks the model tier</b> for you."),
("Research flows into outreach flows into <b>deals</b>, no re-pasting."),
("Output lands as <b>work done</b>: briefs, sequences, PRs, schedules."),
("You pay per token. A day of work costs <b>cents, not seats</b>.")]
featrows="".join(f'<div class="feat"><i></i><span class="x">{x}</span></div>' for x in feats)
main2=f'''<div class="col"><div class="hd"><span class="t">The tab stack &middot; 6 logins</span><span class="p bad">$168/mo</span></div>{tabrows}</div>
<div class="vs">VS</div>
<div class="one"><div class="hd"><span class="t">One chat box</span><span class="p">cents</span></div>{featrows}
<div class="chips"><span class="chip">CORTEX</span><span class="chip">SPECTER</span><span class="chip">STRIKER</span><span class="chip">PULSE</span><span class="chip">SENTINEL</span><span class="chip">AMPLIFY</span><span class="chip">COUNSEL</span></div></div>'''

# ---------- P3 SOURCE: RUN-TRACE terminal ----------
extra3="""
.term{flex:1;display:flex;flex-direction:column;border-radius:14px;border:1px solid var(--rule);background:#151514;overflow:hidden;}
.tbar{display:flex;align-items:center;gap:8px;padding:11px 16px;background:var(--card2);border-bottom:1px solid var(--rule);}
.dot{width:11px;height:11px;border-radius:50%;background:#5a5955;}
.tbar .tt{margin-left:8px;font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.14em;color:var(--ink46);text-transform:uppercase;}
.ln{flex:1;display:flex;align-items:center;gap:14px;padding:0 18px;font-family:'DM Mono',monospace;font-size:15.5px;border-top:1px solid rgba(250,250,247,.04);}
.ts{color:var(--ink46);width:52px;flex-shrink:0;font-size:13px;}
.ag{width:92px;flex-shrink:0;font-weight:500;color:var(--acc);}
.ms{color:var(--ink70);}.ms b{color:var(--ivory);font-weight:500;}.ms i{color:var(--kraft);font-style:normal;}
.ln.gate .ag{color:var(--ok);} .ln.gate .ms b{color:var(--ok);}
.rail{width:250px;display:flex;flex-direction:column;gap:10px;}
.icp{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:12px 15px;}
.icp .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:8px;}
.icp .r{font-size:14.5px;color:var(--ink70);padding:5px 0;border-top:1px solid var(--rule);}.icp .r b{color:var(--ivory);}
.st{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:12px 15px;}
.st .v{font-size:36px;font-weight:900;color:var(--acc);letter-spacing:-1px;line-height:1;}
.st .k{margin-top:5px;font-size:13.5px;color:var(--ink70);line-height:1.2;}
"""
log=[("09:14","ROUTER","job read: <b>source 200 founders</b> matching my ICP"),
("09:14","CORTEX","pulled <b>1,284</b> companies, IT services, US + UK"),
("09:16","CORTEX","deduped vs CRM: <i>902 net-new</i>"),
("09:19","CORTEX","enriched 902: funding, size, tech stack"),
("09:24","CORTEX","scored vs ICP: <b>471 pass</b> the 2-50 seat filter"),
("09:31","CORTEX","ranked by signal: hiring + recent raise + intent"),
("09:33","CORTEX","top <b>200 exported</b> with 1-page briefs"),
("09:38","SPECTER","drafted <b>200 openers</b>, one trigger each, 62 words"),
("09:44","STRIKER","flagged 37 accounts as <i>deal-ready</i>"),
("09:45","AMPLIFY","queue set: 10:00 local, per timezone"),
("09:46","GATE","<b>240 sends on HOLD</b>, waiting for your approve",True),
("09:47","ROUTER","done in <b>47 min</b>. laptop was closed for 46 of them")]
lns="".join(f'<div class="ln{" gate" if len(r)>3 else ""}"><span class="ts">{r[0]}</span><span class="ag">{r[1]}</span><span class="ms">{r[2]}</span></div>' for r in log)
main3=f'''<div class="term"><div class="tbar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="tt">ultron &middot; run trace &middot; this morning</span></div>{lns}</div>
<div class="rail">
<div class="st"><div class="v">200</div><div class="k">founders sourced, briefed, sequenced</div></div>
<div class="st"><div class="v">47<span style="font-size:22px">min</span></div><div class="k">one sentence in, work out</div></div>
<div class="icp"><div class="h">The ICP it matched</div><div class="r"><b>Founder / CEO</b></div><div class="r"><b>2-50</b> employees</div><div class="r">IT services / software</div><div class="r"><b>US + UK</b></div></div>
<div class="icp"><div class="h">You did</div><div class="r">typed <b>one sentence</b></div><div class="r">will tap <b>approve</b></div></div>
</div>'''

# ---------- P4 BRAIN: BEFORE/AFTER memory ----------
extra4="""
.col{flex:1;display:flex;flex-direction:column;border-radius:14px;border:1px solid var(--rule);background:var(--card);overflow:hidden;}
.col .hd{padding:13px 18px;background:var(--card2);font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);}
.pain{flex:1;display:flex;align-items:center;gap:12px;padding:0 18px;border-top:1px solid var(--rule);}
.pain .x{font-size:16.5px;color:var(--mut);line-height:1.3;}.pain .x b{color:var(--ink70);}
.pain i{font-family:'DM Mono',monospace;color:var(--acc);font-style:normal;flex-shrink:0;}
.tot{padding:14px 18px;border-top:1px solid var(--rule);font-weight:800;font-size:19px;color:var(--ink70);}
.tot b{color:var(--acc);}
.brain{flex:1.2;display:flex;flex-direction:column;border-radius:14px;border:1.5px solid var(--acc);background:linear-gradient(180deg,rgba(204,120,92,.10),var(--card));overflow:hidden;}
.brain .hd{padding:13px 18px;border-bottom:1px solid var(--rule);display:flex;justify-content:space-between;}
.brain .hd .t{font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--acc);}
.brain .hd .s{font-family:'DM Mono',monospace;font-size:12px;color:var(--ink46);}
.mem{flex:1;display:flex;align-items:center;justify-content:space-between;gap:10px;padding:0 18px;border-top:1px solid var(--rule);}
.mem .n{font-weight:800;font-size:17px;}.mem .d{font-size:13.5px;color:var(--ink70);}
.mem .tag{font-family:'DM Mono',monospace;font-size:11.5px;color:var(--acc);border:1px solid rgba(204,120,92,.34);border-radius:6px;padding:3px 8px;flex-shrink:0;}
"""
pains=[("&gt;",""So, my ICP is founders at 2-50..." <b>again</b>"),("&gt;","15 minutes of context <b>every session</b>"),
("&gt;","the voice sample, <b>re-pasted</b>"),("&gt;","pricing tiers, <b>re-explained</b>"),("&gt;","close the tab, <b>everything dies</b>")]
prow="".join(f'<div class="pain"><i>{a}</i><span class="x">{b}</span></div>' for a,b in pains)
mems=[("Your ICP","Founder/CEO, 2-50, IT services, US/UK","every agent"),("Pricing","Starter free, Max $19, Ent $297","STRIKER"),
("Voice sample","how you actually write","PULSE"),("Deal stages","your pipeline, your close plan","STRIKER"),
("Objection bank","what worked, what died","STRIKER"),("Brand system","colors, format, banned words","PULSE"),
("Tool wiring","CRM, mail, calendar, repo","all runs")]
mrow="".join(f'<div class="mem"><div><div class="n">{n}</div><div class="d">{d}</div></div><span class="tag">{t}</span></div>' for n,d,t in mems)
main4=f'''<div class="col"><div class="hd">Every other AI chat</div>{prow}<div class="tot">Cost: <b>15 min per session</b>, forever</div></div>
<div class="brain"><div class="hd"><span class="t">The Ultron brain &middot; briefed once</span><span class="s">recalled in every run</span></div>{mrow}</div>'''

# ---------- P5 AUDIT: SCORECARD ----------
extra5="""
.score{width:270px;display:flex;flex-direction:column;gap:10px;}
.big{background:var(--card);border:1.5px solid var(--acc);border-radius:14px;padding:18px;text-align:left;}
.big .v{font-size:78px;font-weight:900;letter-spacing:-3px;color:var(--acc);line-height:.95;}
.big .of{font-size:20px;color:var(--ink46);font-weight:700;}
.big .k{margin-top:8px;font-size:14.5px;color:var(--ink70);line-height:1.3;}
.sent{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:13px 15px;}
.sent .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:7px;}
.sent .q{font-family:'DM Mono',monospace;font-size:16px;color:var(--ivory);}.sent .q i{color:var(--acc);font-style:normal;}
.leg{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:12px 15px;flex:1;}
.leg .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:6px;}
.leg .r{display:flex;align-items:center;gap:9px;font-size:14px;color:var(--ink70);padding:5px 0;}
.leg .sw{width:12px;height:12px;border-radius:3px;flex-shrink:0;}
.list{flex:1;display:flex;flex-direction:column;border:1px solid var(--rule);border-radius:14px;background:var(--card);overflow:hidden;}
.lhd{display:flex;background:var(--card2);padding:11px 16px;font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink46);}
.li{flex:1;display:flex;align-items:center;gap:13px;padding:0 16px;border-top:1px solid var(--rule);}
.li .n{width:170px;font-weight:800;font-size:17px;}
.li .bar{width:170px;height:10px;border-radius:5px;background:rgba(250,250,247,.07);overflow:hidden;flex-shrink:0;}
.li .bar i{display:block;height:100%;border-radius:5px;background:var(--acc);}
.li .sc{width:44px;font-family:'DM Mono',monospace;font-size:15px;color:var(--kraft);flex-shrink:0;}
.li .fx{flex:1;font-size:14.5px;color:var(--ink70);line-height:1.2;}.li .fx b{color:var(--ivory);}
.li .vd{flex-shrink:0;font-family:'DM Mono',monospace;font-size:11.5px;border-radius:6px;padding:4px 9px;}
.vd.keep{color:var(--ok);border:1px solid rgba(94,168,132,.4);}
.vd.fix{color:var(--acc);border:1px solid rgba(204,120,92,.4);}
"""
audit=[("Positioning",72,"niche is clear, proof is thin: add 2 case studies","KEEP"),
("ICP match",58,"31% of pipeline is <b>outside</b> the 2-50 band","FIX"),
("Outbound",44,"generic openers: one trigger per email, 62 words","FIX"),
("Follow-up",39,"<b>68% of threads die</b> after touch 1: cadence on","FIX"),
("Pricing",70,"page converts, add the cents-per-run math","KEEP"),
("Content",66,"posting random days: fix 10:00 cadence","FIX"),
("Pipeline hygiene",51,"14 deals stale &gt;30 days: kill or revive","FIX"),
("Deliverability",83,"domains warm, keep the ramp","KEEP")]
lis="".join(f'<div class="li"><span class="n">{n}</span><span class="bar"><i style="width:{v}%"></i></span><span class="sc">{v}</span><span class="fx">{f}</span><span class="vd {"keep" if t=="KEEP" else "fix"}">{t}</span></div>' for n,v,f,t in audit)
main5=f'''<div class="list"><div class="lhd">The 8 checks it ran on my funnel</div>{lis}</div>
<div class="score">
<div class="sent"><div class="h">What I typed</div><div class="q"><i>&gt;</i> audit my GTM</div></div>
<div class="big"><span class="v">61</span><span class="of">/100</span><div class="k">funnel score, computed from my real pipeline + sends</div></div>
<div class="leg"><div class="h">Verdict spread</div>
<div class="r"><span class="sw" style="background:var(--ok)"></span>3 keep working</div>
<div class="r"><span class="sw" style="background:var(--acc)"></span>5 fix this week</div>
<div class="r"><span class="sw" style="background:rgba(250,250,247,.25)"></span>each with the exact fix</div></div>
</div>'''

# ---------- P6 BUILDER: FLOW RAIL ----------
extra6="""
.flow{flex:1.35;display:flex;flex-direction:column;gap:0;}
.stage{flex:1;display:flex;gap:14px;position:relative;}
.knob{width:44px;display:flex;flex-direction:column;align-items:center;flex-shrink:0;}
.knob .c{width:34px;height:34px;border-radius:50%;background:rgba(204,120,92,.14);border:1.5px solid var(--acc);display:flex;align-items:center;justify-content:center;font-family:'DM Mono',monospace;font-size:14px;color:var(--acc);flex-shrink:0;}
.knob .l{flex:1;width:2px;background:rgba(204,120,92,.3);}
.stage:last-child .knob .l{display:none;}
.scard{flex:1;background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:11px 16px;margin-bottom:9px;display:flex;align-items:center;justify-content:space-between;gap:10px;}
.scard .t{font-weight:800;font-size:17.5px;}.scard .t small{display:block;font-weight:500;font-size:13.5px;color:var(--ink70);margin-top:3px;}
.scard .t small b{color:var(--ivory);}
.scard .ts{font-family:'DM Mono',monospace;font-size:12.5px;color:var(--ink46);flex-shrink:0;}
.scard.gate{border-color:rgba(94,168,132,.4);background:linear-gradient(180deg,rgba(94,168,132,.07),var(--card));}
.rail{width:250px;display:flex;flex-direction:column;gap:10px;}
.diff{background:#151514;border:1px solid var(--rule);border-radius:12px;padding:13px 15px;font-family:'DM Mono',monospace;font-size:14px;}
.diff .h{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:8px;}
.diff .a{color:var(--ok);}.diff .r{color:var(--acc);}.diff .m{color:var(--ink70);padding:3px 0;}
.st{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:12px 15px;}
.st .v{font-size:34px;font-weight:900;color:var(--acc);line-height:1;letter-spacing:-1px;}
.st .k{margin-top:5px;font-size:13.5px;color:var(--ink70);line-height:1.2;}
.note{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:12px 15px;flex:1;font-size:14.5px;color:var(--ink70);line-height:1.35;}
.note b{color:var(--ivory);}
"""
stages=[("1","I typed the bug",""the pricing toggle is broken on mobile"","08:02"),
("2","SENTINEL read the repo","12 files traced, root cause in <b>Toggle.tsx</b>","08:04"),
("3","Wrote the patch","+38 / -11 across 3 files, matches house style","08:09"),
("4","Ran the tests","<b>42 passed</b>, 0 failed, screenshot attached","08:12"),
("5","Opened the PR","#214 with summary, risk notes, rollback plan","08:14"),
("6","I merged it","the only click I made. <b>Human gate held.</b>","08:17",True)]
sts="".join(f'<div class="stage"><div class="knob"><span class="c">{a}</span><span class="l"></span></div><div class="scard{" gate" if len(s)>4 else ""}"><span class="t">{b}<small>{c}</small></span><span class="ts">{d}</span></div></div>' for s in stages for a,b,c,d in [s[:4]])
main6=f'''<div class="flow">{sts}</div>
<div class="rail">
<div class="st"><div class="v">15<span style="font-size:20px">min</span></div><div class="k">bug report to merged PR</div></div>
<div class="diff"><div class="h">PR #214 &middot; diff</div><div class="m"><span class="a">+38</span> additions</div><div class="m"><span class="r">-11</span> deletions</div><div class="m">3 files &middot; 42 tests</div><div class="m">risk: <span class="a">low</span></div></div>
<div class="note">I never opened the editor. SENTINEL ships like a senior dev and <b>waits at the gate</b> like a junior one.</div>
</div>'''

# ---------- P7 OUTBOUND GATE ----------
extra7="""
.pipe{flex:1.3;display:flex;flex-direction:column;gap:9px;}
.seg{flex:1;background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:12px 16px;display:flex;align-items:center;gap:14px;}
.seg .n{font-family:'DM Mono',monospace;font-size:13px;color:var(--acc);width:70px;flex-shrink:0;}
.seg .b{flex:1;}.seg .b .t{font-weight:800;font-size:17.5px;}.seg .b .d{font-size:14px;color:var(--ink70);margin-top:3px;line-height:1.25;}
.seg .b .d b{color:var(--ivory);}
.seg .num{font-weight:900;font-size:30px;color:var(--kraft);letter-spacing:-1px;flex-shrink:0;}
.seg.gate{border:1.5px solid rgba(94,168,132,.5);background:linear-gradient(180deg,rgba(94,168,132,.09),var(--card));}
.seg.gate .n{color:var(--ok);}.seg.gate .num{color:var(--ok);}
.btns{display:flex;gap:7px;margin-top:7px;}
.btn{font-family:'DM Mono',monospace;font-size:12px;border-radius:7px;padding:4px 11px;}
.btn.a{background:var(--ok);color:#0f1a14;font-weight:500;}
.btn.h{border:1px solid var(--rule);color:var(--ink70);}
.rail{width:250px;display:flex;flex-direction:column;gap:10px;}
.st{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:12px 15px;}
.st .v{font-size:34px;font-weight:900;color:var(--acc);line-height:1;letter-spacing:-1px;}
.st .k{margin-top:5px;font-size:13.5px;color:var(--ink70);line-height:1.2;}
.mini{background:#151514;border:1px solid var(--rule);border-radius:12px;padding:12px 15px;flex:1;}
.mini .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:8px;}
.mini .r{font-family:'DM Mono',monospace;font-size:13px;color:var(--ink70);padding:4px 0;border-top:1px solid rgba(250,250,247,.05);}
.mini .r b{color:var(--kraft);font-weight:500;}
"""
segs=[("09:38","SPECTER wrote 240","4-step sequence, <b>one trigger</b> per email, 62 words a step","240"),
("09:44","Personalised each","company signal + role pain, <b>no mail-merge smell</b>","240"),
("09:46","Queued the sends","10:00 <b>local time</b> per prospect, spread over 4 days","4d"),
("09:47","THE GATE: my approve","every send waits here. I read 12, spot-check the rest, tap once.","240",True),
("10:00","Sends fire","warm domains, <b>99.2% inboxed</b>, replies route to STRIKER","99.2%")]
segrows=""
for s in segs:
    gate=len(s)>4
    btns='<div class="btns"><span class="btn a">Approve all</span><span class="btn h">Hold</span><span class="btn h">Edit 3</span></div>' if gate else ''
    segrows+=f'<div class="seg{" gate" if gate else ""}"><span class="n">{s[0]}</span><div class="b"><div class="t">{s[1]}</div><div class="d">{s[2]}</div>{btns}</div><span class="num">{s[3]}</span></div>'
main7=f'''<div class="pipe">{segrows}</div>
<div class="rail">
<div class="st"><div class="v">240</div><div class="k">emails written by SPECTER</div></div>
<div class="st"><div class="v">1</div><div class="k">tap from me before anything moved</div></div>
<div class="mini"><div class="h">Why the gate matters</div><div class="r">tone drift &middot; <b>caught</b></div><div class="r">wrong tier CC'd &middot; <b>caught</b></div><div class="r">3 edits &middot; <b>2 min</b></div><div class="r">sent alone &middot; <b>0</b></div><div class="r">brand damage &middot; <b>0</b></div></div>
</div>'''

# ---------- P8 PROOF: EVIDENCE LEDGER ----------
extra8="""
.led{flex:1;display:flex;flex-direction:column;border:1px solid var(--rule);border-radius:14px;background:var(--card);overflow:hidden;}
.lhd{display:flex;background:var(--card2);padding:11px 16px;font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink46);gap:12px;}
.lr{flex:1;display:flex;align-items:center;gap:12px;padding:0 16px;border-top:1px solid var(--rule);}
.lr .cl{flex:1;font-size:15.5px;color:var(--ivory);line-height:1.22;}.lr .cl b{color:var(--kraft);}
.lr .src{width:250px;font-family:'DM Mono',monospace;font-size:12.5px;color:var(--ink70);flex-shrink:0;}
.lr .cf{width:76px;flex-shrink:0;font-family:'DM Mono',monospace;font-size:12.5px;color:var(--ok);}
.share{width:264px;display:flex;flex-direction:column;gap:10px;}
.card8{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:13px 15px;}
.card8 .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:7px;}
.card8 .v{font-size:34px;font-weight:900;color:var(--acc);letter-spacing:-1px;line-height:1;}
.card8 .k{margin-top:5px;font-size:13.5px;color:var(--ink70);line-height:1.25;}
.link{background:linear-gradient(180deg,rgba(204,120,92,.1),var(--card));border:1.5px solid var(--acc);border-radius:12px;padding:14px 15px;}
.link .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--acc);margin-bottom:8px;}
.link .u{font-family:'DM Mono',monospace;font-size:14.5px;color:var(--ivory);word-break:break-all;line-height:1.4;}
.link .d{margin-top:8px;font-size:13.5px;color:var(--ink70);line-height:1.3;}
"""
claims=[(""US + UK founders reply <b>3.1x</b> more at 10:00 local"","send logs &middot; n=2,140","98%"),
(""One-trigger openers beat templates <b>4.4x</b>"","201 A/B sends &middot; 10 days","96%"),
(""62-word emails book the most calls"","winner set &middot; n=7","91%"),
(""31% of my pipe was outside ICP"","CRM scan &middot; 214 deals","99%"),
(""Follow-up 2 wins 58% of the meetings"","thread analysis &middot; 90d","94%"),
(""Warm domains inbox at <b>99.2%</b>"","4-domain ramp &middot; 6 wks","97%"),
(""Stale deals die after day 34"","cohort decay curve","89%"),
(""Deep tier only pays off on objections"","cost per close &middot; 60d","92%")]
lrs="".join(f'<div class="lr"><span class="cl">{c}</span><span class="src">{s}</span><span class="cf">{cf}</span></div>' for c,s,cf in claims)
main8=f'''<div class="led"><div class="lhd"><span style="flex:1">Claim in the brief</span><span style="width:250px">Backed by</span><span style="width:76px">Conf.</span></div>{lrs}</div>
<div class="share">
<div class="card8"><div class="h">Instead of screenshots</div><div class="v">1</div><div class="k">live link. Every number clicks through to its source run.</div></div>
<div class="link"><div class="h">Shared with my co-founder</div><div class="u">work.51ultron.com/brief/q3-outbound</div><div class="d">He challenged claim 4. The link settled it in <b>one click</b>.</div></div>
<div class="card8"><div class="h">In the brief</div><div class="v">40</div><div class="k">sources cited across 8 claims, stamped with run IDs</div></div>
</div>'''

# ---------- P9 RESUME: SESSION TIMELINE ----------
extra9="""
.tl{flex:1.35;display:flex;flex-direction:column;gap:8px;}
.day{font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink46);padding:2px 2px;}
.ev{flex:1;background:var(--card);border:1px solid var(--rule);border-radius:11px;padding:10px 15px;display:flex;align-items:center;gap:13px;}
.ev .ts{font-family:'DM Mono',monospace;font-size:12.5px;color:var(--ink46);width:52px;flex-shrink:0;}
.ev .x{font-size:15.5px;color:var(--ink70);line-height:1.25;}.ev .x b{color:var(--ivory);}
.gap{flex-shrink:0;display:flex;align-items:center;gap:12px;padding:4px 2px;}
.gap .l{flex:1;border-top:2px dashed rgba(250,250,247,.14);}
.gap .t{font-family:'DM Mono',monospace;font-size:12.5px;color:var(--acc);letter-spacing:.12em;}
.ev.hot{border:1.5px solid var(--acc);background:linear-gradient(180deg,rgba(204,120,92,.1),var(--card));}
.rail{width:256px;display:flex;flex-direction:column;gap:10px;}
.st{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:12px 15px;}
.st .v{font-size:36px;font-weight:900;color:var(--acc);letter-spacing:-1px;line-height:1;}
.st .k{margin-top:5px;font-size:13.5px;color:var(--ink70);line-height:1.2;}
.keep{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:12px 15px;flex:1;}
.keep .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:6px;}
.keep .r{display:flex;gap:9px;align-items:center;font-size:14px;color:var(--ink70);padding:5px 0;border-top:1px solid var(--rule);}
.keep .r i{width:7px;height:7px;border-radius:50%;background:var(--acc);flex-shrink:0;}
.keep .r b{color:var(--ivory);}
"""
mon=[("14:05","kicked off the Northwind deal: CORTEX brief, <b>40 signals</b>"),
("14:31","SPECTER opener v1-v3, picked v3, <b>62 words</b>"),
("15:02","STRIKER close plan drafted, champion = Sarah"),
("15:40","objection thread started: "too expensive vs in-house""),
("16:12","laptop closed <b>mid-negotiation</b>, draft v3 open")]
wed=[("09:01","typed <b>"resume northwind"</b>. one line.",1),
("09:01","it recalled: stage, champion, v3 draft, the open objection",1),
("09:03","STRIKER finished the rebuttal <b>from where it stopped</b>"),
("09:11","proposal out. <b>Zero re-briefing, zero scrolling up.</b>")]
tl='<div class="day">Monday</div>'+"".join(f'<div class="ev"><span class="ts">{a}</span><span class="x">{b}</span></div>' for a,b in mon)
tl+='<div class="gap"><span class="l"></span><span class="t">2 DAYS AWAY</span><span class="l"></span></div>'
tl+='<div class="day">Wednesday</div>'+"".join(f'<div class="ev{" hot" if len(e)>2 else ""}"><span class="ts">{e[0]}</span><span class="x">{e[1]}</span></div>' for e in wed)
main9=f'''<div class="tl">{tl}</div>
<div class="rail">
<div class="st"><div class="v">0</div><div class="k">minutes re-explaining where we were</div></div>
<div class="st"><div class="v">10<span style="font-size:20px">min</span></div><div class="k">from reopen to proposal sent</div></div>
<div class="keep"><div class="h">What carried over</div>
<div class="r"><i></i>deal stage + <b>champion</b></div><div class="r"><i></i>draft <b>v3</b>, not v1</div>
<div class="r"><i></i>the open <b>objection</b></div><div class="r"><i></i>pricing already quoted</div>
<div class="r"><i></i>next step queue</div></div>
</div>'''

# ---------- P10 INDEX: READINESS SCORECARD ----------
extra10="""
.grid{flex:1;display:flex;flex-direction:column;border:1px solid var(--rule);border-radius:14px;background:var(--card);overflow:hidden;}
.ghd{display:flex;background:var(--card2);padding:11px 16px;font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink46);gap:12px;}
.gr{flex:1;display:flex;align-items:center;gap:12px;padding:0 16px;border-top:1px solid var(--rule);}
.gr .co{width:150px;font-weight:800;font-size:16.5px;flex-shrink:0;}
.gr .co small{display:block;font-weight:500;font-size:12px;color:var(--ink46);font-family:'DM Mono',monospace;margin-top:2px;}
.gr .bar{flex:1;height:11px;border-radius:6px;background:rgba(250,250,247,.07);overflow:hidden;}
.gr .bar i{display:block;height:100%;border-radius:6px;background:var(--acc);}
.gr .sc{width:46px;font-family:'DM Mono',monospace;font-size:15px;color:var(--kraft);flex-shrink:0;text-align:right;}
.gr .vd{width:112px;flex-shrink:0;font-family:'DM Mono',monospace;font-size:11.5px;border-radius:6px;padding:4px 0;text-align:center;}
.vd.now{color:var(--ok);border:1px solid rgba(94,168,132,.4);}
.vd.warm{color:var(--kraft);border:1px solid rgba(212,162,127,.4);}
.vd.skip{color:var(--mut);border:1px solid var(--rule);}
.gr.top{background:linear-gradient(90deg,rgba(204,120,92,.1),transparent);}
.rail{width:252px;display:flex;flex-direction:column;gap:10px;}
.st{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:12px 15px;}
.st .v{font-size:34px;font-weight:900;color:var(--acc);letter-spacing:-1px;line-height:1;}
.st .k{margin-top:5px;font-size:13.5px;color:var(--ink70);line-height:1.2;}
.sig{background:var(--card);border:1px solid var(--rule);border-radius:12px;padding:12px 15px;flex:1;}
.sig .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:6px;}
.sig .r{font-size:13.5px;color:var(--ink70);padding:5px 0;border-top:1px solid var(--rule);line-height:1.25;}
.sig .r b{color:var(--ivory);}
"""
cos=[("Northwind","IT services · 34 ppl",86,"CALL NOW","now",1),("Globex","software · 22 ppl",81,"CALL NOW","now"),
("Initech","consulting · 41 ppl",74,"WARM","warm"),("Stark Labs","software · 12 ppl",70,"WARM","warm"),
("Umbrella","IT services · 48 ppl",63,"WARM","warm"),("Hooli","agency · 19 ppl",52,"NURTURE","skip"),
("Wayne Co","consulting · 26 ppl",41,"NURTURE","skip"),("Oscorp","hardware · 44 ppl",28,"SKIP","skip")]
grs="".join(f'<div class="gr{" top" if len(c)>5 else ""}"><span class="co">{c[0]}<small>{c[1]}</small></span><span class="bar"><i style="width:{c[2]}%"></i></span><span class="sc">{c[2]}</span><span class="vd {c[4]}">{c[3]}</span></div>' for c in cos)
main10=f'''<div class="grid"><div class="ghd"><span style="width:150px">Account</span><span style="flex:1">AI-readiness</span><span style="width:46px;text-align:right">Score</span><span style="width:112px;text-align:center">Verdict</span></div>{grs}</div>
<div class="rail">
<div class="st"><div class="v">40</div><div class="k">accounts scored in one run, 62 min</div></div>
<div class="st"><div class="v">2</div><div class="k">call-now targets I would have found in week 3</div></div>
<div class="sig"><div class="h">Signals in the score</div>
<div class="r">hiring for <b>ops / RevOps</b></div><div class="r">stack has <b>no AI layer</b></div>
<div class="r">founder posts about <b>scaling pain</b></div><div class="r">raised in last <b>18 months</b></div>
<div class="r">2-50 seats &middot; <b>ICP band</b></div></div>
</div>'''

POSTERS=[
 (1,BOOK, "HOW TO <em>&middot;</em> THE ROUTER <em>&middot;</em> ULTRON","USE CASE 01",
  "I ran <em>8 GTM jobs</em> from one chat box.",
  "No model menu, no agent picker. The <b>router</b> reads the job, hires the right agent, picks the tier. This is the actual table.",
  extra1,main1,"ROUTER","and I will send you the 8 exact commands + what each returns"),
 (2,KRAFT,"HOW TO <em>&middot;</em> ONE CONTEXT <em>&middot;</em> ULTRON","USE CASE 02",
  "I closed <em>six AI tabs.</em> One box replaced them.",
  "Six subscriptions, six logins, six dead contexts. The stack on the left is what I cancelled. Do the math with me.",
  extra2,main2,"TABS","and I will send you the migration map, tab by tab"),
 (3,BOOK, "HOW TO <em>&middot;</em> SOURCING <em>&middot;</em> ULTRON","USE CASE 03",
  "I sourced <em>200 founders</em> with the laptop closed.",
  "One sentence at 09:14. This is the unedited run trace of what happened in the next <b>47 minutes</b>.",
  extra3,main3,"SOURCE","and I will send you the exact sourcing sentence + the ICP filter"),
 (4,BDARK,"HOW TO <em>&middot;</em> THE BRAIN <em>&middot;</em> ULTRON","USE CASE 04",
  "I brief my AI <em>once.</em> It never asks twice.",
  "Every other chat starts from zero. The brain holds your business once and every agent recalls it on <b>every run</b>.",
  extra4,main4,"BRAIN","and I will send you the 7-item brief that seeds the brain"),
 (5,BOOK, "HOW TO <em>&middot;</em> THE AUDIT <em>&middot;</em> ULTRON","USE CASE 05",
  "I audited my <em>whole GTM</em> with one sentence.",
  "Three words in, a scored teardown of my real funnel out: 8 checks, a verdict each, and the exact fix.",
  extra5,main5,"AUDIT","and I will send you the audit sentence + the 8-check rubric"),
 (6,KRAFT,"HOW TO <em>&middot;</em> SENTINEL <em>&middot;</em> ULTRON","USE CASE 06",
  "I shipped a fix <em>before my coffee</em> went cold.",
  "Bug report at 08:02, merged PR at 08:17. Every step below is what SENTINEL did while I did nothing.",
  extra6,main6,"SHIP","and I will send you the bug-to-PR workflow, step by step"),
 (7,BDARK,"HOW TO <em>&middot;</em> THE GATE <em>&middot;</em> ULTRON","USE CASE 07",
  "I let AI write <em>240 emails.</em> I approved every one.",
  "Outbound at AI speed without AI accidents: everything queues at the human gate before a single send fires.",
  extra7,main7,"GATE","and I will send you the gated outbound setup + the approve flow"),
 (8,KRAFT,"HOW TO <em>&middot;</em> PROOF <em>&middot;</em> ULTRON","USE CASE 08",
  "I proved <em>3 weeks of research</em> in one link.",
  "No screenshot dumps. Every claim in the brief carries its source, its run ID and a confidence score.",
  extra8,main8,"PROOF","and I will send you the evidence-brief template"),
 (9,BOOK, "HOW TO <em>&middot;</em> RESUME <em>&middot;</em> ULTRON","USE CASE 09",
  "I reopened a <em>2-day-old session.</em> It lost nothing.",
  "Closed the laptop mid-negotiation on Monday. Typed two words on Wednesday. Here is the timeline.",
  extra9,main9,"RESUME","and I will send you the session workflow that never loses state"),
 (10,BDARK,"HOW TO <em>&middot;</em> AI-INDEX <em>&middot;</em> ULTRON","USE CASE 10",
  "I scored <em>40 companies</em> on AI-readiness in an hour.",
  "Stop guessing who is ready to buy. The index reads public signals and ranks your whole list, call-now first.",
  extra10,main10,"INDEX","and I will send you the AI-readiness rubric + the scoring run"),
]

if __name__=="__main__":
    for p in POSTERS: emit(*p)
