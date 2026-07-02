#!/usr/bin/env python3
# 10 LinkedIn posters v3 - design system lifted to the app.51ultron.com bar (operator: v2 = 3/10,
# "basic si monoton"). New language per analysis/design-upgrade-notes.md:
#   SOLID terracotta color-field cards + IVORY cards w/ dark text (pattern interrupts on dark),
#   display numerals 110-150px with warm blooms, white pill CTAs, real 3D logo strip (Vertex),
#   multi-accent per poster, richer gradient dark cards. 5 archetypes kept, form upgraded.
import os

BASE="""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>
@import 'https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700;9..40,800;9..40,900&family=DM+Mono:wght@400;500&display=swap';
:root{--slate:#161615;--ivory:#FAFAF7;--ink70:rgba(250,250,247,.72);--ink46:rgba(250,250,247,.46);
--rule:rgba(250,250,247,.09);--book:#CC785C;--bdark:#C84623;--kraft:#D4A27F;--ok:#5ea884;--mut:#8b857d;
--dark:#1a0f0a;}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#0b0b0a;display:flex;justify-content:center;padding:24px 0;font-family:'DM Sans',sans-serif;-webkit-font-smoothing:antialiased;color:var(--ivory);}
.frame{width:1080px;height:1450px;background:var(--slate);padding:30px 42px 20px;position:relative;overflow:hidden;display:flex;flex-direction:column;}
.frame::before{content:'';position:absolute;inset:0;pointer-events:none;z-index:0;background-image:radial-gradient(rgba(204,120,92,.055) 1.4px,transparent 1.5px);background-size:30px 30px;}
.atm{position:absolute;inset:0;pointer-events:none;z-index:1;
background:radial-gradient(ellipse 62% 26% at 88% -4%,rgba(200,70,35,.30) 0%,transparent 62%),
radial-gradient(ellipse 40% 20% at 4% 104%,rgba(212,162,127,.12) 0%,transparent 60%);}
.frame>*{position:relative;z-index:2;}
.mast{flex-shrink:0;display:flex;align-items:center;justify-content:space-between;padding-bottom:11px;border-bottom:1px solid var(--rule);font-family:'DM Mono',monospace;font-size:12px;font-weight:500;letter-spacing:.18em;text-transform:uppercase;}
.mast .ml{color:var(--ink46);}.mast .ml em{color:var(--book);font-style:normal;}.mast .mr{color:var(--ink70);}
.hook{margin-top:18px;font-weight:900;font-size:64px;line-height:.99;letter-spacing:-2.4px;flex-shrink:0;}
.hook em{color:var(--book);font-style:normal;text-shadow:0 0 44px rgba(204,120,92,.5);}
.sub{margin-top:12px;font-size:20px;font-weight:500;line-height:1.3;color:var(--ink70);flex-shrink:0;max-width:960px;}.sub b{color:var(--ivory);font-weight:700;}
.main{flex:1;min-height:0;margin-top:18px;display:flex;gap:14px;}
/* v3 components */
.solid{background:linear-gradient(160deg,#D0805F 0%,#C84623 78%);border-radius:20px;color:var(--ivory);box-shadow:0 24px 70px rgba(200,70,35,.35);}
.ivory{background:var(--ivory);border-radius:20px;color:#151210;box-shadow:0 24px 60px rgba(0,0,0,.5);}
.dcard{background:linear-gradient(180deg,#232321,#1b1b1a);border:1px solid rgba(250,250,247,.10);border-radius:18px;box-shadow:inset 0 1px 0 rgba(250,250,247,.07),0 14px 34px rgba(0,0,0,.35);}
.pill{display:inline-flex;align-items:center;gap:10px;background:var(--ivory);color:#151210;border-radius:999px;font-weight:800;box-shadow:0 8px 26px rgba(0,0,0,.4);}
.glow{position:relative;}
.glow::before{content:'';position:absolute;left:50%;top:50%;width:130%;height:130%;transform:translate(-50%,-50%);background:radial-gradient(closest-side,rgba(204,120,92,.28),transparent);z-index:-1;}
.cta{flex-shrink:0;margin-top:14px;display:flex;align-items:center;gap:18px;background:linear-gradient(160deg,#D0805F,#C84623);border-radius:18px;padding:15px 15px 15px 26px;box-shadow:0 20px 60px rgba(200,70,35,.35);}
.cta .ph{flex:1;font-size:22px;font-weight:700;color:rgba(255,252,248,.94);}.cta .ph b{color:#fff;font-weight:900;}
.cta .pl{background:var(--ivory);color:#151210;border-radius:999px;padding:13px 26px;font-weight:900;font-size:18px;flex-shrink:0;display:flex;align-items:center;gap:9px;}
.ftr{flex-shrink:0;margin-top:12px;padding-top:10px;border-top:1px solid var(--rule);display:flex;align-items:center;justify-content:space-between;}
.fl{display:flex;align-items:center;gap:11px;}.flogo{width:28px;height:28px;border-radius:50%;object-fit:cover;}
.ftx{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.13em;text-transform:uppercase;color:var(--ink70);}.ftx b{color:var(--ivory);font-weight:500;}
.furl{font-weight:900;font-size:20px;letter-spacing:-.5px;}.furl em{color:var(--book);font-style:normal;}
__EXTRA__
</style></head><body><div class="frame" id="artifact"><div class="atm"></div>
<div class="mast"><span class="ml">__MASTL__</span><span class="mr">__MASTR__</span></div>
<div class="hook">__HOOK__</div><div class="sub">__SUB__</div>
<div class="main">__MAIN__</div>
<div class="cta"><span class="ph">Comment <b>__KW__</b> __TAIL__</span><span class="pl">__KW__ <svg width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="#151210" stroke-width="3" stroke-linecap="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span></div>
<div class="ftr"><div class="fl"><img class="flogo" src="__LOGO__"><span class="ftx"><b>ULTRON</b> &middot; AI OPERATOR FOR FOUNDERS</span></div><span class="furl">51ultron<em>.</em>com</span></div>
</div></body></html>"""

def emit(n,mastl,mastr,hook,sub,extra,main,kw,tail):
    h=(BASE.replace("__MASTL__",mastl).replace("__MASTR__",mastr)
        .replace("__HOOK__",hook).replace("__SUB__",sub).replace("__EXTRA__",extra)
        .replace("__MAIN__",main).replace("__KW__",kw).replace("__TAIL__",tail))
    os.makedirs("content/howto2",exist_ok=True)
    open(f"content/howto2/li-{n:02d}.html","w").write(h); print("wrote",n)

# ================= P1 ROUTER - command table, terracotta header band, ivory focal =================
extra1="""
.tbl{flex:1;display:flex;flex-direction:column;border-radius:20px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.4);}
.thead{display:flex;background:linear-gradient(160deg,#D0805F,#C84623);font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:#fff;padding:14px 18px;gap:12px;font-weight:500;}
.tr{display:flex;align-items:center;gap:12px;padding:0 18px;flex:1;background:#1d1d1c;}
.tr:nth-child(odd){background:#212120;}
.c1{width:300px;font-family:'DM Mono',monospace;font-size:16.5px;color:var(--ivory);}.c1 i{color:var(--book);font-style:normal;}
.c2{width:136px;}.c2 span{display:inline-block;background:rgba(204,120,92,.16);border:1px solid rgba(204,120,92,.4);color:#E8A17F;border-radius:8px;padding:4px 10px;font-weight:800;font-size:14.5px;}
.c3{width:82px;font-family:'DM Mono',monospace;font-size:13px;color:var(--kraft);}
.c4{flex:1;font-size:15.5px;color:var(--ink70);line-height:1.22;}.c4 b{color:var(--ivory);}
.rail{width:240px;display:flex;flex-direction:column;gap:12px;}
.iv{padding:18px;display:flex;flex-direction:column;justify-content:center;}
.iv .v{font-size:96px;font-weight:900;letter-spacing:-5px;line-height:.9;color:#C84623;}
.iv .k{margin-top:8px;font-size:15px;font-weight:700;color:#3a332e;line-height:1.25;}
.sol{padding:16px 18px;}
.sol .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.75);margin-bottom:8px;}
.sol .row{display:flex;justify-content:space-between;font-size:15px;padding:6px 0;border-top:1px solid rgba(255,255,255,.22);color:rgba(255,252,248,.92);}
.sol .row b{font-family:'DM Mono',monospace;font-weight:500;color:#fff;}
.gate{flex:1;background:linear-gradient(180deg,rgba(94,168,132,.10),#1b1b1a);border:1px solid rgba(94,168,132,.4);border-radius:18px;padding:14px 16px;}
.gate .h{display:flex;align-items:center;gap:9px;font-size:16px;font-weight:800;}
.gate .h i{width:10px;height:10px;border-radius:50%;background:var(--ok);box-shadow:0 0 12px rgba(94,168,132,.9);}
.gate .d{margin-top:6px;font-size:13.5px;color:var(--ink70);line-height:1.3;}
"""
rows1=[("profile this founder","CORTEX","SMART","ranked brief, <b>40 signals</b>, 1 page"),
("write the cold sequence","SPECTER","SMART","<b>4-step</b> sequence, 62 words a step"),
("handle this objection","STRIKER","DEEP","rebuttal + <b>close plan</b>, deal-aware"),
("draft the launch post","PULSE","SMART","post <b>in your voice</b>, hook first"),
("fix the pricing page","SENTINEL","DEEP","patch + tests + <b>PR opened</b>"),
("schedule this everywhere","AMPLIFY","LITE","per channel, <b>per timezone</b>"),
("review this NDA","COUNSEL","DEEP","<b>risk flags</b> + redlines in minutes"),
("what changed today","ROUTER","LITE","one-line digest, <b>every agent</b>")]
trs="".join(f'<div class="tr"><div class="c1"><i>&gt;</i> {a}</div><div class="c2"><span>{b}</span></div><div class="c3">{c}</div><div class="c4">{d}</div></div>' for a,b,c,d in rows1)
main1=f'''<div class="tbl"><div class="thead"><span style="width:300px">You type</span><span style="width:136px">Routes to</span><span style="width:82px">Tier</span><span style="flex:1">What comes back</span></div>{trs}</div>
<div class="rail">
<div class="ivory iv glow"><span class="v">8</span><span class="k">jobs from one chat box. Zero picking.</span></div>
<div class="solid sol"><div class="h">The router picks the tier</div>
<div class="row"><span>Lite &middot; lookups</span><b>Haiku</b></div>
<div class="row"><span>Smart &middot; default</span><b>Sonnet</b></div>
<div class="row"><span>Deep &middot; judgement</span><b>Opus</b></div>
<div class="row"><span>You pay</span><b>cents</b></div></div>
<div class="gate"><div class="h"><i></i>Human gate</div><div class="d">Anything that sends waits for your yes. Every agent, every time.</div></div>
</div>'''

# ================= P2 TABS - real 3D logo strip + split =================
extra2="""
.wrap2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0;}
.strip{flex-shrink:0;height:238px;border-radius:20px;overflow:hidden;position:relative;box-shadow:0 24px 60px rgba(0,0,0,.5);}
.strip img{width:100%;height:100%;object-fit:cover;object-position:center 42%;}
.strip .prices{position:absolute;left:0;right:0;bottom:0;display:flex;background:linear-gradient(transparent,rgba(8,7,6,.88) 42%);padding:34px 26px 12px;}
.strip .prices span{flex:1;text-align:center;font-family:'DM Mono',monospace;font-size:15px;color:var(--ink70);}
.strip .prices span b{color:var(--ivory);font-weight:500;}
.duo{flex:1;display:flex;gap:14px;min-height:0;}
.dead{flex:1;display:flex;flex-direction:column;border-radius:18px;overflow:hidden;background:linear-gradient(180deg,#232321,#1b1b1a);border:1px solid var(--rule);}
.dead .hd{padding:12px 18px;font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--ink46);border-bottom:1px solid var(--rule);display:flex;justify-content:space-between;}
.dead .hd b{color:var(--mut);font-size:17px;font-family:'DM Sans',sans-serif;text-decoration:line-through;text-decoration-color:rgba(200,70,35,.75);text-decoration-thickness:3px;}
.dead .r{flex:1;display:flex;align-items:center;gap:11px;padding:0 18px;border-top:1px solid rgba(250,250,247,.05);font-size:15.5px;color:var(--mut);}
.dead .r i{color:var(--bdark);font-style:normal;font-weight:900;}
.one{flex:1.1;display:flex;flex-direction:column;}
.one .top{flex:1;background:var(--ivory);border-radius:20px 20px 0 0;padding:18px 20px;color:#151210;display:flex;flex-direction:column;justify-content:center;gap:9px;box-shadow:0 24px 60px rgba(0,0,0,.45);}
.one .top .t{font-size:24px;font-weight:900;letter-spacing:-.6px;}
.one .top .r{display:flex;gap:10px;align-items:center;font-size:15.5px;color:#40382f;font-weight:600;}
.one .top .r i{width:8px;height:8px;border-radius:50%;background:#C84623;flex-shrink:0;}
.one .bot{background:linear-gradient(160deg,#D0805F,#C84623);border-radius:0 0 20px 20px;padding:14px 20px;display:flex;align-items:baseline;justify-content:space-between;box-shadow:0 24px 60px rgba(200,70,35,.3);}
.one .bot .l{font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:rgba(255,255,255,.8);}
.one .bot .v{font-size:44px;font-weight:900;letter-spacing:-1.5px;color:#fff;}
"""
main2='''<div class="wrap2">
<div class="strip"><img src="../_hitl-src/covers/tabsrow.png"><div class="prices"><span>ChatGPT <b>$20</b></span><span>Claude <b>$20</b></span><span>Perplexity <b>$20</b></span><span>Jasper <b>$49</b></span><span>Midjourney <b>$10</b></span><span>Notion AI <b>$10</b></span></div></div>
<div class="duo">
<div class="dead"><div class="hd"><span>What six tabs cost</span><b>$129/mo</b></div>
<div class="r"><i>x</i>&nbsp;six logins, six histories, six bills</div>
<div class="r"><i>x</i>&nbsp;context dies inside every tab</div>
<div class="r"><i>x</i>&nbsp;you re-paste your ICP all day</div>
<div class="r"><i>x</i>&nbsp;answers, not finished work</div>
<div class="r"><i>x</i>&nbsp;you are the router between them</div></div>
<div class="one"><div class="top"><span class="t">One box. Seven agents.</span>
<span class="r"><i></i>one context: ICP, voice, pipeline, in every job</span>
<span class="r"><i></i>the router picks the model tier for you</span>
<span class="r"><i></i>research flows into outreach into deals</span>
<span class="r"><i></i>output = work done: briefs, sends, PRs</span></div>
<div class="bot"><span class="l">A day of work costs</span><span class="v">cents</span></div></div>
</div></div>'''

# ================= P3 SOURCE - run trace + ivory result =================
extra3="""
.term{flex:1;display:flex;flex-direction:column;border-radius:20px;background:#111110;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.5);border:1px solid rgba(250,250,247,.08);}
.tbar{display:flex;align-items:center;gap:8px;padding:12px 18px;background:#1c1c1b;border-bottom:1px solid var(--rule);}
.dot{width:11px;height:11px;border-radius:50%;}
.tbar .tt{margin-left:8px;font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.14em;color:var(--ink46);text-transform:uppercase;}
.cmd{flex-shrink:0;margin:12px 14px 4px;background:linear-gradient(160deg,#D0805F,#C84623);border-radius:12px;padding:11px 16px;font-family:'DM Mono',monospace;font-size:16px;color:#fff;box-shadow:0 10px 30px rgba(200,70,35,.35);}
.ln{flex:1;display:flex;align-items:center;gap:14px;padding:0 20px;font-family:'DM Mono',monospace;font-size:15.5px;}
.ts{color:var(--ink46);width:52px;flex-shrink:0;font-size:13px;}
.ag{width:92px;flex-shrink:0;font-weight:500;color:var(--book);}
.ms{color:var(--ink70);}.ms b{color:var(--ivory);font-weight:500;}.ms i{color:var(--kraft);font-style:normal;}
.ln.gate{background:linear-gradient(90deg,rgba(94,168,132,.12),transparent);}
.ln.gate .ag{color:var(--ok);} .ln.gate .ms b{color:var(--ok);}
.rail{width:252px;display:flex;flex-direction:column;gap:12px;}
.iv{padding:18px;display:flex;flex-direction:column;justify-content:center;}
.iv .v{font-size:104px;font-weight:900;letter-spacing:-6px;line-height:.9;color:#C84623;}
.iv .k{margin-top:8px;font-size:15px;font-weight:700;color:#3a332e;line-height:1.25;}
.sol{padding:15px 18px;}
.sol .v{font-size:46px;font-weight:900;color:#fff;letter-spacing:-1px;line-height:1;}
.sol .k{margin-top:5px;font-size:14px;color:rgba(255,252,248,.88);line-height:1.25;}
.icp{background:linear-gradient(180deg,#232321,#1b1b1a);border:1px solid var(--rule);border-radius:18px;padding:13px 16px;flex:1;}
.icp .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:7px;}
.icp .r{font-size:14.5px;color:var(--ink70);padding:5px 0;border-top:1px solid var(--rule);}.icp .r b{color:var(--ivory);}
"""
log=[("09:14","CORTEX","pulled <b>1,284</b> companies, IT services, US + UK"),
("09:16","CORTEX","deduped vs CRM: <i>902 net-new</i>"),
("09:19","CORTEX","enriched 902: funding, size, tech stack"),
("09:24","CORTEX","scored vs ICP: <b>471 pass</b> the 2-50 seat filter"),
("09:31","CORTEX","ranked: hiring + recent raise + intent signals"),
("09:33","CORTEX","top <b>200 exported</b> with 1-page briefs"),
("09:38","SPECTER","drafted <b>200 openers</b>, one trigger each, 62 words"),
("09:44","STRIKER","flagged 37 accounts as <i>deal-ready</i>"),
("09:45","AMPLIFY","queue set: 10:00 local, per timezone"),
("09:46","GATE","<b>240 sends on HOLD</b>, waiting for your approve",True),
("09:47","ROUTER","done in <b>47 min</b>. laptop closed for 46 of them")]
lns="".join(f'<div class="ln{" gate" if len(r)>3 else ""}"><span class="ts">{r[0]}</span><span class="ag">{r[1]}</span><span class="ms">{r[2]}</span></div>' for r in log)
main3=f'''<div class="term"><div class="tbar"><span class="dot" style="background:#e0654a"></span><span class="dot" style="background:#e0a54a"></span><span class="dot" style="background:#7fb98a"></span><span class="tt">ultron &middot; run trace &middot; this morning</span></div>
<div class="cmd">&gt; source 200 founders matching my ICP</div>{lns}</div>
<div class="rail">
<div class="ivory iv glow"><span class="v">200</span><span class="k">founders sourced, briefed, sequenced</span></div>
<div class="solid sol"><div class="v">47 min</div><div class="k">one sentence in, finished work out</div></div>
<div class="icp"><div class="h">The ICP it matched</div><div class="r"><b>Founder / CEO</b></div><div class="r"><b>2-50</b> employees</div><div class="r">IT services / software</div><div class="r"><b>US + UK</b></div></div>
</div>'''

# ================= P4 BRAIN - dead chats vs ivory brain =================
extra4="""
.dead{flex:1;display:flex;flex-direction:column;border-radius:18px;overflow:hidden;background:linear-gradient(180deg,#232321,#1b1b1a);border:1px solid var(--rule);}
.dead .hd{padding:13px 18px;font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--ink46);border-bottom:1px solid var(--rule);}
.pain{flex:1;display:flex;align-items:center;gap:12px;padding:0 18px;border-top:1px solid rgba(250,250,247,.05);}
.pain .x{font-size:16px;color:var(--mut);line-height:1.3;}.pain .x b{color:var(--ink70);}
.pain i{font-family:'DM Mono',monospace;color:var(--bdark);font-style:normal;font-weight:900;flex-shrink:0;}
.cost{flex-shrink:0;background:linear-gradient(160deg,#D0805F,#C84623);border-radius:0 0 18px 18px;padding:14px 18px;display:flex;align-items:baseline;justify-content:space-between;}
.cost .l{font-size:14.5px;color:rgba(255,255,255,.85);font-weight:600;}
.cost .v{font-size:34px;font-weight:900;color:#fff;letter-spacing:-1px;}
.brain{flex:1.25;display:flex;flex-direction:column;background:var(--ivory);border-radius:20px;overflow:hidden;color:#151210;box-shadow:0 28px 70px rgba(0,0,0,.5);}
.brain .hd{padding:14px 20px;border-bottom:2px solid #eee7de;display:flex;justify-content:space-between;align-items:center;}
.brain .hd .t{font-size:19px;font-weight:900;letter-spacing:-.4px;color:#C84623;}
.brain .hd .s{font-family:'DM Mono',monospace;font-size:11.5px;color:#8d8479;text-transform:uppercase;letter-spacing:.12em;}
.mem{flex:1;display:flex;align-items:center;justify-content:space-between;gap:10px;padding:0 20px;border-top:1px solid #eee7de;}
.mem .n{font-weight:800;font-size:17.5px;color:#151210;}.mem .d{font-size:13.5px;color:#6e655a;margin-top:2px;}
.mem .tag{font-family:'DM Mono',monospace;font-size:11.5px;color:#C84623;background:rgba(200,70,35,.09);border:1px solid rgba(200,70,35,.3);border-radius:7px;padding:4px 9px;flex-shrink:0;}
"""
pains=[('"So, my ICP is founders at 2-50..." <b>again</b>'),("15 minutes of context <b>every session</b>"),
("the voice sample, <b>re-pasted</b>"),("pricing tiers, <b>re-explained</b>"),("close the tab, <b>everything dies</b>")]
prow="".join(f'<div class="pain"><i>x</i><span class="x">{b}</span></div>' for b in pains)
mems=[("Your ICP","Founder/CEO, 2-50, IT services, US/UK","every agent"),("Pricing","Starter free, Max $19, Ent $297","STRIKER"),
("Voice sample","how you actually write","PULSE"),("Deal stages","your pipeline, your close plan","STRIKER"),
("Objection bank","what worked, what died","STRIKER"),("Brand system","colors, format, banned words","PULSE"),
("Tool wiring","CRM, mail, calendar, repo","all runs")]
mrow="".join(f'<div class="mem"><div><div class="n">{n}</div><div class="d">{d}</div></div><span class="tag">{t}</span></div>' for n,d,t in mems)
main4=f'''<div style="flex:1;display:flex;flex-direction:column;min-height:0"><div class="dead" style="border-radius:18px 18px 0 0"><div class="hd">Every other AI chat</div>{prow}</div>
<div class="cost"><span class="l">Cost of the goldfish memory</span><span class="v">15 min / session</span></div></div>
<div class="brain glow"><div class="hd"><span class="t">The Ultron brain</span><span class="s">briefed once &middot; recalled every run</span></div>{mrow}</div>'''

# ================= P5 AUDIT - giant ivory score + checks =================
extra5="""
.score{width:286px;display:flex;flex-direction:column;gap:12px;}
.big{padding:20px;display:flex;flex-direction:column;justify-content:center;}
.big .v{font-size:150px;font-weight:900;letter-spacing:-9px;color:#C84623;line-height:.85;}
.big .of{font-size:24px;color:#9b9084;font-weight:800;}
.big .k{margin-top:10px;font-size:15px;font-weight:700;color:#3a332e;line-height:1.3;}
.sent{padding:14px 17px;}
.sent .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.78);margin-bottom:7px;}
.sent .q{font-family:'DM Mono',monospace;font-size:17px;color:#fff;}
.leg{background:linear-gradient(180deg,#232321,#1b1b1a);border:1px solid var(--rule);border-radius:18px;padding:13px 16px;flex:1;}
.leg .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:6px;}
.leg .r{display:flex;align-items:center;gap:9px;font-size:14.5px;color:var(--ink70);padding:6px 0;}
.leg .sw{width:13px;height:13px;border-radius:4px;flex-shrink:0;}
.list{flex:1;display:flex;flex-direction:column;border-radius:20px;background:#1d1d1c;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.4);border:1px solid rgba(250,250,247,.08);}
.lhd{background:linear-gradient(160deg,#D0805F,#C84623);padding:13px 18px;font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.15em;text-transform:uppercase;color:#fff;font-weight:500;}
.li{flex:1;display:flex;align-items:center;gap:13px;padding:0 18px;border-top:1px solid rgba(250,250,247,.06);}
.li:nth-child(odd){background:#212120;}
.li .n{width:168px;font-weight:800;font-size:17px;}
.li .bar{width:150px;height:11px;border-radius:6px;background:rgba(250,250,247,.08);overflow:hidden;flex-shrink:0;}
.li .bar i{display:block;height:100%;border-radius:6px;background:linear-gradient(90deg,#D4A27F,#C84623);}
.li .sc{width:42px;font-family:'DM Mono',monospace;font-size:15px;color:var(--kraft);flex-shrink:0;}
.li .fx{flex:1;font-size:14.5px;color:var(--ink70);line-height:1.22;}.li .fx b{color:var(--ivory);}
.li .vd{flex-shrink:0;font-family:'DM Mono',monospace;font-size:11.5px;border-radius:999px;padding:5px 12px;font-weight:500;}
.vd.keep{color:#0f1a14;background:var(--ok);}
.vd.fix{color:#fff;background:#C84623;}
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
main5=f'''<div class="list"><div class="lhd">The 8 checks it ran on my real funnel</div>{lis}</div>
<div class="score">
<div class="solid sent"><div class="h">What I typed</div><div class="q">&gt; audit my GTM</div></div>
<div class="ivory big glow"><div><span class="v">61</span><span class="of">/100</span></div><div class="k">funnel score, computed from my live pipeline + send logs</div></div>
<div class="leg"><div class="h">Verdict spread</div>
<div class="r"><span class="sw" style="background:var(--ok)"></span>3 keep working</div>
<div class="r"><span class="sw" style="background:#C84623"></span>5 fix this week</div>
<div class="r"><span class="sw" style="background:rgba(250,250,247,.3)"></span>each with the exact fix</div></div>
</div>'''

# ================= P6 BUILDER - flow + ivory diff =================
extra6="""
.flow{flex:1.3;display:flex;flex-direction:column;}
.stage{flex:1;display:flex;gap:14px;}
.knob{width:46px;display:flex;flex-direction:column;align-items:center;flex-shrink:0;}
.knob .c{width:36px;height:36px;border-radius:50%;background:linear-gradient(160deg,#D0805F,#C84623);display:flex;align-items:center;justify-content:center;font-family:'DM Mono',monospace;font-size:15px;color:#fff;font-weight:500;flex-shrink:0;box-shadow:0 0 24px rgba(200,70,35,.5);}
.knob .l{flex:1;width:2px;background:linear-gradient(rgba(204,120,92,.5),rgba(204,120,92,.15));}
.stage:last-child .knob .l{display:none;}
.scard{flex:1;background:linear-gradient(180deg,#232321,#1b1b1a);border:1px solid var(--rule);border-radius:14px;padding:12px 18px;margin-bottom:10px;display:flex;align-items:center;justify-content:space-between;gap:10px;box-shadow:inset 0 1px 0 rgba(250,250,247,.06);}
.scard .t{font-weight:800;font-size:18px;}.scard .t small{display:block;font-weight:500;font-size:13.5px;color:var(--ink70);margin-top:3px;}
.scard .t small b{color:var(--ivory);}
.scard .ts{font-family:'DM Mono',monospace;font-size:12.5px;color:var(--ink46);flex-shrink:0;}
.scard.merge{background:linear-gradient(160deg,#D0805F,#C84623);border:none;box-shadow:0 16px 44px rgba(200,70,35,.35);}
.scard.merge .t{color:#fff;}.scard.merge .t small{color:rgba(255,252,248,.85);}.scard.merge .t small b{color:#fff;}
.scard.merge .ts{color:rgba(255,255,255,.7);}
.rail{width:258px;display:flex;flex-direction:column;gap:12px;}
.iv{padding:18px;}
.iv .v{font-size:88px;font-weight:900;letter-spacing:-4px;line-height:.9;color:#C84623;}
.iv .v small{font-size:30px;letter-spacing:-1px;}
.iv .k{margin-top:8px;font-size:15px;font-weight:700;color:#3a332e;line-height:1.25;}
.diff{background:#111110;border:1px solid rgba(250,250,247,.09);border-radius:16px;padding:14px 17px;font-family:'DM Mono',monospace;font-size:14.5px;}
.diff .h{font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:8px;}
.diff .a{color:var(--ok);}.diff .r{color:#E8845F;}.diff .m{color:var(--ink70);padding:3.5px 0;}
.note{background:linear-gradient(180deg,#232321,#1b1b1a);border:1px solid var(--rule);border-radius:16px;padding:13px 16px;flex:1;font-size:15px;color:var(--ink70);line-height:1.38;}
.note b{color:var(--ivory);}
"""
stages=[("1","I typed the bug",'"the pricing toggle is broken on mobile"',"08:02"),
("2","SENTINEL read the repo","12 files traced, root cause in <b>Toggle.tsx</b>","08:04"),
("3","Wrote the patch","+38 / -11 across 3 files, matches house style","08:09"),
("4","Ran the tests","<b>42 passed</b>, 0 failed, screenshot attached","08:12"),
("5","Opened the PR","#214 with summary, risk notes, rollback plan","08:14"),
("6","I merged it","the only click I made. <b>Human gate held.</b>","08:17",True)]
sts="".join(f'<div class="stage"><div class="knob"><span class="c">{s[0]}</span><span class="l"></span></div><div class="scard{" merge" if len(s)>4 else ""}"><span class="t">{s[1]}<small>{s[2]}</small></span><span class="ts">{s[3]}</span></div></div>' for s in stages)
main6=f'''<div class="flow">{sts}</div>
<div class="rail">
<div class="ivory iv glow"><div class="v">15<small>min</small></div><div class="k">bug report to merged PR, coffee still hot</div></div>
<div class="diff"><div class="h">PR #214 &middot; diff</div><div class="m"><span class="a">+38</span> additions</div><div class="m"><span class="r">-11</span> deletions</div><div class="m">3 files &middot; 42 tests</div><div class="m">risk: <span class="a">low</span></div></div>
<div class="note">I never opened the editor. SENTINEL ships like a senior dev and <b>waits at the gate</b> like a junior one.</div>
</div>'''

# ================= P7 GATE - pipeline + ivory gate card =================
extra7="""
.pipe{flex:1.3;display:flex;flex-direction:column;gap:10px;}
.seg{flex:1;background:linear-gradient(180deg,#232321,#1b1b1a);border:1px solid var(--rule);border-radius:14px;padding:12px 18px;display:flex;align-items:center;gap:14px;box-shadow:inset 0 1px 0 rgba(250,250,247,.06);}
.seg .n{font-family:'DM Mono',monospace;font-size:13px;color:var(--book);width:64px;flex-shrink:0;}
.seg .b{flex:1;}.seg .b .t{font-weight:800;font-size:18px;}.seg .b .d{font-size:14.5px;color:var(--ink70);margin-top:3px;line-height:1.26;}
.seg .b .d b{color:var(--ivory);}
.seg .num{font-weight:900;font-size:32px;color:var(--kraft);letter-spacing:-1px;flex-shrink:0;}
.seg.gate{background:var(--ivory);border:none;box-shadow:0 24px 60px rgba(0,0,0,.5);}
.seg.gate .n{color:#3f8f68;font-weight:500;}
.seg.gate .b .t{color:#151210;}.seg.gate .b .d{color:#5d554b;}.seg.gate .b .d b{color:#151210;}
.seg.gate .num{color:#C84623;}
.btns{display:flex;gap:8px;margin-top:8px;}
.btn{font-family:'DM Mono',monospace;font-size:12.5px;border-radius:999px;padding:6px 14px;font-weight:500;}
.btn.a{background:#2e7d54;color:#fff;box-shadow:0 6px 18px rgba(46,125,84,.4);}
.btn.h{border:1.5px solid #d8cfc4;color:#5d554b;}
.rail{width:252px;display:flex;flex-direction:column;gap:12px;}
.sol{padding:16px 18px;}
.sol .v{font-size:76px;font-weight:900;color:#fff;letter-spacing:-3px;line-height:.92;}
.sol .k{margin-top:7px;font-size:14.5px;color:rgba(255,252,248,.9);line-height:1.25;}
.iv{padding:16px 18px;}
.iv .v{font-size:76px;font-weight:900;letter-spacing:-3px;line-height:.92;color:#C84623;}
.iv .k{margin-top:7px;font-size:14.5px;font-weight:700;color:#3a332e;line-height:1.25;}
.mini{background:#111110;border:1px solid rgba(250,250,247,.09);border-radius:16px;padding:13px 16px;flex:1;}
.mini .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:8px;}
.mini .r{font-family:'DM Mono',monospace;font-size:13.5px;color:var(--ink70);padding:4.5px 0;border-top:1px solid rgba(250,250,247,.05);}
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
<div class="solid sol glow"><div class="v">240</div><div class="k">emails written and personalised by SPECTER</div></div>
<div class="ivory iv"><div class="v">1</div><div class="k">tap from me before anything moved</div></div>
<div class="mini"><div class="h">Why the gate matters</div><div class="r">tone drift &middot; <b>caught</b></div><div class="r">wrong tier CC'd &middot; <b>caught</b></div><div class="r">3 edits &middot; <b>2 min</b></div><div class="r">sent alone &middot; <b>0</b></div><div class="r">brand damage &middot; <b>0</b></div></div>
</div>'''

# ================= P8 PROOF - ledger + solid share card =================
extra8="""
.led{flex:1;display:flex;flex-direction:column;border-radius:20px;background:#1d1d1c;overflow:hidden;border:1px solid rgba(250,250,247,.08);box-shadow:0 20px 50px rgba(0,0,0,.4);}
.lhd{display:flex;background:#262625;padding:12px 18px;font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink46);gap:12px;}
.lr{flex:1;display:flex;align-items:center;gap:12px;padding:0 18px;border-top:1px solid rgba(250,250,247,.06);}
.lr:nth-child(odd){background:#212120;}
.lr .cl{flex:1;font-size:15.5px;color:var(--ivory);line-height:1.22;}.lr .cl b{color:var(--kraft);}
.lr .src{width:238px;font-family:'DM Mono',monospace;font-size:12.5px;color:var(--ink70);flex-shrink:0;}
.lr .cf{width:70px;flex-shrink:0;}
.lr .cf span{font-family:'DM Mono',monospace;font-size:12px;color:#0f1a14;background:var(--ok);border-radius:999px;padding:3px 9px;font-weight:500;}
.share{width:270px;display:flex;flex-direction:column;gap:12px;}
.iv{padding:18px;}
.iv .v{font-size:104px;font-weight:900;letter-spacing:-6px;line-height:.88;color:#C84623;}
.iv .k{margin-top:8px;font-size:15px;font-weight:700;color:#3a332e;line-height:1.28;}
.link{padding:16px 18px;}
.link .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.78);margin-bottom:9px;}
.link .u{font-family:'DM Mono',monospace;font-size:14.5px;color:#fff;word-break:break-all;line-height:1.4;background:rgba(0,0,0,.22);border-radius:9px;padding:9px 11px;}
.link .d{margin-top:9px;font-size:13.5px;color:rgba(255,252,248,.9);line-height:1.32;}.link .d b{color:#fff;}
.card8{background:linear-gradient(180deg,#232321,#1b1b1a);border:1px solid var(--rule);border-radius:16px;padding:13px 16px;flex:1;}
.card8 .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:6px;}
.card8 .v{font-size:38px;font-weight:900;color:var(--book);letter-spacing:-1px;line-height:1;}
.card8 .k{margin-top:5px;font-size:13.5px;color:var(--ink70);line-height:1.25;}
"""
claims=[('"US + UK founders reply <b>3.1x</b> more at 10:00 local"',"send logs &middot; n=2,140","98%"),
('"One-trigger openers beat templates <b>4.4x</b>"',"201 A/B sends &middot; 10 days","96%"),
('"62-word emails book the most calls"',"winner set &middot; n=7","91%"),
('"31% of my pipe was outside ICP"',"CRM scan &middot; 214 deals","99%"),
('"Follow-up 2 wins 58% of the meetings"',"thread analysis &middot; 90d","94%"),
('"Warm domains inbox at <b>99.2%</b>"',"4-domain ramp &middot; 6 wks","97%"),
('"Stale deals die after day 34"',"cohort decay curve","89%"),
('"Deep tier only pays off on objections"',"cost per close &middot; 60d","92%")]
lrs="".join(f'<div class="lr"><span class="cl">{c}</span><span class="src">{s}</span><span class="cf"><span>{cf}</span></span></div>' for c,s,cf in claims)
main8=f'''<div class="led"><div class="lhd"><span style="flex:1">Claim in the brief</span><span style="width:238px">Backed by</span><span style="width:70px">Conf.</span></div>{lrs}</div>
<div class="share">
<div class="ivory iv glow"><span class="v">1</span><div class="k">live link instead of 30 screenshots. Every number clicks to its source run.</div></div>
<div class="solid link"><div class="h">Shared with my co-founder</div><div class="u">work.51ultron.com/brief/q3-outbound</div><div class="d">He challenged claim 4. The link settled it in <b>one click</b>.</div></div>
<div class="card8"><div class="h">In the brief</div><div class="v">40</div><div class="k">sources cited across 8 claims, stamped with run IDs</div></div>
</div>'''

# ================= P9 RESUME - timeline + ivory resume card =================
extra9="""
.tl{flex:1.35;display:flex;flex-direction:column;gap:9px;}
.day{font-family:'DM Mono',monospace;font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink46);padding:1px 2px;}
.ev{flex:1;background:linear-gradient(180deg,#232321,#1b1b1a);border:1px solid var(--rule);border-radius:12px;padding:10px 16px;display:flex;align-items:center;gap:13px;}
.ev .ts{font-family:'DM Mono',monospace;font-size:12.5px;color:var(--ink46);width:52px;flex-shrink:0;}
.ev .x{font-size:15.5px;color:var(--ink70);line-height:1.25;}.ev .x b{color:var(--ivory);}
.gap{flex-shrink:0;display:flex;align-items:center;gap:12px;padding:5px 2px;}
.gap .l{flex:1;border-top:2px dashed rgba(204,120,92,.45);}
.gap .t{font-family:'DM Mono',monospace;font-size:12.5px;color:var(--book);letter-spacing:.14em;background:rgba(204,120,92,.1);border:1px solid rgba(204,120,92,.35);border-radius:999px;padding:5px 13px;}
.ev.hot{background:var(--ivory);border:none;box-shadow:0 18px 46px rgba(0,0,0,.45);}
.ev.hot .ts{color:#a5613f;}.ev.hot .x{color:#3f382f;}.ev.hot .x b{color:#151210;}
.rail{width:258px;display:flex;flex-direction:column;gap:12px;}
.iv{padding:18px;}
.iv .v{font-size:130px;font-weight:900;letter-spacing:-8px;line-height:.85;color:#C84623;}
.iv .k{margin-top:9px;font-size:15px;font-weight:700;color:#3a332e;line-height:1.28;}
.sol{padding:15px 18px;}
.sol .v{font-size:44px;font-weight:900;color:#fff;letter-spacing:-1px;line-height:1;}
.sol .k{margin-top:5px;font-size:14px;color:rgba(255,252,248,.9);line-height:1.25;}
.keep{background:linear-gradient(180deg,#232321,#1b1b1a);border:1px solid var(--rule);border-radius:16px;padding:13px 16px;flex:1;}
.keep .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:6px;}
.keep .r{display:flex;gap:9px;align-items:center;font-size:14.5px;color:var(--ink70);padding:5px 0;border-top:1px solid var(--rule);}
.keep .r i{width:7px;height:7px;border-radius:50%;background:var(--book);flex-shrink:0;}
.keep .r b{color:var(--ivory);}
"""
mon=[("14:05","kicked off the Northwind deal: CORTEX brief, <b>40 signals</b>"),
("14:31","SPECTER opener v1-v3, picked v3, <b>62 words</b>"),
("15:02","STRIKER close plan drafted, champion = Sarah"),
("15:40",'objection thread started: "too expensive vs in-house"'),
("16:12","laptop closed <b>mid-negotiation</b>, draft v3 open")]
wed=[("09:01",'typed <b>"resume northwind"</b>. one line.',1),
("09:01","it recalled: stage, champion, v3 draft, the open objection",1),
("09:03","STRIKER finished the rebuttal <b>from where it stopped</b>"),
("09:11","proposal out. <b>Zero re-briefing, zero scrolling up.</b>")]
tl='<div class="day">Monday</div>'+"".join(f'<div class="ev"><span class="ts">{a}</span><span class="x">{b}</span></div>' for a,b in mon)
tl+='<div class="gap"><span class="l"></span><span class="t">2 DAYS AWAY</span><span class="l"></span></div>'
tl+='<div class="day">Wednesday</div>'+"".join(f'<div class="ev{" hot" if len(e)>2 else ""}"><span class="ts">{e[0]}</span><span class="x">{e[1]}</span></div>' for e in wed)
main9=f'''<div class="tl">{tl}</div>
<div class="rail">
<div class="ivory iv glow"><span class="v">0</span><div class="k">minutes re-explaining where we were</div></div>
<div class="solid sol"><div class="v">10 min</div><div class="k">from reopen to proposal sent</div></div>
<div class="keep"><div class="h">What carried over</div>
<div class="r"><i></i>deal stage + <b>champion</b></div><div class="r"><i></i>draft <b>v3</b>, not v1</div>
<div class="r"><i></i>the open <b>objection</b></div><div class="r"><i></i>pricing already quoted</div>
<div class="r"><i></i>next step queue</div></div>
</div>'''

# ================= P10 INDEX - grid, ivory top row =================
extra10="""
.grid{flex:1;display:flex;flex-direction:column;border-radius:20px;background:#1d1d1c;overflow:hidden;border:1px solid rgba(250,250,247,.08);box-shadow:0 20px 50px rgba(0,0,0,.4);}
.ghd{display:flex;background:linear-gradient(160deg,#D0805F,#C84623);padding:12px 18px;font-family:'DM Mono',monospace;font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:#fff;gap:12px;font-weight:500;}
.gr{flex:1;display:flex;align-items:center;gap:12px;padding:0 18px;border-top:1px solid rgba(250,250,247,.06);}
.gr:nth-child(odd){background:#212120;}
.gr .co{width:150px;font-weight:800;font-size:16.5px;flex-shrink:0;}
.gr .co small{display:block;font-weight:500;font-size:12px;color:var(--ink46);font-family:'DM Mono',monospace;margin-top:2px;}
.gr .bar{flex:1;height:12px;border-radius:6px;background:rgba(250,250,247,.08);overflow:hidden;}
.gr .bar i{display:block;height:100%;border-radius:6px;background:linear-gradient(90deg,#D4A27F,#C84623);}
.gr .sc{width:46px;font-family:'DM Mono',monospace;font-size:15px;color:var(--kraft);flex-shrink:0;text-align:right;}
.gr .vd{width:110px;flex-shrink:0;font-family:'DM Mono',monospace;font-size:11.5px;border-radius:999px;padding:5px 0;text-align:center;font-weight:500;}
.vd.now{color:#0f1a14;background:var(--ok);}
.vd.warm{color:#151210;background:var(--kraft);}
.vd.skip{color:var(--mut);border:1px solid var(--rule);}
.gr.top{background:var(--ivory);}
.gr.top .co{color:#151210;}.gr.top .co small{color:#8d8479;}
.gr.top .bar{background:#e9e2d8;}.gr.top .sc{color:#a5613f;}
.rail{width:256px;display:flex;flex-direction:column;gap:12px;}
.iv{padding:18px;}
.iv .v{font-size:104px;font-weight:900;letter-spacing:-6px;line-height:.88;color:#C84623;}
.iv .k{margin-top:8px;font-size:15px;font-weight:700;color:#3a332e;line-height:1.28;}
.sol{padding:15px 18px;}
.sol .v{font-size:56px;font-weight:900;color:#fff;letter-spacing:-2px;line-height:.95;}
.sol .k{margin-top:6px;font-size:14px;color:rgba(255,252,248,.9);line-height:1.25;}
.sig{background:linear-gradient(180deg,#232321,#1b1b1a);border:1px solid var(--rule);border-radius:16px;padding:13px 16px;flex:1;}
.sig .h{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink46);margin-bottom:6px;}
.sig .r{font-size:13.5px;color:var(--ink70);padding:5px 0;border-top:1px solid var(--rule);line-height:1.25;}
.sig .r b{color:var(--ivory);}
"""
cos=[("Northwind","IT services · 34 ppl",86,"CALL NOW","now",1),("Globex","software · 22 ppl",81,"CALL NOW","now"),
("Initech","consulting · 41 ppl",74,"WARM","warm"),("Stark Labs","software · 12 ppl",70,"WARM","warm"),
("Umbrella","IT services · 48 ppl",63,"WARM","warm"),("Hooli","agency · 19 ppl",52,"NURTURE","skip"),
("Wayne Co","consulting · 26 ppl",41,"NURTURE","skip"),("Oscorp","hardware · 44 ppl",28,"SKIP","skip")]
grs="".join(f'<div class="gr{" top" if len(c)>5 else ""}"><span class="co">{c[0]}<small>{c[1]}</small></span><span class="bar"><i style="width:{c[2]}%"></i></span><span class="sc">{c[2]}</span><span class="vd {c[4]}">{c[3]}</span></div>' for c in cos)
main10=f'''<div class="grid"><div class="ghd"><span style="width:150px">Account</span><span style="flex:1">AI-readiness</span><span style="width:46px;text-align:right">Score</span><span style="width:110px;text-align:center">Verdict</span></div>{grs}</div>
<div class="rail">
<div class="ivory iv glow"><span class="v">40</span><div class="k">accounts scored in one run, 62 minutes</div></div>
<div class="solid sol"><div class="v">2</div><div class="k">call-now targets I would have found in week 3</div></div>
<div class="sig"><div class="h">Signals in the score</div>
<div class="r">hiring for <b>ops / RevOps</b></div><div class="r">stack has <b>no AI layer</b></div>
<div class="r">founder posts about <b>scaling pain</b></div><div class="r">raised in last <b>18 months</b></div>
<div class="r">2-50 seats &middot; <b>ICP band</b></div></div>
</div>'''

POSTERS=[
 (1,"HOW TO <em>&middot;</em> THE ROUTER <em>&middot;</em> ULTRON","USE CASE 01",
  "I ran <em>8 GTM jobs</em> from one chat box.",
  "No model menu, no agent picker. The <b>router</b> reads the job, hires the right agent, picks the tier. This is the actual table.",
  extra1,main1,"ROUTER","and I will send you the 8 exact commands + what each returns"),
 (2,"HOW TO <em>&middot;</em> ONE CONTEXT <em>&middot;</em> ULTRON","USE CASE 02",
  "I closed <em>six AI tabs.</em> One box replaced them.",
  "Six subscriptions, six logins, six dead contexts. The row below is what I cancelled last month.",
  extra2,main2,"TABS","and I will send you the migration map, tab by tab"),
 (3,"HOW TO <em>&middot;</em> SOURCING <em>&middot;</em> ULTRON","USE CASE 03",
  "I sourced <em>200 founders</em> with the laptop closed.",
  "One sentence at 09:14. This is the unedited run trace of the next <b>47 minutes</b>.",
  extra3,main3,"SOURCE","and I will send you the exact sourcing sentence + the ICP filter"),
 (4,"HOW TO <em>&middot;</em> THE BRAIN <em>&middot;</em> ULTRON","USE CASE 04",
  "I brief my AI <em>once.</em> It never asks twice.",
  "Every other chat starts from zero. The brain holds your business once and every agent recalls it on <b>every run</b>.",
  extra4,main4,"BRAIN","and I will send you the 7-item brief that seeds the brain"),
 (5,"HOW TO <em>&middot;</em> THE AUDIT <em>&middot;</em> ULTRON","USE CASE 05",
  "I audited my <em>whole GTM</em> with one sentence.",
  "Three words in, a scored teardown of my real funnel out: 8 checks, a verdict each, and the exact fix.",
  extra5,main5,"AUDIT","and I will send you the audit sentence + the 8-check rubric"),
 (6,"HOW TO <em>&middot;</em> SENTINEL <em>&middot;</em> ULTRON","USE CASE 06",
  "I shipped a fix <em>before my coffee</em> went cold.",
  "Bug report at 08:02, merged PR at 08:17. Every step below is what SENTINEL did while I did nothing.",
  extra6,main6,"SHIP","and I will send you the bug-to-PR workflow, step by step"),
 (7,"HOW TO <em>&middot;</em> THE GATE <em>&middot;</em> ULTRON","USE CASE 07",
  "I let AI write <em>240 emails.</em> I approved every one.",
  "Outbound at AI speed without AI accidents: everything queues at the human gate before a single send fires.",
  extra7,main7,"GATE","and I will send you the gated outbound setup + the approve flow"),
 (8,"HOW TO <em>&middot;</em> PROOF <em>&middot;</em> ULTRON","USE CASE 08",
  "I proved <em>3 weeks of research</em> in one link.",
  "No screenshot dumps. Every claim in the brief carries its source, its run ID and a confidence score.",
  extra8,main8,"PROOF","and I will send you the evidence-brief template"),
 (9,"HOW TO <em>&middot;</em> RESUME <em>&middot;</em> ULTRON","USE CASE 09",
  "I reopened a <em>2-day-old session.</em> It lost nothing.",
  "Closed the laptop mid-negotiation on Monday. Typed two words on Wednesday. Here is the timeline.",
  extra9,main9,"RESUME","and I will send you the session workflow that never loses state"),
 (10,"HOW TO <em>&middot;</em> AI-INDEX <em>&middot;</em> ULTRON","USE CASE 10",
  "I scored <em>40 companies</em> on AI-readiness in an hour.",
  "Stop guessing who is ready to buy. The index reads public signals and ranks your whole list, call-now first.",
  extra10,main10,"INDEX","and I will send you the AI-readiness rubric + the scoring run"),
]

if __name__=="__main__":
    for p in POSTERS: emit(*p)
