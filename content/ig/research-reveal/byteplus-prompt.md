# The picture for "ChatGPT for research"  (v2, ARK hub + real logo centre)

v1 was a green-emblem hub with 15 numbered cards. Operator 2026-08-13: redo it ARK-generated like
the master reference, with the real ChatGPT logo central, the prompts at concept level, less text,
much more visible. So ARK draws the premium hub with an EMPTY centre, and `content/_center_logo.py`
places the real ChatGPT mark into it (ARK mangles brand logos, so it is never asked to draw one).

Fifteen prompts collapse to six concept nodes: SCOPE, GAPS, SOURCES, METHOD, TRENDS, CONNECT. Six
big words read in two seconds; the fifteen full prompts live in the DM.

## The ARK prompt (empty centre, no logo)

```
A premium editorial hub-and-spoke infographic, square 1:1, on a clean soft warm off-white
background (#FAF7F2) with a very fine grain. In the exact centre, one large clean solid white
circle with a soft drop shadow, completely empty, no symbol or text inside it. Six large rounded
concept cards arranged evenly in a ring around the central circle, each connected to it by one
thin clean line. Each card is off-white with a soft shadow and holds one simple minimal line icon
in warm terracotta above one short bold uppercase word in dark charcoal. The six words, one per
card: SCOPE, GAPS, SOURCES, METHOD, TRENDS, CONNECT. Big cards, big clear legible text, generous
spacing, minimal, premium, modern flat editorial design, soft shadows, warm terracotta accent. No
title, no numbers, no logo, no watermark, no extra text. The central circle stays empty and white.
```

## Then: drop the real logo in, and reveal

```bash
python3 content/_seedream.py "<the prompt above>" --out content/ig/research-reveal/hub-base.jpg
python3 content/_center_logo.py content/ig/research-reveal/hub-base.jpg \
    content/assets/icons/openai.svg content/ig/research-reveal/picture.jpg --scale 0.56
python3 content/_reveal.py content/ig/research-reveal/picture.jpg \
    "ChatGPT is your research team." "Six jobs, one chat." --accent ChatGPT \
    --out research-reveal --render
```

## Why it is shaped this way

**ARK for the look, a vendored SVG for the mark.** The operator likes the generated premium hub
(the master reference was ARK). ARK cannot render the ChatGPT knot, so it draws a clean empty
circle and `_center_logo.py` finds that circle by density and composites the real mark, sized to
the circle, so it never looks pasted.

**Six concept words, not fifteen prompts.** Less text, big and legible at phone size. ARK renders
six short uppercase words cleanly where fifteen headings crowd. The full fifteen are the DM.
