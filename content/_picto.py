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
"""

VB = "0 0 200 150"


def _svg(body: str, name: str) -> str:
    return (f"<svg class='pic' viewBox='{VB}' data-pic='{name}' "
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
    """A month grid with days actually filled in. For anything measured in days or weeks."""
    grid = _cells(18, 52, 7, 4, 20, 18, 5.5, o["lit"])
    return _svg(
        f"<rect class='ps' x='10' y='22' width='180' height='118' rx='12'/>"
        f"<path class='ps' d='M10 46 H190'/>"
        f"<path class='ps' d='M46 12 V32 M154 12 V32'/>"
        f"<circle class='pa' cx='168' cy='34' r='0'/>"
        f"{grid}", "calendar")


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
        "<path class='ps' d='M40 96 L52 74 L148 74 L160 96'/>", "inbox")


def pipeline(o):
    """Stages that actually narrow, with the count inside each. For a funnel of deals."""
    parts, x = [], 8
    n = len(o["stages"])
    for i, s in enumerate(o["stages"]):
        w = 44 - i * 3
        h = 96 - i * 18
        y = 30 + (96 - h) / 2
        cls = "pf" if i == o.get("lit", -1) else "pd"
        parts.append(f"<rect class='{cls}' x='{x:.1f}' y='{y:.1f}' width='{w}' height='{h}' "
                     f"rx='9'/>")
        parts.append(f"<text class='pt' x='{x + w / 2:.1f}' y='{y + h / 2 + 7:.1f}'>{s}</text>")
        if i < n - 1:
            xa = x + w + 3
            parts.append(f"<path class='pl' d='M{xa:.1f} 78 L{xa + 7:.1f} 78'/>")
        x += w + 10
    return _svg("".join(parts), "pipeline")


def doc(o):
    """A page with a folded corner and one clause lit. For contracts, specs, pages."""
    lines = []
    for i in range(7):
        w = 74 if i % 3 else 52
        cls = "pf" if i == o.get("lit", -1) else "pd"
        lines.append(f"<rect class='{cls}' x='58' y='{44 + i * 12}' width='{w}' height='6' "
                     f"rx='3'/>")
    return _svg(
        "<path class='ps' d='M50 12 H124 L150 38 V140 Q150 144 146 144 H54 "
        "Q50 144 50 140 V16 Q50 12 54 12 Z'/>"
        "<path class='ps' d='M124 12 V38 H150'/>" + "".join(lines), "doc")


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
    return _svg("".join(b), "thread")


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
                "<path class='pfo' d='M108 20 V48 H136'/>" + lines, "files")


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
        f"<circle class='pfc' cx='100' cy='78' r='6'/>", "clockface")


def card(o):
    """A payment card. For money, a bill, a subscription, a renewal."""
    return _svg(
        "<rect class='ps' x='22' y='34' width='156' height='96' rx='14'/>"
        "<rect class='pf' x='22' y='56' width='156' height='16'/>"
        "<rect class='pd' x='38' y='92' width='40' height='22' rx='5'/>"
        "<rect class='pd' x='118' y='104' width='44' height='8' rx='4'/>", "card")


def flow(o):
    """A hub with spokes, one branch lit. For a run, a routing decision, a system."""
    import math
    nodes, lines = [], []
    n = o.get("n", 5)
    for i in range(n):
        a = math.radians(-90 + i * 360 / n)
        x, y = 100 + 62 * math.cos(a), 78 + 56 * math.sin(a)
        cls = "pf" if i == o.get("lit", -1) else "pd"
        lines.append(f"<path class='pl' d='M100 78 L{x:.1f} {y:.1f}'/>")
        nodes.append(f"<circle class='{cls}' cx='{x:.1f}' cy='{y:.1f}' r='15'/>")
    return _svg("".join(lines) + "<circle class='ps' cx='100' cy='78' r='24'/>"
                + "".join(nodes), "flow")


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
        "<rect class='pd' x='30' y='110' width='76' height='9' rx='4'/>", "terminal")


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
    return _svg("".join(p), "people")


def chart(o):
    """A dashboard card with a real trend line. For a number that moved."""
    import math
    pts = o["vals"]
    top = max(pts) or 1
    d = " ".join(
        f"{'M' if i == 0 else 'L'}{30 + i * (140 / (len(pts) - 1)):.1f} "
        f"{124 - 74 * v / top:.1f}" for i, v in enumerate(pts))
    return _svg(
        "<rect class='ps' x='14' y='20' width='172' height='118' rx='12'/>"
        "<rect class='pd' x='30' y='34' width='54' height='8' rx='4'/>"
        f"<path class='pa2' d='{d}'/>"
        f"<circle class='pfc' cx='170' cy='{124 - 74 * pts[-1] / top:.1f}' r='7'/>", "chart")


def tag(o):
    """A price tag. For a number attached to a thing, a plan, a quote."""
    return _svg(
        "<path class='ps' d='M104 22 H166 Q174 22 174 30 V92 L104 158 "
        "Q98 164 92 158 L34 100 Q28 94 34 88 Z' transform='translate(-8,-14)'/>"
        "<circle class='pfc' cx='142' cy='42' r='10'/>"
        "<rect class='pf' x='58' y='72' width='52' height='9' rx='4' "
        "transform='rotate(45 84 76)'/>"
        "<rect class='pf' x='72' y='94' width='34' height='9' rx='4' "
        "transform='rotate(45 89 98)'/>", "tag")


BUILD = {"calendar": calendar, "inbox": inbox, "pipeline": pipeline, "doc": doc,
         "thread": thread, "files": files, "clockface": clockface, "card": card,
         "flow": flow, "terminal": terminal, "people": people, "chart": chart, "tag": tag}
FORMS = tuple(BUILD)


def render(o: dict) -> str:
    return BUILD[o["form"]](o)


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
"""

if __name__ == "__main__":
    print(__doc__)
    print("pictograms:", ", ".join(FORMS))
