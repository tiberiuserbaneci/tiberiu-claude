#!/usr/bin/env python3
"""ULTRON 2.5D: the object system rebuilt around a declared workspace.

Operator, 2026-08-05, rejecting the flat clay objects: "elementele 2.5D desenate pe slide uri
sunt in continuare slabe, repetitive, ffffff mici in comparatie cu layoutul slide ului".

The measurement behind that: across three decks the object filled a median 75% of its stage
width and 50% of its HEIGHT, and the worst was the timeline on 05-posts slide 5, a 720x105
strip floating in an 880x701 box. Fifteen percent of its own workspace. The slide was mostly
air and the eye had nothing to land on.

Three things change here.

1. THE WORKSPACE IS DECLARED AND FIXED. Not "whatever is left after the copy". STAGE is a
   constant, the header gets a fixed budget above it, and an object is built to fill the
   stage rather than sized to its own taste and centred in whatever remains. `fill_report()`
   measures it and the deck build fails below the floor.

2. DEPTH IS REAL, NOT A SOFT SHADOW. A clay blur reads as a sticker; these are solids. Every
   face is extruded by stacking single-pixel shadows into a side wall (`extrude`), sits on a
   contact shadow, and carries a lit top edge. The scene tilts on a shallow rotateX so the
   solidity is visible while the type stays upright: heavy isometric rotation looks like
   design and destroys legibility, and the operator's test is "trebuie sa ma convinga dintr o
   privire", which is a legibility test before it is a style one.

3. EVERY COMPOSITION IS A SCENE, NOT A WIDGET. A scene has a ground, a dominant mass, and
   labelled parts carrying real words. That is what fills 880x680 honestly; a small widget
   scaled up just gets blurry and stays thin.
"""
import pathlib, re

CONTENT = pathlib.Path(__file__).resolve().parent

# ---------------------------------------------------------------- the workspace
CANVAS_W, CANVAS_H = 1080, 1920
SAFE_T, SAFE_R, SAFE_B, SAFE_L = 300, 130, 330, 70          # CLAUDE.md 9, binding
COL_W = CANVAS_W - SAFE_L - SAFE_R                          # 880
BAND_H = CANVAS_H - SAFE_T - SAFE_B                         # 1290

HEADER_H = 430          # eyebrow + hook + subhook, fixed budget
GAP = 22
STAGE_W, STAGE_H = COL_W, 745                               # THE WORKSPACE
CAP_H = 74              # one action line under the scene
FOOT_H = 58
# the header takes whatever the fixed stage, caption and footer leave, and its type
# auto-fits into it at render time rather than clipping a sentence
HEADER_H = BAND_H - (GAP + STAGE_H + GAP + CAP_H + GAP + FOOT_H)   # 412

FILL_W, FILL_H = 0.92, 0.86     # an object must cover this much of the stage


def extrude(depth: int, color: str, dx: int = 1, dy: int = 1) -> str:
    """A solid side wall, built from `depth` stacked hairline shadows.

    One blurred shadow is a sticker. `depth` offset copies with zero blur is a body with a
    real thickness, which is what separates 2.5D from a drop shadow.
    """
    return ", ".join(f"{i*dx}px {i*dy}px 0 {color}" for i in range(1, depth + 1))


CSS = f"""
:root{{
  --base:#F4F1EC; --deep:#E2DCD0; --sink:#EAE4D9;
  --ink:#2D2A26; --muted:#8A857D; --faint:#B8B2A8;
  --acc:#D26446; --accd:#A93A20; --accl:#E4805F;
  --side:#D5CEC1; --sidedk:#C2B9AA;
  --lit:rgba(255,255,255,.92);
}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:#0b0b0b;}}
.slide{{
  width:{CANVAS_W}px;height:{CANVAS_H}px;position:relative;overflow:hidden;
  background:var(--base);font-family:'Plus Jakarta Sans',sans-serif;
}}
.amb{{position:absolute;inset:0;pointer-events:none;
  background:
    radial-gradient(ellipse 70% 40% at 50% 0%,rgba(255,255,255,.85) 0%,transparent 62%),
    radial-gradient(ellipse 60% 34% at 82% 100%,rgba(210,100,70,.07) 0%,transparent 66%);}}
.safe{{position:absolute;top:{SAFE_T}px;left:{SAFE_L}px;
  width:{COL_W}px;height:{BAND_H}px;display:flex;flex-direction:column;}}

/* ---- header: fixed budget, so the stage never gets eaten ---- */
.hd{{height:{HEADER_H}px;flex:0 0 {HEADER_H}px;display:flex;flex-direction:column;
  justify-content:flex-start;overflow:hidden;}}
.eyebrow{{font-family:'DM Mono',monospace;font-size:25px;font-weight:500;letter-spacing:.30em;
  text-transform:uppercase;color:var(--acc);margin-bottom:16px;}}
.h{{font-family:'Anton',sans-serif;font-size:104px;line-height:.92;letter-spacing:-.015em;
  text-transform:uppercase;color:var(--ink);}}
.h em{{font-style:normal;color:var(--acc);}}
.sub{{font-size:34px;line-height:1.32;font-weight:600;color:var(--muted);margin-top:20px;
  max-width:820px;}}
.sub b{{color:var(--ink);font-weight:800;}}

/* ---- the workspace ---- */
.stage{{height:{STAGE_H}px;flex:0 0 {STAGE_H}px;margin-top:{GAP}px;
  position:relative;perspective:1700px;perspective-origin:50% 42%;}}
.scene{{position:absolute;inset:0;transform-style:preserve-3d;}}

/* ---- caption strip: the action line under the scene ---- */
.cap{{height:{CAP_H}px;flex:0 0 {CAP_H}px;margin-top:{GAP}px;display:flex;align-items:center;
  gap:18px;}}
.cap i{{font-style:normal;flex:0 0 auto;background:var(--acc);color:#fff;font-size:21px;
  font-weight:800;letter-spacing:.14em;text-transform:uppercase;padding:12px 20px;
  border-radius:9px;box-shadow:{extrude(6,'var(--accd)')}, 8px 14px 24px rgba(169,58,32,.30);}}
.cap span{{font-size:30px;font-weight:700;color:var(--ink);line-height:1.22;}}

.foot{{height:{FOOT_H}px;flex:0 0 {FOOT_H}px;margin-top:{GAP}px;display:flex;align-items:center;
  gap:14px;}}
.foot img{{width:38px;height:38px;border-radius:50%;}}
.foot span{{font-family:'DM Mono',monospace;font-size:22px;letter-spacing:.20em;
  color:var(--faint);text-transform:uppercase;}}
.foot em{{font-style:normal;color:var(--acc);}}

/* ================= 2.5D primitives ================= */

/* a solid slab: extruded body, lit top edge, contact shadow on the ground */
.slab{{position:relative;border-radius:20px;background:var(--base);
  box-shadow:{extrude(22,'var(--side)')}, 26px 34px 46px rgba(45,42,38,.20),
             inset 0 2px 0 var(--lit);}}
.slab.acc{{background:linear-gradient(168deg,var(--accl),var(--acc) 62%);color:#fff;
  box-shadow:{extrude(22,'var(--accd)')}, 26px 34px 46px rgba(169,58,32,.34),
             inset 0 2px 0 rgba(255,255,255,.44);}}
.slab.sink{{background:var(--sink);
  box-shadow:inset 5px 6px 12px rgba(45,42,38,.16), inset -3px -3px 8px var(--lit);}}

/* the ground the scene stands on */
.ground{{position:absolute;left:0;right:0;bottom:0;height:170px;border-radius:26px;
  background:linear-gradient(180deg,rgba(226,220,208,0),rgba(226,220,208,.72));
  transform:rotateX(58deg) translateZ(-40px);transform-origin:50% 100%;}}
"""


# ------------------------------------------------------------------ scenes

def scene_tower(rows, foot_l, foot_r):
    """A stack of extruded slabs seen slightly from above. Dominant mass, labelled parts.

    Fills the workspace because the stack IS the workspace: the rows divide the full 680px
    rather than sitting inside a smaller card.
    """
    n = len(rows)
    gap = 16
    h = (STAGE_H - 118 - gap * (n - 1)) // n
    out = []
    for k, r in enumerate(rows):
        top = k * (h + gap)
        acc = " acc" if r.get("acc") else ""
        z = 40 - k * 14
        out.append(
            f'<div class="slab{acc}" style="position:absolute;top:{top}px;left:0;'
            f'width:{STAGE_W - 46}px;height:{h}px;transform:translateZ({z}px);'
            f'display:flex;align-items:center;gap:28px;padding:0 34px;">'
            f'<div style="font-family:\'Anton\',sans-serif;font-size:{int(h*.66)}px;'
            f'line-height:1;{"color:#fff" if acc else "color:var(--acc)"};'
            f'min-width:140px;">{r["n"]}</div>'
            f'<div style="min-width:0;"><div style="font-size:38px;font-weight:800;'
            f'line-height:1.06;{"color:#fff" if acc else "color:var(--ink)"};">{r["b"]}</div>'
            f'<div style="font-size:26px;font-weight:600;margin-top:7px;'
            f'{"color:rgba(255,255,255,.86)" if acc else "color:var(--muted)"};">{r["i"]}</div>'
            f'</div></div>')
    out.append(
        f'<div class="slab sink" style="position:absolute;bottom:0;left:0;'
        f'width:{STAGE_W - 46}px;height:96px;display:flex;align-items:center;'
        f'justify-content:space-between;padding:0 34px;">'
        f'<span style="font-family:\'DM Mono\',monospace;font-size:24px;letter-spacing:.20em;'
        f'text-transform:uppercase;color:var(--muted);">{foot_l}</span>'
        f'<span style="font-family:\'Anton\',sans-serif;font-size:46px;color:var(--acc);">'
        f'{foot_r}</span></div>')
    return f'<div class="scene" data-ob="tower"><div class="ground"></div>{"".join(out)}</div>'


def scene_desk(panel_title, chip, rows, note):
    """A tilted product panel: the thing itself, big enough to read across a room."""
    r = "".join(
        f'<div style="display:flex;align-items:center;gap:22px;padding:22px 30px;'
        f'border-radius:16px;margin-bottom:14px;'
        + ("background:linear-gradient(168deg,var(--accl),var(--acc) 60%);color:#fff;"
           f"box-shadow:{extrude(9,'var(--accd)')}, 12px 16px 26px rgba(169,58,32,.28);"
           if x.get("acc") else
           f"background:var(--base);box-shadow:{extrude(9,'var(--side)')}, "
           "12px 16px 26px rgba(45,42,38,.14);")
        + f'">'
        f'<div style="width:54px;height:54px;border-radius:14px;flex:0 0 54px;'
        + ("background:rgba(255,255,255,.28);" if x.get("acc") else "background:var(--sink);")
        + f'display:flex;align-items:center;justify-content:center;font-size:26px;'
        f'font-weight:900;{"color:#fff" if x.get("acc") else "color:var(--acc)"};">'
        f'{k+1}</div>'
        f'<div style="flex:1;min-width:0;"><div style="font-size:33px;font-weight:800;'
        f'line-height:1.1;">{x["b"]}</div>'
        f'<div style="font-size:24px;font-weight:600;margin-top:5px;'
        + ("color:rgba(255,255,255,.84);" if x.get("acc") else "color:var(--muted);")
        + f'">{x["i"]}</div></div>'
        f'<div style="font-family:\'DM Mono\',monospace;font-size:21px;letter-spacing:.14em;'
        f'text-transform:uppercase;'
        + ("color:rgba(255,255,255,.9);" if x.get("acc") else "color:var(--faint);")
        + f'">{x["t"]}</div></div>'
        for k, x in enumerate(rows))
    return (f'<div class="scene" data-ob="desk"><div class="ground"></div>'
            f'<div class="slab" style="position:absolute;top:0;left:0;'
            f'width:{STAGE_W - 46}px;height:{STAGE_H - 46}px;padding:30px;'
            f'transform:rotateX(5deg) translateZ(30px);display:flex;flex-direction:column;">'
            f'<div style="display:flex;align-items:center;justify-content:space-between;'
            f'padding-bottom:22px;margin-bottom:22px;border-bottom:3px solid var(--sink);">'
            f'<span style="font-size:31px;font-weight:900;color:var(--ink);'
            f'letter-spacing:-.01em;">{panel_title}</span>'
            f'<span style="font-family:\'DM Mono\',monospace;font-size:21px;letter-spacing:.16em;'
            f'text-transform:uppercase;color:#fff;background:var(--acc);padding:9px 16px;'
            f'border-radius:8px;box-shadow:{extrude(5,"var(--accd)")};">{chip}</span></div>'
            f'<div style="flex:1;min-height:0;">{r}</div>'
            f'<div style="font-family:\'DM Mono\',monospace;font-size:22px;'
            f'letter-spacing:.10em;color:var(--faint);text-transform:uppercase;">{note}</div>'
            f'</div></div>')


def scene_key(word, sub, meta):
    """The ask, as a keycap you could physically press. COMMENT is the biggest thing here."""
    return (f'<div class="scene" data-ob="key"><div class="ground"></div>'
            f'<div class="slab acc" style="position:absolute;top:14px;left:0;'
            f'width:{STAGE_W - 46}px;height:{STAGE_H - 150}px;border-radius:34px;'
            f'transform:rotateX(7deg) translateZ(40px);display:flex;flex-direction:column;'
            f'align-items:center;justify-content:center;gap:10px;">'
            f'<div style="font-family:\'Anton\',sans-serif;font-size:76px;letter-spacing:.13em;'
            f'color:rgba(255,255,255,.94);text-transform:uppercase;line-height:1;'
            f'text-shadow:0 4px 0 rgba(122,38,18,.36);">COMMENT</div>'
            f'<div style="font-family:\'Anton\',sans-serif;font-size:196px;line-height:.88;'
            f'color:#fff;letter-spacing:.01em;text-shadow:0 5px 0 rgba(122,38,18,.45);">'
            f'{word}</div>'
            f'<div style="font-size:31px;font-weight:700;color:rgba(255,255,255,.92);'
            f'text-align:center;max-width:700px;line-height:1.28;">{sub}</div></div>'
            f'<div class="slab sink" style="position:absolute;bottom:0;left:0;'
            f'width:{STAGE_W - 46}px;height:100px;display:flex;align-items:center;'
            f'justify-content:space-between;padding:0 34px;">'
            f'<span style="font-family:\'DM Mono\',monospace;font-size:23px;letter-spacing:.18em;'
            f'text-transform:uppercase;color:var(--muted);">{meta}</span>'
            f'<span style="font-family:\'DM Mono\',monospace;font-size:23px;letter-spacing:.18em;'
            f'text-transform:uppercase;color:var(--acc);">51ULTRON<em '
            f'style="font-style:normal;">.</em>COM</span></div></div>')


# ------------------------------------------------------------------ page

def slide(s, uri):
    cap = (f'<div class="cap"><i>{s["cap"][0]}</i><span>{s["cap"][1]}</span></div>'
           if s.get("cap") else f'<div class="cap"></div>')
    return (f'<div class="slide"><div class="amb"></div><div class="safe">'
            f'<div class="hd"><div class="eyebrow">{s["eyebrow"]}</div>'
            f'<div class="h">{s["h"]}</div><div class="sub">{s["sub"]}</div></div>'
            f'<div class="stage">{s["scene"]}</div>{cap}'
            f'<div class="foot"><img src="{uri}" alt="">'
            f'<span>ULTRON <em>&middot;</em> 51ULTRON<em>.</em>COM</span></div>'
            f'</div></div>')


def build(slug, title, slides):
    import _clay
    uri = _clay.logo_uri()
    out = ['<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">',
           f'<title>ULTRON 2.5D - {title}</title>',
           f'<style>{_clay.fonts_css()}{CSS}</style></head><body>']
    out += [slide(s, uri) for s in slides]
    out.append("</body></html>")
    p = CONTENT / f"{slug}.html"
    p.write_text("".join(out))
    return p
