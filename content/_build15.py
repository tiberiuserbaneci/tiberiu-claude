#!/usr/bin/env python3
"""Film 15 - the pipeline review that never happens. First film built on real geometry.

WHY IT IS NOT BUILT FROM FILM 12. Films 10, 11 and 12 are one shape: a named window of time
split into numbered rows. That has run three times. There is also a capability reason - the
objects are real geometry now, with a studio environment and a moving key light, so ONE object
can carry a stretch of film by CHANGING. A box-shadow stack cannot turn; there is nothing there
to turn.

THE OBJECT RUN (CLAUDE.md 30, graphic variety - b2's object may not be b4's):

    b1  ring, reading 41            b4  the grid loses ten more
    b2  ring turns, 41 ticks read   b5  one slab lifts out of the nine
    b3  the 41 as a packed grid     b6  the ask, as display type

FRAMING (operator, 2026-08-07: "sa fie la jumatate si sa umple placut vizual tot materialul
nu ceva discret"). Every object is centred in its workspace and built to fill it. The ring is
width-bound because it is circular, so it takes 92% of the 880 column; the grid is bound by
both and takes 41 packed cells across the full band. The hook clears at --hookgone and the
stage takes back its 288px, so from b2 the workspace is 372..1420 rather than 622..1420.

ARITHMETIC. 41 open, 22 stalled with no answer, 10 with no authority, 9 real. It sums.
The clock named is the FOUNDER's - three weeks of not looking - never the machine's.
"""
import base64, importlib.util, pathlib

REPO = pathlib.Path("/home/user/tiberiu-claude")


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


FONTS = load("_fonts").embedded_css()
S3 = load("_stage3d")
LOGO = base64.b64encode((REPO / "content/ultron-logo.png").read_bytes()).decode()

# ---- CLAUDE.md 7 tokens ------------------------------------------------------
BOOK, KRAFT, MANILLA = "CC785C", "D4A27F", "EBDBBC"
IVORY, SLATE, CLOUD = "F0EEE6", "191919", "919180"

# ---- bases solved by _palette3d.py so the RENDER lands on the tokens ---------
CLAY_B, PALE_B, WARM_B = 0xDD8C76, 0xFFFFE8, 0xE5B89B
DIM_B = 0xC9BCA8                       # the receded rows, still warm, never grey

W, H = 1080, 1920
COL_L, COL_R = 70, 950                 # the 880 column
BAND_T, BAND_B = 300, 1590
HOOK_T, HOOK_B = 352, 600
STAGE1_T, STAGE_B = 622, 1420          # while the hook is up
STAGE2_T = 372                         # after it clears
TALLY_T, GRID_T = 372, 545             # the count gets its OWN band, never the grid's
CAP_T, FOOT_T = 1440, 1520

RING_CY1 = (STAGE1_T + STAGE_B) // 2   # 1021
RING_CY2 = (STAGE2_T + STAGE_B) // 2   # 896
GRID_CY = (GRID_T + STAGE_B) // 2      # 982
R, TUBE = 316, 90                      # outer 406 -> 812 wide, 92% of the column

# 7 across, 6 down, the last row 6 and centred, so 41 reads as deliberate rather than ragged
GX, GY, CELL = 124, 140, 106           # 850 x 806 -> 97% of the column, 92% of the band

# Which deals are which. Scattered, not blocked: a pipeline's real deals are not the last
# nine rows, and when the other thirty one recede the survivors read as a scatter that then
# pulls together on b5. Fixed list, so the render is deterministic.
SURV = [3, 9, 14, 20, 25, 28, 33, 37, 40]
NOAUTH = [1, 5, 8, 12, 17, 22, 26, 31, 35, 38]
STALL = [i for i in range(41) if i not in SURV and i not in NOAUTH]
assert len(SURV) == 9 and len(NOAUTH) == 10 and len(STALL) == 22

DUR = 32

BEATS = [
    "Claude read my whole pipeline and told me nine were real. "
    "It had been three weeks since I last looked at it honestly.",
    "Forty one open deals. It read every note, every thread, "
    "and every date I had stopped opening.",
    "Twenty two had not moved in a month, and not one of them had said no.",
    "Ten more were a person who liked me, and could not sign anything.",
    "Nine were real, and one was closer than everything I had ranked above it. "
    "It does not close anything. It tells me where to spend Monday.",
    "Comment PIPELINE and I will send you the exact run.",
]

CAPS = [
    ("41", "open deals", "It had been <b>three weeks</b> since I last looked at it honestly."),
    ("41", "read", "Every note, every thread, every date I had stopped opening."),
    ("22", "no answer", "Not moved in a month. <b>Nobody had said no.</b>"),
    ("10", "no authority", "A person who liked me and could not sign anything."),
    ("9", "real", "<b>One</b> was closer than everything I had ranked above it."),
    ("", "", "It does not close anything. It tells me where to spend Monday."),
]

META = ('{"duration": %d, "w": %d, "h": %d, "fps": 30, "beats": [%s]}'
        % (DUR, W, H, ", ".join('{"vo": %s}' % __import__("json").dumps(b) for b in BEATS)))

# --------------------------------------------------------------------- scene
SCENE = f"""
  const G = {{}};
  function grp(name, x, y) {{
    const g = new T.Group(); g.position.set(x, y, 0); scene.add(g); G[name] = g; return g; }}

  // ---- b1/b2 : the ring, 92% of the column, centred in its workspace
  const ring = grp('ring', 0, {H//2 - RING_CY1});
  ring.add(OB.ring({R}, {TUBE}, {CLAY_B:#08x}, 0.32));
  const face = OB.disc(216, 56, {PALE_B:#08x}, 0.44); face.rotation.x = Math.PI/2; ring.add(face);
  const well = OB.disc(176, 68, {WARM_B:#08x}, 0.54); well.rotation.x = Math.PI/2;
  well.position.z = 16; ring.add(well);
  window.__follow(document.querySelector('.rd-in'), ring);

  // 41 ticks around the face: one per deal, lit in turn on b2. Real prisms, so each one
  // takes the key light and casts its own shadow rather than being a drawn dash.
  const ticks = [];
  for (let i = 0; i < 41; i++) {{
    const a = (i / 41) * Math.PI * 2 - Math.PI / 2;
    const t3 = OB.slab(13, 30, 5, 16, {PALE_B:#08x}, 0.42);
    t3.position.set(Math.cos(a) * 198, Math.sin(a) * 198, 34);
    t3.rotation.z = a + Math.PI / 2;
    ring.add(t3); ticks.push(t3);
  }}

  // ---- b3/b4/b5 : the 41, packed into their own band under the count
  const grid = grp('grid', 0, {H//2 - GRID_CY});
  const cells = [], home = [], seat = [];
  for (let i = 0; i < 41; i++) {{
    const row = Math.floor(i / 7), col = i % 7;
    const short = (row === 5) ? 0.5 : 0;            // the last row is 6, so centre it
    const cx = (col - 3 + short) * {GX}, cy = (2.5 - row) * {GY};
    const c = OB.slab({CELL}, {CELL}, 22, 32, {PALE_B:#08x}, 0.46);
    c.position.set(cx, cy, 0);
    grid.add(c); cells.push(c); home.push([cx, cy]);
  }}
  // Where the nine land on b5: a 3 by 3 block at 2.4x, 824px across and down - 94% of the
  // column and of the band. A single row of nine cannot work: at 106 wide they need a pitch
  // over 118, which is 1062px, so they overlap into one solid bar and stop reading as nine.
  const SURV = {SURV};
  SURV.forEach((idx, k) => {{ seat[idx] = [(k % 3 - 1) * 285, (1 - Math.floor(k / 3)) * 285]; }});
  const NOAUTH = {NOAUTH};
  const KIND = new Array(41).fill(0);               // 0 stall, 1 no authority, 2 real
  NOAUTH.forEach(i => KIND[i] = 1); SURV.forEach(i => KIND[i] = 2);
  const RANK = new Array(41).fill(-1);              // a survivor's place in the gather
  SURV.forEach((idx, k) => RANK[idx] = k);
  window.__RANK = RANK;

  window.__cells = cells; window.__ticks = ticks; window.__G = G;
  window.__home = home; window.__seat = seat; window.__KIND = KIND;
  window.__ONE = {SURV[4]};                          // the one that was closer
"""

SEEK = f"""
    const cs = getComputedStyle(document.documentElement);
    const B = [1,2,3,4,5,6].map(i => parseFloat(cs.getPropertyValue('--b'+i)) || 0);
    const cl = (v,a,b) => Math.min(b, Math.max(a, v));
    const ss = (v) => v*v*(3-2*v);
    const pr = (a,d) => ss(cl((t-a)/d, 0, 1));
    const G = window.__G, cells = window.__cells, ticks = window.__ticks;

    // ---- ring : holds b1 and b2, recentres into the space the hook gives back
    const toB2 = pr(B[1], 0.9), out = pr(B[2], 0.55);
    G.ring.visible = out < 1;
    G.ring.position.y = {H//2 - RING_CY1} + toB2 * {RING_CY1 - RING_CY2};
    G.ring.scale.setScalar(1 - out * 0.16);
    G.ring.rotation.x = -0.26 + Math.sin(t*0.5)*0.045;
    G.ring.rotation.y = 0.26 + Math.cos(t*0.5)*0.09 + toB2 * 0.30;
    // the ticks read one at a time across b2, so the frame is never still
    ticks.forEach((tk, i) => {{
      const on = pr(B[1] + 0.25 + i * 0.052, 0.30);
      tk.scale.set(1, 0.35 + on * 0.65, 0.4 + on * 0.6);
      tk.material.color.setHex(on > 0.5 ? {CLAY_B:#08x} : {DIM_B:#08x});
    }});

    // ---- grid : 41 packed cells, two cuts, then the nine pull together
    const gin = pr(B[2] - 0.30, 0.8);
    G.grid.visible = gin > 0;
    G.grid.scale.setScalar(0.86 + gin * 0.14);
    G.grid.rotation.x = -0.14 + Math.sin(t*0.42)*0.03;
    G.grid.rotation.y = 0.10 + Math.cos(t*0.42)*0.05;
    const home = window.__home, seat = window.__seat, KIND = window.__KIND, RANK = window.__RANK;
    // The nine gather ONE AT A TIME across b5. The measured b5-to-b6 gap is 8.63s; a single
    // 1s convergence left 6.5 seconds of held frame in the middle of the payoff, which is
    // the exact stretch the retention guard was built to catch. Every delay here is derived
    // from that measured gap, not inherited from an earlier film's timings.
    const gather = pr(B[4] + 0.5 + 8 * 0.55, 1.0);  // the LAST one to arrive, for the tally
    cells.forEach((c, i) => {{
      // arrival is staggered so 41 objects never pop as one block
      const land = pr(B[2] - 0.30 + i * 0.018, 0.42);
      const cut = KIND[i] === 0 ? pr(B[2] + 0.9 + i * 0.021, 0.40)
                : KIND[i] === 1 ? pr(B[3] + 0.7 + i * 0.020, 0.40) : 0;
      const one = (i === window.__ONE) ? pr(B[4] + 6.2, 0.9) : 0;
      const g = KIND[i] === 2 ? pr(B[4] + 0.5 + RANK[i] * 0.55, 1.0) : 0;
      c.position.x = home[i][0] + (seat[i] ? (seat[i][0] - home[i][0]) * g : 0);
      c.position.y = home[i][1] + (seat[i] ? (seat[i][1] - home[i][1]) * g : 0);
      c.position.z = -70 + land * 70 - cut * 96 + g * 60 + one * 130;
      c.scale.setScalar((0.5 + land * 0.5) * (1 - cut * 0.26) * (1 + g * 1.40 + one * 0.16));
      c.material.color.setHex(cut > 0.5 ? {DIM_B:#08x}
                            : KIND[i] === 2 && t > B[4] - 0.2 ? {CLAY_B:#08x} : {PALE_B:#08x});
      // the thirty two clear out of the nine's way rather than sitting behind them
      c.material.opacity = 1 - cut * 0.40 - (KIND[i] === 2 ? 0 : gather * 0.50);
      c.material.transparent = c.material.opacity < 1;
    }});

    // ---- b6 : the ask is type, so every object clears the frame for it
    const bye = pr(B[5] - 0.5, 0.55);
    if (bye > 0) {{
      [G.ring, G.grid].forEach(g => {{ g.scale.multiplyScalar(1 - bye); }});
      if (bye > 0.97) {{ G.ring.visible = false; G.grid.visible = false; }}
    }}
"""

HTML = f"""<meta charset="UTF-8">
<style>
/* FILM-META {META} */
/* BAND 300..1590 | mast 52 | hook 248 (clears at --hookgone) | stage 622..1420 then
   372..1420 | caption 1440..1520 | footer 1520..1590 */
{FONTS}
:root{{
  --book:#{BOOK}; --kraft:#{KRAFT}; --manilla:#{MANILLA};
  --ivory:#{IVORY}; --slate:#{SLATE}; --cloud:#{CLOUD};
  --e:cubic-bezier(.2,.85,.25,1);
  --eEmph:cubic-bezier(.05,.7,.1,1); --eExit:cubic-bezier(.3,0,1,1);
  --b1:0s; --b2:6s; --b3:12s; --b4:17s; --b5:22s; --b6:28s;
  --hookout:4.62s; --hookgone:5.24s;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#0C0C0B;display:flex;justify-content:center;align-items:flex-start;
  font-family:'Plus Jakarta Sans',sans-serif;-webkit-font-smoothing:antialiased}}
#film{{width:{W}px;height:{H}px;position:relative;overflow:hidden;background:var(--ivory);
  color:var(--slate)}}
.amb{{position:absolute;inset:0;z-index:0;
  background:radial-gradient(ellipse 66% 34% at 50% 4%,rgba(204,120,92,.07) 0%,transparent 64%),
    radial-gradient(ellipse 58% 32% at 50% 100%,rgba(212,162,127,.16) 0%,transparent 62%),
    linear-gradient(178deg,#F6F5F0 0%,#F0EEE6 48%,#E7E4D8 100%)}}
#gl{{position:absolute;inset:0;z-index:1;pointer-events:none}}

@keyframes fadeout{{to{{opacity:0}}}}
@keyframes fadein{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes rise{{from{{opacity:0;transform:translateY(26px)}}to{{opacity:1;transform:none}}}}
@keyframes sink{{to{{opacity:0;transform:translateY(-20px)}}}}
@keyframes drift{{from{{transform:translateY(5px)}}to{{transform:translateY(-5px)}}}}

.safe{{position:absolute;top:{BAND_T}px;left:{COL_L}px;right:{W-COL_R}px;
  bottom:{H-BAND_B}px;z-index:6}}
.mast{{position:absolute;top:0;left:0;right:0;height:52px;display:flex;
  justify-content:space-between;font-family:'DM Mono',monospace;font-size:21px;font-weight:500;
  letter-spacing:.22em;text-transform:uppercase;color:var(--cloud)}}
.mast .tag{{color:var(--book)}}

/* the hook is type on the ground, never a wall over the picture (CLAUDE.md 30), and it
   clears on its own duration so nothing outlives it */
.hk{{position:absolute;top:{HOOK_T-BAND_T}px;left:0;right:0;z-index:9;
  font-family:'Anton',sans-serif;font-size:88px;line-height:.94;letter-spacing:-1.2px;
  text-transform:uppercase;color:var(--slate);
  animation:fadeout .62s var(--eExit) var(--hookout) both}}
.hk em{{color:var(--book);font-style:normal}}

.rd{{position:absolute;left:0;right:0;top:{RING_CY1-BAND_T}px;z-index:8;text-align:center;
  transform:translateY(-50%);animation:rd-mv .9s var(--e) var(--b2) both}}
@keyframes rd-mv{{to{{transform:translateY(-50%) translateY({RING_CY2-RING_CY1}px)}}}}
.rd-in{{transform-origin:center center;will-change:transform}}
.rd b{{display:block;font-family:'Anton',sans-serif;font-size:124px;line-height:.86;
  color:var(--slate)}}
.rd i{{display:block;font-family:'DM Mono',monospace;font-style:normal;font-size:20px;
  font-weight:500;letter-spacing:.28em;text-transform:uppercase;
  color:rgba(25,25,25,.60);margin-top:10px}}
.rd .v2{{position:absolute;left:0;right:0;top:0;opacity:0;
  animation:fadein .5s var(--e) var(--b2) both}}
.rd .v1{{animation:fadeout .5s var(--e) var(--b2) both}}
.rd.gone{{animation:fadeout .5s var(--eExit) var(--b3) both}}

/* the running count, big, on its own - the grid carries the picture from here */
.tally{{position:absolute;left:0;right:0;top:{STAGE2_T-BAND_T}px;z-index:8;text-align:center;
  opacity:0}}
.tally b{{font-family:'Anton',sans-serif;font-size:132px;line-height:.86;color:var(--slate)}}
.tally i{{display:block;font-family:'DM Mono',monospace;font-style:normal;font-size:21px;
  font-weight:500;letter-spacing:.28em;text-transform:uppercase;
  color:rgba(25,25,25,.58);margin-top:9px}}
.t3{{animation:fadein .5s var(--e) var(--b3) both, sink .5s var(--eExit) var(--b4) both}}
.t4{{animation:fadein .5s var(--e) var(--b4) both, sink .5s var(--eExit) var(--b5) both}}
.t5 b{{color:var(--book)}}
.t5{{animation:fadein .5s var(--e) var(--b5) both, sink .5s var(--eExit) var(--b6) both}}

.cap{{position:absolute;left:0;right:0;top:{CAP_T-BAND_T}px;height:80px;z-index:8;
  font-size:35px;font-weight:600;line-height:1.28;color:rgba(25,25,25,.62)}}
.cap b{{color:var(--slate);font-weight:800}}
.cap span{{position:absolute;left:0;right:0;top:0;opacity:0}}
.c1{{animation:fadein .5s var(--e) 0s both, fadeout .4s var(--eExit) var(--b2) both}}
.c2{{animation:fadein .5s var(--e) var(--b2) both, fadeout .4s var(--eExit) var(--b3) both}}
.c3{{animation:fadein .5s var(--e) var(--b3) both, fadeout .4s var(--eExit) var(--b4) both}}
.c4{{animation:fadein .5s var(--e) var(--b4) both, fadeout .4s var(--eExit) var(--b5) both}}
.c5{{animation:fadein .5s var(--e) var(--b5) both, fadeout .4s var(--eExit) var(--b6) both}}

/* the ask is the biggest thing on the frame (CLAUDE.md 30) */
.cta{{position:absolute;top:{STAGE2_T-BAND_T}px;left:0;right:0;bottom:{BAND_B-CAP_T}px;
  z-index:10;display:flex;flex-direction:column;justify-content:center;opacity:0;
  animation:fadein .6s var(--eEmph) var(--b6) both}}
.cta .kw{{font-family:'Anton',sans-serif;font-size:172px;line-height:.88;
  letter-spacing:-2px;text-transform:uppercase;color:var(--slate)}}
.cta .kw em{{color:var(--book);font-style:normal}}
.cta .sub{{margin-top:26px;font-size:38px;font-weight:600;line-height:1.3;
  color:rgba(25,25,25,.66)}}
.cta .sub b{{color:var(--slate);font-weight:800}}
.ctaw{{animation:drift 7s ease-in-out var(--b6) infinite alternate}}

.foot{{position:absolute;left:0;right:0;top:{FOOT_T-BAND_T}px;height:70px;z-index:8;
  display:flex;align-items:flex-end;gap:13px}}
.foot img{{width:32px;height:32px;border-radius:50%;object-fit:cover;opacity:.9}}
.foot span{{font-family:'DM Mono',monospace;font-size:20px;font-weight:500;letter-spacing:.16em;
  text-transform:uppercase;color:var(--cloud)}}
.foot span em{{color:var(--book);font-style:normal}}
</style>

<div id="film">
  <div class="amb"></div>
  <canvas id="gl" width="{W}" height="{H}"></canvas>
  <div class="safe">
    <div class="mast"><span>FILM 15 <span class="tag">/</span> PIPELINE</span><span>ONE REVIEW</span></div>

    <div class="hk">Claude read my whole<br>pipeline and told me<br><em>nine</em> were real.</div>

    <div class="rd gone"><div class="rd-in">
      <div class="v1"><b>{CAPS[0][0]}</b><i>{CAPS[0][1]}</i></div>
      <div class="v2"><b>{CAPS[1][0]}</b><i>{CAPS[1][1]}</i></div>
    </div></div>

    <div class="tally t3"><b>{CAPS[2][0]}</b><i>{CAPS[2][1]}</i></div>
    <div class="tally t4"><b>{CAPS[3][0]}</b><i>{CAPS[3][1]}</i></div>
    <div class="tally t5"><b>{CAPS[4][0]}</b><i>{CAPS[4][1]}</i></div>

    <div class="cta"><div class="ctaw">
      <div class="kw">Comment<br><em>Pipeline</em></div>
      <div class="sub">and I will send you the <b>exact run</b>.</div>
    </div></div>

    <div class="cap">
      <span class="c1">{CAPS[0][2]}</span>
      <span class="c2">{CAPS[1][2]}</span>
      <span class="c3">{CAPS[2][2]}</span>
      <span class="c4">{CAPS[3][2]}</span>
      <span class="c5">{CAPS[4][2]}</span>
    </div>

    <div class="foot"><img src="data:image/png;base64,{LOGO}">
      <span>ULTRON <em>/</em> 51ULTRON<em>.</em>COM</span></div>
  </div>
</div>

{S3.scene(W, H, [], seek_js=SEEK).replace('const cards = [];', 'const cards = [];' + SCENE)}
"""

out = REPO / "content/pipeline-film-15.html"
out.write_text(HTML)
words = sum(len(b.split()) for b in BEATS)
print(f"{out}  {len(HTML):,} chars")
print(f"script {words} words over {len(BEATS)} beats  (~{words/195*60:.0f}s at the shipped pace)")
