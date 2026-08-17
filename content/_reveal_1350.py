#!/usr/bin/env python3
"""1080x1350 infographic reveal loop.

Format learned from reveal_1350.mp4:
- one continuous canvas, no title-card cut
- header stays fixed and readable from frame one
- body and footer occupy fixed slots and reveal by a single veil
- reveal runs linearly from 0.00s to 3.00s
- total loop duration is 7.00s at 30fps
"""
from __future__ import annotations

import argparse
import base64
import pathlib
import subprocess
import sys

from PIL import Image

W, H, FPS, DUR, REVEAL = 1080, 1350, 30, 7.0, 3.0
MARGIN = 64
HEADER_TOP, HEADER_H = 54, 218
BODY_TOP, BODY_H = 300, 850
FOOT_TOP, FOOT_H = 1178, 118


def uri(path: pathlib.Path) -> str:
    ext = path.suffix.lower().lstrip(".").replace("jpg", "jpeg")
    return f"data:image/{ext};base64," + base64.b64encode(path.read_bytes()).decode()


def dominant_bg(path: pathlib.Path) -> str:
    im = Image.open(path).convert("RGB").resize((96, 96))
    colors = {}
    for r, g, b in im.getdata():
        key = (r // 8 * 8, g // 8 * 8, b // 8 * 8)
        colors[key] = colors.get(key, 0) + 1
    r, g, b = max(colors, key=colors.get)
    return f"rgb({r},{g},{b})"


def html(picture: pathlib.Path, title: str, subtitle: str, footer: str, bg: str) -> str:
    return f'''<!doctype html>
<html><head><meta charset="utf-8"><title>reveal 1350</title>
<style>/* FILM-META {{"duration":7.0,"w":1080,"h":1350,"fps":30,"beats":[]}} */
@font-face{{font-family:DM;src:url(data:font/woff2;base64,{font_data()}) format('woff2');font-weight:100 900}}
*{{box-sizing:border-box;margin:0}} body{{background:#000;overflow:hidden}}
#film{{position:relative;width:{W}px;height:{H}px;background:{bg};overflow:hidden;color:#111}}
.header{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;top:{HEADER_TOP}px;height:{HEADER_H}px;z-index:2}}
.kicker{{font:700 23px/1 DM,sans-serif;letter-spacing:3px;text-transform:uppercase;color:#c44727;margin-bottom:28px}}
h1{{font:800 73px/.98 DM,sans-serif;letter-spacing:-2.7px;max-width:900px}}
.sub{{font:400 28px/1.2 DM,sans-serif;margin-top:24px;max-width:850px;color:rgba(17,17,17,.68)}}
.body{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;top:{BODY_TOP}px;height:{BODY_H}px;overflow:hidden}}
.body img{{display:block;width:100%;height:100%;object-fit:cover;object-position:center}}
.body::after{{content:'';position:absolute;inset:0;border:2px solid rgba(17,17,17,.14);pointer-events:none}}
.footer{{position:absolute;left:{MARGIN}px;right:{MARGIN}px;top:{FOOT_TOP}px;height:{FOOT_H}px;border-top:2px solid rgba(17,17,17,.22);display:flex;align-items:center;justify-content:space-between;z-index:2}}
.footer-label{{font:700 21px/1 DM,sans-serif;letter-spacing:2px;text-transform:uppercase;color:#c44727}}
.footer-copy{{font:600 27px/1.1 DM,sans-serif;white-space:nowrap}}
.veil{{position:absolute;left:0;right:0;top:{BODY_TOP}px;height:{FOOT_TOP+FOOT_H-BODY_TOP}px;background:#000;opacity:.985;z-index:5;pointer-events:none;animation:reveal {REVEAL}s linear forwards}}
@keyframes reveal{{from{{opacity:.985}}to{{opacity:0}}}}
</style></head><body><main id="film">
<section class="header"><div class="kicker">ULTRON · 51ultron.com</div><h1>{title}</h1><p class="sub">{subtitle}</p></section>
<section class="body"><img src="{uri(picture)}" alt=""></section>
<footer class="footer"><span class="footer-label">Save this</span><span class="footer-copy">{footer}</span></footer>
<div class="veil"></div></main></body></html>'''


def font_data() -> str:
    p = pathlib.Path(__file__).parent / "assets" / "fonts" / "DM-Sans-latin.woff2"
    if p.exists():
        return base64.b64encode(p.read_bytes()).decode()
    return ""


def render(page: pathlib.Path, out: pathlib.Path) -> None:
    film = pathlib.Path(__file__).parent / "_film.py"
    subprocess.run([sys.executable, str(film), str(page), "--no-audio", "--out", str(out)], check=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("picture", type=pathlib.Path)
    ap.add_argument("--title", default="The GTM work you keep postponing")
    ap.add_argument("--subtitle", default="One operating layer for the work between idea and pipeline.")
    ap.add_argument("--footer", default="Follow for practical GTM systems")
    ap.add_argument("--out", default="content/ig/reveal-1350/reel")
    ap.add_argument("--render", action="store_true")
    args = ap.parse_args()
    outbase = pathlib.Path(args.out)
    outbase.parent.mkdir(parents=True, exist_ok=True)
    bg = dominant_bg(args.picture)
    page_path = outbase.parent / "reveal-1350.html"
    page_path.write_text(html(args.picture, args.title, args.subtitle, args.footer, bg))
    print(f"built {page_path}")
    print(f"geometry {W}x{H} | header {HEADER_TOP}-{HEADER_TOP+HEADER_H} | body {BODY_TOP}-{BODY_TOP+BODY_H} | footer {FOOT_TOP}-{H}")
    print(f"timing reveal 0.00-3.00s | hold 3.00-7.00s | loop {DUR:.2f}s | {FPS}fps")
    if args.render:
        render(page_path, outbase.with_suffix('.mp4'))
        print(f"rendered {outbase.with_suffix('.mp4')}")


if __name__ == '__main__':
    main()
