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


def render(html: pathlib.Path, out_dir: pathlib.Path, check_only=False, w=1080, h=1920,
           safe=(300, 130, 330, 70), fill_w=0.0, fill_h=0.0):
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
        # Header fit. The stage is a declared constant, so the header cannot be allowed to
        # grow into it - but a three line hook plus a two line subhook overflows the budget
        # and the last line is simply cut, which is what clipped "You do not have the job."
        # Shrink the display type until the block fits instead of losing a sentence.
        pg.evaluate("""() => {
            document.querySelectorAll('.hd').forEach(hd => {
              const h = hd.querySelector('.h'); if (!h) return;
              // Run the title out to the full measure and set it as large as the header
              // budget allows, rather than leaving short lines floating at half the column.
              // Each authored line becomes a block whose inner span reports the real text
              // width, so the fit can grow the type as well as shrink it.
              if (!h.dataset.split) {
                h.innerHTML = h.innerHTML.split(/<br\s*\/?>/i)
                  .map(s => '<span style="display:block"><i style="font-style:normal;' +
                            'display:inline-block">' + s + '</i></span>').join('');
                h.dataset.split = '1';
              }
              const room = h.clientWidth;
              const widest = () => Math.max(...[...h.querySelectorAll('span > i')]
                                    .map(e => e.getBoundingClientRect().width), 0);
              let size = 210;
              h.style.fontSize = size + 'px';
              for (let k = 0; k < 90; k++) {
                if (widest() <= room && hd.scrollHeight <= hd.clientHeight) break;
                size -= 3; h.style.fontSize = size + 'px';
              }
            });
        }""")
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

        # Fill. The operator's rejection was "elementele 2.5D ... ffffff mici in comparatie cu
        # layoutul slide ului", and the number behind it was a median 50% of stage HEIGHT with
        # a worst case of 15%: a 720x105 strip alone in an 880x701 box. The workspace is
        # declared, so an object that does not fill it is a defect the same way a wrong canvas
        # size is. Reported for every deck, so a thin scene is visible before it is posted.
        thin = pg.evaluate("""([fw, fh]) => {
            const out = [];
            document.querySelectorAll('.slide').forEach((s, i) => {
              const st = s.querySelector('.stage'); if (!st) return;
              const a = st.getBoundingClientRect();
              let t = 1e9, bo = -1e9, l = 1e9, r = -1e9, seen = false;
              st.querySelectorAll('*').forEach(e => {
                const q = e.getBoundingClientRect();
                if (q.width < 8 || q.height < 8) return;
                seen = true;
                t = Math.min(t, q.top); bo = Math.max(bo, q.bottom);
                l = Math.min(l, q.left); r = Math.max(r, q.right);
              });
              if (!seen) return;
              const w = (r - l) / a.width, h = (bo - t) / a.height;
              if (w < fw || h < fh)
                out.push({slide: i+1, w: Math.round(w*100), h: Math.round(h*100)});
            });
            return out.slice(0, 8);
        }""", [fill_w, fill_h])
        for x in thin:
            print(f"  THIN slide {x['slide']:02d} fills {x['w']}% wide {x['h']}% tall "
                  f"(floor {int(fill_w*100)}/{int(fill_h*100)})")

        # Two defects the operator caught by eye, now caught by number on every render.
        # "textul iasa din pila" - a solid that does not contain its own words - and
        # "alb pe crem nu se vede" - light type on the light ground, which is invisible
        # rather than merely ugly. Both shipped once because nothing was measuring them.
        leak = pg.evaluate("""() => {
            const out = [];
            const lum = c => {
              const m = c.match(/[\d.]+/g); if (!m) return null;
              if (m.length > 3 && parseFloat(m[3]) < 0.35) return null;
              const [r,g,b] = m.slice(0,3).map(Number);
              return (0.2126*r + 0.7152*g + 0.0722*b) / 255;
            };
            const bgOf = el => {
              for (let n = el; n; n = n.parentElement) {
                const cs = getComputedStyle(n);
                if (cs.backgroundImage && cs.backgroundImage !== 'none') {
                  const m = cs.backgroundImage.match(/rgba?\([^)]+\)/);
                  if (m) { const L = lum(m[0]); if (L !== null) return L; }
                }
                const L = lum(cs.backgroundColor); if (L !== null) return L;
              }
              return 1;
            };
            const words = e => [...e.childNodes].filter(n => n.nodeType === 3)
                                 .map(n => n.textContent.trim()).join('');
            document.querySelectorAll('.slide').forEach((s, i) => {
              s.querySelectorAll('.slab').forEach(sl => {
                const r = sl.getBoundingClientRect();
                sl.querySelectorAll('*').forEach(e => {
                  if (!words(e)) return;
                  const q = e.getBoundingClientRect();
                  if (q.width < 3 || q.height < 3) return;
                  const over = Math.max(r.top - q.top, q.bottom - r.bottom,
                                        r.left - q.left, q.right - r.right);
                  if (over > 3)
                    out.push({slide: i+1, why: 'escapes its solid',
                              txt: words(e).slice(0,22), px: Math.round(over)});
                });
              });
              // any clipping box, not just a solid: the docket hid its last row inside an
              // inner overflow:hidden div and the .slab-only check never saw it
              s.querySelectorAll('*').forEach(e => {
                const cs = getComputedStyle(e);
                if (cs.overflow === 'visible' && cs.overflowY === 'visible') return;
                if (e.scrollHeight <= e.clientHeight + 3 || e.clientHeight <= 30) return;
                // Only a box that clips WORDS is a defect. A deliberate clip around a
                // decorative ground - a blurred photograph scaled past the frame so its blur
                // has something to chew on - is the technique, not a bug, and flagging it
                // trains the operator to ignore the guard.
                if (!e.textContent.trim()) return;
                out.push({slide: i+1, why: 'box clips its own content', txt: '',
                          px: e.scrollHeight - e.clientHeight});
              });
              s.querySelectorAll('*').forEach(e => {
                const w = words(e); if (!w) return;
                const q = e.getBoundingClientRect();
                if (q.width < 4 || q.height < 4) return;
                const fg = lum(getComputedStyle(e).color); if (fg === null) return;
                if (fg > 0.72 && bgOf(e) > 0.72)
                  out.push({slide: i+1, why: 'light type on light ground',
                            txt: w.slice(0,22), px: 0});
              });
            });
            return out.slice(0, 8);
        }""")
        for x in leak:
            print(f"  LEAK slide {x['slide']:02d} {x['why']}"
                  + (f' "{x["txt"]}"' if x["txt"] else "")
                  + (f" by {x['px']}px" if x["px"] else ""))

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
        spill = pg.evaluate("""([sT, sR, sB, sL]) => {
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
                if(top<sT-1||bot<sB-1||left<sL-1||right<sR-1)
                  out.push({i:i+1, cls:(e.className||'').toString().slice(0,24),
                            top:Math.round(top), bot:Math.round(bot),
                            left:Math.round(left), right:Math.round(right)});
              });
            });
            return out.slice(0,6);
        }""", list(safe))
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
    ap.add_argument("--fill-w", type=float, default=0.0, dest="fill_w",
                    help="minimum share of stage width a scene must cover")
    ap.add_argument("--fill-h", type=float, default=0.0, dest="fill_h",
                    help="minimum share of stage height a scene must cover")
    a = ap.parse_args()
    out_dir = pathlib.Path(a.out)
    for d in a.decks:
        html = pathlib.Path(d)
        # CLAUDE.md 9: a filename carrying -45 is TikTok's 4:5 photo carousel, which is a
        # different canvas AND a different safe geometry - photo mode paints no feed UI over
        # the top of the frame, so the 9:16 insets would fail correct work.
        four_five = "-45" in html.stem or "editorial45" in html.stem
        pngs = render(html, out_dir, check_only=a.check,
                      w=1080, h=1350 if four_five else 1920,
                      safe=(96, 90, 110, 90) if four_five else (300, 130, 330, 70),
                      fill_w=a.fill_w, fill_h=a.fill_h)
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
