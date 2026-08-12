#!/usr/bin/env python3
"""Pictograms: things that are recognisably things, with the data drawn inside them.

WHY THIS REPLACES THE ABSTRACT SET. Operator, on the first object pass: "elementele trebuie 2d
intr adevar dar trebuie sa transmita ceva - logo uri icons flows, data, files, pipelines,
calendare, orice poate fi related .... nu patrate goale. alea sunt moarte din start."

He is right and the failure is easy to name. A bar, a ring and a field of dots are CHARTS.
A chart encodes a quantity and nothing else, so before you read the caption it could be about
anything, and a viewer with one second does not read the caption. A rectangle does not say
invoice. A circle does not say calendar. The shape has to be the subject.

THE RULE THIS SET IS BUILT ON. Every pictogram is a recognisable object AND carries its number
inside itself. Not an icon next to a statistic - a calendar where four of the twenty working
days are actually filled in, an inbox where nine of forty one envelopes are actually lit, a
pipeline whose fourth stage is actually the narrow one. The quantity is drawn, not captioned,
which is what lets the slide survive being seen rather than read.

Drawn as inline SVG on the glass palette: structure in the muted ink, the data in Book Cloth,
strokes heavy enough to hold at arm's length on a phone. One object fills the 880 x 700 stage.

SECOND PASS: A PICTOGRAM IS NOT ENOUGH, IT HAS TO BE A SCENE. Operator on the first render:
"pictogramele sunt prea basic ... si nu fac scroll stop". Correct, and CLAUDE.md 30 already
had the words for it: every composition is a scene, not a widget - a ground, a dominant mass,
labelled parts carrying real words. What shipped was a widget. Three things were missing and
each one is worth stating, because they are the difference between an icon and a picture:

  1  NO REAL WORDS. A calendar with nine coloured cells is a diagram of nine. A calendar with
     JAN to DEC set in it, nine of them solid, is a YEAR - and the viewer reads a year without
     being told. Every scene carries the words the thing itself would carry.
  2  NO MASS. Line art is a 3px stroke: at phone size it is nearly nothing, whatever the
     coverage metric says. The mass has to be TYPE and filled surface, which is also what the
     lane that travels is made of (see the reference posts in _glass.py: in every one of them
     the text IS the visual).
  3  NO FOCAL BREAK. Nine identical lit cells have no point of entry. One element must break
     the pattern - the tenth month flagged, the one line that is readable - because that break
     is the thing the eye lands on and the reason it stays.

So the scene forms are HTML and type rather than SVG line art, and they drop the glass card:
a panel behind a wall of solid colour only dulls it. SVG stays for the forms that genuinely
are diagrams.
"""

VB = "0 0 200 150"


def _svg(body: str, name: str, vb: str = VB) -> str:
    """One pictogram, cropped to its own ink.

    The shared 200x150 box was a drawing convenience and it cost fill. A portrait stage is
    about 1.1 wide to tall, so a 1.33 box letterboxes before the drawing inside it even gets
    a chance, and a document that occupies half its own frame arrives on the slide at half
    the size it could be. Each form now declares the box its ink actually occupies, so a tall
    object fills the stage by height and a wide one by width, and the two look different from
    each other on consecutive slides rather than sharing one footprint.
    """
    return (f"<svg class='pic' viewBox='{vb}' data-pic='{name}' "
            f"preserveAspectRatio='xMidYMid meet'>{body}</svg>")


def _cells(x0, y0, cols, rows, w, h, gap, lit, r=3):
    out = []
    for i in range(cols * rows):
        cx = x0 + (i % cols) * (w + gap)
        cy = y0 + (i // cols) * (h + gap)
        cls = "pf" if i < lit else "pd"
        out.append(f"<rect class='{cls}' x='{cx:.1f}' y='{cy:.1f}' width='{w}' height='{h}' "
                   f"rx='{r}'/>")
    return "".join(out)


# --------------------------------------------------------------------------- objects
def calendar(o):
    """A SCENE: the periods themselves, named, the spent ones solid. Not a grid of dots.

    The icon version drew a calendar frame with coloured squares in it, which is a diagram of
    a quantity wearing a calendar costume. This draws the thing: twelve tiles carrying JAN to
    DEC, nine of them solid Book Cloth, and a flag on the one where the story turns. Nobody
    has to be told it is a year, and the tile that breaks the pattern is where the eye lands.

    `labels` are the periods in order, `lit` how many are spent, `flag` an optional
    {"i": index, "t": text} marking the one that matters.
    """
    labels = o.get("labels") or ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
                                 "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    cols = o.get("cols", 4)
    flag = o.get("flag") or {}
    tiles = []
    for i, lab in enumerate(labels):
        on = " on" if i < o["lit"] else ""
        f = (f"<span class='sc-flag'>{flag['t']}</span>"
             if flag.get("i") == i else "")
        tiles.append(f"<div class='sc-m{on}'>{f}"
                     f"<span class='sc-m-i'>{i + 1:02d}</span>"
                     f"<span class='sc-m-l'>{lab}</span></div>")
    return (f"<div class='sc sc-year' data-ob='calendar' "
            f"style='grid-template-columns:repeat({cols},1fr)'>{''.join(tiles)}</div>")


def inbox(o):
    """A tray with real ENVELOPES in it, k of them lit. For replies, sends, threads.

    The first version drew them as flat bars, which is a stack of rectangles rather than mail.
    Each one now carries the flap, because the flap is the entire reason an envelope reads as
    an envelope at a glance.
    """
    env = []
    for i in range(o.get("n", 4)):
        y, w, x = 14 + i * 20, 84, 58
        cls = "pf" if i < o["lit"] else "pd"
        env.append(f"<rect class='{cls}' x='{x}' y='{y}' width='{w}' height='17' rx='3'/>"
                   f"<path class='pe' d='M{x} {y} L{x + w / 2:.0f} {y + 6} L{x + w} {y}'/>")
    return _svg(
        "".join(env) +
        "<path class='ps' d='M22 96 L40 96 L48 112 L152 112 L160 96 L178 96 "
        "L178 132 Q178 138 172 138 L28 138 Q22 138 22 132 Z'/>"
        "<path class='ps' d='M40 96 L52 74 L148 74 L160 96'/>", "inbox", "18 8 164 136")


def pipeline(o):
    """Stages that actually narrow, with the count inside each. For a funnel of deals.

    Drawn DOWNWARD, not across. The horizontal version measured 1.88 wide to tall and could
    never fill a portrait stage: it arrived on the slide as a thin strip with air above and
    below it, which is the exact defect this set exists to remove. A funnel also reads
    correctly falling rather than travelling sideways, and the numbers sit big enough to be
    read at arm's length.
    """
    parts = []
    n = len(o["stages"])
    top, bh, gap, full = 10, 30, 12, 184
    for i, s in enumerate(o["stages"]):
        w = full - i * (full - 66) / max(n - 1, 1)
        x = 100 - w / 2
        y = top + i * (bh + gap)
        cls = "pf" if i == o.get("lit", -1) else "pd"
        parts.append(f"<rect class='{cls}' x='{x:.1f}' y='{y}' width='{w:.1f}' height='{bh}' "
                     f"rx='10'/>")
        # A number sitting on the lit bar takes the ground colour. Left in the muted ink it
        # is book orange type on a book orange fill, which is the one stage nobody can read.
        parts.append(f"<text class='pt pbig{' pon' if cls == 'pf' else ''}' x='100' "
                     f"y='{y + bh / 2 + 8:.0f}'>{s}</text>")
        if i < n - 1:
            ym = y + bh + 2
            parts.append(f"<path class='pl' d='M100 {ym} L100 {ym + gap - 4}'/>")
    bot = top + n * bh + (n - 1) * gap
    return _svg("".join(parts), "pipeline", f"4 {top - 6} 192 {bot - top + 12}")


def doc(o):
    """A SCENE: a real page, on the ground colour's opposite, with ONE line readable.

    The icon version was an outlined page with a coloured rule inside it, and a coloured rule
    is not a sentence. Here the page is a bright surface against the feed's dark one, which is
    the contrast jump that stops a thumb, and every line on it is redacted except the one that
    matters - which is set in real type and can be read in the second the viewer has. Reading
    one line of somebody's bad cold email is a reason to stay; looking at a rectangle is not.

    `hot` is that line, `stamp` the mark at its foot, `n` how many redacted lines carry it.
    """
    n = o.get("n", 8)
    at = o.get("at", 4)
    rules = []
    for i in range(n):
        w = (92, 74, 88, 63, 84, 70, 90, 58)[i % 8]
        rules.append(f"<i class='sc-r' style='width:{w}%'></i>")
    rules.insert(at, f"<span class='sc-hotwrap'><mark class='sc-hot'>{o['hot']}</mark></span>")
    stamp = (f"<div class='sc-stamp'>{o['stamp']}</div>" if o.get("stamp") else "")
    return (f"<div class='sc sc-doc' data-ob='doc'><div class='sc-page'>"
            f"<div class='sc-fold'></div>{''.join(rules)}{stamp}</div></div>")


def thread(o):
    """Chat bubbles, the last one lit. For a conversation, a reply, an objection."""
    b = []
    for i, side in enumerate(o["sides"]):
        y = 18 + i * 34
        lit = (i == len(o["sides"]) - 1)
        cls = "pf" if lit else "pd"
        if side == "l":
            b.append(f"<rect class='{cls}' x='16' y='{y}' width='104' height='26' rx='13'/>"
                     f"<path class='{cls}' d='M22 {y + 26} L22 {y + 34} L36 {y + 26} Z'/>")
        else:
            b.append(f"<rect class='{cls}' x='80' y='{y}' width='104' height='26' rx='13'/>"
                     f"<path class='{cls}' d='M178 {y + 26} L178 {y + 34} L164 {y + 26} Z'/>")
    return _svg("".join(b), "thread", "12 12 176 118")


def files(o):
    """Stacked pages, the front one lit. For a pile of anything: requests, tickets, nos.

    The front page carries a folded corner and text lines. Without them it was a filled
    rectangle, which is the dead empty square the whole set exists to avoid.
    """
    p = []
    for i in range(o.get("n", 4) - 1, 0, -1):
        p.append(f"<rect class='pd' x='{44 + i * 13}' y='{20 + i * 9}' width='92' "
                 f"height='112' rx='9'/>")
    lines = "".join(f"<rect class='pfl' x='58' y='{62 + j * 15}' width='{62 if j % 2 else 46}' "
                    f"height='7' rx='3.5'/>" for j in range(4))
    return _svg("".join(p) +
                "<path class='pf' d='M44 20 H108 L136 48 V123 Q136 132 127 132 H53 "
                "Q44 132 44 123 V29 Q44 20 53 20 Z'/>"
                "<path class='pfo' d='M108 20 V48 H136'/>" + lines, "files", "38 14 144 152")


def clockface(o):
    """A real clock with hands and a shaded sector. For a duration a person recognises."""
    import math
    a = 2 * math.pi * o["pct"] / 100 - math.pi / 2
    lx, ly = 100 + 52 * math.cos(a), 78 + 52 * math.sin(a)
    large = 1 if o["pct"] > 50 else 0
    ticks = "".join(
        f"<path class='pl' d='M{100 + 60 * math.cos(math.radians(t)):.1f} "
        f"{78 + 60 * math.sin(math.radians(t)):.1f} "
        f"L{100 + 68 * math.cos(math.radians(t)):.1f} "
        f"{78 + 68 * math.sin(math.radians(t)):.1f}'/>" for t in range(0, 360, 30))
    return _svg(
        f"<path class='pw' d='M100 78 L100 26 A52 52 0 {large} 1 {lx:.1f} {ly:.1f} Z'/>"
        f"<circle class='ps' cx='100' cy='78' r='68'/>{ticks}"
        f"<path class='pa' d='M100 78 L100 40'/>"
        f"<path class='pa' d='M100 78 L132 92'/>"
        f"<circle class='pfc' cx='100' cy='78' r='6'/>", "clockface", "26 4 148 148")


def card(o):
    """A payment card. For money, a bill, a subscription, a renewal."""
    return _svg(
        "<rect class='ps' x='22' y='34' width='156' height='96' rx='14'/>"
        "<rect class='pf' x='22' y='56' width='156' height='16'/>"
        "<rect class='pd' x='38' y='92' width='40' height='22' rx='5'/>"
        "<rect class='pd' x='118' y='104' width='44' height='8' rx='4'/>", "card", "16 28 168 108")


def flow(o):
    """A hub with spokes. For a run, a routing decision, or every job landing on one person.

    Two readings, and which one you want depends on where the accent goes. `lit` on a branch
    says one path was taken out of five. `hub=True` lights the CENTRE and leaves the branches
    quiet, which says the opposite: five jobs, one place they all come back to. The founder
    doing everything himself is that second picture, and it needed to be drawable.
    """
    import math
    nodes, lines = [], []
    n = o.get("n", 5)
    hub = o.get("hub", False)
    for i in range(n):
        a = math.radians(-90 + i * 360 / n)
        x, y = 100 + 62 * math.cos(a), 78 + 56 * math.sin(a)
        cls = "pf" if i == o.get("lit", -1) else "pd"
        lines.append(f"<path class='{'pa' if hub else 'pl'}' d='M100 78 L{x:.1f} {y:.1f}'/>")
        nodes.append(f"<circle class='{cls}' cx='{x:.1f}' cy='{y:.1f}' r='15'/>")
    centre = (f"<circle class='pfc' cx='100' cy='78' r='26'/>" if hub
              else "<circle class='ps' cx='100' cy='78' r='24'/>")
    label = (f"<text class='pt pbig pon' x='100' y='86'>{o['hub_n']}</text>"
             if hub and o.get("hub_n") else "")
    return _svg("".join(lines) + centre + "".join(nodes) + label, "flow", "17 1 166 154")


def terminal(o):
    """A window with a prompt in it. The AI moment, drawn rather than described."""
    return _svg(
        "<rect class='ps' x='14' y='20' width='172' height='112' rx='12'/>"
        "<path class='ps' d='M14 44 H186'/>"
        "<circle class='pfc' cx='30' cy='32' r='4'/>"
        "<circle class='pdc' cx='44' cy='32' r='4'/>"
        "<circle class='pdc' cx='58' cy='32' r='4'/>"
        "<path class='pa' d='M30 62 L40 70 L30 78'/>"
        "<rect class='pd' x='50' y='64' width='84' height='9' rx='4'/>"
        "<rect class='pf' x='30' y='92' width='120' height='9' rx='4'/>"
        "<rect class='pd' x='30' y='110' width='76' height='9' rx='4'/>", "terminal", "10 14 180 124")


def people(o):
    """Seats, k of them filled. For a team, a hire, a room, a list of buyers.

    Head and shoulders as one silhouette, sized to sit inside the frame. The first pass ran
    the bodies off the bottom edge, so they read as columns with circles on top.
    """
    p = []
    n = o.get("n", 5)
    step = 176 / n
    for i in range(n):
        cx = 24 + step * i + step / 2 - 4
        cls = "pf" if i < o["lit"] else "pd"
        p.append(f"<circle class='{cls}' cx='{cx:.1f}' cy='52' r='16'/>"
                 f"<path class='{cls}' d='M{cx - 26:.1f} 124 Q{cx - 26:.1f} 78 {cx:.1f} 78 "
                 f"Q{cx + 26:.1f} 78 {cx + 26:.1f} 124 Q{cx:.1f} 130 {cx - 26:.1f} 124 Z'/>")
    return _svg("".join(p), "people", "6 30 208 106")


def chart(o):
    """A dashboard card whose trend is an AREA, not a stroke.

    The first version drew one thin line inside an empty rectangle. At a glance that is a box
    with a line in it: the outline says nothing and the stroke covers almost no pixels, so the
    slide reads as the empty square this whole set exists to avoid. A trend is an area, since
    what it covers IS the quantity, so the line closes to the baseline and fills. Gridlines
    and a baseline give it the furniture of a real screen.
    """
    pts = o["vals"]
    top = max(pts) or 1
    x0, x1, base, ceil = 30, 172, 124, 50
    step = (x1 - x0) / max(len(pts) - 1, 1)
    xy = [(x0 + i * step, base - (base - ceil) * v / top) for i, v in enumerate(pts)]
    line = " ".join(f"{'M' if i == 0 else 'L'}{x:.1f} {y:.1f}" for i, (x, y) in enumerate(xy))
    area = f"M{x0} {base} " + " ".join(f"L{x:.1f} {y:.1f}" for x, y in xy) + f" L{x1} {base} Z"
    grid = "".join(f"<path class='pl' d='M{x0} {g} H{x1}' opacity='.4'/>" for g in (62, 87, 112))
    return _svg(
        "<rect class='ps' x='14' y='20' width='172' height='118' rx='12'/>"
        "<rect class='pd' x='30' y='32' width='54' height='8' rx='4'/>"
        f"{grid}<path class='pw' d='{area}'/>"
        f"<path class='ps' d='M{x0} {base} H{x1}'/>"
        f"<path class='pa2' d='{line}'/>"
        f"<circle class='pfc' cx='{xy[-1][0]:.1f}' cy='{xy[-1][1]:.1f}' r='8'/>",
        "chart", "10 14 180 130")


def tag(o):
    """A price tag. For a number attached to a thing, a plan, a quote."""
    return _svg(
        "<path class='ps' d='M104 22 H166 Q174 22 174 30 V92 L104 158 "
        "Q98 164 92 158 L34 100 Q28 94 34 88 Z' transform='translate(-8,-14)'/>"
        "<circle class='pfc' cx='142' cy='42' r='10'/>"
        "<rect class='pf' x='58' y='72' width='52' height='9' rx='4' "
        "transform='rotate(45 84 76)'/>"
        "<rect class='pf' x='72' y='94' width='34' height='9' rx='4' "
        "transform='rotate(45 89 98)'/>", "tag", "20 2 152 148")


BUILD = {"calendar": calendar, "inbox": inbox, "pipeline": pipeline, "doc": doc,
         "thread": thread, "files": files, "clockface": clockface, "card": card,
         "flow": flow, "terminal": terminal, "people": people, "chart": chart, "tag": tag}
FORMS = tuple(BUILD)
# Forms rebuilt as full-bleed HTML scenes. They own the whole stage and take no glass card.
# The rest are still SVG diagrams and are next in line.
SCENES = {"calendar", "doc"}


def render(o: dict) -> str:
    return BUILD[o["form"]](o)


def panel(o: dict) -> str:
    """A pictogram mounted on the stage panel, with its units named underneath.

    `k` is what was counted and `v` is the count, both optional. They are a readout, not a
    caption: the slide's sentence lives outside the panel and this strip only says which
    units the drawing is in, in four words, so the shape never has to be explained.

    A SCENE gets no panel. The glass card exists to give a thin line drawing an edge and a
    surface; put it behind a wall of solid type and it only mutes it, and the readout strip
    repeats a number the scene is already carrying at ten times the size.
    """
    if o["form"] in SCENES:
        return render(o)
    foot = ""
    if o.get("k") or o.get("v"):
        foot = (f"<div class='pcard-f'><span class='pcard-k'>{o.get('k', '')}</span>"
                f"<span class='pcard-v'>{o.get('v', '')}</span></div>")
    return (f"<div class='g pcard' data-ob='{o['form']}'>"
            f"<div class='pcard-art'>{render(o)}</div>{foot}</div>")


def check_run(deck_id: str, run: list[str]) -> None:
    """Refuse a run that repeats a form inside one deck, or names one that does not exist.

    Same contract `_objects.check_run` enforced on the abstract set, kept because the rule it
    serves is CLAUDE.md 30's and has nothing to do with which vocabulary is in use: the object
    changes every three or four slides, and seven slides carrying one shape is one object with
    new words in it.
    """
    bad = [f for f in run if f not in FORMS]
    if bad:
        raise ValueError(f"{deck_id}: unknown pictogram(s) {bad}")
    if len(run) != 7:
        raise ValueError(f"{deck_id}: {len(run)} pictograms declared, needs 7")
    dupes = {f for f in run if run.count(f) > 1}
    if dupes:
        raise ValueError(f"{deck_id}: pictogram repeats inside the deck: {sorted(dupes)}")


CSS = """
.pic{width:100%;height:100%;display:block;overflow:visible}
/* structure: the outline of the object, quiet but present */
.pic .ps{fill:none;stroke:var(--ink45);stroke-width:3.2;stroke-linejoin:round;
  stroke-linecap:round}
/* dim parts: the countable things that are NOT the point */
.pic .pd{fill:var(--rim2);stroke:var(--ink45);stroke-width:1.6}
.pic .pdc{fill:var(--rim2)}
/* lit parts: the data. This is the only place the accent appears. */
.pic .pf{fill:var(--acc);stroke:none}
.pic .pfc{fill:var(--acc)}
.pic .pa{fill:none;stroke:var(--acc);stroke-width:4;stroke-linecap:round;
  stroke-linejoin:round}
.pic .pa2{fill:none;stroke:var(--acc);stroke-width:5;stroke-linecap:round;
  stroke-linejoin:round}
.pic .pl{fill:none;stroke:var(--ink45);stroke-width:2;stroke-linecap:round}
.pic .pw{fill:var(--acc);opacity:.30;stroke:none}
/* an envelope flap and a folded corner: the two strokes that stop a rectangle being a
   rectangle. Drawn in the ground colour so they cut INTO the lit shape. */
.pic .pe{fill:none;stroke:var(--bg);stroke-width:2.6;stroke-linejoin:round;opacity:.85}
.pic .pfo{fill:none;stroke:var(--bg);stroke-width:3;stroke-linejoin:round;opacity:.5}
.pic .pfl{fill:var(--bg);opacity:.42}
.pic .pt{fill:var(--ink);font-family:'Anton',sans-serif;font-size:17px;text-anchor:middle}
.pic .pd + .pt,.pic .pt{fill:var(--ink70)}
/* a number drawn INSIDE a shape, at the size the shape can carry */
.pic .pbig{font-size:20px;letter-spacing:-.5px}
/* the same number when its shape is lit: it takes the ground colour, never the ink */
.pic .pon{fill:var(--bg)}

/* ------------------------------------------------------------------ THE STAGE PANEL
   The pictogram sits ON something. Floating it in the slide's own ground was what made
   the first object pass read as empty: a shape with 200px of nothing around it is a shape
   in a void, and the eye reads the void, not the shape. A glass panel filling the stage
   gives the object an edge, a surface and a lit rim, so the dominant mass of the slide is
   full by construction rather than by tuning each drawing to one aspect ratio.

   The readout strip is the only caption allowed, and it is INSIDE the panel: four words of
   mono naming what was counted. The quantity is still drawn - this says which units. */
.pcard{width:100%;height:100%;display:flex;flex-direction:column;padding:34px 34px 28px}
.pcard-art{flex:1;min-height:0;display:flex;align-items:center;justify-content:center}
.pcard-f{flex-shrink:0;margin-top:20px;padding-top:18px;border-top:1px solid var(--rim2);
  display:flex;align-items:baseline;justify-content:space-between;gap:20px}
.pcard-k{font-family:'DM Mono',monospace;font-weight:500;font-size:23px;letter-spacing:.2em;
  text-transform:uppercase;color:var(--ink45);white-space:nowrap;overflow:hidden;
  text-overflow:ellipsis}
.pcard-v{font-family:'Anton',sans-serif;font-size:44px;line-height:1;letter-spacing:-1px;
  color:var(--acc);flex-shrink:0}

/* ---------------------------------------------------------------------- SCENES
   Type and filled surface, edge to edge, no card. A line drawing needed a panel to have an
   edge at all; a scene IS the edge. Both scenes below are built so their mass is the words
   themselves, which is what the posts that travel in this lane are made of. */
.sc{width:100%;height:100%}

/* THE YEAR. Twelve periods, named, the spent ones solid, and one tile flagged. The flag is
   the whole point: nine identical lit tiles are a texture, and a texture has no way in. */
.sc-year{display:grid;grid-auto-rows:1fr;gap:18px}
.sc-m{position:relative;border-radius:24px;display:flex;align-items:flex-end;
  padding:24px 24px 20px;background:var(--glass2);
  box-shadow:inset 0 0 0 2px var(--rim2)}
.sc-m.on{background:var(--acc);
  box-shadow:inset 0 -7px 0 rgba(0,0,0,.14),0 20px 38px -22px var(--shadow)}
.sc-m:has(.sc-flag){box-shadow:inset 0 0 0 3px var(--acc)}
.sc-m:has(.sc-flag) .sc-m-i{display:none}
.sc-m-i{position:absolute;top:22px;left:26px;font-family:'DM Mono',monospace;font-weight:500;
  font-size:21px;letter-spacing:.2em;color:var(--ink45)}
.sc-m.on .sc-m-i{color:var(--bg);opacity:.55}
.sc-m-l{font-family:'Anton',sans-serif;font-size:64px;line-height:.86;letter-spacing:-1.4px;
  color:var(--ink45)}
.sc-m.on .sc-m-l{color:var(--bg)}
.sc-flag{position:absolute;top:22px;left:26px;right:26px;font-family:'DM Mono',monospace;
  font-weight:500;font-size:18px;line-height:1.25;letter-spacing:.14em;text-transform:uppercase;
  color:var(--acc)}

/* THE PAGE. A bright surface against a dark feed, every line redacted except the one worth
   reading. The corner is really cut, not drawn: a clip path takes it out of the page and the
   triangle under it is the fold. */
.sc-doc{display:flex}
.sc-page{position:relative;width:100%;height:100%;display:flex;flex-direction:column;
  gap:38px;padding:76px 62px 56px;border-radius:12px;background:var(--ink);
  clip-path:polygon(0 0,calc(100% - 104px) 0,100% 104px,100% 100%,0 100%);
  box-shadow:0 34px 64px -26px var(--shadow)}
.sc-fold{position:absolute;top:0;right:0;width:104px;height:104px;background:var(--bg);
  opacity:.17;clip-path:polygon(0 0,100% 100%,0 100%)}
.sc-r{display:block;height:18px;border-radius:9px;background:var(--bg);opacity:.13}
.sc-hotwrap{display:block;margin:6px 0}
.sc-hot{font-family:'DM Sans',sans-serif;font-weight:800;font-size:46px;line-height:1.42;
  letter-spacing:-.8px;color:var(--bg);background:var(--acc);border-radius:7px;
  padding:.1em .26em;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.sc-stamp{margin-top:auto;font-family:'DM Mono',monospace;font-weight:500;font-size:23px;
  letter-spacing:.22em;text-transform:uppercase;color:var(--bg);opacity:.44}
"""

if __name__ == "__main__":
    print(__doc__)
    print("pictograms:", ", ".join(FORMS))
