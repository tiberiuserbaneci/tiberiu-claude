#!/usr/bin/env python3
"""Cut the film's shot list out of one photographic plate, and inline it into the film.

The operator's note was "am vrut niste imagini pe movie" - images in the film, not one
photograph blurred into a backdrop. Two things were wrong with the first pass:

1. The crops were cut far shorter than the frame. A 1080x537 crop behind `background-size:
   cover` on a 1080x1920 layer is upscaled 3.6x vertically, so every trace of the picture
   died before the blur ever touched it. That is why the beat-3 frame read as black. The
   plate is natively 9:16, so every crop here is taken AT 9:16 and only ever scaled down.
2. Two of the five layers carried the same crop, so beat 4 repeated beat 2's picture. That
   is the CLAUDE.md 30 variety rule, which names films explicitly: the object carrying beat
   2 may not be the object carrying beat 4. The SHOTS table below is the single declaration
   of the run, and `inline()` asserts the five crops are distinct before writing.

Blur is baked into the asset, never applied as a CSS filter: a `blur()` over five stacked
full-frame photographs is recomputed on every captured frame and pushed the render past
260ms/frame. Baked, it costs nothing.

Usage:
  python3 content/_plate.py            # cut, blur, and inline into the film
  python3 content/_plate.py --sheet    # also write a contact sheet to review the cuts
"""
import base64, functools, io, pathlib, re, sys

from PIL import Image, ImageEnhance, ImageFilter

print = functools.partial(print, flush=True)  # noqa: A001

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEX = ROOT / "content" / "assets" / "tex"
PLATE = TEX / "desk.jpg"
FILM = ROOT / "content" / "pitch-film-09.html"

AR = 1080 / 1920  # every cut is taken at the frame's aspect so `cover` never upscales it

# The exposure is solved, not guessed. Each shot declares the mean luminance it should land
# on and `expose()` measures its way there, so the grade lives in one file instead of being
# split between a baked multiplier here and a `filter:brightness()` in the film. The five
# targets are deliberately not equal - a film that holds one exposure for forty seconds reads
# as a slideshow - but they sit close enough that no beat drops out of the picture.
# name        centre x, centre y (fraction of plate), width (fraction), blur, warmth, target
SHOTS = [
    ("wide",    0.50, 0.44, 1.00,  8, 1.00, 58),   # b1  the room, establishing, under the hook
    ("blinds",  0.22, 0.33, 0.44, 10, 0.94, 66),   # b2  window slats, cool verticals
    ("screen",  0.61, 0.40, 0.40, 11, 0.98, 62),   # b3  the monitor and its glow
    ("lamp",    0.52, 0.48, 0.44,  9, 1.10, 70),   # b4  laptop and the warm pool, the high point
    ("surface", 0.46, 0.56, 0.62, 12, 1.06, 60),   # b5  desk top, the light on the wood
]


def cut(im, cx, cy, fw):
    """A 9:16 box centred on the point, clamped inside the plate."""
    w = round(im.width * fw)
    h = round(w / AR)
    if h > im.height:                       # never invent pixels the plate does not have
        h = im.height
        w = round(h * AR)
    x = min(max(round(im.width * cx - w / 2), 0), im.width - w)
    y = min(max(round(im.height * cy - h / 2), 0), im.height - h)
    return im.crop((x, y, x + w, y + h))


def mean_luma(im):
    g = im.convert("L")
    return sum(v * c for v, c in enumerate(g.histogram())) / (g.width * g.height)


def soften(im, blur):
    """Blur at the delivery size - blurring then downscaling would blur the picture twice."""
    return im.resize((900, 1600), Image.LANCZOS).filter(ImageFilter.GaussianBlur(blur))


def expose(im, blur, target):
    """Solve the gain that puts the delivered frame on its target mean.

    Brightness is a straight multiply, so one ratio lands close; highlights clip on the
    brighter crops, which is exactly where a single ratio undershoots, so it corrects twice.
    """
    gain = 1.0
    for _ in range(3):
        got = mean_luma(soften(ImageEnhance.Brightness(im).enhance(gain), blur))
        if abs(got - target) < 0.6:
            break
        gain *= target / max(got, 1.0)
    return ImageEnhance.Brightness(im).enhance(gain), gain


def build():
    plate = Image.open(PLATE).convert("RGB")
    out = []
    for name, cx, cy, fw, blur, warm, target in SHOTS:
        im = cut(plate, cx, cy, fw).resize((1080, 1920), Image.LANCZOS)
        if warm != 1.0:                     # warmth as a channel gain, not a colour overlay
            r, g, b = im.split()
            r = r.point(lambda v, k=warm: min(255, int(v * k)))
            b = b.point(lambda v, k=2 - warm: min(255, int(v * k)))
            im = Image.merge("RGB", (r, g, b))
        im, gain = expose(im, blur, target)
        im.save(TEX / f"{name}.jpg", quality=90)
        soft = soften(im, blur)
        buf = io.BytesIO()
        soft.save(buf, "JPEG", quality=80)
        (TEX / f"{name}-b.jpg").write_bytes(buf.getvalue())
        out.append((name, buf.getvalue()))
        print(f"  {name:9} blur {blur:2}  warm {warm:.2f}  gain {gain:.2f}  "
              f"mean {mean_luma(soft):5.1f} (target {target})  {len(buf.getvalue()):,}b")
    return out


def sheet(shots):
    s = Image.new("RGB", (260 * len(shots), 462))
    for i, (name, raw) in enumerate(shots):
        s.paste(Image.open(io.BytesIO(raw)).resize((260, 462)), (260 * i, 0))
    p = TEX / "_sheet.jpg"
    s.save(p, quality=88)
    print(f"  sheet -> {p}")
    return p


def inline(shots):
    if len({raw for _, raw in shots}) != len(shots):
        sys.exit("two shot layers carry the same picture - see CLAUDE.md 30 GRAPHIC VARIETY")
    html = FILM.read_text()
    for i, (name, raw) in enumerate(shots, 1):
        uri = "data:image/jpeg;base64," + base64.b64encode(raw).decode()
        html, n = re.subn(rf'(class="sh sh{i}" style="background-image:url\()[^)]*(\))',
                          lambda m, u=uri: m.group(1) + u + m.group(2), html)
        if n != 1:
            sys.exit(f"sh{i} layer not found in {FILM.name} (matched {n})")
        print(f"  sh{i} <- {name}")
    FILM.write_text(html)
    print(f"  {FILM.name} rewritten, {len(html):,} chars")


if __name__ == "__main__":
    shots = build()
    if "--sheet" in sys.argv:
        sheet(shots)
    inline(shots)
