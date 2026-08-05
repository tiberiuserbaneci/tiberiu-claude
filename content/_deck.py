#!/usr/bin/env python3
"""Build the ULTRON PAPER carousels: ten light-system decks, seven slides each.

Why a builder rather than ten hand written pages. Seventy slides typed by hand drift: a
padding here, a type size there, and by deck four nothing lines up with deck one any more.
The layout primitives live in one place, the decks are data, and every slide is exactly
1080x1920 by construction rather than by inspection.

What this fixes about the reference deck it is modelled on:

  1. The reference loads Tailwind and Google Fonts from a CDN. Headless Chromium in this
     sandbox cannot reach either, so that page renders unstyled and cannot be exported at
     all. Everything here is inlined, fonts included as a local @font-face free stack of
     families already used across the repo.
  2. It sizes slides with `aspect-ratio: 9/16; max-width: 480px`, which is a preview, not a
     canvas. These are 1080x1920 exactly.
  3. Its footer sits at `bottom: 6%`, which is 115px on a 1920 frame, well inside TikTok's
     caption band (CLAUDE.md 9 puts the bottom inset at 330px). Every footer here clears it.
  4. Its accent is #F27A45, which is not in either brand system. These run the REALNUMBERS
     palette (CLAUDE.md 8).
  5. Its content area centres a small object in a large empty box. These pack the band,
     because an airy dominant block is the recurring rejection (CLAUDE.md 27.9).

Usage:
  python3 content/_deck.py            # write all ten decks into content/
  python3 content/_deck.py chat brain # only the named decks
"""
import base64, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

def fonts_css() -> str:
    """Embedded, never linked. The renderer has no network; a <link> to Google Fonts renders
    the whole deck in a fallback grotesque and nothing warns you."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("_fonts", CONTENT / "_fonts.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.embedded_css()


def logo_uri() -> str:
    return "data:image/png;base64," + base64.b64encode(
        (CONTENT / "ultron-logo.png").read_bytes()).decode()


CSS = """
:root{
  --paper:#EFEBE0; --paper2:#E6E0D0; --card:#FAF8F2; --card2:#F4F0E6;
  --ink:#141312; --ink70:rgba(20,19,18,.70); --ink46:rgba(20,19,18,.46);
  --ink26:rgba(20,19,18,.26); --hair:rgba(20,19,18,.13); --rule:rgba(20,19,18,.20);
  --book:#C84623; --bookd:#A8391D; --ed:#D26446; --kraft:#B98A63;
  --booklo:rgba(200,70,35,.09); --bookbd:rgba(200,70,35,.30);
  --dead:#23211E;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#191817;display:flex;flex-direction:column;align-items:center;gap:40px;
  padding:40px 0;font-family:'DM Sans',sans-serif;-webkit-font-smoothing:antialiased;}
.slide{width:1080px;height:1920px;position:relative;overflow:hidden;background:var(--paper);
  color:var(--ink);flex-shrink:0;}
.gr{position:absolute;inset:0;
  background-image:linear-gradient(rgba(20,19,18,.045) 1px,transparent 1px),
    linear-gradient(90deg,rgba(20,19,18,.045) 1px,transparent 1px);
  background-size:100% 120px,120px 100%;}
.wash{position:absolute;inset:0;
  background:radial-gradient(ellipse 70% 34% at 50% -2%,rgba(255,255,255,.66) 0%,transparent 62%),
    radial-gradient(ellipse 50% 28% at 96% 100%,rgba(200,70,35,.08) 0%,transparent 60%);}
.nz{position:absolute;inset:0;opacity:.05;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");}

/* Safe box per CLAUDE.md 9: top 300, right 130, bottom 330, left 70. The reference deck put
   its footer 115px off the bottom, which TikTok's caption band covers outright. */
.safe{position:absolute;top:300px;left:70px;right:130px;bottom:330px;z-index:5;
  display:flex;flex-direction:column;}
.mast{flex-shrink:0;display:flex;justify-content:space-between;align-items:center;
  font-family:'DM Mono',monospace;font-size:21px;font-weight:500;letter-spacing:.20em;
  text-transform:uppercase;color:var(--ink26);padding-bottom:14px;
  border-bottom:2px solid var(--rule);}
.mast .tag{color:var(--book);}
.body{flex:1;min-height:0;display:flex;flex-direction:column;padding-top:26px;gap:22px;}
.foot{flex-shrink:0;display:flex;align-items:center;gap:13px;padding-top:16px;
  border-top:2px solid var(--rule);}
.foot img{width:33px;height:33px;border-radius:50%;object-fit:cover;}
.foot span{font-family:'DM Mono',monospace;font-size:19px;font-weight:500;letter-spacing:.14em;
  text-transform:uppercase;color:var(--ink26);white-space:nowrap;overflow:hidden;}
.foot span em{color:var(--book);font-style:normal;}
.foot .pg{margin-left:auto;font-family:'DM Mono',monospace;font-size:19px;letter-spacing:.14em;
  color:var(--ink46);flex-shrink:0;}

/* ---- shared blocks ---- */
.kicker{font-family:'DM Mono',monospace;font-size:22px;letter-spacing:.20em;
  text-transform:uppercase;color:var(--book);flex-shrink:0;}
.h1{font-family:'Anton',sans-serif;font-size:126px;line-height:.90;letter-spacing:-2px;
  text-transform:uppercase;flex-shrink:0;}
.h1 em{color:var(--book);font-style:normal;}
.h2{font-family:'Anton',sans-serif;font-size:88px;line-height:.92;letter-spacing:-1.4px;
  text-transform:uppercase;flex-shrink:0;}
.h2 em{color:var(--book);font-style:normal;}
.sub{font-size:33px;font-weight:500;line-height:1.28;color:var(--ink70);flex-shrink:0;}
.sub b{color:var(--ink);font-weight:800;}
.sub i{font-family:'Instrument Serif',serif;font-style:italic;color:var(--ink46);}
.note{flex-shrink:0;display:flex;align-items:center;gap:16px;padding:22px 26px;
  border-radius:16px;background:var(--booklo);border:2px solid var(--bookbd);}
.note .l{font-family:'DM Mono',monospace;font-size:19px;letter-spacing:.15em;
  text-transform:uppercase;color:var(--book);flex-shrink:0;}
.note .r{margin-left:auto;font-size:28px;font-weight:800;letter-spacing:-.5px;text-align:right;}

/* rows: the dense reference table */
.rows{flex:1;min-height:0;display:flex;flex-direction:column;gap:12px;}
.row{flex:1;max-height:190px;display:flex;align-items:center;gap:24px;padding:0 26px;
  border-radius:15px;background:var(--card);border:2px solid var(--hair);position:relative;
  overflow:hidden;}
.row::before{content:'';position:absolute;left:0;top:0;bottom:0;width:7px;background:var(--book);
  opacity:.22;}
.row .n{font-family:'Anton',sans-serif;font-size:56px;color:var(--book);width:76px;
  flex-shrink:0;line-height:1;}
.row .t b{display:block;font-size:38px;font-weight:900;letter-spacing:-.8px;line-height:1.06;}
.row .t i{display:block;font-size:26px;font-style:normal;color:var(--ink70);margin-top:8px;
  line-height:1.24;}
.row .v{margin-left:auto;flex-shrink:0;font-family:'DM Mono',monospace;font-size:21px;
  letter-spacing:.12em;text-transform:uppercase;color:var(--book);padding:10px 15px;
  border-radius:9px;background:var(--booklo);border:2px solid var(--bookbd);}
.row.on{background:linear-gradient(180deg,#FFF2EB,#FFE6DA);border-color:var(--bookbd);}

/* grid: tiles */
.grid{flex:1;min-height:0;display:grid;gap:14px;}
.tile{border-radius:15px;background:var(--card);border:2px solid var(--hair);padding:22px;
  display:flex;flex-direction:column;justify-content:center;gap:8px;}
.tile u{font-family:'DM Mono',monospace;font-size:19px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--book);text-decoration:none;}
.tile b{font-size:35px;font-weight:900;letter-spacing:-.8px;line-height:1.06;}
.tile i{font-size:23px;font-style:normal;color:var(--ink70);line-height:1.26;}
.tile.dark{background:var(--dead);border-color:var(--dead);}
.tile.dark b{color:#FAF8F2;} .tile.dark i{color:rgba(250,248,242,.62);}
.tile.dark u{color:var(--ed);}

/* split: the before and after */
.split{flex:1;min-height:0;display:flex;gap:16px;}
.split>div{flex:1;border-radius:16px;padding:26px;display:flex;flex-direction:column;gap:14px;}
.split .old{background:var(--dead);color:#FAF8F2;}
.split .new{background:linear-gradient(180deg,#FFF2EB,#FFE4D7);border:2px solid var(--bookbd);}
.split h4{font-family:'DM Mono',monospace;font-size:20px;letter-spacing:.16em;
  text-transform:uppercase;font-weight:500;}
.split .old h4{color:rgba(250,248,242,.50);} .split .new h4{color:var(--book);}
.split ul{list-style:none;display:flex;flex-direction:column;gap:12px;flex:1;
  justify-content:center;}
.split li{font-size:29px;font-weight:600;line-height:1.2;padding-left:34px;position:relative;}
.split li::before{content:'';position:absolute;left:0;top:11px;width:20px;height:3px;
  border-radius:2px;background:currentColor;opacity:.45;}
.split .old li{color:rgba(250,248,242,.80);}
.split .big{font-family:'Anton',sans-serif;font-size:70px;line-height:1;letter-spacing:-1px;}
.split .old .big{color:#FAF8F2;} .split .new .big{color:var(--book);}

/* chart: proportional bars, drawn against a full track so the frame is never thin */
.chart{flex:1;min-height:0;display:flex;flex-direction:column;gap:14px;}
.bar{flex:1;display:flex;align-items:center;gap:20px;}
.bar .k{width:220px;flex-shrink:0;font-size:28px;font-weight:800;letter-spacing:-.4px;
  line-height:1.12;}
.bar .k s{display:block;font-family:'DM Mono',monospace;font-size:18px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--ink46);text-decoration:none;margin-top:4px;}
.bar .tr{flex:1;height:100%;border-radius:12px;background:var(--dead);overflow:hidden;
  display:flex;align-items:center;}
.bar .tr i{display:block;height:100%;border-radius:10px;
  background:linear-gradient(90deg,var(--ed),var(--book));display:flex;align-items:center;
  justify-content:flex-end;padding-right:20px;}
.bar .tr i em{font-family:'Anton',sans-serif;font-size:44px;color:#FFF3EA;font-style:normal;}

/* stack: layered steps with a spine */
.stack{flex:1;min-height:0;display:flex;flex-direction:column;gap:0;position:relative;
  padding-left:56px;}
.stack::before{content:'';position:absolute;left:19px;top:26px;bottom:26px;width:4px;
  border-radius:2px;background:var(--rule);}
.step{flex:1;max-height:190px;display:flex;align-items:center;gap:22px;position:relative;}
.step::before{content:'';position:absolute;left:-46px;top:50%;transform:translateY(-50%);
  width:30px;height:30px;border-radius:50%;background:var(--book);
  box-shadow:0 0 0 7px var(--paper),0 0 0 10px var(--bookbd);}
.step .c{flex:1;border-radius:15px;background:var(--card);border:2px solid var(--hair);
  padding:20px 26px;}
.step .c b{display:block;font-size:36px;font-weight:900;letter-spacing:-.8px;line-height:1.06;}
.step .c i{display:block;font-size:25px;font-style:normal;color:var(--ink70);margin-top:7px;
  line-height:1.26;}
.step .c u{float:right;font-family:'DM Mono',monospace;font-size:19px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--book);text-decoration:none;margin-left:16px;}

/* cover signature object */
.mark{flex:1;min-height:0;display:flex;align-items:center;justify-content:center;
  border-radius:20px;background:var(--dead);position:relative;overflow:hidden;}
.mark .num{font-family:'Anton',sans-serif;font-size:430px;line-height:.78;color:var(--book);
  letter-spacing:-10px;}
.mark .num s{font-size:.42em;text-decoration:none;color:var(--ed);}
.mark .cap{position:absolute;left:34px;right:34px;bottom:30px;
  font-family:'DM Mono',monospace;font-size:21px;letter-spacing:.15em;text-transform:uppercase;
  color:rgba(250,248,242,.55);display:flex;justify-content:space-between;}
.mark .tick{position:absolute;inset:0;
  background-image:repeating-linear-gradient(90deg,rgba(250,248,242,.07) 0 2px,transparent 2px 60px);}

/* cta */
.ctaw{flex:1;min-height:0;display:flex;flex-direction:column;gap:20px;}
.ctaw .kw{font-family:'Anton',sans-serif;font-size:158px;line-height:.86;color:var(--book);
  letter-spacing:-4px;text-transform:uppercase;flex-shrink:0;}
.ctaw .ln{font-size:34px;font-weight:600;color:var(--ink70);line-height:1.22;flex-shrink:0;}
.recap{flex:1;min-height:0;display:flex;flex-direction:column;gap:13px;}
.recap div{flex:1;max-height:180px;display:flex;align-items:center;gap:20px;padding:0 26px;
  border-radius:15px;background:var(--card);border:2px solid var(--hair);position:relative;
  overflow:hidden;}
.recap div::before{content:'';position:absolute;left:0;top:0;bottom:0;width:7px;
  background:var(--book);opacity:.22;}
.recap u{font-family:'Anton',sans-serif;font-size:50px;color:var(--book);text-decoration:none;
  width:74px;flex-shrink:0;line-height:1;}
.recap b{font-size:35px;font-weight:900;letter-spacing:-.8px;line-height:1.06;}
"""


# ----------------------------------------------------------------- layout primitives

def esc(s: str) -> str:
    return s


def cover(kicker, h1, sub, num, capl, capr):
    return (f'<div class="kicker">{kicker}</div><div class="h1">{h1}</div>'
            f'<div class="sub">{sub}</div>'
            f'<div class="mark"><div class="tick"></div><div class="num">{num}</div>'
            f'<div class="cap"><span>{capl}</span><span>{capr}</span></div></div>')


def rows(h2, sub, items, note=None):
    body = "".join(
        f'<div class="row{" on" if it.get("on") else ""}"><div class="n">{it["n"]}</div>'
        f'<div class="t"><b>{it["b"]}</b><i>{it["i"]}</i></div>'
        + (f'<div class="v">{it["v"]}</div>' if it.get("v") else "")
        + '</div>' for it in items)
    out = f'<div class="h2">{h2}</div><div class="sub">{sub}</div><div class="rows">{body}</div>'
    if note:
        out += f'<div class="note"><span class="l">{note[0]}</span><span class="r">{note[1]}</span></div>'
    return out


def grid(h2, sub, items, cols=2, note=None):
    body = "".join(
        f'<div class="tile{" dark" if it.get("dark") else ""}">'
        f'<u>{it["u"]}</u><b>{it["b"]}</b><i>{it["i"]}</i></div>' for it in items)
    out = (f'<div class="h2">{h2}</div><div class="sub">{sub}</div>'
           f'<div class="grid" style="grid-template-columns:repeat({cols},1fr)">{body}</div>')
    if note:
        out += f'<div class="note"><span class="l">{note[0]}</span><span class="r">{note[1]}</span></div>'
    return out


def split(h2, sub, old, new, note=None):
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)
    out = (f'<div class="h2">{h2}</div><div class="sub">{sub}</div><div class="split">'
           f'<div class="old"><h4>{old["h"]}</h4><div class="big">{old["big"]}</div>'
           f'<ul>{li(old["li"])}</ul></div>'
           f'<div class="new"><h4>{new["h"]}</h4><div class="big">{new["big"]}</div>'
           f'<ul>{li(new["li"])}</ul></div></div>')
    if note:
        out += f'<div class="note"><span class="l">{note[0]}</span><span class="r">{note[1]}</span></div>'
    return out


def chart(h2, sub, bars, note=None):
    body = "".join(
        f'<div class="bar"><div class="k">{b["k"]}<s>{b["s"]}</s></div>'
        f'<div class="tr"><i style="width:{b["p"]}%"><em>{b["v"]}</em></i></div></div>'
        for b in bars)
    out = f'<div class="h2">{h2}</div><div class="sub">{sub}</div><div class="chart">{body}</div>'
    if note:
        out += f'<div class="note"><span class="l">{note[0]}</span><span class="r">{note[1]}</span></div>'
    return out


def stack(h2, sub, steps, note=None):
    body = "".join(
        f'<div class="step"><div class="c">'
        + (f'<u>{s["u"]}</u>' if s.get("u") else "")
        + f'<b>{s["b"]}</b><i>{s["i"]}</i></div></div>' for s in steps)
    out = f'<div class="h2">{h2}</div><div class="sub">{sub}</div><div class="stack">{body}</div>'
    if note:
        out += f'<div class="note"><span class="l">{note[0]}</span><span class="r">{note[1]}</span></div>'
    return out


def cta(kw, line, recap, link):
    body = "".join(f'<div><u>{i+1:02d}</u><b>{r}</b></div>' for i, r in enumerate(recap))
    return (f'<div class="ctaw"><div class="kicker">COMMENT</div>'
            f'<div class="kw">{kw}</div><div class="ln">{line}</div>'
            f'<div class="recap">{body}</div>'
            f'<div class="note"><span class="l">where it lives</span>'
            f'<span class="r">{link}</span></div></div>')


# ----------------------------------------------------------------- page assembly

def build(slug: str, title: str, tag: str, slides: list) -> pathlib.Path:
    uri = logo_uri()
    out = [f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">',
           f'<title>ULTRON PAPER - {title}</title>',
           f'<style>{fonts_css()}{CSS}</style></head><body>']
    n = len(slides)
    for i, s in enumerate(slides, 1):
        out.append(
            f'<div class="slide"><div class="gr"></div><div class="wash"></div><div class="nz"></div>'
            f'<div class="safe">'
            f'<div class="mast"><span>ULTRON PAPER &middot; {title}</span>'
            f'<span class="tag">{tag}</span></div>'
            f'<div class="body">{s}</div>'
            f'<div class="foot"><img src="{uri}" alt="">'
            f'<span>ULTRON <em>&middot;</em> AI OPERATOR FOR FOUNDERS <em>&middot;</em> '
            f'51ULTRON<em>.</em>COM</span><span class="pg">{i:02d}/{n:02d}</span></div>'
            f'</div></div>')
    out.append("</body></html>")
    p = CONTENT / f"{slug}.html"
    p.write_text("".join(out))
    return p
