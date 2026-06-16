#!/usr/bin/env python3
"""Render the REALNUMBERS AGENT MATH stack infographic (single image, editorial 4:5 1080x1350).
PNG name matches the HTML stem so the portal groups + classifies it (TikTok). Scrubs metadata.
Usage: python3 content/_render_realnumbers_stack.py
"""
import os, base64, subprocess, tempfile
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(HERE, 'realnumbers-stack-editorial45-infographic.html')
OUT = os.path.join(HERE, 'realnumbers-stack-editorial45-infographic.png')
LOGO = os.path.join(HERE, 'ultron-logo.png')

def main():
    src = open(HTML, encoding='utf-8').read()
    logo = 'data:image/png;base64,' + base64.b64encode(open(LOGO, 'rb').read()).decode()
    fd, tmp = tempfile.mkstemp(suffix='.html', dir=HERE)
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(src.replace('__LOGO_URI__', logo))
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=2)
        pg.goto('file://' + tmp, wait_until='networkidle')
        try:
            pg.wait_for_function("document.fonts && document.fonts.status==='loaded'", timeout=8000)
        except Exception:
            pass
        pg.wait_for_timeout(700)
        pg.locator('.slide').screenshot(path=OUT)
        b.close()
    os.unlink(tmp)
    subprocess.run(['python3', os.path.join(HERE, '_scrub.py'), OUT], check=True)
    print('rendered + scrubbed:', OUT)

if __name__ == '__main__':
    main()
