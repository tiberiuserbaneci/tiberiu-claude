# BytePlus prompt: the picture for "Claude for solopreneurs, 25 commands"  (v2, on white)

v1 was a calm symmetric ring of six icon tiles. Operator: "nu face scroll stop deloc ... e jalnic
... vreau totul pe alb nu pe crem". A taxonomy has no tension; it reads as a corporate slide. v2
is the model-4 line (a dark "business OS" hero on a light ground) distilled to a single dominant
object with growth energy, on PURE WHITE, high contrast, minimal text.

Square, 1:1, **no title, no words, no numbers** - the hook lives in the white band on top (32).

## The prompt

```
A premium minimal product visualization on a pure solid white background (#FFFFFF), no grain,
generous clean negative space and wide white margins. Centered, a single sleek matte dark
charcoal (#1a1a1a) dashboard panel with softly rounded corners, floating with a soft realistic
drop shadow, tilted very slightly. On the dark panel: one bold smooth upward-trending line chart
glowing in warm terracotta (#C84623), rising confidently to the top right, with a soft
terracotta gradient fill beneath it; beside it three small abstract KPI blocks drawn as simple
rounded rectangles holding tiny bar shapes, and two small circular status indicators glowing
soft terracotta.

Modern SaaS marketing aesthetic, Linear and Notion style, restrained and clean, flat design with
subtle depth, soft shadows only, matte surfaces, high contrast dark panel on pure white.

NOT glossy, not neon, not a sci-fi HUD, not a busy interface, no plastic 3D render. Absolutely NO
legible text, no words, no letters, no numbers, no labels, no watermark, no logo anywhere. Only
abstract UI shapes: the rising chart, the small blocks, the status dots. Balanced, minimal.
```

## Why the prompt is shaped this way

**One dominant object with tension, not six equal calm tiles.** Scroll-stop comes from a money
shot: a business visibly thriving on autopilot. A single dark panel with a confident upward curve
on pure white is high contrast and reads in half a second as "it is working, and it is going up".

**Pure white, stated at the top and reinforced.** "#FFFFFF, no grain, wide white margins" makes
white the dominant pixel value, so the reveal band and footer, which take the mode colour of the
picture (32), come out white too - which is the "totul pe alb" instruction, enforced by the image
rather than by a hardcoded colour.

**No text at all, so nothing can mangle.** v1 got its six words right, but a dashboard full of
labels and numbers is where Seedream produces gibberish. The picture carries meaning through
shape (a rising chart), the hook carries the words, the caption carries the detail.

**Restrained, so it is not slop.** "Linear and Notion style, matte, not neon, not a sci-fi HUD"
is the guard against the glowing-blue-HUD render that reads as AI slop. Warm terracotta on matte
charcoal on white is the brand, not a stock-3D cliche.

## Then

    python3 content/_seedream.py "<the prompt above>" --out content/ig/solopreneur/picture.jpg
    # validate the picture, then render with the chosen hook (accent one word):
    python3 content/_reveal.py content/ig/solopreneur/picture.jpg "Stop hiring." \
      "25 Claude commands run it." --accent hiring --out solopreneur --render
