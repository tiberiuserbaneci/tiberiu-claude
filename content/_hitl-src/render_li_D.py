#!/usr/bin/env python3
# LinkedIn v4 FORMATS D+E from the second reference batch:
#  D LADDER (ref: "THE CLAUDE CODE LADDER") - stacked bands, colored level tile, bold-lead numbered
#    micro-bullets w/ inline mono chips, ghosted mini-diagram right.  -> li-07 (the outbound gate)
#  E STEP-GRID (ref: "How to build a course with Claude") - 3x3 numbered cards each with mini-bullets
#    + a PASTE-THIS prompt box (dark, mono, send arrow), black 4-step band at bottom. -> li-10 (AI-index)
import os

# ============================ D: LADDER (li-07) ============================
CSS_D="""
@import 'https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700;9..40,800;9..40,900&family=DM+Mono:wght@400;500&display=swap';
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#d9d2c4;display:flex;justify-content:center;padding:24px 0;font-family:'DM Sans',sans-serif;-webkit-font-smoothing:antialiased;color:#17150F;}
.frame{width:1080px;height:1450px;background:#F6F1E7;position:relative;overflow:hidden;display:flex;flex-direction:column;padding:26px 40px 0;}
.frame::before{content:'';position:absolute;inset:0;pointer-events:none;background-image:linear-gradient(rgba(23,21,15,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(23,21,15,.045) 1px,transparent 1px);background-size:40px 40px;}
.frame>*{position:relative;}
.hdr{flex-shrink:0;display:flex;align-items:center;gap:16px;justify-content:center;}
.hdr img{width:56px;height:56px;border-radius:13px;}
.hdr .t{font-weight:900;font-size:49px;letter-spacing:-1.8px;}
.hdr .t em{font-style:normal;color:#A85B38;}
.sub{flex-shrink:0;text-align:center;margin-top:6px;font-size:18px;font-weight:600;color:#5d564a;}
.sub b{color:#17150F;}
.band{flex:1;min-height:0;margin-top:13px;background:#FDFAF3;border:2px solid #17150F;border-radius:16px;box-shadow:0 4px 0 rgba(23,21,15,.16);display:flex;gap:16px;padding:13px 16px;}
.lvl{flex-shrink:0;width:86px;border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;border:2px solid #17150F;}
.lvl .a{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:.1em;}
.lvl .n{font-weight:900;font-size:38px;line-height:1;}
.bmain{flex:1;min-width:0;display:flex;flex-direction:column;justify-content:center;}
.brow{display:flex;align-items:center;gap:10px;}
.brow .bt{font-weight:900;font-size:24px;letter-spacing:-.5px;}
.brow .chipc{font-family:'DM Mono',monospace;font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:#fff;border-radius:999px;padding:3.5px 11px;font-weight:500;}
.bi{display:flex;gap:8px;align-items:flex-start;margin-top:5.5px;font-size:14px;color:#57503f;line-height:1.3;}
.bi b{color:#17150F;}
.bi .d{flex-shrink:0;width:17px;height:17px;border-radius:50%;color:#fff;font-size:10.5px;font-weight:900;display:flex;align-items:center;justify-content:center;margin-top:1.5px;}
.bi code{font-family:'DM Mono',monospace;font-size:12.5px;background:#F0E9DA;border:1px solid #d8cdb8;border-radius:5px;padding:1px 7px;}
.ghost{flex-shrink:0;width:210px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:7px;opacity:.65;}
.gp{font-family:'DM Mono',monospace;font-size:11.5px;color:#8d8371;background:#F0E9DA;border:1.5px solid #d8cdb8;border-radius:8px;padding:5px 14px;white-space:nowrap;}
.gp.hot{color:#fff;background:var(--gc);border-color:var(--gc);opacity:1;}
.garr{width:2px;height:9px;background:#c4b89f;}
.ctab{flex-shrink:0;margin:12px 0 0;background:#211F1A;border-radius:14px;display:flex;align-items:center;justify-content:space-between;padding:12px 20px;box-shadow:0 3px 0 rgba(23,21,15,.18);}
.ctab .l{font-size:18px;font-weight:700;color:#F7F1E6;}.ctab .l b{color:#E5A183;font-weight:900;}
.ctab .r{background:#F7F1E6;color:#17150F;border-radius:999px;padding:8px 18px;font-weight:900;font-size:15px;}
.ftr{flex-shrink:0;height:48px;margin:11px -40px 0;background:#17150F;display:flex;align-items:center;justify-content:center;gap:12px;color:#F6F1E7;}
.ftr img{width:26px;height:26px;border-radius:50%;}
.ftr .a{font-weight:900;font-size:15.5px;}.ftr .b{font-size:14.5px;color:rgba(246,241,231,.6);}
.ftr .kw{font-family:'DM Mono',monospace;font-size:13px;color:#E8A17F;}
"""
def bi(c,i,txt): return f'<div class="bi"><span class="d" style="background:{c}">{i}</span><span>{txt}</span></div>'
def band(color,tile_a,tile_n,title,chip,bullets,ghost):
    gh="".join((f'<span class="gp{" hot" if g[1] else ""}" style="--gc:{color}">{g[0]}</span>' if isinstance(g,tuple) else f'<span class="garr"></span>') for g in ghost)
    bl="".join(bi(color,i+1,b) for i,b in enumerate(bullets))
    tilefg="#fff" if color!="#D4A27F" else "#211505"
    return (f'<div class="band"><div class="lvl" style="background:{color};color:{tilefg}"><span class="a">{tile_a}</span><span class="n">{tile_n}</span></div>'
            f'<div class="bmain"><div class="brow"><span class="bt">{title}</span><span class="chipc" style="background:{color};{"color:#211505" if color=="#D4A27F" else ""}">{chip}</span></div>{bl}</div>'
            f'<div class="ghost">{gh}</div></div>')

def emit_ladder():
    T="#B4693F"; B="#C08A6C"; K="#CDB392"; G="#3f7d5c"; BK="#211F1A"
    bands=(
     band(BK,"STEP","5","Replies route back","AFTER THE SEND",
      ["<b>STRIKER takes every reply.</b> Qualify, objection, book the call.",
       "<b>You read a digest</b>, not an inbox. Hot threads flagged first.",
       "Every send logged with <code>run id</code>. The loop is auditable."],
      [("reply",0),"",("STRIKER",1),"",("booked call",0)])
    +band(G,"STEP","4","THE GATE: your tap","THE WHOLE TRICK",
      ["<b>All 240 park on HOLD.</b> Nothing external ever fires alone.",
       "<b>Read 12, spot-check the rest</b>, one tap: <code>approve all</code> &middot; <code>hold</code> &middot; <code>edit 3</code>.",
       "It caught <b>tone drift on 3</b>, a wrong CC and a broken merge field."],
      [("240 on HOLD",1),"",("your tap",0),"",("released",0)])
    +band(K,"STEP","3","Queue the sends","RAMPED, NOT BLASTED",
      ["<b>10:00 local time</b> per prospect, spread over 4 days.",
       "<b>Warm domains only.</b> The ramp keeps you at <b>99.2% inboxed</b>.",
       "AMPLIFY owns the calendar: <code>/amplify schedule</code>."],
      [("Mon 60",0),"",("Tue 60",0),"",("10:00 local",1)])
    +band(B,"STEP","2","Personalise each","NO MERGE SMELL",
      ["<b>One trigger per email</b>, pulled from the account brief.",
       "Company signal + role pain, <b>62 words a step</b>.",
       "Winners carry a trigger. Templates carry adjectives."],
      [("brief",0),"",("trigger",1),"",("62 words",0)])
    +band(T,"STEP","1","SPECTER writes 240","09:38 THIS MORNING",
      ["<b>4-step sequence</b> per account, drafted from one sentence.",
       "You typed: <code>&gt; run outbound on the 200 list</code>.",
       "Drafts, not sends. <b>Everything waits at step 4.</b>"],
      [("one sentence",0),"",("SPECTER",1),"",("240 drafts",0)]))
    html=f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>{CSS_D}</style></head><body>
<div class="frame" id="artifact">
<div class="hdr"><img src="__LOGO__"><span class="t">AI wrote 240 emails. <em>Zero</em> left alone.</span></div>
<div class="sub">The outbound gate ladder: five steps, <b>one human tap</b>, zero accidents. Save it.</div>
{bands}
<div class="ctab"><span class="l">Comment <b>GATE</b> and I will DM you the gated outbound setup + the architecture doc</span><span class="r">GATE &rarr;</span></div>
<div class="ftr"><img src="__LOGO__"><span class="a">ULTRON</span><span class="b">&middot; 51ultron.com &middot;</span><span class="kw">PINPOINT: app.51ultron.com/docs/architecture</span></div>
</div></body></html>"""
    open("content/howto2/li-07.html","w").write(html); print("wrote li-07 (ladder)")

# ============================ E: STEP-GRID (li-10) ============================
CSS_E="""
@import 'https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700;9..40,800;9..40,900&family=DM+Mono:wght@400;500&display=swap';
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#d9d2c4;display:flex;justify-content:center;padding:24px 0;font-family:'DM Sans',sans-serif;-webkit-font-smoothing:antialiased;color:#17150F;}
.frame{width:1080px;height:1450px;background:#F6F1E7;position:relative;overflow:hidden;display:flex;flex-direction:column;padding:28px 36px 0;}
.frame::before{content:'';position:absolute;inset:0;pointer-events:none;background-image:linear-gradient(rgba(23,21,15,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(23,21,15,.045) 1px,transparent 1px);background-size:40px 40px;}
.frame>*{position:relative;}
.hdr{flex-shrink:0;display:flex;align-items:center;gap:14px;}
.hdr svg{width:50px;height:50px;flex-shrink:0;}
.hdr .t{font-weight:900;font-size:46px;letter-spacing:-1.8px;}
.hdr .t em{font-style:normal;color:#A85B38;}
.sub{flex-shrink:0;margin:5px 0 0 64px;font-size:17.5px;font-weight:600;color:#5d564a;}
.sub b{background:#EED9A3;padding:1px 7px;border-radius:5px;color:#17150F;}
.gridw{flex:1;min-height:0;margin-top:12px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:11px;}
.cell{background:#FDFAF3;border:1.5px solid #d8cdb8;border-radius:14px;padding:11px 13px;display:flex;flex-direction:column;box-shadow:0 3px 0 rgba(23,21,15,.08);}
.cell .top{display:flex;align-items:center;gap:8px;}
.cell .num{width:25px;height:25px;border-radius:50%;color:#fff;font-weight:900;font-size:14px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.cell .tt{font-weight:900;font-size:17.5px;letter-spacing:-.3px;}
.mb{display:flex;gap:7px;align-items:flex-start;margin-top:5px;font-size:12.5px;color:#57503f;line-height:1.28;}
.mb b{color:#17150F;}
.mb .d{flex-shrink:0;width:15px;height:15px;border-radius:50%;background:#e5dbc6;color:#57503f;font-size:9.5px;font-weight:900;display:flex;align-items:center;justify-content:center;margin-top:1px;}
.pb{margin-top:auto;background:#1B1A16;border-radius:9px;padding:8px 10px;display:flex;gap:8px;align-items:flex-start;}
.pb .c{flex:1;font-family:'DM Mono',monospace;font-size:11px;line-height:1.42;color:#E8D9C4;}
.pb .c i{color:#E8845F;font-style:normal;}
.pb .go{width:20px;height:20px;border-radius:50%;background:#A85B38;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:1px;}
.pb .go svg{width:10px;height:10px;stroke:#fff;stroke-width:3;fill:none;stroke-linecap:round;}
.pbl{font-family:'DM Mono',monospace;font-size:9.5px;letter-spacing:.12em;color:#a5613f;text-transform:uppercase;margin:7px 0 3px;}
.band9{flex-shrink:0;margin-top:12px;background:#17150F;border-radius:14px;padding:12px 16px;display:flex;align-items:center;gap:12px;color:#F6F1E7;}
.band9 .n9{width:26px;height:26px;border-radius:50%;background:#A85B38;color:#fff;font-weight:900;font-size:14px;display:flex;align-items:center;justify-content:center;flex-shrink:0;}
.band9 .t9{font-weight:900;font-size:16.5px;flex-shrink:0;}
.b9s{flex:1;display:flex;align-items:center;gap:8px;}
.b9c{flex:1;background:#242219;border:1px solid rgba(246,241,231,.14);border-radius:9px;padding:6px 10px;}
.b9c .k{font-family:'DM Mono',monospace;font-size:9px;letter-spacing:.13em;color:#E8A17F;text-transform:uppercase;}
.b9c .v{font-size:12px;color:rgba(246,241,231,.8);margin-top:1px;}
.b9a{flex-shrink:0;color:#8d8371;font-weight:900;}
.ctab{flex-shrink:0;margin:11px 0 0;background:#211F1A;border-radius:14px;display:flex;align-items:center;justify-content:space-between;padding:12px 20px;box-shadow:0 3px 0 rgba(23,21,15,.18);}
.ctab .l{font-size:18px;font-weight:700;color:#F7F1E6;}.ctab .l b{color:#E5A183;font-weight:900;}
.ctab .r{background:#F7F1E6;color:#17150F;border-radius:999px;padding:8px 18px;font-weight:900;font-size:15px;}
.ftr{flex-shrink:0;height:46px;margin:10px -36px 0;background:#F6F1E7;border-top:2px solid #17150F;display:flex;align-items:center;justify-content:space-between;padding:0 56px;}
.ftr .l{font-size:15.5px;font-weight:600;color:#3d3427;}.ftr .l b{font-weight:900;color:#A85B38;}
.ftr .r{display:flex;align-items:center;gap:9px;font-size:15.5px;font-weight:600;color:#3d3427;}
.ftr .r img{width:25px;height:25px;border-radius:50%;}
.ftr .r b{font-weight:900;color:#17150F;}
"""
SPARK='<svg viewBox="0 0 100 100"><g fill="#C84623"><path d="M50 4 L56 38 L50 50 L44 38 Z"/><path d="M50 96 L56 62 L50 50 L44 62 Z"/><path d="M4 50 L38 44 L50 50 L38 56 Z"/><path d="M96 50 L62 44 L50 50 L62 56 Z"/><path d="M17 17 L44 40 L50 50 L38 46 Z"/><path d="M83 83 L56 60 L50 50 L62 54 Z"/><path d="M83 17 L60 44 L50 50 L54 38 Z"/><path d="M17 83 L40 56 L50 50 L46 62 Z"/></g></svg>'
GO='<span class="go"><svg viewBox="0 0 24 24"><path d="M12 19V5M6 11l6-6 6 6"/></svg></span>'

def mb(i,txt): return f'<div class="mb"><span class="d">{i}</span><span>{txt}</span></div>'
def cell(color,n,tt,bullets,pbl,pb):
    bl="".join(mb(i+1,b) for i,b in enumerate(bullets))
    pbh=f'<div class="pbl">{pbl}</div><div class="pb"><span class="c">{pb}</span>{GO}</div>' if pb else ''
    return f'<div class="cell"><div class="top"><span class="num" style="background:{color}">{n}</span><span class="tt">{tt}</span></div>{bl}{pbh}</div>'

def emit_grid():
    T="#B4693F"; B="#C08A6C"; K="#B08A62"; G="#3f7d5c"; BK="#211F1A"
    cells=(
     cell(T,1,"Drop your list.",["<b>40 accounts</b>, straight from your CRM export.","Or say the niche and <b>CORTEX builds the list</b>."],
      "PASTE THIS","<i>&gt;</i> score my list on AI-readiness. CSV attached. Rank call-now first.")
    +cell(B,2,"It reads the signals.",["<b>Hiring</b> for ops / RevOps roles.","Stack has <b>no AI layer</b> yet.","Founder posts about <b>scaling pain</b>.","Raised in the last <b>18 months</b>."],"","")
    +cell(K,3,"Every account scored.",["0-100, from <b>public data only</b>.","Scored against <b>your ICP band</b>, not a generic one."],
      "THE OUTPUT","Northwind 86 &middot; Globex 81 &middot; Initech 74 &middot; Stark 70 &middot; ...")
    +cell(G,4,"Verdicts, not vibes.",["<b>CALL NOW</b> &middot; 2 accounts, ready to buy.","<b>WARM</b> &middot; 3 accounts, nurture + re-score.","<b>SKIP</b> &middot; 3 accounts, not this quarter."],"","")
    +cell(BK,5,"Briefs attached.",["Each call-now account ships with a <b>1-page brief</b>.","Champion, signals, opener angle, <b>next step</b>."],
      "PASTE THIS","<i>&gt;</i> brief me on Northwind before the call.")
    +cell(T,6,"The week-3 test.",["Manual research finds these in <b>week 3</b>.","The index found both call-nows <b>before lunch</b>.","62 minutes, <b>40 accounts</b>, zero tabs."],"","")
    +cell(B,7,"Wire the outreach.",["SPECTER drafts openers <b>for call-nows only</b>.","One trigger each, from the brief."],
      "PASTE THIS","<i>&gt;</i> draft openers for the call-now accounts.")
    +cell(K,8,"Gate before send.",["Everything parks at the <b>human gate</b>.","You read, you tap, <b>then</b> it moves."],"","")
    +cell(G,9,"Re-run weekly.",["Scores <b>decay and spike</b> with the news.","A warm account crossing 80 <b>pings you</b>."],
      "SET ONCE","<i>&gt;</i> re-score every Monday 07:00. Ping me on movers."))
    band=('<div class="band9"><span class="n9">&#10003;</span><span class="t9">The loop, on autopilot.</span><div class="b9s">'
      '<div class="b9c"><div class="k">Score</div><div class="v">40 accounts, weekly</div></div><span class="b9a">&rarr;</span>'
      '<div class="b9c"><div class="k">Rank</div><div class="v">call-now first</div></div><span class="b9a">&rarr;</span>'
      '<div class="b9c"><div class="k">Brief</div><div class="v">1 page per target</div></div><span class="b9a">&rarr;</span>'
      '<div class="b9c"><div class="k">Call</div><div class="v">you, at the right time</div></div></div></div>')
    html=f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>{CSS_E}</style></head><body>
<div class="frame" id="artifact">
<div class="hdr">{SPARK}<span class="t">Two buyers were <em>hiding</em> in my list of 40.</span></div>
<div class="sub">The AI-readiness index: 9 steps, one run, <b>62 minutes</b>. It found both before lunch.</div>
<div class="gridw">{cells}</div>
{band}
<div class="ctab" style="margin-top:11px"><span class="l">Comment <b>INDEX</b> and I will DM you the rubric + the scoring run</span><span class="r">INDEX &rarr;</span></div>
<div class="ftr"><span class="l">PINPOINT: app.51ultron.com/techniques</span><span class="r"><img src="__LOGO__"><span><b>ULTRON</b> &middot; 51ultron.com</span></span></div>
</div></body></html>"""
    open("content/howto2/li-10.html","w").write(html); print("wrote li-10 (grid)")

if __name__=="__main__":
    os.makedirs("content/howto2",exist_ok=True)
    emit_ladder(); emit_grid()
