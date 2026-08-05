#!/usr/bin/env python3
"""ULTRON CLAY: the reference deck's design language, rebuilt as an exportable canvas.

Operator, 2026-08-05: the clean claymorphic look of `ultron_24h_startup.html`, and its
narrative genre, which is the aspirational time-boxed transformation. Launch a startup in 24
hours. Become the CEO. Zero code. Not a feature tour.

This is deliberately the opposite of the ULTRON PAPER decks in `_deck.py`. Those pack the band
because CLAUDE.md 27.9 treats an airy dominant block as the recurring failure. The reference
does the opposite and performs, so per CLAUDE.md 0.1 the operator's call stands: centred, soft,
one object per slide, generous space around it. Density is not the lever on this one; the
promise is.

Faithful to the reference where it matters:
  - claymorphic double shadow, light from the top left, on a warm cream ground
  - Oswald for the headline, Plus Jakarta Sans for everything else (its own faces, embedded)
  - centred column, one visual object per slide, progress pills along the bottom
  - the same slide spine: headline, subtitle, body line, object, progress

Changed on purpose, all mechanical:
  - 1080x1920 exact, not `aspect-ratio` on a 480px preview
  - safe box top 300 / right 130 / bottom 330 / left 70; the reference footer sat at 115px,
    inside TikTok's caption band
  - accent is REALNUMBERS editorial orange #D26446 rather than #F27A45, which is in neither
    brand system. Closest documented match to the reference's warmth.
  - fonts embedded; the reference links a CDN the renderer cannot reach, so it exports blank
"""
import base64, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"


def fonts_css() -> str:
    import importlib.util
    spec = importlib.util.spec_from_file_location("_fonts", CONTENT / "_fonts.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.embedded_css()


def logo_uri() -> str:
    return "data:image/png;base64," + base64.b64encode(
        (CONTENT / "ultron-logo.png").read_bytes()).decode()


CSS = """
:root{
  --base:#F4F1EC; --deep:#E2DCD0; --ink:#2D2A26; --muted:#8A857D;
  --acc:#D26446; --accd:#B2492C; --accl:#E8845F;
  --lo:#DAD5CC; --hi:#FFFFFF;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#CFC8BA;display:flex;flex-direction:column;align-items:center;gap:44px;
  padding:44px 0;font-family:'Plus Jakarta Sans',sans-serif;-webkit-font-smoothing:antialiased;}
.slide{width:1080px;height:1920px;position:relative;overflow:hidden;background:var(--base);
  color:var(--ink);flex-shrink:0;}
.amb{position:absolute;inset:0;
  background:radial-gradient(ellipse 74% 40% at 50% 6%,#FBF9F5 0%,transparent 62%),
    radial-gradient(ellipse 60% 34% at 50% 100%,rgba(210,100,70,.07) 0%,transparent 60%);}

/* safe box: the reference put its footer 115px off the bottom, inside the caption band */
.safe{position:absolute;top:300px;left:70px;right:130px;bottom:330px;z-index:5;
  display:flex;flex-direction:column;align-items:center;text-align:center;}

/* claymorphism: soft double shadow, light from the top left, never a hard border */
.clay{background:var(--base);border-radius:38px;
  box-shadow:22px 22px 44px var(--lo),-22px -22px 44px var(--hi);
  border:1px solid rgba(255,255,255,.72);}
.clay-in{background:var(--base);border-radius:32px;
  box-shadow:inset 15px 15px 30px var(--lo),inset -15px -15px 30px var(--hi);}
.clay-acc{background:linear-gradient(158deg,var(--accl),var(--acc) 52%,var(--accd));
  border-radius:30px;color:#fff;
  box-shadow:16px 16px 32px rgba(178,73,44,.30),-14px -14px 28px var(--hi),
             inset 0 2px 0 rgba(255,255,255,.34);}

.eyebrow{font-family:'Plus Jakarta Sans',sans-serif;font-size:24px;font-weight:800;
  letter-spacing:.34em;text-transform:uppercase;color:var(--acc);flex-shrink:0;}
.h{font-family:'Oswald',sans-serif;font-weight:600;font-size:104px;line-height:1.02;
  letter-spacing:-.5px;text-transform:uppercase;margin-top:22px;flex-shrink:0;}
.h em{color:var(--acc);font-style:normal;}
.sub{font-size:35px;font-weight:700;line-height:1.3;margin-top:24px;flex-shrink:0;
  max-width:88%;}
.body{font-size:27px;font-weight:500;line-height:1.55;color:var(--muted);margin-top:20px;
  flex-shrink:0;max-width:86%;}

.stage{flex:1;min-height:0;width:100%;display:flex;align-items:center;justify-content:center;
  padding:26px 0;}

/* the progress rail: which hour of the run this slide is */
.rail{flex-shrink:0;width:100%;max-width:720px;margin-top:8px;}
.rail .in{border-radius:34px;padding:24px 30px;display:flex;align-items:center;
  justify-content:center;gap:14px;}
.rail span{font-size:22px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);opacity:.42;}
.rail span.on{opacity:1;color:#fff;background:linear-gradient(158deg,var(--accl),var(--accd));
  padding:11px 20px;border-radius:30px;
  box-shadow:6px 6px 14px rgba(178,73,44,.30),-4px -4px 10px var(--hi);}
.rail i{color:var(--acc);font-style:normal;font-weight:800;opacity:.5;}

.foot{position:absolute;left:70px;right:130px;bottom:calc(330px - 96px);z-index:6;
  display:flex;align-items:center;justify-content:center;gap:13px;}
.foot img{width:31px;height:31px;border-radius:50%;object-fit:cover;opacity:.85;}
.foot span{font-size:20px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
  color:var(--muted);}
.foot span em{color:var(--acc);font-style:normal;}

/* ---------- slide objects ---------- */
/* one per slide, centred, nothing competing with it */

.dial{width:520px;height:520px;border-radius:50%;position:relative;
  display:flex;align-items:center;justify-content:center;}
.dial .ring{position:absolute;inset:26px;border-radius:50%;border:26px solid var(--deep);
  opacity:.55;}
.dial .arc{position:absolute;inset:26px;border-radius:50%;border:26px solid var(--acc);
  border-right-color:transparent;border-bottom-color:transparent;transform:rotate(42deg);}
.dial .core{width:322px;height:322px;border-radius:50%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;}
.dial .core b{font-family:'Oswald',sans-serif;font-size:150px;font-weight:600;color:var(--acc);
  line-height:.9;}
.dial .core u{font-size:23px;font-weight:800;letter-spacing:.30em;color:var(--muted);
  text-decoration:none;margin-top:10px;}
.dial .pip{position:absolute;top:16px;right:96px;width:34px;height:34px;border-radius:50%;
  background:var(--acc);box-shadow:0 0 26px rgba(210,100,70,.66);border:4px solid #fff;}

.cards{display:flex;flex-direction:column;align-items:center;gap:26px;width:100%;}
.card{width:660px;border-radius:34px;padding:30px 34px;display:flex;align-items:center;gap:24px;
  text-align:left;}
.card .no{font-family:'Oswald',sans-serif;font-size:52px;font-weight:600;color:var(--acc);
  width:74px;flex-shrink:0;line-height:1;}
.card b{display:block;font-size:31px;font-weight:800;letter-spacing:-.4px;line-height:1.1;}
.card i{display:block;font-size:23px;font-style:normal;color:var(--muted);margin-top:6px;
  line-height:1.28;}
.card.acc b,.card.acc i{color:#fff;}
.card.acc i{opacity:.86;}
.card.acc .no{color:#fff;opacity:.7;}

.badge{width:640px;border-radius:38px;padding:44px 40px;text-align:center;}
.badge u{display:block;font-size:22px;font-weight:800;letter-spacing:.30em;
  text-decoration:none;opacity:.82;}
.badge b{display:block;font-family:'Oswald',sans-serif;font-size:78px;font-weight:600;
  line-height:1.02;margin-top:14px;text-transform:uppercase;}
.badge .rule{height:3px;border-radius:2px;background:rgba(255,255,255,.24);margin:26px 0;}
.badge .row{display:flex;justify-content:space-between;font-size:21px;font-weight:700;
  letter-spacing:.10em;opacity:.9;}

.stack3{display:flex;flex-direction:column;align-items:center;gap:0;width:100%;}
.stack3 .lay{width:600px;border-radius:32px;padding:28px 34px;display:flex;align-items:center;
  justify-content:space-between;position:relative;}
.stack3 .lay+.lay{margin-top:26px;}
.stack3 .lay b{font-size:27px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;}
.stack3 .lay u{font-size:21px;font-weight:700;color:var(--muted);text-decoration:none;}
.stack3 .lay.acc b,.stack3 .lay.acc u{color:#fff;}
.stack3 .lay.acc u{opacity:.85;}
.stack3 .lay::after{content:'';position:absolute;left:50%;bottom:-26px;width:3px;height:26px;
  background:var(--deep);}
.stack3 .lay:last-child::after{display:none;}

.phone{width:430px;height:640px;border-radius:62px;padding:22px;}
.phone .scr{width:100%;height:100%;border-radius:46px;padding:30px;display:flex;
  flex-direction:column;align-items:center;}
.phone .notch{width:112px;height:9px;border-radius:6px;background:var(--deep);margin-bottom:34px;}
.phone .chart{width:100%;height:170px;display:flex;align-items:flex-end;justify-content:space-between;
  padding:0 14px 14px;border-bottom:3px solid var(--deep);}
.phone .chart i{width:34px;border-radius:8px 8px 0 0;background:var(--deep);}
.phone .chart i.on{background:linear-gradient(180deg,var(--accl),var(--acc));}
.phone .pop{width:100%;border-radius:26px;padding:24px 26px;margin-top:40px;
  display:flex;align-items:center;justify-content:space-between;transform:rotate(-2.4deg);}
.phone .pop u{font-size:20px;font-weight:800;letter-spacing:.16em;text-decoration:none;}
.phone .pop b{font-family:'Oswald',sans-serif;font-size:44px;font-weight:600;}

.grid2{display:grid;grid-template-columns:1fr 1fr;gap:24px;width:700px;}
.grid2 .cell{border-radius:32px;padding:30px 26px;text-align:center;}
.grid2 .cell u{display:block;font-size:20px;font-weight:800;letter-spacing:.22em;
  color:var(--acc);text-decoration:none;}
.grid2 .cell b{display:block;font-family:'Oswald',sans-serif;font-size:56px;font-weight:600;
  line-height:1;margin-top:12px;}
.grid2 .cell i{display:block;font-size:21px;font-style:normal;color:var(--muted);margin-top:10px;
  line-height:1.26;}
.grid2 .cell.acc u,.grid2 .cell.acc b{color:#fff;}
.grid2 .cell.acc i{color:rgba(255,255,255,.86);}
"""


# ------------------------------------------------------------------ objects

def dial(num, label, pip=True):
    return (f'<div class="dial clay"><div class="ring"></div><div class="arc"></div>'
            f'<div class="core clay-in"><b>{num}</b><u>{label}</u></div>'
            + ('<div class="pip"></div>' if pip else '') + '</div>')


def cards(items):
    body = "".join(
        f'<div class="card {"clay-acc acc" if it.get("acc") else "clay"}">'
        f'<div class="no">{it["n"]}</div><div><b>{it["b"]}</b><i>{it["i"]}</i></div></div>'
        for it in items)
    return f'<div class="cards">{body}</div>'


def badge(kicker, title, left, right):
    return (f'<div class="badge clay-acc"><u>{kicker}</u><b>{title}</b>'
            f'<div class="rule"></div><div class="row"><span>{left}</span>'
            f'<span>{right}</span></div></div>')


def stack3(layers):
    body = "".join(
        f'<div class="lay {"clay-acc acc" if l.get("acc") else ("clay-in" if l.get("inset") else "clay")}">'
        f'<b>{l["b"]}</b><u>{l["u"]}</u></div>' for l in layers)
    return f'<div class="stack3">{body}</div>'


def phone(bars, pop_l, pop_r):
    b = "".join(f'<i class="{"on" if on else ""}" style="height:{h}%"></i>' for h, on in bars)
    return (f'<div class="phone clay"><div class="scr clay-in"><div class="notch"></div>'
            f'<div class="chart">{b}</div>'
            f'<div class="pop clay-acc"><u>{pop_l}</u><b>{pop_r}</b></div></div></div>')


def grid2(cells):
    body = "".join(
        f'<div class="cell {"clay-acc acc" if c.get("acc") else "clay"}">'
        f'<u>{c["u"]}</u><b>{c["b"]}</b><i>{c["i"]}</i></div>' for c in cells)
    return f'<div class="grid2">{body}</div>'


def rail(steps, active):
    inner = ""
    for i, s in enumerate(steps):
        inner += f'<span class="{"on" if i == active else ""}">{s}</span>'
        if i < len(steps) - 1:
            inner += '<i>&rarr;</i>'
    return f'<div class="rail"><div class="in clay-in">{inner}</div></div>'


# ------------------------------------------------------------------ page

def slide(eyebrow, h, sub, body, obj, rail_html, i, n, uri):
    return (f'<div class="slide"><div class="amb"></div><div class="safe">'
            f'<div class="eyebrow">{eyebrow}</div>'
            f'<div class="h">{h}</div>'
            f'<div class="sub">{sub}</div>'
            + (f'<div class="body">{body}</div>' if body else '')
            + f'<div class="stage">{obj}</div>{rail_html}</div>'
            f'<div class="foot"><img src="{uri}" alt="">'
            f'<span>ULTRON <em>&middot;</em> 51ULTRON<em>.</em>COM</span></div></div>')


def build(slug: str, title: str, slides: list) -> pathlib.Path:
    uri = logo_uri()
    n = len(slides)
    out = ['<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">',
           f'<title>ULTRON CLAY - {title}</title>',
           f'<style>{fonts_css()}{CSS}</style></head><body>']
    for i, s in enumerate(slides, 1):
        out.append(slide(s["eyebrow"], s["h"], s["sub"], s.get("body", ""),
                         s["obj"], s.get("rail", ""), i, n, uri))
    out.append("</body></html>")
    p = CONTENT / f"{slug}.html"
    p.write_text("".join(out))
    return p
