#!/usr/bin/env python3
"""Composite a real brand logo into the empty centre of an ARK-generated hub picture.

The operator wants the master-reference hub aesthetic (ARK/Seedream), but ARK mangles real brand
logos. So ARK draws the hub with a clean empty white centre circle, and this places the real logo
(a vendored SVG) into it. The circle is found by density, not a hard-coded box, so it survives
ARK moving the centre a few pixels between generations.

    python3 content/_center_logo.py <hub.jpg> <logo.svg> <out.jpg> [--scale 0.56] [--ink #111]
"""
import argparse, glob, pathlib, re, sys
from PIL import Image
import numpy as np

REPO = pathlib.Path(__file__).resolve().parent.parent


def rasterize(svg_path: pathlib.Path, px: int, ink: str) -> Image.Image:
    from playwright.sync_api import sync_playwright
    svg = re.sub(r"<title>.*?</title>", "", svg_path.read_text(), flags=re.S)
    svg = re.sub(r'\swidth="[^"]*"', "", svg)
    svg = re.sub(r'\sheight="[^"]*"', "", svg)
    html = (f'<!doctype html><meta charset=utf-8>'
            f'<style>html,body{{margin:0;background:transparent}}'
            f'#w{{width:{px}px;height:{px}px;display:flex;align-items:center;'
            f'justify-content:center}}svg{{width:{int(px*.95)}px;height:{int(px*.95)}px;'
            f'color:{ink}}}</style><div id=w>{svg}</div>')
    tmp = REPO / "content/_logo_tmp.html"
    tmp.write_text(html)
    exe = next((h for p in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",)
                for h in sorted(glob.glob(p))), None)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe)
        pg = b.new_page(viewport={"width": px, "height": px}, device_scale_factor=2)
        pg.goto(tmp.as_uri()); pg.wait_for_timeout(400)
        pg.locator("#w").screenshot(path=str(REPO / "content/_logo_tmp.png"), omit_background=True)
        b.close()
    tmp.unlink(missing_ok=True)
    img = Image.open(REPO / "content/_logo_tmp.png").convert("RGBA")
    (REPO / "content/_logo_tmp.png").unlink(missing_ok=True)
    return img


def find_circle(base: Image.Image) -> tuple[int, int, int]:
    """The empty centre disc, found by brightness inside a central window.

    ARK's disc is a warm off-white (a centre pixel measured 248,245,238), not neutral, so a
    "neutral white" test misses it; and once the hub grows a faint guide ring and tick marks a
    density scan latches onto the wrong dense strip. The disc is simply the brightest large mass
    in the middle of the frame, so mask bright pixels, ignore the outer third where the cards and
    ring live, and take the bounding box of what is left.
    """
    a = np.asarray(base.convert("RGB")).astype(int)
    H, W, _ = a.shape
    mn = np.minimum(np.minimum(a[:, :, 0], a[:, :, 1]), a[:, :, 2])
    bright = mn >= 244
    win = np.zeros((H, W), bool)
    win[int(H * .27):int(H * .73), int(W * .27):int(W * .73)] = True
    ys, xs = np.where(bright & win)
    x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
    return (x0 + x1) // 2, (y0 + y1) // 2, min(x1 - x0, y1 - y0)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("hub"); ap.add_argument("svg"); ap.add_argument("out")
    ap.add_argument("--scale", type=float, default=0.56, help="logo size as a fraction of the circle")
    ap.add_argument("--ink", default="#111111")
    a = ap.parse_args()
    base = Image.open(a.hub).convert("RGBA")
    cx, cy, dia = find_circle(base)
    tgt = int(dia * a.scale)
    logo = rasterize(pathlib.Path(a.svg), tgt, a.ink)
    base.alpha_composite(logo, (cx - tgt // 2, cy - tgt // 2))
    base.convert("RGB").save(a.out, quality=94)
    print(f"circle center=({cx},{cy}) dia={dia}  logo={tgt}px  ->  {a.out}")
