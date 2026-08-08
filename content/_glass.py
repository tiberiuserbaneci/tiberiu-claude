#!/usr/bin/env python3
"""Glassmorphism deck, black and white themes. A different carousel shape entirely.

WHY THIS EXISTS. The clay decks and the 3D films put ONE beautiful object on a slide with six
words next to it. Measured against what actually travels in this exact lane, that is the wrong
bet. Pulled off Instagram the day this was written:

    11.0M  "What happens when you let AI manage your production infrastructure?
            One developer found out the hard way."      dark, text-heavy, bullets
     6.6M  "Comment 'Tools' and I'll send you my full list"   text-dense carousel by category
     4.2M  "ChatGPT Secret Codes"                             text overlay
     2.5M  "Comment CODES and I'll send 7. Most people use Claude like a basic
            search engine."                             dark, bold type, numbered list
     2.3M  "5 tricks to stop hitting Claude's usage limits"   dense text, sections

Not one of them is an object with a caption. In every one of them THE TEXT IS THE VISUAL:
a countable promise, a wrong belief named out loud, and enough real content per slide that
saving it is worth doing. So this format makes typography the hero and uses glass only as the
surface the type sits on.

THE GLASS. The mistake that makes glassmorphism look like grey plastic is putting it over a
flat ground: `backdrop-filter: blur()` needs something WORTH blurring. So every deck paints a
colour field behind the panels first - two or three wide chroma blooms - and the panel then
samples it. The rest is the physics of a real edge: a bright 1px top-left rim where the light
catches the bevel, a darker bottom-right, an inner sheen, and a soft drop shadow with the
panel's own tint in it rather than neutral black.

THEMES. `black` and `white` are the same geometry with the tokens swapped, not two designs.
Every colour is a variable, so a deck renders both ways from one source.
"""
import base64, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent

W, H = 1080, 1350                       # the operator's editorial 4:5, CLAUDE.md 9
PAD = 76                                # side padding for photo-mode 4:5 (no 300px inset)

THEMES = {
    "black": {
        "bg":      "#08080A",
        "bloom1":  "rgba(204,120,92,.30)",     # Book Cloth, the brand accent
        "bloom2":  "rgba(120,140,200,.16)",    # a cool counter so the blur has CHROMA
        "bloom3":  "rgba(212,162,127,.14)",
        "glass":   "rgba(255,255,255,.055)",
        "glass2":  "rgba(255,255,255,.030)",
        "rim":     "rgba(255,255,255,.30)",    # the lit edge
        "rim2":    "rgba(255,255,255,.055)",   # the shaded edge
        "sheen":   "rgba(255,255,255,.10)",
        "ink":     "#FFFFFF",
        "ink70":   "rgba(255,255,255,.72)",
        "ink45":   "rgba(255,255,255,.46)",
        "acc":     "#E08B68",
        "shadow":  "rgba(0,0,0,.55)",
    },
    "white": {
        "bg":      "#F4F3F1",
        "bloom1":  "rgba(204,120,92,.34)",
        "bloom2":  "rgba(120,140,200,.20)",
        "bloom3":  "rgba(212,162,127,.22)",
        "glass":   "rgba(255,255,255,.52)",
        "glass2":  "rgba(255,255,255,.34)",
        "rim":     "rgba(255,255,255,.92)",
        "rim2":    "rgba(15,15,20,.07)",
        "sheen":   "rgba(255,255,255,.55)",
        "ink":     "#0E0E12",
        "ink70":   "rgba(14,14,18,.72)",
        "ink45":   "rgba(14,14,18,.48)",
        "acc":     "#B4522E",
        "shadow":  "rgba(60,40,30,.16)",
    },
}


def logo_b64() -> str:
    return base64.b64encode((REPO / "content" / "ultron-logo.png").read_bytes()).decode()


def css(theme: str) -> str:
    """Tokens plus the whole glass system. Geometry is identical across themes."""
    t = THEMES[theme]
    v = "\n  ".join(f"--{k}:{val};" for k, val in t.items())
    return f""":root{{
  {v}
  --r:34px;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#000;display:flex;flex-direction:column;align-items:center;gap:26px;
  font-family:'Plus Jakarta Sans',sans-serif;-webkit-font-smoothing:antialiased}}
.slide{{width:{W}px;height:{H}px;position:relative;overflow:hidden;
  background:var(--bg);color:var(--ink);isolation:isolate}}

/* THE COLOUR FIELD. Glass over a flat ground reads as grey plastic, because there is nothing
   in the backdrop for the blur to sample. These blooms are what the panels are made of. */
.field{{position:absolute;inset:-14%;z-index:0;filter:saturate(1.15)}}
.field i{{position:absolute;display:block;border-radius:50%;filter:blur(96px)}}
.f1{{width:74%;height:52%;left:-14%;top:-10%;background:var(--bloom1)}}
.f2{{width:62%;height:46%;right:-12%;top:26%;background:var(--bloom2)}}
.f3{{width:80%;height:50%;left:6%;bottom:-18%;background:var(--bloom3)}}
/* a fine grain over everything kills the banding a big blur always produces */
.grain{{position:absolute;inset:0;z-index:1;opacity:.30;pointer-events:none;
  background-image:url("data:image/svg+xml;utf8,\
<svg xmlns='http://www.w3.org/2000/svg' width='140' height='140'>\
<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.82' numOctaves='3'/>\
<feColorMatrix type='saturate' values='0'/></filter>\
<rect width='140' height='140' filter='url(%23n)' opacity='.5'/></svg>")}}

.safe{{position:absolute;inset:0;z-index:3;padding:{PAD}px;
  display:flex;flex-direction:column}}

/* THE PANEL. A real edge, not a flat rectangle: lit rim top-left, shaded rim bottom-right,
   an inner sheen where the surface curves, and a shadow carrying the panel's own tint. */
.g{{position:relative;border-radius:var(--r);background:var(--glass);
  backdrop-filter:blur(26px) saturate(1.5);-webkit-backdrop-filter:blur(26px) saturate(1.5);
  box-shadow:
    inset 1.4px 1.4px 0 var(--rim),
    inset -1.2px -1.2px 0 var(--rim2),
    inset 0 34px 54px -34px var(--sheen),
    0 26px 54px -22px var(--shadow);
  overflow:hidden}}
.g::after{{content:'';position:absolute;inset:0;border-radius:inherit;pointer-events:none;
  background:linear-gradient(157deg,var(--sheen) 0%,transparent 34%,transparent 74%,
    var(--rim2) 100%);opacity:.7}}
.g.flat{{background:var(--glass2)}}

.mono{{font-family:'DM Mono',monospace;font-weight:500;letter-spacing:.22em;
  text-transform:uppercase}}
.disp{{font-family:'Anton',sans-serif;text-transform:uppercase;letter-spacing:-1.4px;
  line-height:.92}}

.mast{{flex-shrink:0;display:flex;justify-content:space-between;align-items:center;
  font-size:20px;color:var(--ink45)}}
.mast em{{color:var(--acc);font-style:normal}}

.foot{{flex-shrink:0;margin-top:auto;display:flex;align-items:center;gap:12px;padding-top:22px}}
.foot img{{width:30px;height:30px;border-radius:50%;object-fit:cover;opacity:.92}}
.foot span{{font-family:'DM Mono',monospace;font-weight:500;font-size:19px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--ink45)}}
.foot span em{{color:var(--acc);font-style:normal}}
"""


def shell(theme: str, fonts: str, slides_html: str, title: str = "deck") -> str:
    return (f"<meta charset='UTF-8'><title>{title}</title>\n<style>\n{fonts}\n{css(theme)}\n"
            f"</style>\n{slides_html}\n")


if __name__ == "__main__":
    print(__doc__)
    print(f"canvas {W}x{H}   themes: {', '.join(THEMES)}")
