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
  the ramp ends at exactly 3.00s, and the frame then holds unchanged to 7.00s
  THE BAND NEVER CHANGES: 232.4 at t=0, 232.5 at t=6.9. The hook is at full strength in frame
  one and is never part of the fade. Anything that dims the hook is not this format.

So the reveal is a black sheet over the BODY and FOOTER, opacity 0.982 to 0, linear, 3.00s; the HEADER stays fixed.

THE HOOK, read off the band crop: two centred lines in a neutral grotesque, line one heavy
with a capitalised phrase inside it, line two regular. The model runs 16 and 21 characters, so
that is the budget - a longer line would have to be set smaller, and the type size is part of
the look the operator froze.

Usage:
  python3 content/_reveal.py <picture.png> "line one" "line two" --accent WORD --out <slug>
"""
import argparse, base64, importlib.util, pathlib, re, subprocess, sys

REPO = pathlib.Path(__file__).resolve().parent.parent

# measured geometry for the 1080x1350 infographic card. Header is fixed at the top; body and footer reveal below it.
BAND_TOP, BAND_H = 0, 187
PIC_TOP = BAND_TOP + BAND_H
RAMP, DUR = 3.00, 7.00
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

# THE OUTPUT CARD IS THE REQUESTED 1080x1350 INFOGRAPHIC. Header, body and footer occupy
# the full frame with no black rails: 187px header, 1003px body, 160px footer.
CARD_H = 1350
PIC_H = CARD_H - BAND_H - 160                # 1003px body
FOOT_H = CARD_H - BAND_H - PIC_H             # 160px footer
FOOT_TOP = PIC_TOP + PIC_H                   # 1190


def set_geometry(pic_h: int, foot_h: int) -> None:
    """Re-derive the card from a different picture and footer height.

    Operator 2026-08-14: "designul tb sa fie 1080x1080px tu adaugi restul pentru format 3:4" and
    "footerul e prea mare". The card stays 3:4 and the black margin above stays where the
    reference put it, so the band simply takes whatever the other two leave: at 1080 of picture
    and 108 of footer that is 252, which is also the room the split title needs. The arithmetic
    is done here rather than in three places that can disagree.
    """
    g = globals()
    g["PIC_H"], g["FOOT_H"] = pic_h, foot_h
    g["BAND_H"] = CARD_H - pic_h - foot_h
    g["PIC_TOP"] = BAND_TOP + g["BAND_H"]
    g["FOOT_TOP"] = g["PIC_TOP"] + pic_h
    g["AV_PX"] = round(foot_h * 0.41)
    g["TXT_PX"] = round(foot_h * 0.232)
    if g["BAND_H"] < 120:
        sys.exit(f"band would be {g['BAND_H']}px, too short to carry a hook")

# The vertical safe insets (CLAUDE.md 9). The card is full bleed, so the frame's rails are the
# card's rails and every element on the strip is measured against these, not against 1080.
SAFE_L, SAFE_R = 70, 130
FOOT_ROOM = CARD_W - SAFE_L - SAFE_R          # 880, all the footer ever gets

# The footer line, in one place so its length can be checked before it is drawn. Measured on the
# rendered build: 58 characters of DM Sans 600 at 30px with -.4px tracking come to 773px, so a
# character averages 13.3px. The disc and its gap take 78, leaving 802px, which is 60 characters.
# The ceiling is 59 so the estimate has a character of slack and never has to be exactly right.
#
# The handle is OFF by default (operator 2026-08-13): this set posts on a second IG account whose
# handle is long, so the frame carries "Follow ... for more" with no handle, keeping the avatar.
# --handle <name> puts one back in the hook's accent colour for the first account.
FOOT_LINE = 'Follow for more AI tools and productivity hacks'
FOOT_MAX_CHARS = 59

# The disc and the type are set by the strip, not typed twice. These are the measured defaults
# for a 160px strip; set_geometry re-derives them for any other, so "footerul e prea mare" is
# fixed by changing one number instead of three.
AV_PX, TXT_PX = 58, 30


def foot_line(handle: str | None) -> str:
    if handle:
        return f'Follow <em>{handle}</em> for more AI tools and productivity hacks'
    return 'Follow for more AI tools and productivity hacks'

# The operator's portrait, committed once and picked up by every material after it. He does not
# have to pass it, and no material has to remember to. --avatar still overrides for a one-off.
# Two names, first one wins: the short documented drop, and the name his phone exported it under
# on 2026-08-13. Renaming his commit would break the link he sent, so the resolver bends instead.
AVATARS = [REPO / "content/assets/tiberiu.jpg",
           REPO / "content/assets/tibi poza_profil_instagram_bw_square_1080.jpg"]


def find_avatar() -> pathlib.Path | None:
    return next((p for p in AVATARS if p.exists()), None)


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


# The split band's two columns, in card space. Defaults match a picture whose own columns are
# centred inside the safe box (70..950), which is where _board01pic.py puts them.
VS: tuple[str, str] | None = None
VS_CENTRES = (270, 750)
VS_MID = 510


def band_html(l1: str, l2: str, accent: str | None) -> str:
    """One band. Two rows either way; the split only changes what sits on row two."""
    if not VS:
        return (f'<div class="band">\n    <span class="l1">{hook_html(l1, accent)}</span>'
                f'\n    <span class="l2">{hook_html(l2, accent)}</span>\n  </div>')
    left, right = VS
    cl, cr = VS_CENTRES
    acc_l = " acc" if accent and accent.upper() == left.upper() else ""
    acc_r = " acc" if accent and accent.upper() == right.upper() else ""
    return (f'<div class="band vs">\n    <span class="vs-pre">{l1}</span>'
            f'\n    <div class="vs-row">'
            f'<span class="vs-rule" style="left:{VS_MID}px"></span>'
            f'<span class="vs-nm{acc_l}" style="left:{cl}px">{left}</span>'
            f'<span class="vs-nm{acc_r}" style="left:{cr}px">{right}</span>'
            f'</div>\n  </div>')


def page(pic_uri: str, l1: str, l2: str, accent: str | None,
         paper: str, hair: str, avatar: str) -> str:
    BAND_TOP, PIC_TOP = globals()["BAND_TOP"], globals()["PIC_TOP"]
    fonts = load("_fonts").embedded_css()
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<title>reveal</title>
<style>{fonts}
/* FILM-META {{"duration":{DUR},"w":1080,"h":1350,"fps":30,"beats":[{{"from":0,"to":3,"name":"reveal"}}]}} */
:root{{--acc:#C84623}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#000;display:flex;justify-content:center}}
#film{{position:relative;width:1080px;height:1350px;overflow:hidden;background:#000}}

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

/* THE SPLIT BAND. Operator 2026-08-14: "banda unica alba dar separi modelele din banda -
   folosesti doar doua randuri ca si pana acum" and "titul tb sa fie fiecare model in dreptul
   lui". So it stays ONE band of TWO rows: the shared prefix runs centred on row one, and row two
   carries the two model names, each centred over its own column in the picture below, with the
   picture's own centre rule continuing up through the band so the split is one line, not two
   boxes. No second band, no per-half background: the paper is unbroken. */
.band.vs{{gap:0;padding-top:0;justify-content:center}}
.vs-pre{{font-family:'DM Sans',sans-serif;font-weight:400;font-size:46px;line-height:1.1;
  letter-spacing:-.9px;color:#0B0B0B;white-space:nowrap;margin-bottom:10px;
  transform:translateX(-{CARD_W // 2 - VS_MID}px)}}
.vs-row{{position:relative;width:{CARD_W}px;height:82px}}
.vs-nm{{position:absolute;top:0;transform:translateX(-50%);
  font-family:'DM Sans',sans-serif;font-weight:800;font-size:70px;line-height:1.14;
  letter-spacing:-1.6px;color:#0B0B0B;white-space:nowrap}}
.vs-nm.acc{{color:var(--acc)}}
/* the rule is the picture's, carried up so the two halves read as one split sheet. It starts
   BELOW the prefix: run through it and the shared line reads as struck out. */
.vs-rule{{position:absolute;top:-8px;height:{BAND_H - 97}px;width:1px;
  background:rgba(17,17,17,.13)}}

/* THE PICTURE, square, directly under the band. */
.pic{{position:absolute;left:{SIDE}px;top:{PIC_TOP}px;width:{CARD_W}px;height:{PIC_H}px;
  overflow:hidden;background:{paper};padding:0 {PAD}px}}

/* THE FOOTER, on the strip that makes the card 3:4. It is not decoration filling a gap: the
   gap exists because the format asks for it, and an empty 160px of paper under a finished
   picture reads as a crop that went wrong. */
/* CENTRED ON THE SAFE BOX, NOT ON THE FRAME. Measured on the 2026-08-13 build: the block ran
   114..966 while the right rail starts at 950, so the last three letters of "hacks" sat under
   the like/comment/share column and were never seen, with 44px going spare on the left. The
   card is full bleed, so the frame's insets are the card's: pad 70 left and 130 right and the
   optical centre lands at 510 where it belongs. Symmetric padding is the bug; this is the fix. */
.foot{{position:absolute;left:{SIDE}px;top:{FOOT_TOP}px;width:{CARD_W}px;height:{FOOT_H}px;
  background:{paper};display:flex;align-items:center;justify-content:center;gap:20px;
  padding:0 {SAFE_R}px 0 {SAFE_L}px}}
/* THE DISC IS SET BY THE TYPE, NOT BY THE STRIP. Operator: "fa cercul mai mic in armonie cu
   restul footerului". At 80px it was half the height of the whole strip and 2.7x the type, so
   it read as a portrait with a caption beside it rather than as a footer. 58px is a shade
   under twice the 30px type and about 1.6x its line box, which is the proportion an avatar
   sits at next to a name everywhere else. The ring comes down with it: 2px of paper and 2px of
   accent, the accent held at 2 because 1 disappears once the reel is scaled to a phone. */
.foot .av{{width:{AV_PX}px;height:{AV_PX}px;border-radius:50%;object-fit:cover;flex-shrink:0;
  box-shadow:0 0 0 2px {paper},0 0 0 4px rgba(200,70,35,.34)}}
.foot .av.ph{{background:rgba(25,23,19,.10)}}
/* ONE LINE. 57 characters across the 930px the avatar and the padding leave, which sets the
   size rather than the other way round: at 38px it wrapped, and a footer that wraps in a 160px
   strip stops being a footer and becomes a second paragraph. */
.foot .txt{{font-family:'DM Sans',sans-serif;font-weight:600;font-size:{TXT_PX}px;line-height:1.2;
  letter-spacing:-.4px;color:#161412;white-space:nowrap}}
/* the handle takes the hook's accent, operator: "tiberiu.ai in culoarea de la research" */
.foot .txt em{{font-style:normal;font-weight:800;color:var(--acc)}}
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
/* The reference uses an open-bottom callout frame: rounded top corners and side rails, but no
   lower horizontal rule. The footer continues directly from the body instead of being trapped
   inside a closed box. */
.pic::after{{content:"";position:absolute;inset:0;border:3px solid #111;border-bottom:0;
  border-radius:28px 28px 0 0;pointer-events:none;z-index:2}}
/* the fade lives over the picture and NOWHERE else, because the band never dims in the model */
/* The veil covers the picture AND the footer, operator: "Follow pastreaza tonul de reveal al
   backgroundului, adica apare progresiv". The band stays outside it, as in the model. */
.veil{{position:absolute;left:0;right:0;top:{PIC_TOP}px;height:{PIC_H + FOOT_H}px;
  background:#000;opacity:{ALPHA0};z-index:4;pointer-events:none;
  animation:up {RAMP}s linear forwards 0s}}
@keyframes up{{from{{opacity:{ALPHA0}}}to{{opacity:0}}}}
</style></head>
<body>
<div id="film">
  {band_html(l1, l2, accent)}
  <div class="pic"><img src="{pic_uri}" alt=""></div>
  <div class="foot">{avatar}
    <span class="txt">{FOOT_LINE}</span>
  </div>
  <div class="veil"></div>
  <div class="edge"></div>
</div>
</body></html>
"""


def data_uri(p: pathlib.Path) -> str:
    ext = p.suffix.lstrip(".").lower().replace("jpg", "jpeg")
    return f"data:image/{ext};base64," + base64.b64encode(p.read_bytes()).decode()


def build(picture: pathlib.Path, l1: str, l2: str, accent: str | None,
          slug: str, avatar: pathlib.Path | None = None) -> pathlib.Path:
    if accent and accent.upper() not in (l1 + " " + l2 + " " + " ".join(VS or ())).upper():
        sys.exit(f"accent word {accent!r} appears in neither hook line")
    plain = re.sub(r"<[^>]+>", "", FOOT_LINE)
    if len(plain) > FOOT_MAX_CHARS:
        sys.exit(f"footer line is {len(plain)} characters, {FOOT_MAX_CHARS} fit inside the "
                 f"{FOOT_ROOM}px safe box. It would run under the right rail and lose its tail.")
    paper, hair = ground(picture)
    # The operator's portrait when there is one, and an honest empty disc when there is not,
    # rather than a stand-in face. The slot is the same either way, so dropping the real file
    # in changes one argument and nothing else.
    av = (f'<img class="av" src="{data_uri(avatar)}" alt="">' if avatar
          else '<span class="av ph"></span>')
    out = REPO / f"content/{slug}.html"
    out.write_text(page(data_uri(picture), l1, l2, accent, paper, hair, av))
    print(f"  paper {paper}   hairline {hair}   "
          f"avatar {'embedded' if avatar else 'PLACEHOLDER, pass --avatar'}")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("picture")
    ap.add_argument("line1")
    ap.add_argument("line2", nargs="?", default="")
    ap.add_argument("--accent", default=None, help="the ONE word to colour")
    ap.add_argument("--out", default="reveal")
    ap.add_argument("--render", action="store_true")
    ap.add_argument("--band-top", type=int, default=None,
                    help="override the frozen band top, e.g. to balance the black margins")
    ap.add_argument("--avatar", default=None, help="the operator's portrait for the footer")
    ap.add_argument("--handle", default=None,
                    help="put a handle back in the footer, coloured (default: no handle)")
    ap.add_argument("--pic-h", type=int, default=None, help="picture height, e.g. 1080")
    ap.add_argument("--foot-h", type=int, default=None, help="footer strip height, e.g. 108")
    ap.add_argument("--vs", nargs=2, metavar=("LEFT", "RIGHT"), default=None,
                    help="split the band: line1 is the shared prefix, these two sit on row two")
    ap.add_argument("--vs-centres", default=None, help="e.g. 270,750")
    a = ap.parse_args()
    globals()["FOOT_LINE"] = foot_line(a.handle)
    if a.pic_h or a.foot_h:
        set_geometry(a.pic_h or PIC_H, a.foot_h or FOOT_H)
    if a.vs:
        globals()["VS"] = tuple(a.vs)
        if a.vs_centres:
            globals()["VS_CENTRES"] = tuple(int(v) for v in a.vs_centres.split(","))
    if a.band_top is not None:
        globals()["BAND_TOP"] = a.band_top
        globals()["PIC_TOP"] = a.band_top + BAND_H
    av = pathlib.Path(a.avatar) if a.avatar else find_avatar()
    html = build(pathlib.Path(a.picture), a.line1, a.line2, a.accent, a.out, av)
    print(f"built  {html.relative_to(REPO)}")
    print(f"  band {BAND_TOP}..{BAND_TOP + BAND_H}   picture {PIC_TOP}..{PIC_TOP + PIC_H}   "
          f"footer {FOOT_TOP}..{FOOT_TOP + FOOT_H}")
    print(f"  card {CARD_W}x{CARD_H} = 1080x1350   "
          f"header {BAND_TOP}..{BAND_TOP + BAND_H}   body {PIC_TOP}..{PIC_TOP + PIC_H}   "
          f"footer {FOOT_TOP}..{FOOT_TOP + FOOT_H}   reveal {RAMP}s of {DUR}s")
    if a.render:
        subprocess.run([sys.executable, str(REPO / "content/_film.py"), str(html),
                        "--no-audio"], check=True)
