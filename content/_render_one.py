#!/usr/bin/env python3
"""Render one or more editorial-4:5 (1080x1350) materials, base64 the logo, scrub metadata.
Usage: python3 content/_render_one.py content/<file>.html [more.html ...]
Single .slide -> <stem>.png ; multiple .slide -> <stem>-NN.png (+ <stem>.pdf)."""
import os, sys, base64, tempfile, subprocess
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
logo = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(HERE, 'ultron-logo.png'), 'rb').read()).decode()


def render(path):
    stem = os.path.splitext(os.path.basename(path))[0]
    src = open(path, encoding='utf-8').read().replace('__LOGO_URI__', logo)
    fd, tmp = tempfile.mkstemp(suffix='.html', dir=HERE)
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(src)
    outs = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
        pg.goto('file://' + tmp, wait_until='networkidle')
        try:
            pg.wait_for_function("document.fonts && document.fonts.status==='loaded'", timeout=8000)
        except Exception:
            pass
        pg.wait_for_timeout(700)
        els = pg.locator('.slide'); n = els.count()
        for i in range(n):
            out = os.path.join(HERE, f"{stem}.png" if n == 1 else f"{stem}-{i+1:02d}.png")
            els.nth(i).screenshot(path=out); outs.append(out)
        b.close()
    os.unlink(tmp)
    if n > 1:
        import img2pdf
        pdf = os.path.join(HERE, f"{stem}.pdf")
        open(pdf, 'wb').write(img2pdf.convert(outs)); outs.append(pdf)
    return outs


def main():
    allouts = []
    for arg in sys.argv[1:]:
        allouts += render(arg if os.path.isabs(arg) else os.path.join(os.getcwd(), arg))
    if allouts:
        subprocess.run(['python3', os.path.join(HERE, '_scrub.py'), *allouts], check=True)
    print(f"rendered + scrubbed {len(allouts)} file(s): " + ", ".join(os.path.basename(o) for o in allouts))


if __name__ == '__main__':
    main()
