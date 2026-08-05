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
STAGE_W, STAGE_H = COL_W, 640                               # THE WORKSPACE
CAP_H = 74              # one action line under the scene
FOOT_H = 58
# the header takes whatever the fixed stage, caption and footer leave, and its type
# auto-fits into it at render time rather than clipping a sentence
HEADER_H = BAND_H - (GAP + STAGE_H + GAP + CAP_H + GAP + FOOT_H)   # 452
# Operator, 2026-08-05, approving the model: "vreau titlul paginilor derulat si putin
# mai mare sa fie extrem de vizibil". The header was 347px, so a three line title was
# auto-shrunk to fit and its short lines floated at half the column. The stage gives
# back 105px and the renderer now sizes the title UP until the longest line reaches
# the full measure, so it runs out across the column instead of sitting in the middle.

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
  text-transform:uppercase;color:var(--acc);margin-bottom:12px;}}
.h{{font-family:'Anton',sans-serif;font-size:104px;line-height:.92;letter-spacing:-.015em;
  text-transform:uppercase;color:var(--ink);}}
.h em{{font-style:normal;color:var(--acc);}}
.sub{{font-size:32px;line-height:1.30;font-weight:600;color:var(--muted);margin-top:14px;
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
  box-shadow:{extrude(22,'var(--side)')}, 16px 20px 26px rgba(45,42,38,.20),
             inset 0 2px 0 var(--lit);}}
.slab.acc{{background:linear-gradient(168deg,var(--accl),var(--acc) 62%);color:#fff;
  box-shadow:{extrude(22,'var(--accd)')}, 16px 20px 26px rgba(169,58,32,.34),
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


# ---------------------------------------------------------------- scene library
# CLAUDE.md 30 wants the visual to change every three or four slides, no form twice inside a
# deck, and a different opener on every deck of a set. Eight decks of seven need a library
# wider than the seven, so these are fourteen distinct compositions. Each is a SCENE: a ground,
# a dominant mass and labelled parts carrying real words, built to the declared workspace
# rather than sized to itself and centred in the leftovers.

def _wrap(form, body):
    return f'<div class="scene" data-ob="{form}"><div class="ground"></div>{body}</div>'


def _W():
    # the extrusion runs 22px right, so the layout box stops just short of the column
    # edge and the solid side wall lands on it rather than past it
    return STAGE_W - 24


def scene_ladder(rows, cap):
    """Stepped slabs, each wider than the last. Progress you can see the shape of."""
    n = len(rows)
    h = (STAGE_H - 104 - 14 * (n - 1)) // n
    out = []
    for k, r in enumerate(rows):
        w = int(_W() * (0.58 + 0.42 * (k + 1) / n))
        acc = " acc" if r.get("acc") else ""
        out.append(
            f'<div class="slab{acc}" style="position:absolute;top:{k*(h+14)}px;left:0;'
            f'width:{w}px;height:{h}px;transform:translateZ({34-k*10}px);display:flex;'
            f'align-items:center;gap:24px;padding:0 30px;">'
            f'<div style="font-family:\'DM Mono\',monospace;font-size:23px;letter-spacing:.16em;'
            f'{"color:rgba(255,255,255,.82)" if acc else "color:var(--muted)"};'
            f'min-width:92px;">{r["k"]}</div>'
            f'<div style="flex:1;min-width:0;font-size:37px;font-weight:800;line-height:1.06;'
            f'{"color:#fff" if acc else "color:var(--ink)"};">{r["b"]}</div></div>')
    out.append(_foot(cap))
    return _wrap("ladder", "".join(out))


def _foot(cap, right=None):
    r = (f'<span style="font-family:\'Anton\',sans-serif;font-size:42px;color:var(--acc);">'
         f'{right}</span>') if right else ""
    return (f'<div class="slab sink" style="position:absolute;bottom:0;left:0;width:{_W()}px;'
            f'height:88px;display:flex;align-items:center;justify-content:space-between;'
            f'padding:0 32px;">'
            f'<span style="font-family:\'DM Mono\',monospace;font-size:23px;letter-spacing:.18em;'
            f'text-transform:uppercase;color:var(--muted);">{cap}</span>{r}</div>')


def scene_split(left, right):
    """Two solids side by side, the second one lit. The comparison IS the picture."""
    def col(d, win):
        return (f'<div class="slab{" acc" if win else ""}" style="position:absolute;top:0;'
                f'{"right:0" if win else "left:0"};width:{(_W()-20)//2}px;height:{STAGE_H-24}px;'
                f'padding:34px 30px;display:flex;flex-direction:column;'
                f'transform:translateZ({34 if win else 12}px);">'
                f'<div style="font-family:\'DM Mono\',monospace;font-size:22px;letter-spacing:.18em;'
                f'text-transform:uppercase;{"color:rgba(255,255,255,.82)" if win else "color:var(--muted)"};'
                f'">{d["u"]}</div>'
                f'<div style="font-family:\'Anton\',sans-serif;font-size:132px;line-height:.94;'
                f'margin-top:14px;{"color:#fff" if win else "color:var(--ink)"};">{d["b"]}</div>'
                f'<div style="margin-top:auto;font-size:29px;font-weight:700;line-height:1.2;'
                f'{"color:rgba(255,255,255,.9)" if win else "color:var(--muted)"};">{d["i"]}</div>'
                f'</div>')
    return _wrap("split", col(left, False) + col(right, True))


def scene_board(title, chips_, cap):
    """A pegboard of labelled tiles. Reads as a set at a glance."""
    n = len(chips_)
    cols = 2
    rows = (n + cols - 1) // cols
    gw = (_W() - 20) // cols
    gh = (STAGE_H - 150 - 20 * (rows - 1)) // rows
    out = [f'<div style="position:absolute;top:0;left:0;width:{_W()}px;height:52px;'
           f'font-family:\'DM Mono\',monospace;font-size:24px;letter-spacing:.20em;'
           f'text-transform:uppercase;color:var(--muted);">{title}</div>']
    for k, c in enumerate(chips_):
        x = (k % cols) * (gw + 20); y = 62 + (k // cols) * (gh + 20)
        acc = " acc" if c.get("acc") else ""
        out.append(
            f'<div class="slab{acc}" style="position:absolute;top:{y}px;left:{x}px;'
            f'width:{gw}px;height:{gh}px;padding:24px 26px;display:flex;flex-direction:column;'
            f'justify-content:center;transform:translateZ({26 if c.get("acc") else 10}px);">'
            f'<div style="font-size:35px;font-weight:800;line-height:1.08;'
            f'{"color:#fff" if acc else "color:var(--ink)"};">{c["b"]}</div>'
            f'<div style="font-size:24px;font-weight:600;margin-top:8px;'
            f'{"color:rgba(255,255,255,.86)" if acc else "color:var(--muted)"};">{c["i"]}</div>'
            f'</div>')
    out.append(_foot(cap))
    return _wrap("board", "".join(out))


def scene_bill(head, lines, total_l, total_r):
    """A single tall docket. One mass, dense with real rows."""
    rows = "".join(
        f'<div style="flex:1;min-height:0;display:flex;justify-content:space-between;'
        f'align-items:center;border-bottom:2px solid var(--sink);">'
        f'<span style="font-size:32px;font-weight:700;color:var(--ink);">{a}</span>'
        f'<span style="font-family:\'Anton\',sans-serif;font-size:44px;'
        f'color:{"var(--acc)" if str(b) not in ("0","none") else "var(--faint)"};">{b}</span>'
        f'</div>' for a, b in lines)
    return _wrap("bill",
        f'<div class="slab" style="position:absolute;inset:0 24px 0 0;padding:32px 34px;'
        f'display:flex;flex-direction:column;transform:rotateX(4deg) translateZ(28px);">'
        f'<div style="display:flex;justify-content:space-between;padding-bottom:18px;'
        f'border-bottom:3px solid var(--ink);font-family:\'DM Mono\',monospace;font-size:23px;'
        f'letter-spacing:.18em;text-transform:uppercase;color:var(--muted);">'
        f'<span>{head[0]}</span><span>{head[1]}</span></div>'
        f'<div style="flex:1;min-height:0;display:flex;flex-direction:column;">{rows}</div>'
        f'<div style="flex:0 0 auto;display:flex;justify-content:space-between;'
        f'align-items:baseline;padding-top:20px;">'
        f'<span style="font-family:\'DM Mono\',monospace;font-size:24px;letter-spacing:.18em;'
        f'text-transform:uppercase;color:var(--muted);">{total_l}</span>'
        f'<span style="font-family:\'Anton\',sans-serif;font-size:78px;line-height:1;'
        f'color:var(--acc);">{total_r}</span></div></div>')


def scene_clock(big, label, marks, cap):
    """A dial built as a solid ring with labelled stations around it."""
    d = min(STAGE_H - 150, _W() - 200)
    pos = [f"top:0;left:50%;margin-left:-{d//2}px", f"top:50%;right:0;margin-top:-46px",
           f"bottom:0;left:50%;margin-left:-{d//2}px", f"top:50%;left:0;margin-top:-46px"]
    sat = "".join(
        f'<div class="slab{" acc" if m.get("acc") else ""}" style="position:absolute;'
        f'{pos[k]};{"width:%dpx;" % d if k in (0,2) else "width:190px;"}padding:15px 18px;'
        f'text-align:center;font-size:26px;font-weight:800;'
        f'{"color:#fff" if m.get("acc") else "color:var(--ink)"};">{m["t"]}</div>'
        for k, m in enumerate(marks[:4]))
    return _wrap("clock",
        f'<div style="position:absolute;inset:0 24px 0 0;">'
        f'<div class="slab" style="position:absolute;top:50%;left:50%;width:{d}px;height:{d}px;'
        f'margin:-{d//2}px 0 0 -{d//2}px;border-radius:50%;display:flex;flex-direction:column;'
        f'align-items:center;justify-content:center;transform:translateZ(34px);">'
        f'<div style="font-family:\'Anton\',sans-serif;font-size:{int(d*0.40)}px;line-height:.9;'
        f'color:var(--acc);">{big}</div>'
        f'<div style="font-family:\'DM Mono\',monospace;font-size:23px;letter-spacing:.22em;'
        f'text-transform:uppercase;color:var(--muted);margin-top:10px;">{label}</div></div>'
        f'{sat}</div>' + _foot(cap))


def scene_thread(msgs, cap):
    """A conversation as stacked solids, alternating sides."""
    n = len(msgs)
    h = (STAGE_H - 104 - 16 * (n - 1)) // n
    out = []
    for k, m in enumerate(msgs):
        you = m.get("you")
        w = int(_W() * 0.80)
        out.append(
            f'<div class="slab{" acc" if you else ""}" style="position:absolute;'
            f'top:{k*(h+16)}px;{"right:0" if you else "left:0"};width:{w}px;height:{h}px;'
            f'padding:0 30px;display:flex;align-items:center;'
            f'transform:translateZ({30 if you else 12}px);'
            f'font-size:33px;font-weight:{"800" if you else "700"};line-height:1.16;'
            f'{"color:#fff" if you else "color:var(--ink)"};">{m["t"]}</div>')
    out.append(_foot(cap))
    return _wrap("thread", "".join(out))


def scene_meter(pct, big, label, notes, cap):
    """A filled track with the number riding it."""
    bars = "".join(
        f'<div style="margin-top:18px;"><div style="display:flex;justify-content:space-between;'
        f'font-size:27px;font-weight:700;color:var(--ink);margin-bottom:9px;">'
        f'<span>{x["b"]}</span><span style="color:var(--acc);font-weight:900;">{x["v"]}</span></div>'
        f'<div class="slab sink" style="height:34px;border-radius:17px;overflow:hidden;">'
        f'<div style="height:100%;width:{x["p"]}%;border-radius:17px;'
        f'background:linear-gradient(90deg,var(--accl),var(--acc));'
        f'box-shadow:{extrude(6,"var(--accd)")};"></div></div></div>' for x in notes)
    return _wrap("meter",
        f'<div style="position:absolute;inset:0 24px 100px 0;display:flex;flex-direction:column;">'
        f'<div class="slab acc" style="height:{int(STAGE_H*0.40)}px;display:flex;'
        f'flex-direction:column;align-items:center;justify-content:center;'
        f'transform:translateZ(36px);">'
        f'<div style="font-family:\'Anton\',sans-serif;font-size:150px;line-height:.9;'
        f'color:#fff;">{big}</div>'
        f'<div style="font-family:\'DM Mono\',monospace;font-size:23px;letter-spacing:.22em;'
        f'text-transform:uppercase;color:rgba(255,255,255,.86);margin-top:8px;">{label}</div></div>'
        f'{bars}</div>' + _foot(cap))


def scene_grid(cells, cap):
    """A dense field of small labelled solids: quantity made visible."""
    cols, rows = 3, 3
    gw = (_W() - 2 * 16) // cols
    gh = (STAGE_H - 150 - 2 * 16) // rows
    out = []
    for k, c in enumerate(cells[:9]):
        x = (k % cols) * (gw + 16); y = (k // cols) * (gh + 16)
        acc = " acc" if c.get("acc") else ""
        out.append(
            f'<div class="slab{acc}" style="position:absolute;top:{y}px;left:{x}px;'
            f'width:{gw}px;height:{gh}px;padding:18px;display:flex;flex-direction:column;'
            f'justify-content:center;transform:translateZ({24 if c.get("acc") else 8}px);">'
            f'<div style="font-family:\'Anton\',sans-serif;font-size:52px;line-height:1;'
            f'{"color:#fff" if acc else "color:var(--acc)"};">{c["n"]}</div>'
            f'<div style="font-size:22px;font-weight:700;margin-top:7px;line-height:1.14;'
            f'{"color:rgba(255,255,255,.9)" if acc else "color:var(--muted)"};">{c["t"]}</div>'
            f'</div>')
    out.append(_foot(cap))
    return _wrap("grid", "".join(out))


def scene_arch(steps, cap):
    """A left rail of numbered stations with a solid body beside each."""
    n = len(steps)
    h = (STAGE_H - 104 - 14 * (n - 1)) // n
    out = []
    for k, s in enumerate(steps):
        acc = " acc" if s.get("acc") else ""
        y = k * (h + 14)
        out.append(
            f'<div class="slab{acc}" style="position:absolute;top:{y}px;left:0;width:{h}px;'
            f'height:{h}px;display:flex;align-items:center;justify-content:center;'
            f'font-family:\'Anton\',sans-serif;font-size:{int(h*0.52)}px;'
            f'{"color:#fff" if acc else "color:var(--acc)"};transform:translateZ(30px);">'
            f'{k+1}</div>'
            f'<div class="slab" style="position:absolute;top:{y}px;left:{h+16}px;'
            f'width:{_W()-h-16}px;height:{h}px;padding:0 28px;display:flex;'
            f'flex-direction:column;justify-content:center;transform:translateZ(10px);">'
            f'<div style="font-size:35px;font-weight:800;line-height:1.06;color:var(--ink);">'
            f'{s["b"]}</div>'
            f'<div style="font-size:24px;font-weight:600;color:var(--muted);margin-top:6px;">'
            f'{s["i"]}</div></div>')
    out.append(_foot(cap))
    return _wrap("arch", "".join(out))


def scene_stack(cards, cap):
    """A fanned deck: every card shows its own strip, the last one opens fully.

    Nesting them concentrically hid all but the top card, so the 04-night opener read as one
    line of text with three empty frames behind it. A deck is only legible if each card keeps
    a strip of itself in view.
    """
    n = len(cards)
    room = STAGE_H - 104
    step = min(132, (room - 150) // max(1, n - 1))
    h = room - step * (n - 1)
    out = []
    for k, c in enumerate(cards):
        inset = k * 26
        acc = " acc" if c.get("acc") else ""
        out.append(
            f'<div class="slab{acc}" style="position:absolute;top:{k*step}px;left:{inset}px;'
            f'width:{_W()-inset}px;height:{h}px;padding:22px 30px;'
            f'transform:translateZ({10+k*12}px);display:flex;flex-direction:column;">'
            f'<div style="font-family:\'DM Mono\',monospace;font-size:22px;letter-spacing:.18em;'
            f'text-transform:uppercase;{"color:rgba(255,255,255,.82)" if acc else "color:var(--muted)"};'
            f'">{c["u"]}</div>'
            f'<div style="font-size:37px;font-weight:900;margin-top:8px;line-height:1.08;'
            f'{"color:#fff" if acc else "color:var(--ink)"};">{c["b"]}</div></div>')
    out.append(_foot(cap))
    return _wrap("stack", "".join(out))


def scene_gantt(bars, cap):
    """Time as solid bars on a track: a label gutter, then the bar, then its value.

    The label used to sit inside the bar, so a short bar wrapped its own text over three lines
    and pushed the value out past its right edge. A chart reads left to right: the name is
    always in the same place and the bar is free to be as short as the truth requires.
    """
    n = len(bars)
    h = (STAGE_H - 104 - 16 * (n - 1)) // n
    lab = 320
    track = _W() - lab - 20
    # the solid side wall runs 22px past the bar's box, so a value set right against the bar
    # lands on its own shadow. Clear the extrusion, then leave real air after it.
    clear = 46
    out = []
    for k, b in enumerate(bars):
        acc = " acc" if b.get("acc") else ""
        w = max(96, int((track - clear - 120) * b["p"] / 100))
        y = k * (h + 16)
        out.append(
            f'<div style="position:absolute;top:{y}px;left:0;width:{lab}px;height:{h}px;'
            f'display:flex;align-items:center;font-size:31px;font-weight:800;line-height:1.08;'
            f'color:var(--ink);padding-right:16px;">{b["b"]}</div>'
            f'<div style="position:absolute;top:{y}px;left:{lab+20}px;width:{track}px;'
            f'height:{h}px;display:flex;align-items:center;gap:{clear}px;">'
            f'<div class="slab{acc}" style="width:{w}px;height:{h-14}px;border-radius:14px;'
            f'transform:translateZ({26 if b.get("acc") else 8}px);"></div>'
            f'<span style="font-family:\'Anton\',sans-serif;font-size:46px;line-height:1;'
            f'{"color:var(--acc)" if b.get("acc") else "color:var(--muted)"};">{b["v"]}</span>'
            f'</div>')
    out.append(_foot(cap))
    return _wrap("gantt", "".join(out))


def scene_screen(url, title, rows, cap):
    """The product, as a tilted window with real rows in it."""
    r = "".join(
        f'<div style="display:flex;align-items:center;gap:20px;padding:14px 0;'
        f'border-bottom:2px solid var(--sink);">'
        f'<div style="width:12px;height:12px;border-radius:50%;flex:0 0 12px;'
        f'background:{"var(--acc)" if x.get("acc") else "var(--faint)"};"></div>'
        f'<span style="flex:1;font-size:31px;font-weight:700;color:var(--ink);">{x["b"]}</span>'
        f'<span style="font-family:\'DM Mono\',monospace;font-size:22px;letter-spacing:.14em;'
        f'text-transform:uppercase;color:{"var(--acc)" if x.get("acc") else "var(--faint)"};">'
        f'{x["t"]}</span></div>' for x in rows)
    return _wrap("screen",
        f'<div class="slab" style="position:absolute;inset:0 24px 100px 0;padding:0;'
        f'overflow:hidden;transform:rotateX(5deg) translateZ(30px);'
        f'display:flex;flex-direction:column;">'
        f'<div style="height:74px;flex:0 0 74px;background:var(--sink);display:flex;'
        f'align-items:center;gap:12px;padding:0 24px;">'
        f'<div style="width:13px;height:13px;border-radius:50%;background:var(--faint);"></div>'
        f'<div style="width:13px;height:13px;border-radius:50%;background:var(--faint);"></div>'
        f'<div style="flex:1;height:38px;border-radius:19px;background:var(--base);'
        f'display:flex;align-items:center;padding:0 18px;font-family:\'DM Mono\',monospace;'
        f'font-size:20px;color:var(--muted);margin-left:10px;">{url}</div></div>'
        f'<div style="flex:1;min-height:0;padding:22px 28px;display:flex;'
        f'flex-direction:column;overflow:hidden;">'
        f'<div style="flex:0 0 auto;font-size:34px;font-weight:900;color:var(--ink);'
        f'margin-bottom:8px;">{title}</div>'
        f'<div style="flex:1;min-height:0;overflow:hidden;">{r}</div>'
        f'</div></div>' + _foot(cap))


def scene_pillars(cols, cap):
    """Three standing solids of different height: a chart you can read at a glance."""
    n = len(cols)
    gw = (_W() - 24 * (n - 1)) // n
    out = []
    for k, c in enumerate(cols):
        acc = " acc" if c.get("acc") else ""
        hh = int((STAGE_H - 150) * c["p"] / 100)
        out.append(
            f'<div style="position:absolute;bottom:100px;left:{k*(gw+24)}px;width:{gw}px;">'
            f'<div style="font-family:\'Anton\',sans-serif;font-size:64px;line-height:1;'
            f'text-align:center;margin-bottom:12px;'
            f'{"color:var(--acc)" if c.get("acc") else "color:var(--ink)"};">{c["v"]}</div>'
            f'<div class="slab{acc}" style="height:{hh}px;border-radius:16px;'
            f'transform:translateZ({26 if c.get("acc") else 8}px);"></div>'
            f'<div style="font-family:\'DM Mono\',monospace;font-size:21px;letter-spacing:.12em;'
            f'text-transform:uppercase;color:var(--muted);text-align:center;margin-top:12px;">'
            f'{c["b"]}</div></div>')
    out.append(_foot(cap))
    return _wrap("pillars", "".join(out))


def _seal_size(word, d):
    """Anton runs about 0.52em per capital, so a nine letter keyword needs a smaller face
    than a three letter one to stay inside the seal instead of walking out of it."""
    return int(min(d * 0.30, (d - 110) / max(1, len(word)) / 0.52))


def scene_seal(word, sub, meta):
    """The ask as a pressed seal. Alternates with the keycap so eight decks do not all close
    on one identical object, which is the saturation CLAUDE.md 30 forbids."""
    d = min(STAGE_H - 130, _W() - 120)
    return _wrap("seal",
        f'<div class="slab acc" style="position:absolute;top:0;left:50%;margin-left:-{d//2}px;'
        f'width:{d}px;height:{d}px;border-radius:50%;display:flex;flex-direction:column;'
        f'align-items:center;justify-content:center;gap:6px;transform:translateZ(40px);">'
        f'<div style="font-family:\'Anton\',sans-serif;font-size:66px;letter-spacing:.12em;'
        f'color:rgba(255,255,255,.94);line-height:1;">COMMENT</div>'
        f'<div style="font-family:\'Anton\',sans-serif;font-size:{_seal_size(word, d)}px;'
        f'line-height:.9;color:#fff;text-shadow:0 5px 0 rgba(122,38,18,.42);">{word}</div>'
        f'<div style="font-size:27px;font-weight:700;color:rgba(255,255,255,.92);'
        f'text-align:center;max-width:{d-90}px;line-height:1.24;margin-top:6px;">{sub}</div>'
        f'</div>' + _foot(meta, "51ULTRON.COM"))
