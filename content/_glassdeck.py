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

CANVAS. 1080x1920 with the reel safe band (300 top / 130 right / 330 bottom / 70 left), so
the operator can drop the slides straight into a reel without the platform UI eating them.
The 4:5 crop for a carousel post is derived from the same render, centred on the band.
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


def logo_b64() -> str:
    return base64.b64encode((REPO / "content" / "ultron-logo.png").read_bytes()).decode()


# --------------------------------------------------------------------- chrome
def _mast(spec, n):
    return (f"<div class='mast'><span class='mono'>{spec['mast']}</span>"
            f"<span class='mono'>{n:02d} <em>/</em> 09</span></div>")


def _foot(logo):
    return (f"<div class='foot'><img src='data:image/png;base64,{logo}'>"
            f"<span>51ULTRON<em>.</em>COM</span></div>")


def _ai(spec, logo):
    """The AI signal, on every cover.

    Operator, 2026-08-08: "nu imi dau seama din materialele facute de tine ca este vorba de AI
    intr un punct." Correct and serious. CLAUDE.md 21 says to say what the thing DOES rather
    than name an agent, and I took that so far that the copy said "it" for nine slides running
    and never once said Claude. Saying what it does only works when the reader already knows
    what "it" is. So the cover names it, in the frame, every time.
    """
    return (f"<div class='g aichip'><img src='data:image/png;base64,{logo}'>"
            f"<span class='aichip-t'>{spec.get('ai_line', 'Claude, running as Ultron')}</span>"
            f"</div>")


def _slide(spec, n, inner, logo, extra_cls=""):
    return f"""<div class="slide {extra_cls}">
  <div class="field"><i class="f1"></i><i class="f2"></i><i class="f3"></i></div>
  <div class="grain"></div>
  <div class="safe">{_mast(spec, n)}{inner}{_foot(logo)}</div>
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
        out.append(_slide(spec, k + 2, f"""<div class="rc-h disp">{r['h']}</div>
    <div class="g rc"><div class="rc-top mono">{spec['receipt_head']}</div>
      <div class="rc-body">{lines}</div>
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
           "trace": d_trace, "score": d_score, "console": d_console, "stamp": d_stamp}


def build(spec, css_extra: str, fonts: str) -> str:
    """Nine slides: cover, seven content, the ask."""
    logo = logo_b64()
    slides = DESIGNS[spec["design"]](spec, logo)
    if len(slides) != 8:
        raise ValueError(f"{spec['id']}: design produced {len(slides)} slides before the CTA, "
                         f"needs 8 (cover + 7). Give the spec exactly 7 items.")
    slides.append(_cta(spec, logo))
    html = GL.shell(spec["theme"], fonts, "\n".join(slides), spec["id"])
    return html.replace("</style>", css_extra + "\n</style>")


if __name__ == "__main__":
    print(__doc__)
    print(f"canvas {W}x{H}   4:5 crop at y={CROP45_TOP}   designs: {', '.join(DESIGNS)}")
