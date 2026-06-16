#!/usr/bin/env python3
"""Render the Master Claude editorial 4:5 materials (operator's own reference, rebuilt in Ultron).

  - master-claude-editorial45-infographic.html  -> 1 PNG  (single image)
  - master-claude-editorial45-carousel.html      -> 6 PNGs + combined PDF

1080x1350 per slide, device_scale_factor=2. Base64 logo substituted, then metadata scrubbed.
Usage: python3 content/_render_master_claude.py
"""
import os, base64, subprocess, tempfile, img2pdf
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, 'ultron-logo.png')
INFO = os.path.join(HERE, 'master-claude-editorial45-infographic.html')
CARO = os.path.join(HERE, 'master-claude-editorial45-carousel.html')
logo = 'data:image/png;base64,' + base64.b64encode(open(LOGO, 'rb').read()).decode()


def render(html_path, out_tpl, expect):
    src = open(html_path, encoding='utf-8').read().replace('__LOGO_URI__', logo)
    fd, tmp = tempfile.mkstemp(suffix='.html', dir=HERE)
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(src)
    paths = []
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
        assert n == expect, f"{os.path.basename(html_path)}: expected {expect} slides, got {n}"
        for i in range(n):
            out = out_tpl if expect == 1 else out_tpl.format(i + 1)
            slides.nth(i).screenshot(path=out)
            paths.append(out)
        b.close()
    os.unlink(tmp)
    return paths


def main():
    # PNG names match the HTML stems (and carry 'editorial45') so the portal groups them with the
    # source and classifies them as TikTok (PNG-zip download), not LinkedIn (PDF).
    info = render(INFO, os.path.join(HERE, 'master-claude-editorial45-infographic.png'), 1)
    caro = render(CARO, os.path.join(HERE, 'master-claude-editorial45-carousel-{:02d}.png'), 6)
    pdf = os.path.join(HERE, 'master-claude-editorial45-carousel.pdf')
    with open(pdf, 'wb') as f:
        f.write(img2pdf.convert(caro))
    subprocess.run(['python3', os.path.join(HERE, '_scrub.py'), *info, *caro, pdf], check=True)
    print(f"rendered: 1 infographic + {len(caro)} carousel slides + PDF, scrubbed.")


if __name__ == '__main__':
    main()
