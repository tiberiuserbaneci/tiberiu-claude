#!/usr/bin/env python3
"""The deck engine. A deck is DATA plus a design name; this renders the nine slides.

Built for volume. The operator needs a hundred of these, so a deck cannot be a hand-built
page - it is a spec dict, and the design is a function that lays that spec out. Adding a deck
is writing twenty lines of content. Adding a design is writing one function.

WHAT THE FORMAT IS (operator, 2026-08-08):
  - The reel opens on the operator's own REACTION, filmed by him, carrying a scroll-stop line.
    The deck's slide 1 must ADVANCE past that line, never repeat it - a repeated hook wastes
    the second where attention is highest. Every spec therefore carries `reaction` (what goes
    over his face) and a separate `hook` (slide 1), deliberately different.
  - Nine slides, one second each, assembled by the operator. Slide 9 is the ask, and it is
    the biggest thing on that slide.
  - No single theme. A hundred reels that look alike is audience saturation, which kills a
    set faster than a weak hook, so designs rotate and both themes are live.
  - Subjects age out at 30 days. A model name that has gone legacy is updated on sight:
    Opus 4.x reads as Opus 5, because a stale version number is the cheapest way to look
    like a repost.

THE DESIGNS. Five mechanics, each with a real graphic element, none of them 3D:

  ledger    the whole system on every slide, one row expanded
  verdict   two columns, the wrong way struck through against the right way
  receipt   an itemised bill with a perforated edge and one heavy TOTAL
  trace     a timestamped spine, one event per slide, for what-happened-when stories
  score     a dense scorecard grid, for which-thing-for-which-job
  console   THE BREAK, and the AI moment. A glass product window: what the founder types on
            one line, and what comes back. Replaces `stamp`, which broke the rhythm by being
            thin and therefore did not stop the scroll at all - a break has to be the most
            ARRESTING slide in the set, not the emptiest. Marked break=True.
  stamp     retired. Kept only so old manifests still resolve.

TWO VARIANTS, NOT ONE RENDER CROPPED (operator, 2026-08-08). They stopped being the same
picture the moment the chrome differed, so each is built at its own size:

  reel      1080x1920, safe band 300/130/330/70. NO mast, NO footer, no badge. The operator
            edits these in Edits over his own footage, so my header and footer are somebody
            else's furniture inside his cut. Slide 1 carries a large centred Claude mark
            instead, which says what this is without a sentence claiming it.
  carousel  1080x1350, even 76px margins because a carousel post has no platform UI over it.
            Keeps the mast and footer, and the badge slot becomes a plain "Swipe" cue.

The badge used to read "Claude, running as Ultron". The operator: it looks like a cheap ad.
He is right - a chip asserting a partnership is advertising, whereas the mark simply being
there is identification. Show the thing, do not caption it.
"""
import base64, importlib.util, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent


def _load(n):
    s = importlib.util.spec_from_file_location(n, REPO / "content" / f"{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


GL = _load("_glass")
W, H = 1080, 1920
SAFE_T, SAFE_R, SAFE_B, SAFE_L = 300, 130, 330, 70
CROP45_TOP = (SAFE_T + (H - SAFE_B)) // 2 - 1350 // 2      # 4:5 centred on the content band


CM = _load("_claudemark")
OB = _load("_objects")
PC = _load("_picto")


def logo_b64() -> str:
    return base64.b64encode((REPO / "content" / "ultron-logo.png").read_bytes()).decode()


def _mark() -> str:
    """The Claude mark, large and centred, on the reel's first slide only.

    It replaces a chip that read "Claude, running as Ultron" and looked, correctly, like a
    cheap ad. A sentence asserting a partnership is advertising; the mark simply being on
    the frame is identification. Behind the type, at low opacity, so it registers without
    competing with the hook.
    """
    return f'<div class="markwrap">{CM.svg()}</div>'


_VARIANT_CSS = {
    # the reel keeps the platform safe band and loses every piece of my chrome
    "reel": """
.slide{width:1080px;height:1920px}
.safe{padding:300px 130px 330px 70px}
/* the mark is an ELEMENT, not a watermark. Ghosting it behind the hook made it a texture,
   and a texture identifies nothing. Full strength, centred, on slide 1 only. */
.markrow{flex-shrink:0;display:flex;justify-content:center;padding-top:18px}
.markrow svg{width:300px;height:300px}
""",
    # same safe band as the reel, plus the object system. Content differs, geometry does not.
    "reelx": """
.slide{width:1080px;height:1920px}
.safe{padding:300px 130px 330px 70px}
.markrow{flex-shrink:0;display:flex;justify-content:center;padding-top:18px}
.markrow svg{width:300px;height:300px}
""" + OB.CSS + PC.CSS,
    # a carousel post has no platform UI over it, so the margins are even and the chrome stays
    "carousel": """
.slide{width:1080px;height:1350px}
.safe{padding:76px}
.markrow{display:none}
""",
}


# --------------------------------------------------------------------- chrome
def _mast(spec, n):
    if str(spec.get("_variant")).startswith("reel"):
        return ""                      # his cut, his chrome
    return (f"<div class='mast'><span class='mono'>{spec['mast']}</span>"
            f"<span class='mono'>{n:02d} <em>/</em> 09</span></div>")


def _foot(logo, spec=None):
    """Logo and the brand name. NO DOMAIN (operator, 2026-08-09).

    "am sesizat ca toti algoritmii ma penalizeaza pentru link ul asta. si linkedin si ig si
    tiktok." A domain rendered into the image is read by OCR on all three platforms and
    scored as off-platform traffic, which is a reach penalty paid on every single slide for a
    URL nobody was going to type off a phone screen anyway.

    The brand name is not a link. `51ULTRON.COM` is a destination, `ULTRON` is an identity,
    and the identity is the only part the footer was ever doing useful work for. The link
    lives where it costs nothing: the first comment and the DM.
    """
    if spec is not None and str(spec.get("_variant")).startswith("reel"):
        return ""
    return (f"<div class='foot'><img src='data:image/png;base64,{logo}'>"
            f"<span>ULTRON</span></div>")


def _ai(spec, logo):
    """The AI signal, on every cover.

    Operator, 2026-08-08: "nu imi dau seama din materialele facute de tine ca este vorba de AI
    intr un punct." Correct and serious. CLAUDE.md 21 says to say what the thing DOES rather
    than name an agent, and I took that so far that the copy said "it" for nine slides running
    and never once said Claude. Saying what it does only works when the reader already knows
    what "it" is. So the cover names it, in the frame, every time.
    """
    if str(spec.get("_variant")).startswith("reel"):
        return f'<div class="markrow">{CM.svg()}</div>'
    return ("<div class='g aichip'><span class='aichip-t'>Swipe</span>"
            "<span class='aichip-a'>&rarr;</span></div>")


def _slide(spec, n, inner, logo, extra_cls=""):
    return f"""<div class="slide {extra_cls}">
  <div class="field"><i class="f1"></i><i class="f2"></i><i class="f3"></i></div>
  <div class="grain"></div>
  <div class="safe">{_mast(spec, n)}{inner}{_foot(logo, spec)}</div>
</div>"""


def _cta(spec, logo):
    """Slide 9. The ask is the biggest thing on it, and it names what arrives."""
    inner = f"""<div class="cta">
    <div class="cta-eye mono">{spec['cta_eye']}</div>
    <div class="cta-kw disp">Comment<br><em>{spec['keyword']}</em></div>
    <div class="g cta-box">
      <div class="cta-b">{spec['cta_line']}</div>
      <div class="cta-s mono">{spec['cta_sub']}</div>
    </div>
  </div>"""
    return _slide(spec, 9, inner, logo)


# --------------------------------------------------------------------- designs
def d_ledger(spec, logo):
    """The whole system on every slide, one row expanded. Keeps the map while giving detail."""
    rows = spec["items"]
    out = []
    slivers = "".join(f"<div class='sl g flat'><span class='rn mono'>{i+1:02d}</span>"
                      f"<span class='st'>{r['t']}</span></div>" for i, r in enumerate(rows))
    out.append(_slide(spec, 1, f"""<div class="cv">
    <div class="cv-eye mono">{spec['eyebrow']}</div>
    <div class="cv-h disp">{spec['hook']}</div>
    <div class="cv-sl">{slivers}</div>
    {_ai(spec, logo)}
  </div>""", logo))
    for k, r in enumerate(rows):
        body = "".join(
            f"<div class='row g{'' if i == k else ' flat'}{' on' if i == k else ''}'>"
            f"<span class='rn mono'>{i+1:02d}</span><span class='rt'>{x['t']}</span>"
            + (f"<span class='rb'>{x['b']}</span><span class='ra mono'>{x['a']}</span>"
               if i == k else "") + "</div>"
            for i, x in enumerate(rows))
        out.append(_slide(spec, k + 2,
                          f"<div class='lg-h disp'>{r['h']}</div><div class='lg'>{body}</div>",
                          logo))
    return out


def d_verdict(spec, logo):
    """Two columns: what everyone does, struck through, against what actually works."""
    rows = spec["items"]
    out = [_slide(spec, 1, f"""<div class="cv">
    <div class="cv-eye mono">{spec['eyebrow']}</div>
    <div class="cv-h disp">{spec['hook']}</div>
    <div class="g vd-tot"><span class="vd-tot-n disp">{spec['badge']}</span>
      <span class="vd-tot-l">{spec['badge_l']}</span></div>
    {_ai(spec, logo)}
  </div>""", logo)]
    for k, r in enumerate(rows):
        # The two panels are sized to their content, never stretched - a card whose copy fills
        # a third of it is the airy block that gets rejected. The space under them carries the
        # RAIL: all seven, current one lit, so the slide keeps the map like the ledger does.
        rail = "".join(f"<span class='vd-p{' on' if i == k else ''}'></span>"
                       for i in range(len(rows)))
        out.append(_slide(spec, k + 2, f"""<div class="vd-h disp">{r['h']}</div>
    <div class="vd">
      <div class="g flat vd-c bad"><div class="vd-tag mono">Everyone does</div>
        <div class="vd-x">{r['x']}</div><div class="vd-w">{r['xw']}</div></div>
      <div class="g vd-c good"><div class="vd-tag mono">What works</div>
        <div class="vd-y">{r['y']}</div><div class="vd-w">{r['yw']}</div></div>
      <div class="vd-cost"><span class="vd-cn disp">{r['cn']}</span>
        <span class="vd-cl">{r['cl']}</span></div>
      <div class="vd-rail"><div class="vd-bars">{rail}</div>
        <div class="vd-rl mono">{k+1} of {len(rows)} <em>&middot;</em> {spec['rail_l']}</div></div>
    </div>""", logo))
    return out


def d_receipt(spec, logo):
    """An itemised bill. The graphic element is the perforation and one heavy TOTAL."""
    rows = spec["items"]
    out = [_slide(spec, 1, f"""<div class="cv">
    <div class="cv-eye mono">{spec['eyebrow']}</div>
    <div class="cv-h disp">{spec['hook']}</div>
    <div class="g rc-tot"><span class="rc-tot-l mono">{spec['badge_l']}</span>
      <span class="rc-tot-n disp">{spec['badge']}</span></div>
    {_ai(spec, logo)}
  </div>""", logo)]
    for k, r in enumerate(rows):
        lines = "".join(
            f"<div class='rc-li{' on' if i == k else ''}'>"
            f"<span class='rc-d'>{x['t']}</span><span class='rc-dot'></span>"
            f"<span class='rc-v mono'>{x['v']}</span></div>" for i, x in enumerate(rows))
        # A bill without a total is a table. The total is the line the whole design exists
        # to arrive at, so it sits inside the body, above the perforation.
        total = (f"<div class='rc-tl'><span class='rc-tl-l'>{spec['total_l']}</span>"
                 f"<span class='rc-tl-n'>{spec['total']}</span></div>"
                 if spec.get("total") else "")
        out.append(_slide(spec, k + 2, f"""<div class="rc-h disp">{r['h']}</div>
    <div class="g rc"><div class="rc-top mono">{spec['receipt_head']}</div>
      <div class="rc-body">{lines}</div>{total}
      <div class="rc-perf"></div>
      <div class="rc-note">{r['b']}</div></div>""", logo))
    return out


def d_trace(spec, logo):
    """A timestamped spine. One event lit per slide. Built for what-happened-when."""
    rows = spec["items"]
    out = [_slide(spec, 1, f"""<div class="cv">
    <div class="cv-eye mono">{spec['eyebrow']}</div>
    <div class="cv-h disp">{spec['hook']}</div>
    <div class="g tr-tot"><span class="tr-tot-n disp">{spec['badge']}</span>
      <span class="tr-tot-l">{spec['badge_l']}</span></div>
    {_ai(spec, logo)}
  </div>""", logo)]
    for k, r in enumerate(rows):
        ev = "".join(
            f"<div class='tr-e{' on' if i == k else ''}'>"
            f"<span class='tr-t mono'>{x['v']}</span><span class='tr-dot'></span>"
            f"<span class='tr-x'>{x['t']}</span>"
            + (f"<span class='tr-b'>{x['b']}</span>" if i == k else "") + "</div>"
            for i, x in enumerate(rows))
        out.append(_slide(spec, k + 2,
                          f"<div class='tr-h disp'>{r['h']}</div><div class='tr'>{ev}</div>",
                          logo))
    return out


def d_score(spec, logo):
    """A dense scorecard. For which-thing-for-which-job, where the grid IS the argument."""
    rows, cols = spec["items"], spec["cols"]
    head = "".join(f"<span class='sc-ch mono'>{c}</span>" for c in cols)
    out = [_slide(spec, 1, f"""<div class="cv">
    <div class="cv-eye mono">{spec['eyebrow']}</div>
    <div class="cv-h disp">{spec['hook']}</div>
    <div class="g sc-tot"><span class="sc-tot-n disp">{spec['badge']}</span>
      <span class="sc-tot-l">{spec['badge_l']}</span></div>
    {_ai(spec, logo)}
  </div>""", logo)]
    for k, r in enumerate(rows):
        body = "".join(
            f"<div class='sc-r{' on' if i == k else ''}'><span class='sc-n'>{x['t']}</span>"
            + "".join(f"<span class='sc-c {v}'>{'+' if v == 'yes' else '-'}</span>"
                      for v in x['m']) + "</div>" for i, x in enumerate(rows))
        out.append(_slide(spec, k + 2, f"""<div class="sc-h disp">{r['h']}</div>
    <div class="g sc"><div class="sc-hd"><span class="sc-ch mono">{spec['col0']}</span>{head}</div>
      {body}<div class="sc-note">{r['b']}</div></div>""", logo))
    return out


def d_console(spec, logo):
    """THE BREAK, and the AI moment: a glass product window, one input, what comes back.

    Two problems, one fix. The break was a thin slide, which broke the rhythm without
    stopping anybody - an audience skips empty as fast as it skips repetitive. And no deck
    was showing the AI at all, so the value read as generic advice. A recognisable product
    window solves both: it is the most arresting frame in the set AND it is unmistakably a
    machine doing the work.

    Founder-facing UI only, per CLAUDE.md 30. What he types, and what he gets. Never code.
    """
    rows = spec["items"]
    out = [_slide(spec, 1, f"""<div class="cv">
    <div class="cv-eye mono">{spec['eyebrow']}</div>
    <div class="cv-h disp">{spec['hook']}</div>
    {_ai(spec, logo)}
  </div>""", logo)]
    for k, r in enumerate(rows):
        pills = "".join(f"<span class='cn-pill{' on' if i == k else ''}'>{x['t']}</span>"
                        for i, x in enumerate(rows))
        outs = "".join(f"<div class='cn-o'><span class='cn-ok'>&#10003;</span>"
                       f"<span>{line}</span></div>" for line in r["out"])
        out.append(_slide(spec, k + 2, f"""<div class="cn-h disp">{r['h']}</div>
    <div class="g cn">
      <div class="cn-bar"><span class="cn-d"></span><span class="cn-d"></span>
        <span class="cn-d"></span><span class="cn-title mono">{spec['window']}</span></div>
      <div class="cn-in"><span class="cn-p mono">You</span><span class="cn-q">{r['in']}</span></div>
      <div class="cn-out"><span class="cn-p mono">Claude</span><div class="cn-lines">{outs}</div></div>
      <div class="cn-foot mono">{r['note']}</div>
    </div>
    <div class="cn-pills">{pills}</div>""", logo))
    return out


def d_meter(spec, logo):
    """THE BREAK, second form: a proportional bar chart and nothing else.

    `console` was the only break in the set, which made the break itself predictable - after
    two of them the audience knows the interrupt is a product window. So the break slot now
    has two shapes and they alternate.

    A chart is the right second shape because it is SIMPLE to read and HEAVY to look at, which
    is the pair `stamp` failed. One idea, taken in at a glance, filling the block with real
    mass. And the bar lengths carry the argument on their own: the row that is longest is the
    one the founder cannot repeat, and you see that before you read a word.

    A zero bar still draws a stub. A row rendering as nothing reads as a bug, and the zeros
    are usually the punchline.
    """
    rows = spec["items"]
    top = max(r["v"] for r in rows) or 1
    pct = lambda v: max(3.0, v / top * 100.0)

    mini = "".join(
        f"<div class='mt-m'><span class='mt-ml'>{r['t']}</span>"
        f"<span class='mt-mb'><i style='width:{pct(r['v']):.1f}%'></i></span>"
        f"<span class='mt-mv mono'>{r['d']}</span></div>" for r in rows)
    out = [_slide(spec, 1, f"""<div class="cv">
    <div class="cv-eye mono">{spec['eyebrow']}</div>
    <div class="cv-h disp">{spec['hook']}</div>
    <div class="g mt-mini">{mini}</div>
    {_ai(spec, logo)}
  </div>""", logo)]
    for k, r in enumerate(rows):
        bars = "".join(
            f"<div class='mt-r{' on' if i == k else ''}'>"
            f"<span class='mt-l'>{x['t']}</span>"
            f"<span class='mt-v disp'>{x['d']}</span>"
            f"<span class='mt-t'><i style='width:{pct(x['v']):.1f}%'></i></span></div>"
            for i, x in enumerate(rows))
        out.append(_slide(spec, k + 2, f"""<div class="mt-h disp">{r['h']}</div>
    <div class="g mt">
      <div class="mt-hd mono"><span>{spec['axis']}</span><span>{spec['unit']}</span></div>
      <div class="mt-body">{bars}</div>
      <div class="mt-note">{r['b']}<span class="mt-a mono">{r['a']}</span></div>
    </div>""", logo))
    return out


def d_grid(spec, logo):
    """THE BREAK, third form: a field of cells, and the argument is how few are lit.

    Two break shapes alternating is still a pattern, and the break slot exists so the eye
    cannot settle. This one reads proportion by COUNTING rather than by bar length, so the
    whole set sits on screen at once and the rare thing is rare on sight.

    One cell is the outcome and carries `win` rather than a category, so the field always
    shows what all the others were for.
    """
    rows = spec["items"]
    total = sum(r["n"] for r in rows)

    def cells(lit=-1):
        out, i = [], 0
        for k, r in enumerate(rows):
            for _ in range(r["n"]):
                i += 1
                out.append(f"<span class='gr-c{' on' if k == lit else ''}'>{i:02d}</span>")
        out.append(f"<span class='gr-c win'>{spec['win']}</span>")
        return "".join(out)

    out = [_slide(spec, 1, f"""<div class="cv">
    <div class="cv-eye mono">{spec['eyebrow']}</div>
    <div class="cv-h disp">{spec['hook']}</div>
    <div class="g gr-mini">{cells()}</div>
    {_ai(spec, logo)}
  </div>""", logo)]
    for k, r in enumerate(rows):
        out.append(_slide(spec, k + 2, f"""<div class="gr-h disp">{r['h']}</div>
    <div class="g gr">
      <div class="gr-hd mono"><span>{r['t']}</span>
        <span>{r['n']} of {total} {spec['unit']}</span></div>
      <div class="gr-f">{cells(k)}</div>
      <div class="gr-note">{r['b']}<span class="gr-a mono">{r['a']}</span></div>
    </div>""", logo))
    return out




def d_reelx(spec, logo):
    """THE ONE SECOND REEL. Hook, object, one line - and nothing else on the slide.

    Operator, after posting A and B: "e prea mult text si nu retine audienta ... ne trebuie
    totusi si un element grafic sugestiv pe fiecare slide."

    Measured first: the old reel slides carried a mean of 75 words each, at one second per
    slide. That is roughly ten times what anybody takes in. The cause was structural - the
    same content was serving a reader-paced carousel and a platform-paced reel, and density
    is right for one and fatal for the other.

    So this is not the carousel with a smaller font. It is different content: about twenty
    words, and an object that carries the number so the sentence does not have to. Seven
    distinct forms per deck, checked, because the same shape seven times is one object with
    new words in it.

    THE OBJECT IS A PICTOGRAM, NOT A CHART (operator, on the first object pass: "nu patrate
    goale. alea sunt moarte din start"). A bar and a ring encode a quantity and nothing else,
    so at one second the viewer has a shape and no subject. `_picto` draws the thing itself
    with the number inside it, mounted on a glass panel that fills the stage. `_objects` is
    still dispatched for any spec that declares an abstract form, so the older demo resolves,
    but nothing new should reach for it.
    """
    rows = spec["reel"]
    run = [r["obj"]["form"] for r in rows]
    (PC.check_run if all(f in PC.FORMS for f in run) else OB.check_run)(spec["id"], run)
    out = [_slide(spec, 1, f"""<div class="cv">
    <div class="cv-eye mono">{spec['eyebrow']}</div>
    <div class="cv-h disp">{spec['hook']}</div>
    {_ai(spec, logo)}
  </div>""", logo)]
    for k, r in enumerate(rows):
        art = (PC.panel(r["obj"]) if r["obj"]["form"] in PC.FORMS
               else OB.render(r["obj"]))
        out.append(_slide(spec, k + 2, f"""<div class="rx">
      <div class="rx-h"><span>{r['h']}</span></div>
      <div class="rx-stage">{art}</div>
      <div class="rx-l">{r['line']}</div>
    </div>""", logo))
    return out


def d_stamp(spec, logo):
    """THE BREAK. One line, one mark, nothing else. Deliberately the thinnest deck in the set.

    Every other design is dense because density is what earns a save. This one is not, and
    that is the whole point: after three list decks the eye has learned the shape and starts
    skipping. A slide read in half a second resets that. Density is a rule about the dominant
    block, never a rule that every slide must be busy.
    """
    rows = spec["items"]
    chips = "".join(f"<span class='stm-chip g flat'>{r['t']}</span>" for r in rows)
    out = [_slide(spec, 1, f"""<div class="cv">
    <div class="cv-eye mono">{spec['eyebrow']}</div>
    <div class="cv-h disp">{spec['hook']}</div>
    <div class="stm-chips">{chips}</div>
  </div>""", logo)]
    for k, r in enumerate(rows):
        out.append(_slide(spec, k + 2, f"""<div class="stm">
      <div class="stm-n mono">{k+1:02d} <em>/</em> {len(rows)}</div>
      <div class="g stm-mark"><span class="stm-x">{r.get('mark', '&times;')}</span></div>
      <div class="stm-l disp">{r['t']}</div>
      <div class="stm-b">{r['b']}</div>
    </div>""", logo))
    return out


DESIGNS = {"ledger": d_ledger, "verdict": d_verdict, "receipt": d_receipt,
           "trace": d_trace, "score": d_score, "console": d_console, "meter": d_meter,
           "grid": d_grid, "stamp": d_stamp}


def build(spec, css_extra: str, fonts: str, variant: str = "reel") -> str:
    """Nine slides: cover, seven content, the ask. `variant` is reel or carousel."""
    spec = dict(spec, _variant=variant)
    logo = logo_b64()
    slides = (d_reelx(spec, logo) if variant == "reelx"
              else DESIGNS[spec["design"]](spec, logo))
    if len(slides) != 8:
        raise ValueError(f"{spec['id']}: design produced {len(slides)} slides before the CTA, "
                         f"needs 8 (cover + 7). Give the spec exactly 7 items.")
    slides.append(_cta(spec, logo))
    html = GL.shell(spec["theme"], fonts, "\n".join(slides), spec["id"])
    return html.replace("</style>", css_extra + f"\n{_VARIANT_CSS[variant]}\n</style>")


if __name__ == "__main__":
    print(__doc__)
    print(f"canvas {W}x{H}   4:5 crop at y={CROP45_TOP}   designs: {', '.join(DESIGNS)}")
