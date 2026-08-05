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
import base64, functools, pathlib, re

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

/* ---------- expanded object library (CLAUDE.md 30, graphic variety) ----------
   Six forms across eight decks meant every cover was the same dial and every middle slide
   the same list. Twenty forms means a deck never repeats itself and no two decks open alike. */

.bars{width:700px;display:flex;flex-direction:column;gap:22px;}
.bars .b{display:flex;align-items:center;gap:20px;}
.bars .b u{width:190px;flex-shrink:0;text-align:left;font-size:24px;font-weight:800;
  text-decoration:none;letter-spacing:-.3px;}
.bars .b .tr{flex:1;height:52px;border-radius:26px;display:flex;align-items:center;}
.bars .b .tr i{height:100%;border-radius:26px;display:flex;align-items:center;
  justify-content:flex-end;padding-right:22px;font-size:22px;font-weight:800;color:#fff;}
.bars .b.acc .tr i{background:linear-gradient(158deg,var(--accl),var(--accd));}
.bars .b .tr i.mut{background:var(--deep);color:var(--muted);}

.timeline{width:720px;position:relative;padding:44px 0 0;}
.timeline .line{height:8px;border-radius:4px;margin:0 40px;}
.timeline .row{display:flex;justify-content:space-between;margin-top:-30px;padding:0 22px;}
.timeline .n{width:78px;display:flex;flex-direction:column;align-items:center;gap:14px;}
.timeline .dot{width:44px;height:44px;border-radius:50%;background:var(--deep);}
.timeline .n.on .dot{background:linear-gradient(158deg,var(--accl),var(--accd));
  box-shadow:0 0 0 8px rgba(210,100,70,.14);}
.timeline .n b{font-size:20px;font-weight:800;letter-spacing:.12em;color:var(--muted);}
.timeline .n.on b{color:var(--acc);}

.orbit{width:520px;height:460px;position:relative;display:flex;align-items:center;
  justify-content:center;}
.orbit .ring{position:absolute;width:430px;height:430px;border-radius:50%;
  border:3px dashed rgba(138,133,125,.30);}
.orbit .mid{width:210px;height:210px;border-radius:50%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:6px;}
.orbit .mid b{font-family:'Oswald',sans-serif;font-size:56px;font-weight:600;color:var(--acc);
  line-height:1;}
.orbit .mid u{font-size:18px;font-weight:800;letter-spacing:.20em;color:var(--muted);
  text-decoration:none;}
.orbit .s{position:absolute;width:118px;height:118px;border-radius:50%;display:flex;
  align-items:center;justify-content:center;text-align:center;font-size:19px;font-weight:800;
  line-height:1.1;padding:8px;}
.orbit .s.acc{color:#fff;}

.slip{width:600px;border-radius:28px;padding:36px 38px;}
.slip .t{display:flex;justify-content:space-between;font-size:20px;font-weight:800;
  letter-spacing:.16em;text-transform:uppercase;color:var(--muted);}
.slip .r{display:flex;justify-content:space-between;align-items:baseline;
  padding:20px 0;border-bottom:2px dashed rgba(138,133,125,.28);font-size:25px;font-weight:700;}
.slip .r span:last-child{font-weight:800;}
.slip .tot{display:flex;justify-content:space-between;align-items:baseline;padding-top:24px;}
.slip .tot span:first-child{font-size:21px;font-weight:800;letter-spacing:.16em;
  text-transform:uppercase;color:var(--muted);}
.slip .tot span:last-child{font-family:'Oswald',sans-serif;font-size:58px;font-weight:600;
  color:var(--acc);line-height:1;}

.cal{width:640px;border-radius:30px;padding:34px;}
.cal .hd{display:flex;justify-content:space-between;font-size:20px;font-weight:800;
  letter-spacing:.16em;text-transform:uppercase;color:var(--muted);margin-bottom:24px;}
.cal .g{display:grid;grid-template-columns:repeat(6,1fr);gap:13px;}
.cal .d{aspect-ratio:1;border-radius:12px;background:var(--deep);}
.cal .d.on{background:linear-gradient(158deg,var(--accl),var(--accd));}

.funnel{width:660px;display:flex;flex-direction:column;align-items:center;gap:18px;}
.funnel .s{border-radius:22px;padding:24px 30px;display:flex;align-items:center;
  justify-content:space-between;}
.funnel .s b{font-size:26px;font-weight:800;}
.funnel .s u{font-family:'Oswald',sans-serif;font-size:34px;font-weight:600;color:var(--acc);
  text-decoration:none;}
.funnel .s.acc b,.funnel .s.acc u{color:#fff;}

.chat{width:660px;display:flex;flex-direction:column;gap:20px;}
.chat .m{max-width:78%;border-radius:26px;padding:24px 28px;font-size:25px;font-weight:600;
  line-height:1.3;text-align:left;}
.chat .m.you{align-self:flex-end;color:#fff;border-bottom-right-radius:8px;}
.chat .m.them{align-self:flex-start;border-bottom-left-radius:8px;}

.meter{width:520px;height:300px;position:relative;display:flex;align-items:flex-end;
  justify-content:center;overflow:hidden;}
.meter .arc{position:absolute;top:0;width:500px;height:500px;border-radius:50%;
  border:44px solid var(--deep);}
.meter .fill{position:absolute;top:0;width:500px;height:500px;border-radius:50%;
  border:44px solid var(--acc);border-right-color:transparent;border-bottom-color:transparent;
  transform:rotate(var(--rot,-45deg));}
.meter .v{position:relative;z-index:2;text-align:center;padding-bottom:14px;}
.meter .v b{display:block;font-family:'Oswald',sans-serif;font-size:104px;font-weight:600;
  color:var(--acc);line-height:1;}
.meter .v u{display:block;font-size:20px;font-weight:800;letter-spacing:.20em;
  color:var(--muted);text-decoration:none;margin-top:8px;}

.stamp{width:400px;height:400px;border-radius:50%;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:10px;transform:rotate(-7deg);}
.stamp b{font-family:'Oswald',sans-serif;font-size:74px;font-weight:600;line-height:.96;
  color:#fff;text-transform:uppercase;text-align:center;padding:0 30px;}
.stamp u{font-size:20px;font-weight:800;letter-spacing:.24em;color:rgba(255,255,255,.82);
  text-decoration:none;}
.stamp .edge{position:absolute;width:344px;height:344px;border-radius:50%;
  border:4px solid rgba(255,255,255,.32);}

.versus{width:700px;display:flex;align-items:stretch;gap:18px;position:relative;}
.versus>div{flex:1;border-radius:28px;padding:34px 26px;display:flex;flex-direction:column;
  gap:14px;justify-content:center;}
.versus u{font-size:19px;font-weight:800;letter-spacing:.20em;text-transform:uppercase;
  color:var(--muted);text-decoration:none;}
.versus b{font-family:'Oswald',sans-serif;font-size:66px;font-weight:600;line-height:.98;}
.versus i{font-size:21px;font-style:normal;color:var(--muted);line-height:1.26;}
.versus .new u,.versus .new i{color:rgba(255,255,255,.84);}
.versus .new b{color:#fff;}

.stepper{width:700px;display:flex;align-items:center;}
.stepper .st{display:flex;flex-direction:column;align-items:center;gap:14px;width:110px;}
.stepper .st .c{width:76px;height:76px;border-radius:50%;display:flex;align-items:center;
  justify-content:center;font-family:'Oswald',sans-serif;font-size:34px;font-weight:600;
  color:var(--muted);}
.stepper .st.on .c{color:#fff;}
.stepper .st b{font-size:19px;font-weight:800;letter-spacing:.10em;text-transform:uppercase;
  color:var(--muted);}
.stepper .st.on b{color:var(--acc);}
.stepper .ln{flex:1;height:6px;border-radius:3px;background:var(--deep);}

.chips{width:700px;display:flex;flex-wrap:wrap;justify-content:center;gap:16px;}
.chips span{border-radius:40px;padding:20px 30px;font-size:25px;font-weight:800;
  letter-spacing:-.2px;}
.chips span.acc{color:#fff;}
.chips span.off{color:var(--muted);text-decoration:line-through;}

.inbox{width:680px;display:flex;flex-direction:column;gap:14px;}
.inbox .m{border-radius:22px;padding:22px 26px;display:flex;align-items:center;gap:20px;
  text-align:left;}
.inbox .av{width:56px;height:56px;border-radius:50%;flex-shrink:0;background:var(--deep);}
.inbox .m.acc .av{background:rgba(255,255,255,.28);}
.inbox .tx{flex:1;}
.inbox .tx b{display:block;font-size:24px;font-weight:800;}
.inbox .tx i{display:block;font-size:20px;font-style:normal;color:var(--muted);margin-top:4px;}
.inbox .m.acc .tx b{color:#fff;} .inbox .m.acc .tx i{color:rgba(255,255,255,.80);}
.inbox .tag{font-size:18px;font-weight:800;letter-spacing:.14em;color:var(--acc);}
.inbox .m.acc .tag{color:#fff;}

.counter{width:600px;border-radius:32px;padding:48px 40px;text-align:center;}
.counter u{display:block;font-size:21px;font-weight:800;letter-spacing:.24em;
  text-transform:uppercase;color:var(--muted);text-decoration:none;}
.counter b{display:block;font-family:'Oswald',sans-serif;font-size:150px;font-weight:600;
  line-height:.92;color:var(--acc);margin-top:14px;}
.counter i{display:inline-block;font-style:normal;margin-top:20px;border-radius:30px;
  padding:12px 24px;font-size:22px;font-weight:800;color:#fff;}
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

# ---- expanded library: fourteen more forms, so a deck never repeats itself ----

def bars(items):
    b = "".join(
        f'<div class="b {"acc" if i.get("acc") else ""}"><u>{i["k"]}</u>'
        f'<div class="tr clay-in"><i class="{"" if i.get("acc") else "mut"}" '
        f'style="width:{i["p"]}%">{i["v"]}</i></div></div>' for i in items)
    return f'<div class="bars">{b}</div>'


def timeline(nodes, active):
    n = "".join(f'<div class="n {"on" if k == active else ""}">'
                f'<div class="dot"></div><b>{v}</b></div>' for k, v in enumerate(nodes))
    return f'<div class="timeline"><div class="line clay-in"></div><div class="row">{n}</div></div>'


def orbit(center, label, sats):
    POS = [("top:0;left:50%;margin-left:-59px", 0), ("top:50%;right:0;margin-top:-59px", 1),
           ("bottom:0;left:50%;margin-left:-59px", 2), ("top:50%;left:0;margin-top:-59px", 3)]
    s = "".join(f'<div class="s {"clay-acc acc" if x.get("acc") else "clay"}" '
                f'style="{POS[k][0]}">{x["t"]}</div>' for k, x in enumerate(sats[:4]))
    return (f'<div class="orbit"><div class="ring"></div>'
            f'<div class="mid clay"><b>{center}</b><u>{label}</u></div>{s}</div>')


def slip(head, rows, total_label, total):
    r = "".join(f'<div class="r"><span>{a}</span><span>{b}</span></div>' for a, b in rows)
    return (f'<div class="slip clay"><div class="t"><span>{head[0]}</span>'
            f'<span>{head[1]}</span></div>{r}'
            f'<div class="tot"><span>{total_label}</span><span>{total}</span></div></div>')


def calendar(head, filled, total=30):
    d = "".join(f'<div class="d {"on" if i < filled else ""}"></div>' for i in range(total))
    return (f'<div class="cal clay"><div class="hd"><span>{head[0]}</span>'
            f'<span>{head[1]}</span></div><div class="g">{d}</div></div>')


def funnel(stages):
    w = [100, 78, 56]
    s = "".join(f'<div class="s {"clay-acc acc" if i == len(stages)-1 else "clay"}" '
                f'style="width:{w[min(i,2)]}%"><b>{x["b"]}</b><u>{x["v"]}</u></div>'
                for i, x in enumerate(stages))
    return f'<div class="funnel">{s}</div>'


def chat(msgs):
    m = "".join(f'<div class="m {"you clay-acc" if x.get("you") else "them clay"}">{x["t"]}</div>'
                for x in msgs)
    return f'<div class="chat">{m}</div>'


def meter(pct, big, label):
    rot = -45 + (pct / 100) * 180
    return (f'<div class="meter"><div class="arc clay-in"></div>'
            f'<div class="fill" style="--rot:{rot:.0f}deg"></div>'
            f'<div class="v"><b>{big}</b><u>{label}</u></div></div>')


def stamp(word, sub):
    return f'<div class="stamp clay-acc"><div class="edge"></div><b>{word}</b><u>{sub}</u></div>'


def versus(old, new):
    return (f'<div class="versus"><div class="old clay-in"><u>{old["u"]}</u>'
            f'<b>{old["b"]}</b><i>{old["i"]}</i></div>'
            f'<div class="new clay-acc"><u>{new["u"]}</u><b>{new["b"]}</b>'
            f'<i>{new["i"]}</i></div></div>')


def stepper(steps, active):
    out = []
    for i, s in enumerate(steps):
        on = "on" if i <= active else ""
        cls = "clay-acc" if i <= active else "clay-in"
        out.append(f'<div class="st {on}"><div class="c {cls}">{i+1}</div><b>{s}</b></div>')
        if i < len(steps) - 1:
            out.append('<div class="ln"></div>')
    return f'<div class="stepper">{"".join(out)}</div>'


def chips(items):
    c = "".join(f'<span class="{"clay-acc acc" if x.get("acc") else ("clay off" if x.get("off") else "clay")}">'
                f'{x["t"]}</span>' for x in items)
    return f'<div class="chips">{c}</div>'


def inbox(rows):
    m = "".join(f'<div class="m {"clay-acc acc" if x.get("acc") else "clay"}">'
                f'<div class="av"></div><div class="tx"><b>{x["b"]}</b><i>{x["i"]}</i></div>'
                f'<div class="tag">{x["t"]}</div></div>' for x in rows)
    return f'<div class="inbox">{m}</div>'


def counter(label, big, delta):
    return (f'<div class="counter clay"><u>{label}</u><b>{big}</b>'
            f'<i class="clay-acc">{delta}</i></div>')


# ---- object identity travels with the markup ----
# The graphic-variety rule (CLAUDE.md 30) is only enforceable if the guard can see what a
# slide actually renders. It used to read a hand-typed `run=` string next to the deck, which
# went stale the moment the objects were swapped: every run still claimed to open on `dial`
# while the built pages opened on eight different forms, so the uniqueness assertion passed
# against fiction. Each object now stamps its own name on its root node, and the run is read
# back off the slides.

OBJECTS = ("dial cards badge stack3 phone grid2 bars timeline orbit slip calendar funnel "
           "chat meter stamp versus stepper chips inbox counter").split()


def _tag(name, fn):
    @functools.wraps(fn)
    def wrapped(*a, **k):
        return fn(*a, **k).replace("<div ", f'<div data-ob="{name}" ', 1)
    return wrapped


for _name in OBJECTS:
    globals()[_name] = _tag(_name, globals()[_name])


def obj_name(html: str) -> str:
    m = re.search(r'data-ob="([a-z0-9]+)"', html)
    return m.group(1) if m else "?"
