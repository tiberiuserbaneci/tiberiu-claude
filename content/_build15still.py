#!/usr/bin/env python3
"""Film 15, beat 1, as a still - so the proposal is looked at rather than read.

PALETTE. The Anthropic tokens from CLAUDE.md 7, and nothing else. v2 used B03A17 for the
ring, which is not a Dark Ultron token at all - it is a saturated rust that reads as RED,
which is what the operator rejected. Book Cloth CC785C is the accent primary and it is a
dusty clay, not a red. The ground is Anthropic ivory, the face manilla, the well kraft, the
type slate. Only one word in the hook carries the accent, which is how the colour is used
on Anthropic's own surfaces: near-black type on ivory, the clay reserved for the object.

A MATERIAL'S BASE COLOUR IS NOT WHAT RENDERS. The studio environment adds light and
NeutralToneMapping rolls it off, so a base of CC785C renders lighter and flatter than Book
Cloth. The base is therefore SOLVED: render, measure the lit mid-tone off the ring, and
scale the base until the rendered pixel lands on the token. RING_BASE below is that solved
value, not a guess - see the calibrate pass at the bottom.

LAYOUT. The band is declared in pixels first, per CLAUDE.md 30. v1 sized the ring to its own
taste and centred it, so the hook landed on the object and one word was unreadable.

    band 300..1590            column 880 wide
    mast    300..352    52
    hook    352..640   288    three lines, Anton 92, line-height .94
    stage   662..1420   758   <- THE WORKSPACE
    caption 1440..1520  80
    footer  1520..1590  70

An orthographic camera projects a group's origin to its own screen position whatever the
rotation is, so the readout's CSS y is exactly 960 - worldY. Solved, not eyeballed.
"""
import base64, importlib.util, pathlib

REPO = pathlib.Path("/home/user/tiberiu-claude")


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


FONTS = load("_fonts").embedded_css()
S3 = load("_stage3d")
LOGO = base64.b64encode((REPO / "content/ultron-logo.png").read_bytes()).decode()

# ---- the binding tokens, CLAUDE.md 7 -----------------------------------------
BOOK       = "CC785C"   # accent primary, Book Cloth
BOOK_DARK  = "C84623"   # accent strong
KRAFT      = "D4A27F"   # accent secondary warm
MANILLA    = "EBDBBC"   # Anthropic pale, the face
IVORY_GRD  = "F0EEE6"   # Anthropic ivory, the ground
SLATE      = "191919"   # type
CLOUD      = "919180"   # muted

# solved so the RENDERED lit mid-tone lands on Book Cloth, not the base colour
RING_BASE  = 0xDD8C76
FACE_BASE  = 0xFFFFE8
WELL_BASE  = 0xE5B89B
PIP_BASE   = 0x191919

W, H = 1080, 1920
STAGE_TOP, STAGE_BOT = 662, 1420
RING_CY = (STAGE_TOP + STAGE_BOT) // 2          # 1041 in CSS
RING_WY = H // 2 - RING_CY                      # world y, y-up
R, TUBE = 300, 84                               # outer 384 -> 768 wide, 87% of the 880 column

SCENE = f"""
  const G = [];
  function group(x, y) {{ const g = new T.Group(); g.position.set(x, y, 0); scene.add(g); G.push(g); return g; }}
  const ring = group(0, {RING_WY});
  ring.add(OB.ring({R}, {TUBE}, {RING_BASE:#08x}, 0.32));
  const face = OB.disc(206, 54, {FACE_BASE:#08x}, 0.44); face.rotation.x = Math.PI/2; ring.add(face);
  const well = OB.disc(168, 66, {WELL_BASE:#08x}, 0.54); well.rotation.x = Math.PI/2;
  well.position.z = 16; ring.add(well);
  const pip = OB.ring(252, 17, {PIP_BASE:#08x}, 0.46); pip.position.z = -46; ring.add(pip);
"""

SEEK = """
    const sp = Math.sin(t * 0.5), co = Math.cos(t * 0.5);
    G.forEach(g => { g.rotation.x = -0.26 + sp * 0.045; g.rotation.y = 0.26 + co * 0.09; });
"""

HTML = f"""<meta charset="UTF-8">
<style>
/* FILM-META {{"duration": 6, "w": {W}, "h": {H}, "fps": 30}} */
/* BUDGET 1290 band: mast 52 + hook 288 + stage 758 + caption 80 + footer 70 + gaps 42 */
{FONTS}
:root{{
  --book:#{BOOK}; --book-dark:#{BOOK_DARK}; --kraft:#{KRAFT};
  --manilla:#{MANILLA}; --ivory:#{IVORY_GRD}; --slate:#{SLATE}; --cloud:#{CLOUD};
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

.safe{{position:absolute;top:300px;left:70px;right:130px;bottom:330px;z-index:6;
  display:flex;flex-direction:column}}
.mast{{flex-shrink:0;height:52px;display:flex;justify-content:space-between;align-items:flex-start;
  font-family:'DM Mono',monospace;font-size:21px;font-weight:500;letter-spacing:.22em;
  text-transform:uppercase;color:var(--cloud)}}
.mast .tag{{color:var(--book)}}

.hk{{flex-shrink:0;height:288px;font-family:'Anton',sans-serif;font-size:92px;line-height:.94;
  letter-spacing:-1.2px;text-transform:uppercase;color:var(--slate)}}
.hk em{{color:var(--book);font-style:normal}}

.stage{{flex:1;min-height:0}}

.cap{{flex-shrink:0;height:80px;font-size:35px;font-weight:600;line-height:1.28;
  color:rgba(25,25,25,.62)}}
.cap b{{color:var(--slate);font-weight:800}}

.foot{{flex-shrink:0;height:70px;display:flex;align-items:flex-end;gap:13px}}
.foot img{{width:32px;height:32px;border-radius:50%;object-fit:cover;opacity:.9}}
.foot span{{font-family:'DM Mono',monospace;font-size:20px;font-weight:500;letter-spacing:.16em;
  text-transform:uppercase;color:var(--cloud)}}
.foot span em{{color:var(--book);font-style:normal}}

/* the readout rides the recessed face. Orthographic: the group origin projects to its own
   screen position, so this y is solved, not eyeballed. */
.rd{{position:absolute;left:0;right:0;top:{RING_CY}px;z-index:8;text-align:center;
  transform:translateY(-50%)}}
.rd b{{display:block;font-family:'Anton',sans-serif;font-size:124px;line-height:.86;
  color:var(--slate)}}
.rd i{{display:block;font-family:'DM Mono',monospace;font-style:normal;font-size:20px;
  font-weight:500;letter-spacing:.28em;text-transform:uppercase;
  color:rgba(25,25,25,.60);margin-top:10px}}
</style>

<div id="film">
  <div class="amb"></div>
  <canvas id="gl" width="{W}" height="{H}"></canvas>
  <div class="rd"><b>41</b><i>open deals</i></div>
  <div class="safe">
    <div class="mast"><span>FILM 15 <span class="tag">/</span> PIPELINE</span><span>BEAT 1</span></div>
    <div class="hk">Claude read my whole<br>pipeline and told me<br><em>nine</em> were real.</div>
    <div class="stage"></div>
    <div class="cap">It had been <b>three weeks</b> since I last<br>looked at it honestly.</div>
    <div class="foot"><img src="data:image/png;base64,{LOGO}">
      <span>ULTRON <em>/</em> 51ULTRON<em>.</em>COM</span></div>
  </div>
</div>

{S3.scene(W, H, [], seek_js=SEEK).replace('const cards = [];', 'const cards = [];' + SCENE)}
"""

out = REPO / "content/pipeline-film-15-still.html"
out.write_text(HTML)
print(f"{out}  {len(HTML):,} chars   ring centre CSS y={RING_CY}  world y={RING_WY}")
print(f"ring base {RING_BASE:#08x} -> target render #{BOOK}")
