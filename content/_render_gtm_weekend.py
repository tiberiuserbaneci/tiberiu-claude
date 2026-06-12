#!/usr/bin/env python3
"""Render the gtm-weekend-45 carousel.

7 slides -> PNGs in both name-sets (LinkedIn + TikTok) + a combined PDF.
Editorial 4:5: 1080x1350 per slide, device_scale_factor=2 (2160x2700 px).
Last step scrubs metadata (PNG chunks + PDF Producer/Creator) to operator authorship.

Usage: python3 content/_render_gtm_weekend.py
"""
import os, base64, subprocess, tempfile, img2pdf
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(HERE, 'gtm-weekend-45-tiktok-carousel.html')
LOGO = os.path.join(HERE, 'ultron-logo.png')
LI   = os.path.join(HERE, 'gtm-weekend-45-carousel-{:02d}.png')         # LinkedIn name-set
TT   = os.path.join(HERE, 'gtm-weekend-45-tiktok-carousel-{:02d}.png')  # TikTok name-set
PDF  = os.path.join(HERE, 'gtm-weekend-45-carousel.pdf')

def main():
    # the committed source keeps the __LOGO_URI__ placeholder; substitute the base64
    # logo at export time and render the temp copy (exports run headless, no external URLs)
    src = open(HTML, encoding='utf-8').read()
    logo = 'data:image/png;base64,' + base64.b64encode(open(LOGO, 'rb').read()).decode()
    fd, tmp = tempfile.mkstemp(suffix='.html', dir=HERE)
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(src.replace('__LOGO_URI__', logo))
    li_paths, tt_paths = [], []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
        pg.goto('file://' + tmp, wait_until='networkidle')
        try:
            pg.wait_for_function("document.fonts && document.fonts.status==='loaded'", timeout=8000)
        except Exception:
            pass
        pg.wait_for_timeout(800)
        slides = pg.locator('.slide')
        n = slides.count()
        assert n == 7, f"expected 7 slides, got {n}"
        for i in range(n):
            li, tt = LI.format(i + 1), TT.format(i + 1)
            slides.nth(i).screenshot(path=li)
            with open(li, 'rb') as s, open(tt, 'wb') as d:   # TikTok name-set = identical bytes
                d.write(s.read())
            li_paths.append(li); tt_paths.append(tt)
        b.close()
    os.unlink(tmp)
    with open(PDF, 'wb') as f:                               # combined carousel PDF
        f.write(img2pdf.convert(li_paths))
    subprocess.run(['python3', os.path.join(HERE, '_scrub.py'), *li_paths, *tt_paths, PDF], check=True)
    print(f"rendered {len(li_paths)} slides x2 name-sets + PDF, scrubbed.")

if __name__ == '__main__':
    main()
