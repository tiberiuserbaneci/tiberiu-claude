#!/usr/bin/env python3
"""Render a slide deck to PNGs and a PDF carousel at exact canvas size.

Same discipline as the film renderer: the page is the source of truth, the export never
guesses. Each `.slide` is screenshotted at its own box, so a slide that is not exactly
1080x1920 shows up as a wrong-sized file rather than as a silently letterboxed upload.

Usage:
  python3 content/_carousel.py content/paper-01-chat.html
  python3 content/_carousel.py content/paper-*.html --pdf-only
  python3 content/_carousel.py content/paper-01-chat.html --check   # geometry only, no files
"""
import argparse, functools, glob, pathlib, subprocess, sys

print = functools.partial(print, flush=True)  # noqa: A001

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
SCRUB = CONTENT / "_scrub.py"


def chromium_path():
    for pat in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                "/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell"):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    return None


def render(html: pathlib.Path, out_dir: pathlib.Path, check_only=False, w=1080, h=1920):
    from playwright.sync_api import sync_playwright
    exe = chromium_path()
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        pg = b.new_page(viewport={"width": w, "height": 900}, device_scale_factor=1)
        pg.goto(f"file://{html.resolve()}")
        pg.wait_for_timeout(1400)
        pg.evaluate("document.fonts.ready")
        n = pg.locator(".slide").count()
        if n == 0:
            sys.exit(f"{html.name}: no .slide elements")

        # Fit pass. The header block is variable height, so a tall object squeezes into a
        # short stage and runs under the copy. Scale the object to the room it actually has
        # rather than tuning every slide by hand, then assert the two never overlap.
        #
        # The origin has to be the stage's centre, not the object's top. `.stage` centres its
        # child, so an oversized object already hangs off BOTH edges before any scaling: the
        # phone on 01-ceo slide 05 is 640px in a 595px stage and starts 23px above the stage,
        # under the body copy. Scaling from `center top` pins that overflowed top in place and
        # the text stays covered however small the object gets. From the centre, both overflows
        # close together, which is what the operator saw as text running under the element.
        # A clay object is bigger than its box. The signature shadow is 22px offset with 44px
        # of blur, so the halo reaches ~66px past every edge and the last line of body copy
        # lands in it while the rectangles still read as clear. That is the "text under the
        # element" the operator saw on 01-ceo: legally no overlap, visibly washed out. Both
        # the fit and the assertion use the halo, and the copy keeps a real gap from it.
        pg.add_script_tag(content="""
            window.__halo = el => {
              const r = el.getBoundingClientRect();
              let up = 0, dn = 0;
              const scan = n => {
                const sh = getComputedStyle(n).boxShadow;
                if (!sh || sh === 'none') return;
                const nr = n.getBoundingClientRect();
                for (const m of sh.matchAll(/(-?[\\d.]+)px\\s+(-?[\\d.]+)px\\s+([\\d.]+)px(?:\\s+(-?[\\d.]+)px)?/g)) {
                  const oy = +m[2], bl = +m[3], sp = +(m[4] || 0);
                  up = Math.max(up, (r.top - nr.top) - oy + bl + sp);
                  dn = Math.max(dn, (nr.bottom - r.bottom) + oy + bl + sp);
                }
              };
              scan(el); el.querySelectorAll('*').forEach(scan);
              return {top: r.top - Math.max(up, 0), bottom: r.bottom + Math.max(dn, 0)};
            };
        """)
        pg.evaluate("""() => {
            const GAP = 16;  // clear air the copy keeps from the halo
            document.querySelectorAll('.slide').forEach(s => {
              const st = s.querySelector('.stage'); if (!st) return;
              const o = st.firstElementChild; if (!o) return;
              o.style.transform = ''; o.style.transformOrigin = 'center center';
              const r = o.getBoundingClientRect(), h = window.__halo(o);
              const bleed = (r.top - h.top) + (h.bottom - r.bottom);
              const avail = st.clientHeight - 8 - GAP * 2;
              const need = r.height + bleed;
              if (need > avail && need > 0)
                o.style.transform = 'scale(' + (avail / need).toFixed(3) + ')';
            });
        }""")
        pg.wait_for_timeout(120)
        overlap = pg.evaluate("""() => {
            const out = [];
            document.querySelectorAll('.slide').forEach((s, i) => {
              const st = s.querySelector('.stage'); if (!st) return;
              const o = st.firstElementChild; if (!o) return;
              const ob = window.__halo(o);
              ['.eyebrow', '.h', '.sub', '.body'].forEach(sel => {
                const e = s.querySelector(sel); if (!e) return;
                const b = e.getBoundingClientRect();
                const ov = Math.min(b.bottom, ob.bottom) - Math.max(b.top, ob.top);
                if (ov > 2) out.push({slide: i+1, el: sel, px: Math.round(ov)});
              });
            });
            return out.slice(0, 8);
        }""")
        if overlap:
            for o in overlap:
                print(f"  TEXT slide {o['slide']:02d} {o['el']} overlaps the object by {o['px']}px")

        bad = pg.evaluate("""([w,h]) => [...document.querySelectorAll('.slide')]
            .map((s,i)=>({i:i+1, w:Math.round(s.scrollWidth), h:Math.round(s.scrollHeight)}))
            .filter(s=>s.w!==w||s.h!==h)""", [w, h])
        if bad:
            for s in bad:
                print(f"  DIM  slide {s['i']:02d} is {s['w']}x{s['h']}, expected {w}x{h}")
            b.close()
            sys.exit(f"{html.name}: {len(bad)} slide(s) off canvas")

        # Anything painted outside the safe box will be cropped by the app UI. Judge the
        # PAINTED rect, not the layout rect: a gauge draws a 500px circle inside a 300px box
        # with `overflow:hidden`, so its layout rect hangs 200px below something the viewer
        # never sees. Intersect with every clipping ancestor first, or the guard cries wolf on
        # correct work and gets ignored on the day it is right.
        spill = pg.evaluate("""() => {
            const painted = e => {
              let b = e.getBoundingClientRect();
              let t = b.top, bo = b.bottom, l = b.left, r = b.right;
              for (let p = e.parentElement; p; p = p.parentElement) {
                const cs = getComputedStyle(p);
                if (cs.overflow === 'visible' && cs.overflowX === 'visible'
                    && cs.overflowY === 'visible') continue;
                const c = p.getBoundingClientRect();
                t = Math.max(t, c.top); bo = Math.min(bo, c.bottom);
                l = Math.max(l, c.left); r = Math.min(r, c.right);
              }
              return {top:t, bottom:bo, left:l, right:r, w:r-l, h:bo-t};
            };
            const out=[];
            document.querySelectorAll('.slide').forEach((s,i)=>{
              const r=s.getBoundingClientRect();
              s.querySelectorAll('.safe *').forEach(e=>{
                const b=painted(e);
                if(b.w<=0||b.h<=0) return;   // fully clipped: nothing reaches the frame
                const top=b.top-r.top, bot=r.bottom-b.bottom,
                      left=b.left-r.left, right=r.right-b.right;
                if(top<299||bot<329||left<69||right<129)
                  out.push({i:i+1, cls:(e.className||'').toString().slice(0,24),
                            top:Math.round(top), bot:Math.round(bot),
                            left:Math.round(left), right:Math.round(right)});
              });
            });
            return out.slice(0,6);
        }""")
        if spill:
            for s in spill:
                print(f"  SAFE slide {s['i']:02d} .{s['cls']} t{s['top']} b{s['bot']} "
                      f"l{s['left']} r{s['right']}")
        print(f"  {html.name:28} {n} slides  all {w}x{h}"
              + ("" if not spill else f"  ({len(spill)} outside the safe box)"))
        if check_only:
            b.close()
            return []

        out_dir.mkdir(parents=True, exist_ok=True)
        pngs = []
        for i in range(n):
            f = out_dir / f"{html.stem}-{i+1:02d}.png"
            pg.locator(".slide").nth(i).screenshot(path=str(f))
            pngs.append(f)
        b.close()
    return pngs


def to_pdf(pngs, dest: pathlib.Path):
    """One page per slide, page box equal to the image box. No resampling, no margins."""
    from PIL import Image
    ims = [Image.open(p).convert("RGB") for p in pngs]
    ims[0].save(dest, save_all=True, append_images=ims[1:], resolution=72.0)
    return dest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("decks", nargs="+")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--out", default=str(CONTENT / "paper"))
    a = ap.parse_args()
    out_dir = pathlib.Path(a.out)
    for d in a.decks:
        html = pathlib.Path(d)
        pngs = render(html, out_dir, check_only=a.check)
        if a.check or not pngs:
            continue
        pdf = to_pdf(pngs, out_dir / f"{html.stem}.pdf")
        subprocess.run([sys.executable, str(SCRUB), str(pdf)], check=False,
                       capture_output=True)
        for p in pngs:
            subprocess.run([sys.executable, str(SCRUB), str(p)], check=False,
                           capture_output=True)
        print(f"  -> {pdf.name}  ({len(pngs)} pages, scrubbed)")


if __name__ == "__main__":
    main()
