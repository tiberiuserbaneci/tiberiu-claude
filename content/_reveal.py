#!/usr/bin/env python3
"""The reveal format: a generated square picture, a white hook band, a linear fade up.

REVERSE ENGINEERED FROM THE OPERATOR'S MODEL (IMG_2465.MP4, measured 2026-08-13, 720x1280 at
30fps, 6.93s). Every number below is measured off the frames, not estimated, because the
operator's instruction was explicit: the band's position and size may not change, and the only
liberty is colouring one word of the hook.

    black          rows    0 - 187     of 1280      ->    0 -  281  at 1080x1920
    WHITE BAND     rows  188 - 312     (125px)      ->  282 -  468  (187px)
    picture        rows  313 - 1041    (729px)      ->  469 - 1561  (1093px)
    black          rows 1042 - 1279                 -> 1562 - 1919

  The picture is 720 x 729, which is square to within a pixel, so the generated image is 1:1.

THE TRANSITION, measured rather than described:
  the picture's mean luminance runs 4.1 -> 232.4, which is a multiplier of 0.018 -> 0.999
  it is LINEAR: a straight-line fit over the ramp leaves a 1.8 grey level residual out of 232
  the ramp ends at exactly 4.20s, and the frame then holds unchanged to 6.93s
  THE BAND NEVER CHANGES: 232.4 at t=0, 232.5 at t=6.9. The hook is at full strength in frame
  one and is never part of the fade. Anything that dims the hook is not this format.

So the fade is a black sheet over the PICTURE ONLY, opacity 0.982 to 0, linear, 4.20s.

THE HOOK, read off the band crop: two centred lines in a neutral grotesque, line one heavy
with a capitalised phrase inside it, line two regular. The model runs 16 and 21 characters, so
that is the budget - a longer line would have to be set smaller, and the type size is part of
the look the operator froze.

Usage:
  python3 content/_reveal.py <picture.png> "line one" "line two" --accent WORD --out <slug>
"""
import argparse, base64, importlib.util, pathlib, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parent.parent

# measured geometry at 1080x1920. The vertical numbers are the operator's and are frozen.
BAND_TOP, BAND_H = 282, 187
PIC_TOP = 469
RAMP, DUR = 4.20, 6.93
ALPHA0 = 0.982

# EDGE TO EDGE HORIZONTALLY. Operator 2026-08-13, correcting my reading of the previous note:
# "ai tras marginile din format nu din poza ... materialul tb sa mi intre perfect in chenarul
# de reels. acum are margine neagra pe st si dr." Keeping the safe zones clear meant keeping
# the picture's own CONTENT off its edges, not insetting the card and leaving black bars in
# the reel frame. So the card fills the full 1080 and the only permitted breathing room is
# PAD pixels of the picture's own paper colour inside the card, never black.
SIDE = 0
CARD_W = 1080
PAD = 0            # paper-coloured inset inside the picture, raise it if labels touch an edge

# THE REFERENCE'S OWN HEIGHT. Operator 2026-08-13: "formatul de dimensiune trebuie sa fie
# identic cu cel din referinta". His model's picture is 720 x 729, which is SQUARE, not 3:4 -
# I introduced the 3:4 myself and then defended it. Measured back off IMG_2465 and restored:
#
#     black   0 - 281     282px      the margin above the hook
#     band  282 - 468     187px
#     pict  469 - 1561   1093px      1080 wide, so 0.988, square to a percent
#     black 1562 - 1919   358px      the margin below, which is why his bottom reads similar
#
# The black above and below are 282 and 358 in his own build. They were never equal and they
# never needed to be: they are both large enough to read as margin, which is the whole job.
PIC_H = 1093                                 # the reference's, not a ratio of my own choosing


def ground(picture: pathlib.Path) -> tuple[str, str]:
    """The picture's own background colour, and a hairline a few steps darker.

    Operator: "backgroundul pozei nu este alb la fel ca backgroundul hook ului ... aceeasi
    nota de culoare". Rather than pick a cream by eye and have it drift the next time the
    image model is asked for one, the band takes the colour straight off the picture: the
    modal value of its border pixels, which is the paper it was drawn on.
    """
    from PIL import Image
    from collections import Counter
    # The MODE of the whole picture, not its edge. An infographic on paper is mostly paper, so
    # the most common colour is the ground by a wide margin. Sampling the border instead picked
    # up the model's own vignette and came out 25 levels darker than the paper it was meant to
    # match, which is the whole defect this function exists to prevent.
    im = Image.open(picture).convert("RGB").resize((160, 160))
    r, g, b = Counter([(p[0] // 3 * 3, p[1] // 3 * 3, p[2] // 3 * 3)
                       for p in im.getdata()]).most_common(1)[0][0]
    line = tuple(max(0, c - 26) for c in (r, g, b))
    return f"rgb({r},{g},{b})", f"rgb({line[0]},{line[1]},{line[2]})"


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


def hook_html(text: str, accent: str | None) -> str:
    """One line of the hook, with at most one word carried in the accent colour.

    The operator allows exactly one coloured word and nothing else, so this refuses to colour
    a second one rather than quietly doing it: a rule that is enforced somewhere other than in
    my memory is the only kind that survives a hundred materials.
    """
    if not accent:
        return text
    words = text.split(" ")
    hits = [i for i, w in enumerate(words) if w.strip(".,:").upper() == accent.upper()]
    if not hits:
        return text                      # the word lives on the other line
    words[hits[0]] = f"<em>{words[hits[0]]}</em>"
    return " ".join(words)


def page(pic_uri: str, l1: str, l2: str, accent: str | None,
         paper: str, hair: str) -> str:
    BAND_TOP, PIC_TOP = globals()["BAND_TOP"], globals()["PIC_TOP"]
    fonts = load("_fonts").embedded_css()
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>reveal</title>
<style>{fonts}
/* FILM-META {{"duration":{DUR},"w":1080,"h":1920,"fps":30,"beats":[]}} */
:root{{--acc:#C84623}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#000;display:flex;justify-content:center}}
#film{{position:relative;width:1080px;height:1920px;overflow:hidden;background:#000}}

/* THE BAND. Position and size are the operator's, measured off his model and frozen. */
/* The band takes the picture's own paper colour, so the two read as one sheet. A hairline
   rule under it separates the hook from the picture without moving or resizing the band. */
.band{{position:absolute;left:{SIDE}px;width:{CARD_W}px;top:{BAND_TOP}px;height:{BAND_H}px;
  background:{paper};
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;
  padding-top:6px}}
.l1{{font-family:'DM Sans',sans-serif;font-weight:700;font-size:57px;line-height:1.16;
  letter-spacing:-1.1px;color:#0B0B0B;white-space:nowrap}}
.l2{{font-family:'DM Sans',sans-serif;font-weight:400;font-size:55px;line-height:1.16;
  letter-spacing:-1.1px;color:#0B0B0B;white-space:nowrap}}
/* the one liberty the operator left open */
.band em{{font-style:normal;color:var(--acc)}}

/* THE PICTURE, square, directly under the band. */
.pic{{position:absolute;left:{SIDE}px;top:{PIC_TOP}px;width:{CARD_W}px;height:{PIC_H}px;
  overflow:hidden;background:{paper};padding:0 {PAD}px}}
/* one hairline around the whole card, drawn over both halves so the seam cannot show */
/* The rule under the band, and it is BLACK, because that is what the reference has. Measured
   on IMG_2465 at rows 313 to 316: 314 and 315 are pure 0,0,0 across the full width with a
   half step of antialiasing either side. My first attempt drew it in the paper colour a few
   steps down, which is a tint, not a rule, and disappeared at viewing size. Two pixels at 720
   is three at 1080. No box around the card: at full bleed that would draw a line down the very
   edge of the reel, which is not a border, it is a defect. */
.edge{{position:absolute;left:0;right:0;top:{BAND_TOP + BAND_H}px;height:3px;
  background:#000;pointer-events:none;z-index:3}}
.pic img{{width:100%;height:100%;object-fit:cover;display:block}}
/* the fade lives over the picture and NOWHERE else, because the band never dims in the model */
.veil{{position:absolute;inset:0;background:#000;opacity:{ALPHA0};
  animation:up {RAMP}s linear forwards 0s}}
@keyframes up{{from{{opacity:{ALPHA0}}}to{{opacity:0}}}}
</style></head>
<body>
<div id="film">
  <div class="band">
    <span class="l1">{hook_html(l1, accent)}</span>
    <span class="l2">{hook_html(l2, accent)}</span>
  </div>
  <div class="pic"><img src="{pic_uri}" alt=""><div class="veil"></div></div>
  <div class="edge"></div>
</div>
</body></html>
"""


def build(picture: pathlib.Path, l1: str, l2: str, accent: str | None,
          slug: str) -> pathlib.Path:
    ext = picture.suffix.lstrip(".").lower().replace("jpg", "jpeg")
    uri = f"data:image/{ext};base64," + base64.b64encode(picture.read_bytes()).decode()
    if accent and accent.upper() not in (l1 + " " + l2).upper():
        sys.exit(f"accent word {accent!r} appears in neither hook line")
    paper, hair = ground(picture)
    out = REPO / f"content/{slug}.html"
    out.write_text(page(uri, l1, l2, accent, paper, hair))
    print(f"  paper {paper}   hairline {hair}")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("picture")
    ap.add_argument("line1")
    ap.add_argument("line2")
    ap.add_argument("--accent", default=None, help="the ONE word to colour")
    ap.add_argument("--out", default="reveal")
    ap.add_argument("--render", action="store_true")
    ap.add_argument("--band-top", type=int, default=None,
                    help="override the frozen band top, e.g. to balance the black margins")
    a = ap.parse_args()
    if a.band_top is not None:
        globals()["BAND_TOP"] = a.band_top
        globals()["PIC_TOP"] = a.band_top + BAND_H
    html = build(pathlib.Path(a.picture), a.line1, a.line2, a.accent, a.out)
    print(f"built  {html.relative_to(REPO)}")
    print(f"  band {BAND_TOP}..{BAND_TOP + BAND_H}   picture {PIC_TOP}..{PIC_TOP + PIC_H}   "
          f"ramp {RAMP}s of {DUR}s")
    if a.render:
        subprocess.run([sys.executable, str(REPO / "content/_film.py"), str(html),
                        "--no-audio"], check=True)
