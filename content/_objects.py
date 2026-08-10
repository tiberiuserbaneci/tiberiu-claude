#!/usr/bin/env python3
"""Glass objects: one per reel slide, carrying the meaning so the words do not have to.

WHY THIS EXISTS. Operator, after posting decks A and B: "e prea mult text si nu retine
audienta ... ne trebuie totusi si un element grafic sugestiv pe fiecare slide."

Measured before changing anything: the reel content slides carried a mean of 75 words each, on
a format the operator assembles at ONE SECOND per slide. A person scanning a screen takes in
somewhere around five to eight words in that second. Seventy five is not a slide, it is a page.

The cause is mine and it is structural rather than careless. I built LinkedIn carousels, where
the reader sets the pace and the density rule in CLAUDE.md 27.9 is exactly right, and then
shipped the identical content as reels, where the platform sets the pace. Density earns saves
on a carousel and destroys retention on a reel. The two formats needed different content, not
the same content at two sizes.

So the reel slide becomes HOOK + OBJECT + ONE LINE, about twenty words, and the object is
where the information actually lives. The dense list stays on the carousel, untouched.

TEN FORMS. Each takes a small payload and fills an 880 x 700 stage. They are deliberately
simple: a shape read in half a second beats a diagram read in three.

  figure   one enormous number, unit, caption
  bar      a proportion along a track, both ends labelled
  dots     a count as a field of cells, k lit
  stack    n blocks, k lit, for "how many of these were real"
  split    two masses sized by their values, side by side
  clock    a ring with a wedge, for a duration
  steps    a run of bars, for a shape over time
  arrow    one chip, a heavy arrow, another chip
  strike   the wrong line struck through above the right one
  window   minimal product chrome with a single line in it

VARIETY IS ENFORCED BY USE, NOT BY HOPE. CLAUDE.md 30 requires the object to change every
three or four slides and forbids two materials opening on the same form, so every deck
declares a seven form run and `check_run` refuses a repeat inside a deck.
"""

FORMS = ("figure", "bar", "dots", "stack", "split", "clock", "steps", "arrow",
         "strike", "window")


def check_run(deck_id: str, run: list[str]) -> None:
    """Refuse a run that repeats a form inside one deck, or names one that does not exist."""
    bad = [f for f in run if f not in FORMS]
    if bad:
        raise ValueError(f"{deck_id}: unknown object form(s) {bad}")
    if len(run) != 7:
        raise ValueError(f"{deck_id}: {len(run)} objects declared, needs 7")
    dupes = {f for f in run if run.count(f) > 1}
    if dupes:
        raise ValueError(f"{deck_id}: object form repeats inside the deck: {sorted(dupes)}")


# --------------------------------------------------------------------------- forms
def figure(o):
    """One enormous number. For a cost, a total, a count that speaks alone."""
    unit = f"<span class='ob-fig-u'>{o['unit']}</span>" if o.get("unit") else ""
    return (f"<div class='ob ob-figure' data-ob='figure'>"
            f"<div class='ob-fig-n disp'>{o['n']}{unit}</div>"
            f"<div class='ob-cap mono'>{o['cap']}</div></div>")


def bar(o):
    """A proportion along a track. `pct` is the fill, both ends carry a label."""
    return (f"<div class='ob ob-bar' data-ob='bar'>"
            f"<div class='ob-bar-top'><span class='ob-bar-v disp'>{o['n']}</span>"
            f"<span class='ob-bar-of mono'>{o['of']}</span></div>"
            f"<div class='ob-bar-t'><i style='width:{o['pct']}%'></i></div>"
            f"<div class='ob-cap mono'>{o['cap']}</div></div>")


def dots(o):
    """A count as a field. `n` cells, the first `lit` of them filled."""
    cells = "".join(f"<span class='ob-dot{' on' if i < o['lit'] else ''}'></span>"
                    for i in range(o["n"]))
    cols = o.get("cols", 10)
    return (f"<div class='ob ob-dots' data-ob='dots'>"
            f"<div class='ob-dot-f' style='grid-template-columns:repeat({cols},1fr)'>"
            f"{cells}</div><div class='ob-cap mono'>{o['cap']}</div></div>")


def stack(o):
    """n blocks in a column, the last `lit` of them filled. For how-many-were-real."""
    rows = "".join(f"<span class='ob-blk{' on' if i >= o['n'] - o['lit'] else ''}'></span>"
                   for i in range(o["n"]))
    return (f"<div class='ob ob-stack' data-ob='stack'>"
            f"<div class='ob-stk'>{rows}</div>"
            f"<div class='ob-stk-l'><span class='disp'>{o['lit']}</span>"
            f"<span class='mono'>of {o['n']}</span></div>"
            f"<div class='ob-cap mono'>{o['cap']}</div></div>")


def split(o):
    """Two masses sized by their values. The ratio is the argument."""
    a, b = o["a"], o["b"]
    fa = max(18, round(100 * a["w"] / (a["w"] + b["w"])))
    return (f"<div class='ob ob-split' data-ob='split'>"
            f"<div class='ob-spl'>"
            f"<div class='ob-spl-p dim' style='flex:{fa}'>"
            f"<span class='ob-spl-n disp'>{a['n']}</span>"
            f"<span class='ob-spl-l'>{a['l']}</span></div>"
            f"<div class='ob-spl-p hot' style='flex:{100 - fa}'>"
            f"<span class='ob-spl-n disp'>{b['n']}</span>"
            f"<span class='ob-spl-l'>{b['l']}</span></div></div>"
            f"<div class='ob-cap mono'>{o['cap']}</div></div>")


def clock(o):
    """A ring with a wedge. For a duration, where the shape of the slice is the point."""
    deg = round(360 * o["pct"] / 100)
    return (f"<div class='ob ob-clock' data-ob='clock'>"
            f"<div class='ob-ring' style=\"--deg:{deg}deg\">"
            f"<div class='ob-ring-in'><span class='ob-ring-n disp'>{o['n']}</span>"
            f"<span class='ob-ring-u mono'>{o.get('unit','')}</span></div></div>"
            f"<div class='ob-cap mono'>{o['cap']}</div></div>")


def steps(o):
    """A run of bars. For a shape over time, where the profile is the message."""
    top = max(o["vals"]) or 1
    bars = "".join(
        f"<span class='ob-st{' on' if i == o.get('lit', -1) else ''}' "
        f"style='height:{max(6, round(100 * v / top))}%'></span>"
        for i, v in enumerate(o["vals"]))
    return (f"<div class='ob ob-steps' data-ob='steps'>"
            f"<div class='ob-st-f'>{bars}</div>"
            f"<div class='ob-cap mono'>{o['cap']}</div></div>")


def arrow(o):
    """From one thing to another. The heaviest possible way to say a change happened."""
    return (f"<div class='ob ob-arrow' data-ob='arrow'>"
            f"<div class='ob-arw'>"
            f"<div class='ob-arw-c dim'><span class='disp'>{o['a']}</span>"
            f"<span class='mono'>{o['al']}</span></div>"
            f"<div class='ob-arw-x'>&rarr;</div>"
            f"<div class='ob-arw-c hot'><span class='disp'>{o['b']}</span>"
            f"<span class='mono'>{o['bl']}</span></div></div>"
            f"<div class='ob-cap mono'>{o['cap']}</div></div>")


def strike(o):
    """The wrong way struck through, the right way lit. Two short lines, never paragraphs."""
    return (f"<div class='ob ob-strike' data-ob='strike'>"
            f"<div class='ob-str-x'>{o['x']}</div>"
            f"<div class='ob-str-y'>{o['y']}</div>"
            f"<div class='ob-cap mono'>{o['cap']}</div></div>")


def window(o):
    """Minimal product chrome around a single line. The AI moment, at reel speed."""
    return (f"<div class='ob ob-window' data-ob='window'>"
            f"<div class='ob-win'>"
            f"<div class='ob-win-bar'><span></span><span></span><span></span></div>"
            f"<div class='ob-win-q'>{o['q']}</div>"
            f"<div class='ob-win-a'><span class='ob-win-k mono'>Claude</span>"
            f"<span>{o['a']}</span></div></div>"
            f"<div class='ob-cap mono'>{o['cap']}</div></div>")


BUILD = {"figure": figure, "bar": bar, "dots": dots, "stack": stack, "split": split,
         "clock": clock, "steps": steps, "arrow": arrow, "strike": strike, "window": window}


def render(o: dict) -> str:
    return BUILD[o["form"]](o)


# ----------------------------------------------------------------------------- css
CSS = """
/* THE STAGE. Fixed, never eaten by the copy, per CLAUDE.md 30's working model. The object
   fills it - a small graphic centred in a big box is the thin element the operator rejects. */
.rx{flex:1;min-height:0;display:flex;flex-direction:column}
.rx-h{flex-shrink:0;font-family:'Anton',sans-serif;text-transform:uppercase;
  letter-spacing:-1.6px;line-height:.94;font-size:82px;color:var(--ink);margin:0 0 30px}
.rx-h em{color:var(--acc);font-style:normal}
.rx-stage{flex:1;min-height:0;display:flex;align-items:center;justify-content:center}
.rx-l{flex-shrink:0;margin-top:30px;font-size:38px;font-weight:700;color:var(--ink);
  line-height:1.26}
.rx-l em{color:var(--acc);font-style:normal}

.ob{width:100%;height:100%;display:flex;flex-direction:column;align-items:center;
  justify-content:center;gap:30px}
.ob-cap{flex-shrink:0;font-size:22px;letter-spacing:.2em;color:var(--ink45);text-align:center}

/* figure */
.ob-figure{justify-content:center}
.ob-fig-n{flex:0 0 auto;font-size:420px;line-height:.78;color:var(--acc);letter-spacing:-14px;display:flex;align-items:baseline}
.ob-fig-u{font-size:130px;letter-spacing:-3px;margin-left:14px}

/* bar */
.ob-bar{justify-content:center;gap:26px}
.ob-bar-top{width:100%;display:flex;align-items:baseline;justify-content:space-between}
.ob-bar-v{font-size:190px;line-height:.82;color:var(--acc);letter-spacing:-6px}
.ob-bar-of{font-size:30px;letter-spacing:.16em;color:var(--ink45)}
.ob-bar-t{width:100%;flex:1;min-height:0;border-radius:40px;background:var(--rim2);overflow:hidden;
  box-shadow:inset 0 2px 0 var(--rim)}
.ob-bar-t i{display:block;height:100%;border-radius:40px;background:var(--acc);
  box-shadow:inset 0 3px 0 rgba(255,255,255,.30)}

/* dots */
/* Cells stay CIRCULAR. `grid-auto-rows:1fr` filled the stage by stretching them into
   ovals, and the fill guard reported 100 percent while the object was visually wrong -
   filling the stage is necessary and not sufficient. The field is centred instead and
   the cell size is what makes it big. */
.ob-dot-f{flex:1;min-height:0;display:grid;gap:18px;align-content:center;
  justify-content:center}
.ob-dot{width:74px;height:74px;border-radius:50%;background:var(--rim2);
  box-shadow:inset 0 1px 0 var(--rim)}
.ob-dot.on{background:var(--acc);box-shadow:none}

/* stack */
.ob-stack{flex-direction:row;align-items:stretch;gap:44px;position:relative}
.ob-stk{flex:1;display:flex;flex-direction:column;gap:9px;justify-content:stretch}
.ob-blk{flex:1;border-radius:12px;background:var(--rim2);box-shadow:inset 0 1px 0 var(--rim)}
.ob-blk.on{background:var(--acc);box-shadow:none}
.ob-stk-l{flex-shrink:0;display:flex;flex-direction:column;justify-content:center;gap:10px}
.ob-stk-l .disp{font-family:'Anton',sans-serif;font-size:190px;line-height:.82;
  color:var(--acc);letter-spacing:-5px}
.ob-stk-l .mono{font-family:'DM Mono',monospace;font-size:28px;letter-spacing:.18em;
  text-transform:uppercase;color:var(--ink45)}
.ob-stack .ob-cap{position:absolute;left:0;right:0;bottom:-4px}

/* split */
.ob-spl{width:100%;flex:1;display:flex;gap:18px;min-height:0}
.ob-spl-p{display:flex;flex-direction:column;justify-content:center;gap:14px;
  padding:34px 30px;border-radius:30px;min-width:0}
.ob-spl-p.dim{background:var(--glass2);box-shadow:inset 0 1px 0 var(--rim)}
.ob-spl-p.hot{background:var(--acc)}
.ob-spl-n{font-size:104px;line-height:.85;letter-spacing:-3px;color:var(--ink)}
.ob-spl-p.hot .ob-spl-n{color:var(--bg)}
.ob-spl-l{font-size:28px;font-weight:600;color:var(--ink70);line-height:1.2}
.ob-spl-p.hot .ob-spl-l{color:var(--bg);opacity:.82}

/* clock */
.ob-ring{width:640px;height:640px;border-radius:50%;flex-shrink:0;
  background:conic-gradient(var(--acc) var(--deg),var(--rim2) 0);
  display:flex;align-items:center;justify-content:center}
.ob-ring-in{width:452px;height:452px;border-radius:50%;background:var(--bg);
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px}
.ob-ring-n{font-size:184px;line-height:.85;color:var(--ink);letter-spacing:-4px}
.ob-ring-u{font-size:28px;letter-spacing:.2em;color:var(--ink45)}

/* steps */
.ob-st-f{width:100%;flex:1;min-height:0;display:flex;align-items:flex-end;gap:16px}
.ob-st{flex:1;border-radius:16px 16px 6px 6px;background:var(--rim2);
  box-shadow:inset 0 1px 0 var(--rim)}
.ob-st.on{background:var(--acc);box-shadow:none}

/* arrow */
.ob-arw{width:100%;flex:1;min-height:0;display:flex;align-items:stretch;gap:26px}
.ob-arw-c{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;
  padding:30px 22px;border-radius:34px}
.ob-arw-c.dim{background:var(--glass2);box-shadow:inset 0 1px 0 var(--rim)}
.ob-arw-c.hot{background:var(--acc)}
.ob-arw-c .disp{font-family:'Anton',sans-serif;font-size:186px;line-height:.85;
  letter-spacing:-4px;color:var(--ink)}
.ob-arw-c.hot .disp{color:var(--bg)}
.ob-arw-c .mono{font-family:'DM Mono',monospace;font-size:22px;letter-spacing:.18em;
  text-transform:uppercase;color:var(--ink45);text-align:center}
.ob-arw-c.hot .mono{color:var(--bg);opacity:.78}
.ob-arw-x{flex-shrink:0;align-self:center;font-family:'Anton',sans-serif;font-size:120px;line-height:1;
  color:var(--acc)}

/* strike */
.ob-strike{gap:34px;justify-content:center}
.ob-str-x{width:100%;font-size:78px;font-weight:800;line-height:1.08;letter-spacing:-1px;
  color:var(--ink45);text-decoration:line-through;text-decoration-thickness:6px}
.ob-str-y{width:100%;font-size:92px;font-weight:800;line-height:1.06;letter-spacing:-1.4px;
  color:var(--ink)}

/* window */
.ob-win{width:100%;flex:1;min-height:0;display:flex;flex-direction:column;border-radius:32px;background:var(--glass);overflow:hidden;
  box-shadow:inset 1.4px 1.4px 0 var(--rim),inset -1.2px -1.2px 0 var(--rim2),
    0 26px 54px -22px var(--shadow)}
.ob-win-bar{display:flex;gap:12px;padding:26px 30px;border-bottom:1px solid var(--rim2)}
.ob-win-bar span{width:17px;height:17px;border-radius:50%;background:var(--rim2)}
.ob-win-bar span:first-child{background:var(--acc)}
.ob-win-q{flex:1;display:flex;align-items:center;padding:36px 34px 30px;font-size:58px;font-weight:800;line-height:1.14;
  letter-spacing:-1px;color:var(--ink)}
.ob-win-a{display:grid;grid-template-columns:130px 1fr;gap:16px;align-items:baseline;
  padding:28px 34px 40px;border-top:1px solid var(--rim2);font-size:38px;font-weight:600;
  color:var(--ink70);line-height:1.24}
.ob-win-k{font-size:22px;letter-spacing:.2em;color:var(--acc)}
"""

if __name__ == "__main__":
    print(__doc__)
    print("forms:", ", ".join(FORMS))
