#!/usr/bin/env python3
"""Render the docs-12 skills-catalog materials that exist on disk.
  - docs-12-skills-linkedin.html              -> .frame 1080x1450 -> docs-12-skills-linkedin.png
  - docs-12-skills-editorial45-infographic    -> .slide 1080x1350 -> ...-infographic.png
  - docs-12-skills-editorial45-carousel       -> N x .slide 1080x1350 -> ...-carousel-NN.png (+pdf)
Base64 logo substituted, then metadata scrubbed. Usage: python3 content/_render_skills.py
"""
import os, base64, subprocess, tempfile, glob
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = os.path.join(HERE, 'ultron-logo.png')
logo = 'data:image/png;base64,' + base64.b64encode(open(LOGO, 'rb').read()).decode()


def render(html_name, sel, h, out_tpl):
    path = os.path.join(HERE, html_name)
    if not os.path.exists(path):
        return []
    src = open(path, encoding='utf-8').read().replace('__LOGO_URI__', logo)
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
        pg.wait_for_timeout(800)
        els = pg.locator(sel)
        n = els.count()
        for i in range(n):
            out = os.path.join(HERE, out_tpl if n == 1 else out_tpl.format(i + 1))
            els.nth(i).screenshot(path=out)
            outs.append(out)
        b.close()
    os.unlink(tmp)
    return outs


def main():
    allouts = []
    allouts += render('docs-12-skills-linkedin.html', '.frame', 1450, 'docs-12-skills-linkedin.png')
    allouts += render('docs-12-skills-editorial45-infographic.html', '.slide', 1350, 'docs-12-skills-editorial45-infographic.png')
    caro = render('docs-12-skills-editorial45-carousel.html', '.slide', 1350, 'docs-12-skills-editorial45-carousel-{:02d}.png')
    allouts += caro
    if caro:
        import img2pdf
        pdf = os.path.join(HERE, 'docs-12-skills-editorial45-carousel.pdf')
        with open(pdf, 'wb') as f:
            f.write(img2pdf.convert(caro))
        allouts.append(pdf)
    if allouts:
        subprocess.run(['python3', os.path.join(HERE, '_scrub.py'), *allouts], check=True)
    print(f"rendered + scrubbed {len(allouts)} files.")


if __name__ == '__main__':
    main()
