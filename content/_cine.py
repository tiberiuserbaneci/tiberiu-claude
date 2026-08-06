#!/usr/bin/env python3
"""ULTRON CINE: glass on a photograph, for the UGC-film look.

Operator, 2026-08-06, handing over a reference clip: a founder talking to camera, intercut with
cinematic B-roll - warm keyboard bokeh, a desk at night, monitor glow - with word-by-word
captions over it. "Adapteaza la Ultron... fara personaj, replit etc... te poti juca cu tema
carouselului sa nu devenim plictisitori."

So the transferable part is not the presenter and not their product. It is the PHOTOGRAPHIC
GROUND, which eleven clay decks have never used, and which is exactly what CLAUDE.md 18 ranks
second behind operator captures: "texture and atmosphere (paper, desk, warm light), heavily
blurred, as background only". The reference does the same thing with its keyboard shot.

The photograph is blurred hard and graded down. That is not only a look: at this blur the
monitor in the frame is unreadable, so nothing of anyone else's product is on screen, which is
the trademark caution in 18 satisfied by construction rather than by promise. No people are in
frame either, which is the operator's own condition and 18's stock-photo caution.

Everything above the photograph is frosted glass. Clay is a solid on cream; this is a pane on a
photograph. Same grid, same guards, a completely different material.
"""
import base64, pathlib, re

CONTENT = pathlib.Path(__file__).resolve().parent
TEX = CONTENT / "assets" / "tex"

CANVAS_W, CANVAS_H = 1080, 1920
SAFE_T, SAFE_R, SAFE_B, SAFE_L = 300, 130, 330, 70
COL_W = CANVAS_W - SAFE_L - SAFE_R
BAND_H = CANVAS_H - SAFE_T - SAFE_B

GAP = 22
STAGE_W, STAGE_H = COL_W, 660
CAP_H = 74
FOOT_H = 58
HEADER_H = BAND_H - (GAP + STAGE_H + GAP + CAP_H + GAP + FOOT_H)

_SPEC = {"9x16": (1080, 1920, 300, 130, 330, 70, 660),
         "4x5":  (1080, 1350,  96,  90, 110, 90, 566)}


def set_format(name: str) -> None:
    global CANVAS_W, CANVAS_H, SAFE_T, SAFE_R, SAFE_B, SAFE_L
    global COL_W, BAND_H, STAGE_W, STAGE_H, HEADER_H
    (CANVAS_W, CANVAS_H, SAFE_T, SAFE_R, SAFE_B, SAFE_L, STAGE_H) = _SPEC[name]
    COL_W = CANVAS_W - SAFE_L - SAFE_R
    BAND_H = CANVAS_H - SAFE_T - SAFE_B
    STAGE_W = COL_W
    HEADER_H = BAND_H - (GAP + STAGE_H + GAP + CAP_H + GAP + FOOT_H)


def ground_uri(name: str = "desk") -> str:
    raw = (TEX / f"{name}.jpg").read_bytes()
    return "data:image/jpeg;base64," + base64.b64encode(raw).decode()


def css() -> str:
    return f"""
:root{{
  --ink:#FAF7F2; --ink70:rgba(250,247,242,.74); --ink46:rgba(250,247,242,.48);
  --ink18:rgba(250,247,242,.18); --ink10:rgba(250,247,242,.10);
  --acc:#E9784E; --accd:#B44521; --accl:#F5966F;
  --glass:rgba(24,20,17,.52); --glass2:rgba(38,31,26,.62);
}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:#000;}}
.slide{{width:{CANVAS_W}px;height:{CANVAS_H}px;position:relative;overflow:hidden;
  background:#0B0908;font-family:'Plus Jakarta Sans',sans-serif;color:var(--ink);}}

/* the photograph, blurred to atmosphere and graded warm */
.bgwrap{{position:absolute;inset:0;overflow:hidden;}}
.bg{{position:absolute;inset:0;background-size:cover;background-position:center 38%;
  filter:blur(26px) saturate(1.15) brightness(.62);transform:scale(1.22);
  transform-origin:center 42%;}}
.grade{{position:absolute;inset:0;
  background:
    radial-gradient(ellipse 62% 34% at 50% 8%,rgba(233,120,78,.20) 0%,transparent 62%),
    radial-gradient(ellipse 70% 44% at 50% 100%,rgba(0,0,0,.72) 0%,transparent 64%),
    linear-gradient(180deg,rgba(8,6,5,.58) 0%,rgba(8,6,5,.30) 40%,rgba(8,6,5,.80) 100%);}}
.grain{{position:absolute;inset:0;opacity:.5;
  background-image:radial-gradient(rgba(255,255,255,.05) 1px,transparent 1.2px);
  background-size:3px 3px;}}

.safe{{position:absolute;top:{SAFE_T}px;left:{SAFE_L}px;
  width:{COL_W}px;height:{BAND_H}px;display:flex;flex-direction:column;z-index:2;}}
.hd{{height:{HEADER_H}px;flex:0 0 {HEADER_H}px;display:flex;flex-direction:column;
  justify-content:flex-start;overflow:hidden;}}
.eyebrow{{font-family:'DM Mono',monospace;font-size:25px;font-weight:500;letter-spacing:.30em;
  text-transform:uppercase;color:var(--acc);margin-bottom:12px;}}
.h{{font-family:'Anton',sans-serif;font-size:104px;line-height:.92;letter-spacing:-.015em;
  text-transform:uppercase;color:var(--ink);text-shadow:0 6px 40px rgba(0,0,0,.55);}}
.h em{{font-style:normal;color:var(--acc);}}
.sub{{font-size:32px;line-height:1.30;font-weight:600;color:var(--ink70);margin-top:14px;
  max-width:{COL_W - 40}px;text-shadow:0 3px 22px rgba(0,0,0,.6);}}
.sub b{{color:var(--ink);font-weight:800;}}

.stage{{height:{STAGE_H}px;flex:0 0 {STAGE_H}px;margin-top:{GAP}px;position:relative;}}
.scene{{position:absolute;inset:0;}}

.cap{{height:{CAP_H}px;flex:0 0 {CAP_H}px;margin-top:{GAP}px;display:flex;align-items:center;
  gap:18px;}}
.cap i{{font-style:normal;flex:0 0 auto;background:var(--acc);color:#1A0B05;font-size:21px;
  font-weight:900;letter-spacing:.14em;text-transform:uppercase;padding:12px 20px;
  border-radius:9px;box-shadow:0 10px 30px rgba(233,120,78,.34);}}
.cap span{{font-size:30px;font-weight:700;color:var(--ink);line-height:1.22;
  text-shadow:0 3px 18px rgba(0,0,0,.6);}}

.foot{{height:{FOOT_H}px;flex:0 0 {FOOT_H}px;margin-top:{GAP}px;display:flex;align-items:center;
  gap:14px;}}
.foot img{{width:38px;height:38px;border-radius:50%;}}
.foot span{{font-family:'DM Mono',monospace;font-size:22px;letter-spacing:.20em;
  color:var(--ink46);text-transform:uppercase;}}
.foot em{{font-style:normal;color:var(--acc);}}

/* ---- the material: a frosted pane, not a solid ---- */
.pane{{background:var(--glass);backdrop-filter:blur(18px);
  border:1px solid var(--ink18);border-radius:22px;
  box-shadow:0 26px 60px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.14);}}
.pane.hot{{background:linear-gradient(155deg,rgba(233,120,78,.90),rgba(180,69,33,.86));
  border-color:rgba(255,255,255,.30);color:#fff;
  box-shadow:0 26px 60px rgba(180,69,33,.42), inset 0 1px 0 rgba(255,255,255,.36);}}
.pane.dim{{background:rgba(16,13,11,.44);}}
"""


# ------------------------------------------------------------------ scenes

def _wrap(form, body):
    return f'<div class="scene" data-ob="{form}">{body}</div>'


def scene_rows(rows, foot):
    """Stacked panes, each one a line of the argument."""
    n = len(rows)
    gap = 14
    h = (STAGE_H - 86 - gap * (n - 1)) // n
    out = []
    for k, r in enumerate(rows):
        hot = " hot" if r.get("hot") else (" dim" if r.get("dim") else "")
        out.append(
            f'<div class="pane{hot}" style="position:absolute;top:{k*(h+gap)}px;left:0;'
            f'width:{STAGE_W}px;height:{h}px;padding:0 30px;display:flex;align-items:center;'
            f'gap:26px;overflow:hidden;">'
            f'<div style="font-family:\'Anton\',sans-serif;font-size:{int(h*.52)}px;'
            f'line-height:1;{"color:#fff" if r.get("hot") else "color:var(--acc)"};'
            f'min-width:150px;">{r["n"]}</div>'
            f'<div style="flex:1;min-width:0;">'
            f'<div style="font-size:36px;font-weight:800;line-height:1.06;">{r["b"]}</div>'
            f'<div style="font-size:25px;font-weight:600;margin-top:5px;'
            f'{"color:rgba(255,255,255,.86)" if r.get("hot") else "color:var(--ink46)"};">'
            f'{r["i"]}</div></div></div>')
    out.append(f'<div style="position:absolute;bottom:0;left:0;width:{STAGE_W}px;height:70px;'
               f'display:flex;align-items:center;font-family:\'DM Mono\',monospace;'
               f'font-size:23px;letter-spacing:.18em;text-transform:uppercase;'
               f'color:var(--ink46);">{foot}</div>')
    return _wrap("rows", "".join(out))


def scene_screen(url, title, lines, foot):
    """A window on the desk: the page or the inbox the story is about."""
    r = "".join(
        f'<div style="flex:1;min-height:0;display:flex;align-items:center;gap:20px;'
        f'border-bottom:1px solid var(--ink10);overflow:hidden;">'
        f'<div style="width:11px;height:11px;border-radius:50%;flex:0 0 11px;'
        f'background:{"var(--acc)" if x.get("hot") else "var(--ink18)"};"></div>'
        f'<span style="flex:1;font-size:31px;font-weight:700;">{x["b"]}</span>'
        f'<span style="font-family:\'DM Mono\',monospace;font-size:21px;letter-spacing:.14em;'
        f'text-transform:uppercase;color:{"var(--acc)" if x.get("hot") else "var(--ink46)"};">'
        f'{x["t"]}</span></div>' for x in lines)
    return _wrap("screen",
        f'<div class="pane" style="position:absolute;inset:0 0 76px 0;padding:0;'
        f'display:flex;flex-direction:column;overflow:hidden;">'
        f'<div style="flex:0 0 64px;background:rgba(255,255,255,.06);display:flex;'
        f'align-items:center;gap:11px;padding:0 24px;">'
        f'<div style="width:12px;height:12px;border-radius:50%;background:var(--ink18);"></div>'
        f'<div style="width:12px;height:12px;border-radius:50%;background:var(--ink18);"></div>'
        f'<div style="flex:1;height:36px;border-radius:18px;background:rgba(0,0,0,.34);'
        f'display:flex;align-items:center;padding:0 18px;margin-left:10px;'
        f'font-family:\'DM Mono\',monospace;font-size:20px;color:var(--ink46);">{url}</div></div>'
        f'<div style="flex:1;min-height:0;padding:20px 28px;display:flex;flex-direction:column;">'
        f'<div style="flex:0 0 auto;font-size:33px;font-weight:900;margin-bottom:8px;">{title}</div>'
        f'<div style="flex:1;min-height:0;display:flex;flex-direction:column;">{r}</div>'
        f'</div></div>'
        f'<div style="position:absolute;bottom:0;left:0;width:{STAGE_W}px;height:60px;'
        f'display:flex;align-items:center;font-family:\'DM Mono\',monospace;font-size:23px;'
        f'letter-spacing:.18em;text-transform:uppercase;color:var(--ink46);">{foot}</div>')


def scene_versus(left, right):
    """Two panes, the second lit. The comparison is the picture."""
    def col(d, win):
        return (f'<div class="pane{" hot" if win else " dim"}" style="position:absolute;top:0;'
                f'{"right:0" if win else "left:0"};width:{(STAGE_W-20)//2}px;'
                f'height:{STAGE_H}px;padding:32px 28px;display:flex;flex-direction:column;'
                f'overflow:hidden;">'
                f'<div style="font-family:\'DM Mono\',monospace;font-size:21px;'
                f'letter-spacing:.18em;text-transform:uppercase;'
                f'{"color:rgba(255,255,255,.84)" if win else "color:var(--ink46)"};">{d["u"]}</div>'
                f'<div style="font-family:\'Anton\',sans-serif;font-size:100px;line-height:.96;'
                f'margin-top:12px;{"color:#fff" if win else "color:var(--ink)"};">{d["b"]}</div>'
                f'<div style="margin-top:auto;font-size:27px;font-weight:700;line-height:1.2;'
                f'{"color:rgba(255,255,255,.9)" if win else "color:var(--ink46)"};">{d["i"]}</div>'
                f'</div>')
    return _wrap("versus", col(left, False) + col(right, True))


def scene_quote(big, sub, foot):
    """One pane, one number, nothing else. The frame breathes with the photograph."""
    return _wrap("quote",
        f'<div class="pane" style="position:absolute;inset:0 0 76px 0;padding:44px 40px;'
        f'display:flex;flex-direction:column;justify-content:center;overflow:hidden;">'
        f'<div style="font-family:\'Anton\',sans-serif;font-size:190px;line-height:.86;'
        f'color:var(--acc);">{big}</div>'
        f'<div style="font-size:40px;font-weight:800;line-height:1.16;margin-top:18px;">'
        f'{sub}</div></div>'
        f'<div style="position:absolute;bottom:0;left:0;width:{STAGE_W}px;height:60px;'
        f'display:flex;align-items:center;font-family:\'DM Mono\',monospace;font-size:23px;'
        f'letter-spacing:.18em;text-transform:uppercase;color:var(--ink46);">{foot}</div>')


def scene_chat(msgs, foot):
    """The one line you type, and what comes back."""
    n = len(msgs)
    gap = 14
    h = (STAGE_H - 76 - gap * (n - 1)) // n
    out = []
    for k, m in enumerate(msgs):
        you = m.get("you")
        out.append(
            f'<div class="pane{" hot" if you else ""}" style="position:absolute;'
            f'top:{k*(h+gap)}px;{"right:0" if you else "left:0"};width:{int(STAGE_W*0.84)}px;'
            f'height:{h}px;padding:0 30px;display:flex;align-items:center;overflow:hidden;'
            f'font-size:33px;font-weight:{"800" if you else "700"};line-height:1.16;">'
            f'{m["t"]}</div>')
    out.append(f'<div style="position:absolute;bottom:0;left:0;width:{STAGE_W}px;height:60px;'
               f'display:flex;align-items:center;font-family:\'DM Mono\',monospace;'
               f'font-size:23px;letter-spacing:.18em;text-transform:uppercase;'
               f'color:var(--ink46);">{foot}</div>')
    return _wrap("chat", "".join(out))


def scene_ask(word, sub, meta):
    """The ask, on a lit pane over the photograph."""
    size = int(min(190, (STAGE_W - 120) / max(1, len(word)) / 0.52))
    return _wrap("ask",
        f'<div class="pane hot" style="position:absolute;inset:0 0 74px 0;padding:40px;'
        f'display:flex;flex-direction:column;align-items:flex-start;justify-content:center;'
        f'overflow:hidden;">'
        f'<div style="font-family:\'Anton\',sans-serif;font-size:74px;letter-spacing:.10em;'
        f'color:rgba(255,255,255,.94);line-height:1;">COMMENT</div>'
        f'<div style="font-family:\'Anton\',sans-serif;font-size:{size}px;line-height:.9;'
        f'color:#fff;text-shadow:0 5px 0 rgba(120,38,14,.42);margin-top:6px;">{word}</div>'
        f'<div style="font-size:30px;font-weight:700;color:rgba(255,255,255,.94);'
        f'line-height:1.24;margin-top:16px;">{sub}</div></div>'
        f'<div style="position:absolute;bottom:0;left:0;width:{STAGE_W}px;height:58px;'
        f'display:flex;align-items:center;justify-content:space-between;'
        f'font-family:\'DM Mono\',monospace;font-size:23px;letter-spacing:.18em;'
        f'text-transform:uppercase;color:var(--ink46);">'
        f'<span>{meta}</span><span style="color:var(--acc);">51ULTRON.COM</span></div>')


# ------------------------------------------------------------------ page

def slide(s, uri, ground):
    cap = (f'<div class="cap"><i>{s["cap"][0]}</i><span>{s["cap"][1]}</span></div>'
           if s.get("cap") else '<div class="cap"></div>')
    return (f'<div class="slide">'
            f'<div class="bgwrap"><div class="bg" style="background-image:url({ground})">'
            f'</div></div>'
            f'<div class="grade"></div><div class="grain"></div>'
            f'<div class="safe"><div class="hd">'
            f'<div class="eyebrow">{s["eyebrow"]}</div>'
            f'<div class="h">{s["h"]}</div><div class="sub">{s["sub"]}</div></div>'
            f'<div class="stage">{s["scene"]}</div>{cap}'
            f'<div class="foot"><img src="{uri}" alt="">'
            f'<span>ULTRON <em>&middot;</em> 51ULTRON<em>.</em>COM</span></div>'
            f'</div></div>')


def build(slug, title, slides):
    import _clay
    uri = _clay.logo_uri()
    ground = ground_uri()
    out = ['<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">',
           f'<title>ULTRON CINE - {title}</title>',
           f'<style>{_clay.fonts_css()}{css()}</style></head><body>']
    out += [slide(s, uri, ground) for s in slides]
    out.append("</body></html>")
    p = CONTENT / f"{slug}.html"
    p.write_text("".join(out))
    return p
