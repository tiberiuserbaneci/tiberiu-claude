#!/usr/bin/env python3
"""Re-render the docs-11-turn material after the Stripe->Worldpay swap + today's-date calendar update.
  - docs-11-turn-linkedin.html        -> .frame  1080x1450 -> docs-11-turn-linkedin.png
  - docs-11-turn-tiktok-infographic   -> .slide  1080x1920 -> docs-11-turn-tiktok-infographic.png
  - docs-11-turn-tiktok-carousel      -> 8x .slide 1080x1920 -> docs-11-turn-tiktok-carousel-NN.png
Base64 logo substituted, then metadata scrubbed. Usage: python3 content/_render_docs11.py
"""
import os, base64, subprocess, tempfile
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, 'ultron-logo.png')
logo = 'data:image/png;base64,' + base64.b64encode(open(LOGO, 'rb').read()).decode()

JOBS = [
    ('docs-11-turn-linkedin.html', '.frame', 1450, 'docs-11-turn-linkedin.png', 1),
    ('docs-11-turn-tiktok-infographic.html', '.slide', 1920, 'docs-11-turn-tiktok-infographic.png', 1),
    ('docs-11-turn-tiktok-carousel.html', '.slide', 1920, 'docs-11-turn-tiktok-carousel-{:02d}.png', 8),
]

def render(html_name, sel, h, out_tpl, n):
    src = open(os.path.join(HERE, html_name), encoding='utf-8').read().replace('__LOGO_URI__', logo)
    fd, tmp = tempfile.mkstemp(suffix='.html', dir=HERE)
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(src)
    outs = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': h}, device_scale_factor=2)
        pg.goto('file://' + tmp, wait_until='networkidle')
        try:
            pg.wait_for_function("document.fonts && document.fonts.status==='loaded'", timeout=8000)
        except Exception:
            pass
        pg.wait_for_timeout(700)
        els = pg.locator(sel)
        assert els.count() == n, f"{html_name}: expected {n} {sel}, got {els.count()}"
        for i in range(n):
            out = os.path.join(HERE, out_tpl if n == 1 else out_tpl.format(i + 1))
            els.nth(i).screenshot(path=out)
            outs.append(out)
        b.close()
    os.unlink(tmp)
    return outs

def main():
    allouts = []
    for html_name, sel, h, out_tpl, n in JOBS:
        allouts += render(html_name, sel, h, out_tpl, n)
    subprocess.run(['python3', os.path.join(HERE, '_scrub.py'), *allouts], check=True)
    print(f"rendered + scrubbed {len(allouts)} PNGs.")

if __name__ == '__main__':
    main()
