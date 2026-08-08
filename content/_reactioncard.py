#!/usr/bin/env python3
"""The reaction opener: the text that goes over the operator's own face, as a real asset.

WHY THIS EXISTS. The reaction was being written into the deck spec and then nowhere - it
lived in a Python dict and never became something the operator could look at or drop into
Edits. A line nobody can see is not a deliverable.

TWO DIFFERENT THINGS, and the first pass conflated them:

  on-screen   what the viewer READS in the first second. Eight words at most. It has to
              land while he is still inhaling, so it is a fragment, not a sentence.
  spoken      what he SAYS over it. Longer, because the ear takes more than the eye, and
              it carries the turn that the on-screen line only promises.

The operator's own examples are all short on screen: "Office end at 5 pm. Me at 11 pm",
"Stop paying for AI", "Stop spending 6 months building a startup". None of them is a
paragraph. Writing a 20 word overlay is how you lose the second you were trying to buy.

WHAT IT PRODUCES. A 1080x1920 overlay with a transparent ground, so it drops straight onto
his footage, plus a preview against a neutral plate so the treatment can be judged before he
films anything. Type sits inside the reel safe band and carries its own legibility: a graded
scrim behind the words rather than a solid card, because a solid card over a face is the
same mistake as an opaque scrim over a hook.
"""
import importlib.util, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
W, H = 1080, 1920
SAFE_T, SAFE_R, SAFE_B, SAFE_L = 300, 130, 330, 70


def _load(n):
    s = importlib.util.spec_from_file_location(n, REPO / "content" / f"{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


GL = _load("_glass")

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#101014;display:flex;flex-direction:column;align-items:center;gap:28px;
  font-family:'Plus Jakarta Sans',sans-serif;-webkit-font-smoothing:antialiased}
.card{width:1080px;height:1920px;position:relative;overflow:hidden}
/* the preview plate stands in for his footage, so the treatment can be judged before filming */
.card.preview{background:
  radial-gradient(ellipse 52% 34% at 50% 34%,#5a5148 0%,#2b2724 62%,#141312 100%)}
.card.preview::after{content:'FOOTAGE';position:absolute;top:44%;left:0;right:0;
  text-align:center;font-family:'DM Mono',monospace;font-size:26px;letter-spacing:.5em;
  color:rgba(255,255,255,.13)}
/* omit_background only removes the DEFAULT white page background. An explicitly declared
   body colour still paints, which silently flattened every overlay to RGB - they were
   shipped as "transparent" and were not. The alpha page therefore has no background at all,
   on the body OR the card. */
.card.alpha{background:transparent}
body:has(.card.alpha){background:transparent}

/* A graded scrim, never a solid card. The words have to be readable over any frame without
   putting a black box on his face - the same rule the films learned the hard way. */
.scrim{position:absolute;left:0;right:0;bottom:0;height:56%;z-index:1;
  background:linear-gradient(to top,rgba(6,6,8,.86) 0%,rgba(6,6,8,.62) 34%,
    rgba(6,6,8,.22) 68%,transparent 100%)}

.wrap{position:absolute;inset:0;z-index:2;
  padding:300px 130px 330px 70px;display:flex;flex-direction:column;justify-content:flex-end}
.kick{font-family:'DM Mono',monospace;font-size:22px;font-weight:500;letter-spacing:.26em;
  text-transform:uppercase;color:#E08B68;margin-bottom:22px}
.line{font-family:'Anton',sans-serif;font-size:104px;line-height:.96;letter-spacing:-1.4px;
  text-transform:uppercase;color:#fff;text-shadow:0 6px 40px rgba(0,0,0,.55)}
.line em{color:#E08B68;font-style:normal}
.say{margin-top:30px;padding-top:24px;border-top:1px solid rgba(255,255,255,.18);
  font-size:31px;font-weight:600;line-height:1.36;color:rgba(255,255,255,.80)}
.say b{color:#fff;font-weight:800}
.tagline{position:absolute;left:70px;right:130px;top:300px;z-index:2;
  font-family:'DM Mono',monospace;font-size:20px;letter-spacing:.22em;text-transform:uppercase;
  color:rgba(255,255,255,.42)}
"""


def card(spec: dict, mode: str) -> str:
    say = (f'<div class="say">{spec["reaction_say"]}</div>'
           if mode == "preview" and spec.get("reaction_say") else "")
    tag = (f'<div class="tagline">reaction opener &middot; {spec["id"]} '
           f'&middot; comment {spec["keyword"]}</div>' if mode == "preview" else "")
    return f"""<div class="card {mode}">
  <div class="scrim"></div>{tag}
  <div class="wrap">
    <div class="kick">{spec.get('reaction_kick', 'Founder, year one')}</div>
    <div class="line">{spec['reaction_text']}</div>
    {say}
  </div>
</div>"""


def page(specs, fonts: str, mode: str) -> str:
    body = "\n".join(card(s, mode) for s in specs)
    return f"<meta charset='UTF-8'><title>reactions</title>\n<style>\n{fonts}\n{CSS}\n</style>\n{body}"


if __name__ == "__main__":
    print(__doc__)
