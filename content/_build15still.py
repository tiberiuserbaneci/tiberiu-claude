#!/usr/bin/env python3
"""Film 15, beat 1, as a still - so the proposal is looked at rather than read.

The ring is real geometry: a torus, a recessed face, a sand well and an espresso pip, taking
the studio environment and a moving key light. The 41 sits in HTML over the recessed face,
because type stays crisp in HTML and blurs in a texture.

The band is declared in pixels first and the ring is built to it, per CLAUDE.md 30. v1 sized
the ring to its own taste and the hook landed on top of it - the "nine" was unreadable on
terracotta, which is the standing "text peste continut" rejection.

    band 300..1590            column 880 wide
    mast    300..352    52
    hook    352..640   288    three lines, Anton 92, line-height .94
    stage   662..1420   758   <- THE WORKSPACE
    caption 1420..1500  80
    footer  1520..1590  70

An orthographic camera projects a group's origin to its own screen position whatever the
rotation is, so the readout's CSS y is exactly 960 - worldY. No guessing, no eyeballing.
"""
import base64, importlib.util, pathlib

REPO = pathlib.Path("/home/user/tiberiu-claude")


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


FONTS = load("_fonts").embedded_css()
S3 = load("_stage3d")
LOGO = base64.b64encode((REPO / "content/ultron-logo.png").read_bytes()).decode()

W, H = 1080, 1920
STAGE_TOP, STAGE_BOT = 662, 1420
RING_CY = (STAGE_TOP + STAGE_BOT) // 2          # 1041 in CSS
RING_WY = H // 2 - RING_CY                      # world y, y-up
R, TUBE = 300, 84                               # outer 384 -> 768 wide, 87% of the 880 column

SCENE = f"""
  const G = [];
  function group(x, y) {{ const g = new T.Group(); g.position.set(x, y, 0); scene.add(g); G.push(g); return g; }}
  const ring = group(0, {RING_WY});
  ring.add(OB.ring({R}, {TUBE}, 0xB03A17, 0.30));
  const face = OB.disc(206, 54, 0xF4EADB, 0.40); face.rotation.x = Math.PI/2; ring.add(face);
  const well = OB.disc(168, 66, 0xCDB294, 0.52); well.rotation.x = Math.PI/2;
  well.position.z = 16; ring.add(well);
  const pip = OB.ring(252, 17, 0x2E241C, 0.44); pip.position.z = -46; ring.add(pip);
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
:root{{--base:#F1EBE1;--ink:#2A2724;--muted:rgba(42,39,36,.46);--acc:#B03A17;--esp:#2E241C;}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#0C0C0B;display:flex;justify-content:center;align-items:flex-start;
  font-family:'Plus Jakarta Sans',sans-serif;-webkit-font-smoothing:antialiased}}
#film{{width:{W}px;height:{H}px;position:relative;overflow:hidden;background:var(--base);
  color:var(--ink)}}
.amb{{position:absolute;inset:0;z-index:0;
  background:radial-gradient(ellipse 66% 34% at 50% 4%,rgba(176,58,23,.09) 0%,transparent 64%),
    radial-gradient(ellipse 58% 32% at 50% 100%,rgba(205,178,148,.22) 0%,transparent 62%),
    linear-gradient(178deg,#F6F1E9 0%,#F1EBE1 48%,#E7DECF 100%)}}
#gl{{position:absolute;inset:0;z-index:1;pointer-events:none}}

.safe{{position:absolute;top:300px;left:70px;right:130px;bottom:330px;z-index:6;
  display:flex;flex-direction:column}}
.mast{{flex-shrink:0;height:52px;display:flex;justify-content:space-between;align-items:flex-start;
  font-family:'DM Mono',monospace;font-size:21px;font-weight:500;letter-spacing:.22em;
  text-transform:uppercase;color:var(--muted)}}
.mast .tag{{color:var(--acc)}}

.hk{{flex-shrink:0;height:288px;font-family:'Anton',sans-serif;font-size:92px;line-height:.94;
  letter-spacing:-1.2px;text-transform:uppercase}}
.hk em{{color:var(--acc);font-style:normal}}

.stage{{flex:1;min-height:0}}

.cap{{flex-shrink:0;height:80px;font-size:35px;font-weight:600;line-height:1.28;
  color:rgba(42,39,36,.70)}}
.cap b{{color:var(--ink);font-weight:800}}

.foot{{flex-shrink:0;height:70px;display:flex;align-items:flex-end;gap:13px}}
.foot img{{width:32px;height:32px;border-radius:50%;object-fit:cover;opacity:.9}}
.foot span{{font-family:'DM Mono',monospace;font-size:20px;font-weight:500;letter-spacing:.16em;
  text-transform:uppercase;color:var(--muted)}}
.foot span em{{color:var(--acc);font-style:normal}}

/* the readout rides the recessed face. Orthographic: the group origin projects to its own
   screen position, so this y is solved, not eyeballed. */
.rd{{position:absolute;left:0;right:0;top:{RING_CY}px;z-index:8;text-align:center;
  transform:translateY(-50%)}}
.rd b{{display:block;font-family:'Anton',sans-serif;font-size:124px;line-height:.86;
  color:var(--esp)}}
.rd i{{display:block;font-family:'DM Mono',monospace;font-style:normal;font-size:20px;
  font-weight:500;letter-spacing:.28em;text-transform:uppercase;
  color:rgba(46,36,28,.58);margin-top:10px}}
</style>

<div id="film">
  <div class="amb"></div>
  <canvas id="gl" width="{W}" height="{H}"></canvas>
  <div class="rd"><b>41</b><i>open deals</i></div>
  <div class="safe">
    <div class="mast"><span>FILM 15 <span class="tag">/</span> PIPELINE</span><span>BEAT 1</span></div>
    <div class="hk"><em>Claude</em> read my whole<br>pipeline and told me<br><em>nine</em> were real.</div>
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
