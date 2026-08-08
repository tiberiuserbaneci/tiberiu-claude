#!/usr/bin/env python3
"""Layout for the five deck designs, on the 1080x1920 reel canvas.

One rule runs through all of it: every stack that owns the middle of the slide distributes
its children with `flex`, never `flex-shrink:0` plus whatever space is left over. A panel
with a title and one line under it, floating in a tall box, is the airy block that gets
rejected on sight - so the rows share the column and the largest dead band is measured, not
hoped for.
"""

W, H = 1080, 1920
SAFE_T, SAFE_R, SAFE_B, SAFE_L = 300, 130, 330, 70

CSS = f"""
.slide{{width:{W}px;height:{H}px}}
.safe{{padding:{SAFE_T}px {SAFE_R}px {SAFE_B}px {SAFE_L}px}}
.mast{{font-size:22px}}
.foot{{padding-top:26px}}
.foot span{{font-size:21px}}

/* ---------- cover, shared by every design ---------- */
.cv{{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;gap:30px}}
.cv-eye{{font-size:24px;color:var(--ink70);letter-spacing:.13em;line-height:1.4}}
.cv-h{{font-size:112px;color:var(--ink)}}
.cv-h em{{color:var(--acc);font-style:normal}}
.cv-sl{{display:flex;flex-direction:column;gap:8px}}
.sl{{display:grid;grid-template-columns:64px 1fr;align-items:center;padding:14px 24px;
  border-radius:16px}}
.sl .rn{{font-size:19px;color:var(--ink45)}}
.sl .st{{font-size:25px;font-weight:600;color:var(--ink70)}}

/* a badge that carries the deck's one number, so the cover is never just type */
.vd-tot,.rc-tot,.tr-tot,.sc-tot{{display:flex;align-items:center;gap:22px;
  padding:26px 32px;border-radius:24px}}
.vd-tot-n,.tr-tot-n,.sc-tot-n,.rc-tot-n{{font-size:76px;color:var(--acc)}}
.vd-tot-l,.tr-tot-l,.sc-tot-l{{font-size:27px;font-weight:600;color:var(--ink70);
  line-height:1.3}}
.rc-tot{{justify-content:space-between}}
.rc-tot-l{{font-size:22px;color:var(--ink70);letter-spacing:.2em}}

/* ---------- every content slide gets a display hook of its own ---------- */
.lg-h,.vd-h,.rc-h,.tr-h,.sc-h{{flex-shrink:0;font-size:62px;color:var(--ink);
  margin:26px 0 24px}}
.lg-h em,.vd-h em,.rc-h em,.tr-h em,.sc-h em{{color:var(--acc);font-style:normal}}

/* ---------- LEDGER ---------- */
.lg{{flex:1;min-height:0;display:flex;flex-direction:column;gap:12px}}
.row{{flex:1;display:grid;grid-template-columns:76px 1fr;column-gap:8px;align-items:center;
  align-content:center;padding:16px 28px;border-radius:24px}}
.row .rn{{font-size:22px;color:var(--ink45)}}
.row .rt{{font-size:28px;font-weight:700;color:var(--ink70);line-height:1.22}}
.row.on{{flex:3.2;padding:32px 30px}}
.row.on .rn{{font-size:26px;color:var(--acc)}}
.row.on .rt{{font-size:44px;font-weight:800;color:var(--ink);letter-spacing:-.5px;
  line-height:1.12}}
.row.on .rb{{grid-column:2;font-size:29px;font-weight:500;color:var(--ink70);line-height:1.4;
  margin-top:15px}}
.row.on .ra{{grid-column:2;font-size:20px;letter-spacing:.1em;color:var(--acc);margin-top:20px;
  padding-top:17px;border-top:1px solid var(--rim2)}}

/* ---------- VERDICT ---------- */
.vd{{flex:1;min-height:0;display:flex;flex-direction:column;gap:22px}}
/* content-sized, never stretched: a card whose copy fills a third of it reads as empty */
.vd-c{{flex:0 0 auto;display:flex;flex-direction:column;gap:16px;
  padding:38px 34px;border-radius:28px}}
/* the rail takes the space the panels do not, and it carries the map of all seven */
.vd-cost{{flex:1;min-height:0;display:flex;align-items:center;gap:26px;padding:0 6px}}
.vd-cn{{font-size:96px;color:var(--acc);white-space:nowrap}}
.vd-cl{{font-size:30px;font-weight:600;color:var(--ink70);line-height:1.3}}
.vd-rail{{flex-shrink:0;display:flex;flex-direction:column;gap:20px;padding-bottom:6px}}
.vd-bars{{display:flex;gap:9px;height:15px}}
.vd-p{{flex:1;border-radius:8px;background:var(--rim2);
  box-shadow:inset 0 1px 0 var(--rim)}}
.vd-p.on{{flex:2.4;background:var(--acc)}}
.vd-rl{{font-size:21px;color:var(--ink45);letter-spacing:.18em}}
.vd-rl em{{color:var(--acc);font-style:normal}}
.vd-tag{{font-size:20px;color:var(--ink45)}}
.vd-c.bad .vd-tag{{color:var(--ink45)}}
.vd-c.good .vd-tag{{color:var(--acc)}}
.vd-x{{font-size:46px;font-weight:800;color:var(--ink45);letter-spacing:-.6px;line-height:1.12;
  text-decoration:line-through;text-decoration-thickness:4px}}
.vd-y{{font-size:46px;font-weight:800;color:var(--ink);letter-spacing:-.6px;line-height:1.12}}
.vd-w{{font-size:27px;font-weight:500;color:var(--ink70);line-height:1.38}}

/* ---------- RECEIPT ---------- */
.rc{{flex:1;min-height:0;display:flex;flex-direction:column;padding:34px 34px 0;
  border-radius:28px}}
.rc-top{{flex-shrink:0;font-size:21px;color:var(--ink45);padding-bottom:18px;
  border-bottom:2px dashed var(--rim2)}}
.rc-body{{flex:1;min-height:0;display:flex;flex-direction:column;padding:8px 0}}
.rc-li{{flex:1;display:flex;align-items:center;gap:16px}}
.rc-d{{font-size:29px;font-weight:600;color:var(--ink70);white-space:nowrap}}
.rc-dot{{flex:1;border-bottom:2px dotted var(--rim2);transform:translateY(-6px)}}
.rc-v{{font-size:27px;color:var(--ink70);letter-spacing:.08em;white-space:nowrap}}
.rc-li.on .rc-d{{font-size:38px;font-weight:800;color:var(--ink)}}
.rc-li.on .rc-v{{font-size:34px;color:var(--acc)}}
/* the perforation: the one graphic element that makes it read as a bill, not a table */
.rc-perf{{flex-shrink:0;height:0;border-top:3px dashed var(--rim2);margin:6px -34px 0;
  position:relative}}
.rc-perf::before,.rc-perf::after{{content:'';position:absolute;top:-19px;width:38px;height:38px;
  border-radius:50%;background:var(--bg)}}
.rc-perf::before{{left:-19px}} .rc-perf::after{{right:-19px}}
.rc-note{{flex-shrink:0;padding:26px 0 30px;font-size:28px;font-weight:600;color:var(--ink);
  line-height:1.36}}

/* ---------- TRACE ---------- */
.tr{{flex:1;min-height:0;display:flex;flex-direction:column;position:relative;
  padding-left:6px}}
.tr::before{{content:'';position:absolute;left:150px;top:22px;bottom:22px;width:3px;
  background:var(--rim2)}}
.tr-e{{flex:1;display:grid;grid-template-columns:132px 34px 1fr;align-items:center;
  column-gap:6px;position:relative}}
.tr-t{{font-size:22px;color:var(--ink45);text-align:right}}
.tr-dot{{width:16px;height:16px;border-radius:50%;background:var(--rim2);justify-self:center;
  z-index:2}}
.tr-x{{font-size:28px;font-weight:700;color:var(--ink70);line-height:1.22}}
.tr-e.on{{flex:3.1;align-content:center}}
.tr-e.on .tr-t{{font-size:26px;color:var(--acc)}}
.tr-e.on .tr-dot{{width:26px;height:26px;background:var(--acc);
  box-shadow:0 0 0 9px var(--glass)}}
.tr-e.on .tr-x{{font-size:44px;font-weight:800;color:var(--ink);letter-spacing:-.5px;
  line-height:1.12}}
.tr-e.on .tr-b{{grid-column:3;font-size:28px;font-weight:500;color:var(--ink70);
  line-height:1.4;margin-top:14px}}

/* ---------- SCORE ---------- */
.sc{{flex:1;min-height:0;display:flex;flex-direction:column;padding:30px 30px 0;
  border-radius:28px}}
.sc-hd{{flex-shrink:0;display:grid;grid-template-columns:1fr repeat(3,104px);
  align-items:center;padding-bottom:16px;border-bottom:1px solid var(--rim2)}}
.sc-ch{{font-size:19px;color:var(--ink45);text-align:center}}
.sc-hd .sc-ch:first-child{{text-align:left}}
.sc-r{{flex:1;display:grid;grid-template-columns:1fr repeat(3,104px);align-items:center;
  border-bottom:1px solid var(--rim2)}}
.sc-n{{font-size:27px;font-weight:600;color:var(--ink70);line-height:1.2}}
.sc-c{{font-family:'Anton',sans-serif;font-size:34px;text-align:center;color:var(--ink45)}}
.sc-c.yes{{color:var(--acc)}}
.sc-r.on{{flex:1.9}}
.sc-r.on .sc-n{{font-size:38px;font-weight:800;color:var(--ink);letter-spacing:-.4px}}
.sc-r.on .sc-c{{font-size:46px}}
.sc-note{{flex-shrink:0;padding:24px 0 28px;font-size:27px;font-weight:600;color:var(--ink);
  line-height:1.36}}

/* ---------- STAMP, the break ---------- */
.stm{{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;gap:34px}}
.stm-n{{font-size:22px;color:var(--ink45);letter-spacing:.24em}}
.stm-n em{{color:var(--acc);font-style:normal}}
/* one simple glass mark. The only graphic on the slide, and it carries the verdict. */
.stm-mark{{width:172px;height:172px;border-radius:50%;display:flex;align-items:center;
  justify-content:center;flex-shrink:0}}
.stm-x{{font-family:'Anton',sans-serif;font-size:96px;line-height:1;color:var(--acc)}}
.stm-l{{font-size:104px;color:var(--ink)}}
.stm-l em{{color:var(--acc);font-style:normal}}
.stm-b{{font-size:32px;font-weight:600;color:var(--ink70);line-height:1.36}}
.stm-chips{{display:flex;flex-wrap:wrap;gap:11px}}
.stm-chip{{padding:15px 22px;border-radius:16px;font-size:24px;font-weight:600;
  color:var(--ink70)}}

/* ---------- the ask ---------- */
.cta{{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:center;gap:30px}}
.cta-eye{{font-size:24px;color:var(--ink70);letter-spacing:.13em;line-height:1.4}}
.cta-kw{{font-size:150px;color:var(--ink)}}
.cta-kw em{{color:var(--acc);font-style:normal}}
.cta-box{{padding:34px;border-radius:28px}}
.cta-b{{font-size:34px;font-weight:700;color:var(--ink);line-height:1.32}}
.cta-s{{font-size:21px;color:var(--acc);margin-top:18px;padding-top:16px;
  border-top:1px solid var(--rim2);letter-spacing:.13em;line-height:1.5}}
"""
