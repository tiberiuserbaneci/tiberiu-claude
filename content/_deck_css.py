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
.mast{{font-size:22px}}
.foot{{padding-top:26px}}
/* with the domain gone the wordmark is alone down there, so it gets the tracking and the
   weight of a mark rather than the faintness of a caption trailing a URL */
.foot span{{font-size:21px;letter-spacing:.34em;color:var(--ink70)}}

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
.lg-h,.vd-h,.rc-h,.tr-h,.sc-h,.cn-h,.mt-h,.gr-h{{flex-shrink:0;font-size:62px;color:var(--ink);
  margin:26px 0 24px}}
.lg-h em,.vd-h em,.rc-h em,.tr-h em,.sc-h em,.cn-h em,.mt-h em,.gr-h em{{color:var(--acc);
  font-style:normal}}

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
/* Rows are `flex:1`, so each one is handed roughly a seventh of a tall block. At 29px type
   that filled about a quarter of the row and the bill read as seven lines floating in air -
   the operator's standing rejection. The fix is not to stop distributing, it is to make the
   type worth the height it was already given, and to end the bill on a TOTAL, which is the
   one line a receipt is actually for. */
.rc-body{{flex:1;min-height:0;display:flex;flex-direction:column;padding:4px 0}}
.rc-li{{flex:1;display:flex;align-items:center;gap:16px;
  border-bottom:1px solid var(--rim2)}}
.rc-li:last-child{{border-bottom:0}}
.rc-d{{font-size:37px;font-weight:600;color:var(--ink70);white-space:nowrap}}
.rc-dot{{flex:1;border-bottom:2px dotted var(--rim2);transform:translateY(-8px)}}
.rc-v{{font-size:35px;color:var(--ink70);letter-spacing:.06em;white-space:nowrap}}
/* The lit row is the only one that can outgrow the column: a long description at 48px plus a
   long value at 46px, both nowrap, overran deck B's last slide by 217px. The value stays on
   one line because a price broken across two lines stops being a price; the description is
   allowed to wrap instead. */
.rc-li.on .rc-d{{font-size:48px;font-weight:800;color:var(--ink);letter-spacing:-.5px;
  white-space:normal;line-height:1.06;min-width:0}}
.rc-li.on .rc-v{{font-size:42px;color:var(--acc);align-self:center}}
.rc-tl{{flex-shrink:0;display:flex;align-items:baseline;justify-content:space-between;
  gap:18px;margin-top:14px;padding-top:20px;border-top:2px solid var(--rim2)}}
.rc-tl-l{{font-family:'DM Mono',monospace;font-weight:500;font-size:21px;letter-spacing:.2em;
  text-transform:uppercase;color:var(--ink45)}}
.rc-tl-n{{font-family:'Anton',sans-serif;text-transform:uppercase;letter-spacing:-1px;
  font-size:74px;line-height:.9;color:var(--acc)}}
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
.tr-x{{font-size:33px;font-weight:700;color:var(--ink70);line-height:1.2}}
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
/* 1.35, not 1.9. The lit row is already marked by weight, size and colour; the extra
   height was empty and read as a hole punched in the middle of the matrix. */
.sc-r.on{{flex:1.35}}
.sc-r.on .sc-n{{font-size:38px;font-weight:800;color:var(--ink);letter-spacing:-.4px}}
.sc-r.on .sc-c{{font-size:46px}}
.sc-note{{flex-shrink:0;padding:24px 0 28px;font-size:27px;font-weight:600;color:var(--ink);
  line-height:1.36}}

/* ---------- the AI signal, on every cover ---------- */
.aichip{{display:flex;align-items:center;gap:14px;padding:16px 26px;border-radius:18px;
  align-self:flex-start}}
.aichip-t{{font-family:'DM Mono',monospace;font-size:22px;font-weight:500;letter-spacing:.24em;
  text-transform:uppercase;color:var(--ink70)}}
.aichip-a{{font-size:26px;color:var(--acc);line-height:1}}

/* ---------- CONSOLE, the break and the AI moment ---------- */
.cn{{flex:1;min-height:0;display:flex;flex-direction:column;border-radius:30px;
  padding:0 0 26px}}
.cn-bar{{flex-shrink:0;display:flex;align-items:center;gap:11px;padding:22px 28px;
  border-bottom:1px solid var(--rim2)}}
.cn-d{{width:15px;height:15px;border-radius:50%;background:var(--rim2)}}
.cn-d:first-child{{background:var(--acc)}}
.cn-title{{margin-left:16px;font-size:19px;color:var(--ink45)}}
.cn-in{{flex-shrink:0;display:grid;grid-template-columns:112px 1fr;align-items:baseline;
  padding:30px 28px 24px}}
.cn-p{{font-size:19px;color:var(--ink45);letter-spacing:.2em}}
.cn-q{{font-size:40px;font-weight:800;color:var(--ink);line-height:1.2;
  letter-spacing:-.5px}}
.cn-out{{flex:1;min-height:0;display:grid;grid-template-columns:112px 1fr;
  align-items:start;padding:26px 28px 0;border-top:1px solid var(--rim2)}}
.cn-out .cn-p{{color:var(--acc)}}
.cn-lines{{display:flex;flex-direction:column;justify-content:center;gap:16px;height:100%}}
.cn-o{{display:grid;grid-template-columns:38px 1fr;align-items:baseline;
  font-size:28px;font-weight:600;color:var(--ink70);line-height:1.34}}
.cn-ok{{color:var(--acc);font-size:24px}}
.cn-foot{{flex-shrink:0;margin:22px 28px 0;padding-top:18px;border-top:1px solid var(--rim2);
  font-size:19px;letter-spacing:.14em;color:var(--acc)}}
.cn-pills{{flex-shrink:0;display:flex;gap:8px;padding-top:20px}}
.cn-pill{{flex:1;text-align:center;padding:13px 6px;border-radius:13px;
  font-size:18px;font-weight:600;white-space:nowrap;overflow:hidden;
  text-overflow:ellipsis;color:var(--ink45);background:var(--glass2);
  box-shadow:inset 0 1px 0 var(--rim)}}
.cn-pill.on{{color:var(--ink);background:var(--acc);box-shadow:none}}

/* ---------- METER, the break: a proportional bar chart and nothing else ----------

   The break has to be SIMPLE to read and HEAVY to look at. `stamp` got the first half and
   failed the second - an audience skips empty as fast as it skips repetitive. A chart is one
   idea, taken in at a glance, and it fills the block with real mass.

   The row is a two-row grid whose SECOND row is `1fr`, so the bar absorbs whatever height the
   row was given. That is what makes dead space structurally impossible here: there is nothing
   left over to be empty, because the graphic grows into it. */
.mt-mini{{padding:24px 28px;display:flex;flex-direction:column;gap:13px;border-radius:26px}}
.mt-m{{display:grid;grid-template-columns:1fr 280px 52px;align-items:center;column-gap:18px}}
.mt-ml{{font-size:23px;font-weight:600;color:var(--ink70);white-space:nowrap;overflow:hidden;
  text-overflow:ellipsis}}
.mt-mb{{height:15px;border-radius:8px;background:var(--rim2);overflow:hidden;
  box-shadow:inset 0 1px 0 var(--rim)}}
.mt-mb i{{display:block;height:100%;border-radius:8px;background:var(--acc)}}
.mt-mv{{font-size:20px;color:var(--acc);text-align:right}}

.mt{{flex:1;min-height:0;display:flex;flex-direction:column;padding:28px 32px 0;
  border-radius:28px}}
.mt-hd{{flex-shrink:0;display:flex;justify-content:space-between;font-size:19px;
  color:var(--ink45);padding-bottom:16px;border-bottom:1px solid var(--rim2)}}
.mt-body{{flex:1;min-height:0;display:flex;flex-direction:column;gap:6px;padding:12px 0}}
.mt-r{{flex:1;min-height:0;display:grid;grid-template-columns:1fr auto;
  grid-template-rows:auto 1fr;row-gap:10px;column-gap:22px;padding:7px 0}}
.mt-l{{font-size:25px;font-weight:600;color:var(--ink70);line-height:1.18;align-self:center}}
.mt-v{{font-size:30px;color:var(--ink45);justify-self:end;align-self:center;line-height:1}}
.mt-t{{grid-column:1/3;align-self:stretch;min-height:20px;border-radius:12px;
  background:var(--rim2);overflow:hidden;box-shadow:inset 0 1px 0 var(--rim)}}
.mt-t i{{display:block;height:100%;border-radius:12px;background:var(--bar);
  box-shadow:inset 0 2px 0 rgba(255,255,255,.28),inset 0 -4px 10px rgba(0,0,0,.10)}}
.mt-r.on{{flex:1.55}}
.mt-r.on .mt-l{{font-size:40px;font-weight:800;color:var(--ink);letter-spacing:-.4px;
  line-height:1.08}}
.mt-r.on .mt-v{{font-size:68px;color:var(--acc)}}
.mt-r.on .mt-t i{{background:var(--acc)}}
.mt-note{{flex-shrink:0;padding:22px 0 26px;font-size:28px;font-weight:600;color:var(--ink);
  line-height:1.36}}
.mt-a{{display:block;margin-top:16px;padding-top:15px;border-top:1px solid var(--rim2);
  font-size:19px;letter-spacing:.13em;color:var(--acc)}}
.mt-h{{flex-shrink:0;font-size:62px;color:var(--ink);margin:26px 0 24px}}
.mt-h em{{color:var(--acc);font-style:normal}}

/* ---------- GRID, the third break: a field of cells, counted ----------

   Break shape number three. Two shapes alternating is still a pattern the eye learns, and the
   break slot exists precisely so the eye cannot settle. This one reads proportion by COUNTING
   rather than by length, which is a different mechanic from the chart and a different object
   from the product window: the whole set is on screen at once and the argument is how few of
   the cells are lit.

   Cells are painted blocks, so the density is structural - they tile the area or they do not.
   That is why the row-fill guard does not measure this one; there are no text rows to be thin. */
.gr{{flex:1;min-height:0;display:flex;flex-direction:column;padding:28px 30px 0;
  border-radius:28px}}
.gr-hd{{flex-shrink:0;display:flex;justify-content:space-between;font-size:19px;
  color:var(--ink45);padding-bottom:18px;border-bottom:1px solid var(--rim2)}}
/* `align-content:center` floated three rows of cells in the middle of a tall panel and left
   about 280px dead above and 250px below. `grid-auto-rows:1fr` makes the cells absorb the
   block instead - 18 cells is exactly 6 by 3, so they tile it with no orphan row. */
.gr-f{{flex:1;min-height:0;display:grid;grid-template-columns:repeat(6,1fr);
  grid-auto-rows:1fr;gap:14px;padding:22px 0}}
.gr-c{{border-radius:18px;background:var(--glass2);box-shadow:inset 0 1px 0 var(--rim);
  display:flex;align-items:center;justify-content:center;min-height:0;
  font-family:'DM Mono',monospace;font-size:24px;font-weight:500;color:var(--ink45)}}
/* the lit colour is the theme's own ground, so the label stays legible whichever way round
   the accent sits: dark type on a light accent, light type on a dark one */
.gr-c.on{{background:var(--acc);color:var(--bg);box-shadow:none;font-weight:700;font-size:27px}}
.gr-c.win{{background:transparent;box-shadow:inset 0 0 0 3px var(--acc);color:var(--acc);
  font-weight:700;font-size:24px}}
.gr-note{{flex-shrink:0;padding:22px 0 26px;font-size:28px;font-weight:600;color:var(--ink);
  line-height:1.36}}
.gr-a{{display:block;margin-top:16px;padding-top:15px;border-top:1px solid var(--rim2);
  font-size:19px;letter-spacing:.13em;color:var(--acc)}}
.gr-mini{{padding:26px 28px;border-radius:26px;display:grid;
  grid-template-columns:repeat(9,1fr);gap:9px}}
.gr-mini .gr-c{{min-height:54px;font-size:15px;border-radius:11px}}
.gr-mini .gr-c.on{{font-size:17px}}
.gr-mini .gr-c.win{{font-size:15px;box-shadow:inset 0 0 0 2px var(--acc)}}

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
