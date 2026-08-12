#!/usr/bin/env python3
"""Six second Instagram reel: a title that holds, then the sheet fills in under it.

THE BRIEF (operator, 2026-08-12): "in primele 2.5 secunde se vede doar titlul dupa care se
face reveal la continut. nu stiu cum sa fac asta sa nu se simta diferenta de text din titlu,
fundal si restul."

WHY THAT NORMALLY FEELS LIKE TWO MATERIALS, AND WHAT IS DONE ABOUT IT HERE. Four causes, and
the page is built against all four:

  1  THE TITLE MOVES. The usual build centres the title big during the hold, then shrinks it
     into a header. That single move is the moment the eye files it as two designs. Here the
     title is at its final size, in its final position, at full opacity, in frame ONE, and it
     never moves again. It does not even have an entrance. The first frame is the strongest
     frame and there is nothing to reconcile later.
  2  THE GROUND CHANGES. A clean title card cutting into a busy layout is two rooms. One
     paper, one grain, one bloom, one light, start to finish.
  3  THE STRUCTURE ARRIVES WITH THE CONTENT. This is the real one. Hold a title over an empty
     page for 2.5 seconds of a 6 second reel and 42 percent of the film is a dead frame,
     which is exactly where the audience leaves. So the whole sheet is present from the first
     frame - spine, five nodes, five dividers, five SYSTEM numerals - just EMPTY and quiet.
     The viewer reads a form waiting to be filled, which also telegraphs that five things are
     coming. Straight out of episode 05 (accumulate, never crossfade) and out of the note in
     PARALLEL-SESSION.md: rows legible from the seam at low opacity, brightening on their
     span, because hiding them leaves an empty frame right after the scroll stop.
  4  THE REVEAL IS A CUT OR A DISSOLVE. During a dissolve the frame holds neither state. So
     nothing here is ever removed or crossfaded: coverage only ever rises.

TIMING. 6.0s at 30fps.
  0.00        everything present. Title readable, skeleton at 14 to 30 percent ink.
  0.55 - 1.55 the spine draws downward. Motion, but nothing new to read.
  0.95 - 1.95 the five nodes and their numerals settle in sequence.
  2.50        reveal opens, one station every 0.26s, each 0.5s long.
  4.04 - 6.00 the complete board holds for 1.96s. That is the frame worth sending, and a send
              carries 3 to 5x a like for unconnected reach, so it may not be a flash.
A slow push in runs the whole 6s so the final hold is never a frozen frame.

THE LOOP SEAM. A build reveal cannot loop invisibly: at 6.0s the filled board is replaced by
an empty one. The seam is made as soft as it can be by keeping the paper, the title, the
skeleton and the footer pixel identical at t=0 and t=6, so the loop reads as the content
resetting rather than as a different picture arriving.

WORD BUDGET. The reference graphic carries about 200 words of body copy. At 0.7s per station
nobody reads any of it, so the body is gone: five names, five tools, five outcomes, about 30
words total, plus the title.

THIRD PARTY NAMES. CLAUDE.md 21 allows Claude, AI and Ultron and nothing else. The operator
SUSPENDED that for this material on 2026-08-12, choosing to keep the five real products. It is
a scoped exception for this file, not a rewrite of the rule, so 21 still binds everywhere else.
The names are set in type only - no third party logos are drawn, which is a separate permission
under CLAUDE.md 18 and was not given.

Build:  python3 content/_toolkit_reel.py
Render: python3 content/_film.py content/creator-toolkit-film-6s.html --no-audio
"""
import base64, importlib.util, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO / "content" / "creator-toolkit-film-6s.html"


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


# The reveal clock. One place, so a change to the pacing cannot half apply.
HOLD = 2.50          # the title owns the frame until here
STEP = 0.26          # one station to the next
DUR = 6.0

# name, tool, outcome. The outcome is deliberately the quietest thing in the row: at 0.26s
# apart the eye takes the name and the tool, and the outcome is what a rewatch is for -
# and on this platform a rewatch is the top ranking signal.
ROWS = [
    ("Ideate &amp; research", "ChatGPT",    "Ideate faster"),
    ("Copywriting engine",    "Copy.ai",    "Create content"),
    ("Visual design suite",   "Canva",      "Save time daily"),
    ("Creative generation",   "Midjourney", "Grow your audience"),
    ("Workflow management",   "Notion",     "Monetize your work"),
]


def rows_html() -> str:
    out = []
    for i, (name, tool, res) in enumerate(ROWS, 1):
        out.append(f"""    <div class="row r{i}">
      <span class="node"></span>
      <span class="div"></span>
      <span class="rl">
        <span class="sys">System {i:02d}</span>
        <span class="name">{name}</span>
        <span class="tool">{tool}</span>
      </span>
      <span class="out">{res}</span>
    </div>""")
    return "\n".join(out)


def station_css() -> str:
    """Per station delays, all measured off the one HOLD clock."""
    css = []
    for i in range(1, 6):
        t = HOLD + (i - 1) * STEP
        settle = 0.95 + (i - 1) * 0.20
        css.append(
            f".r{i} .node{{animation:pop .42s var(--eo) both {settle:.2f}s,"
            f"fill .40s var(--e) forwards {t:.2f}s}}\n"
            f".r{i} .div{{animation:draw .55s var(--e) both {settle + 0.15:.2f}s}}\n"
            f".r{i} .sys{{animation:dim .50s var(--e) both {settle + 0.25:.2f}s}}\n"
            f".r{i} .name{{animation:rise .50s var(--eo) both {t:.2f}s}}\n"
            f".r{i} .tool{{animation:rise .50s var(--eo) both {t + 0.07:.2f}s}}\n"
            f".r{i} .out{{animation:fade .50s var(--e) both {t + 0.13:.2f}s}}")
    return "\n".join(css)


def page() -> str:
    fonts = load("_fonts").embedded_css()
    logo = base64.b64encode((REPO / "content" / "ultron-logo.png").read_bytes()).decode()
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>AI CREATOR TOOLKIT - 6s reel</title>
<style>{fonts}
/* FILM-META {{"duration":{DUR},"w":1080,"h":1920,"beats":[]}} */
:root{{
  --paper:#F5ECE3;
  --ink:#111111;
  --ink70:rgba(17,17,17,.70);
  --ink45:rgba(17,17,17,.46);
  --ink26:rgba(17,17,17,.26);
  --ink14:rgba(17,17,17,.14);
  --rule:rgba(17,17,17,.13);
  --acc:#C84623;
  --acc2:#D26446;
  --e:cubic-bezier(.4,0,.2,1);
  --eo:cubic-bezier(.05,.7,.1,1);
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#000;display:flex;justify-content:center}}
#film{{position:relative;width:1080px;height:1920px;overflow:hidden;
  background:var(--paper);color:var(--ink);isolation:isolate}}

/* ONE GROUND, START TO FINISH. Paper tone, a warm bloom top left where the light falls, and
   grain over both so the gradient cannot band. All of it inside one painted layer so the
   blur rasterises once instead of on all 180 frames. */
.bg{{position:absolute;inset:0;z-index:0;contain:paint}}
.bg::before{{content:'';position:absolute;inset:-10%;
  background:radial-gradient(ellipse 60% 40% at 12% 4%,rgba(200,70,35,.10) 0%,transparent 62%),
    radial-gradient(ellipse 54% 38% at 96% 92%,rgba(17,17,17,.07) 0%,transparent 64%)}}
.bg::after{{content:'';position:absolute;inset:0;opacity:.5;
  background-image:url("data:image/svg+xml;utf8,\
<svg xmlns='http://www.w3.org/2000/svg' width='150' height='150'>\
<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.86' numOctaves='3'/>\
<feColorMatrix type='saturate' values='0'/></filter>\
<rect width='150' height='150' filter='url(%23n)' opacity='.42'/></svg>")}}

/* THE SAFE BAND, CLAUDE.md 9, plus a 10px buffer on every side so the slow push in cannot
   walk the content out of it. Measured at 1.014 the band grows 12px across and 18px down,
   which is 4px and 6px per edge, and the buffer covers both. */
.safe{{position:absolute;top:310px;left:80px;right:140px;bottom:340px;z-index:2;
  display:flex;flex-direction:column;
  transform-origin:50% 50%;animation:push {DUR}s var(--e) both 0s}}

/* THE TITLE DOES NOT ARRIVE AND DOES NOT MOVE. No entrance, no transform, no opacity ramp:
   it is simply there in frame one, at the size and position it keeps for all six seconds.
   Every other element in the file animates; this block is the fixed point they move against,
   and that is the whole reason the reveal reads as one material. */
.head{{flex-shrink:0}}
.kick{{display:block;font-family:'DM Mono',monospace;font-weight:500;font-size:22px;
  letter-spacing:.30em;text-transform:uppercase;color:var(--acc);margin-bottom:20px}}
h1{{font-family:'Anton',sans-serif;font-size:104px;line-height:.90;letter-spacing:-1.6px;
  text-transform:uppercase;color:var(--ink)}}
.sub{{display:block;margin-top:18px;font-family:'DM Sans',sans-serif;font-weight:700;
  font-size:31px;letter-spacing:-.2px;color:var(--ink45)}}
.hr{{flex-shrink:0;height:2px;background:var(--ink);opacity:.16;margin:30px 0 0}}

/* THE SHEET IS PRESENT AND EMPTY FROM FRAME ONE. */
.list{{position:relative;flex:1;min-height:0;display:flex;flex-direction:column;
  padding-left:76px}}
/* THE HOLD MAY NOT BE A FROZEN FRAME (CLAUDE.md 30). Once the board completes at 4.04s the
   only thing still moving is the push in, and at 1.4 percent over six seconds that is about
   two pixels a second: the retention guard read the last stretch as dead, and it was right.
   So a light band walks down the five rows through the hold. It adds nothing and removes
   nothing, which keeps the accumulation intact, and the motion is on message - it reads the
   five in order and leads the eye back to the top for the loop. Its own element, because a
   second animation on a row would replace the one already running there. */
/* Left edge sits INSIDE the safe box, not tucked under the spine. At -52px it started at
   x=28 and hung 42px past the 70px inset, which is the halo class of mistake all over again:
   the element that decorates is the one nobody thinks to measure. */
.scan{{position:absolute;left:8px;right:6px;top:0;height:20%;border-radius:16px;
  background:linear-gradient(90deg,rgba(200,70,35,.13) 0%,rgba(200,70,35,.03) 68%,
    transparent 100%);opacity:0;pointer-events:none;
  animation:scan 1.86s var(--e) both 4.04s}}
.spine{{position:absolute;left:20px;top:26px;bottom:26px;width:2px;background:var(--ink26);
  transform-origin:50% 0;animation:draw 1.00s var(--e) both .55s}}
.row{{position:relative;flex:1;display:flex;align-items:center;justify-content:space-between;
  gap:26px}}
.node{{position:absolute;left:-66px;top:50%;width:22px;height:22px;margin-top:-11px;
  border-radius:50%;background:var(--paper);
  box-shadow:inset 0 0 0 2.5px var(--ink26)}}
.div{{position:absolute;left:-44px;right:0;bottom:0;height:1px;background:var(--rule);
  transform-origin:0 50%}}
.row:last-child .div{{display:none}}
.rl{{display:flex;flex-direction:column;gap:9px;min-width:0}}
.sys{{font-family:'DM Mono',monospace;font-weight:500;font-size:20px;letter-spacing:.24em;
  text-transform:uppercase;color:var(--ink26)}}
.name{{font-family:'DM Sans',sans-serif;font-weight:900;font-size:45px;line-height:1;
  letter-spacing:-1px;color:var(--ink)}}
.tool{{font-family:'DM Sans',sans-serif;font-weight:700;font-size:33px;line-height:1;
  letter-spacing:-.4px;color:var(--acc)}}
.out{{flex-shrink:0;max-width:246px;text-align:right;font-family:'DM Mono',monospace;
  font-weight:500;font-size:20px;line-height:1.42;letter-spacing:.14em;
  text-transform:uppercase;color:var(--ink45)}}

/* CLAUDE.md 11, as rewritten 2026-08-09: the wordmark identifies, a domain is a reach
   penalty every platform reads out of the image. The link lives in the caption. */
.foot{{flex-shrink:0;display:flex;align-items:center;gap:14px;padding-top:26px;
  border-top:2px solid var(--ink14)}}
.foot img{{width:34px;height:34px;border-radius:50%;object-fit:cover}}
.foot span{{font-family:'DM Mono',monospace;font-weight:500;font-size:21px;
  letter-spacing:.34em;text-transform:uppercase;color:var(--ink70)}}

@keyframes push{{from{{transform:scale(1)}}to{{transform:scale(1.009)}}}}
@keyframes draw{{from{{transform:scaleY(0)}}to{{transform:scaleY(1)}}}}
@keyframes pop{{from{{transform:scale(.4);opacity:0}}to{{transform:scale(1);opacity:1}}}}
@keyframes dim{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes fade{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes scan{{
  0%{{opacity:0;transform:translateY(0)}}
  9%{{opacity:1}}
  84%{{opacity:1}}
  100%{{opacity:0;transform:translateY(400%)}}}}
@keyframes rise{{from{{opacity:0;transform:translateY(16px)}}
  to{{opacity:1;transform:translateY(0)}}}}
/* the node does not re-enter on reveal, it FILLS: nothing is added, the existing ring
   becomes solid, which is accumulation rather than a second arrival */
@keyframes fill{{from{{background:var(--paper);box-shadow:inset 0 0 0 2.5px var(--ink26)}}
  to{{background:var(--acc);box-shadow:inset 0 0 0 2.5px var(--acc)}}}}
/* the divider draws sideways, so give it its own axis rather than the spine's */
.div{{animation-name:drawx}}
@keyframes drawx{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}

{station_css()}
</style></head>
<body>
<div id="film">
  <div class="bg"></div>
  <div class="safe">
    <div class="head">
      <span class="kick">The creator stack</span>
      <h1>AI creator<br>toolkit</h1>
      <span class="sub">Five systems. One stack.</span>
    </div>
    <div class="hr"></div>
    <div class="list">
      <span class="spine"></span>
      <span class="scan"></span>
{rows_html()}
    </div>
    <div class="foot">
      <img src="data:image/png;base64,{logo}" alt="">
      <span>Ultron</span>
    </div>
  </div>
</div>
</body></html>
"""


if __name__ == "__main__":
    OUT.write_text(page())
    print(f"built  {OUT.relative_to(REPO)}")
    print(f"  hold {HOLD}s   step {STEP}s   complete "
          f"{HOLD + 4 * STEP + 0.5:.2f}s   duration {DUR}s")
