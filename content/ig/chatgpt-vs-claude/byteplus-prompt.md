# BytePlus prompt: the picture for "People who use ChatGPT vs people who use Claude"

Operator, on the HTML-built v1: "foloseste ark pentru design ... backgroundul tb sa fie intr o
singura culoare alb ... designul tb sa fie 1080x1080px tu adaugi restul pentru format 3:4 ...
featurerurile sunt slabe de cacat nu fac scroll stop."

So: ARK owns the design, square 1080x1080, pure flat white, and the picture is a SPLIT SCENE with
tension, not a table of feature rows. The title lives in the band above and is split per column,
one model over its own half (operator: "titul tb sa fie fiecare model in dreptul lui").

Square 1:1, **no words, no letters, no numbers** - Seedream mangles paragraphs, so the labels are
composited in HTML afterwards where they are exact and legible.

## The prompt

```
A premium minimal split-screen product visualization on a pure solid white background (#FFFFFF),
no grain, no texture, flat uniform white across the entire frame, generous clean negative space.

The composition is divided into two equal vertical halves by a single thin light grey vertical
line running down the exact center.

LEFT HALF: a light warm-grey rounded chat interface panel floating with a soft realistic drop
shadow, tilted very slightly, showing three simple abstract speech bubble shapes stacked
vertically and one small four-pointed sparkle shape, all in soft neutral grey tones, calm and
static.

RIGHT HALF: a matte dark charcoal (#1a1a1a) rounded terminal panel floating with a soft realistic
drop shadow, tilted very slightly the opposite way, slightly larger and more dominant, showing
abstract horizontal code-line bars glowing in warm terracotta (#C84623) with a bright terracotta
cursor block, and one bold upward-trending arrow shape in terracotta rising to the top right.

Modern SaaS marketing aesthetic, Linear and Notion style, restrained and clean, flat design with
subtle depth, soft shadows only, matte surfaces, high contrast, lots of white breathing room
around both panels and clear empty white margins at the top and bottom of the frame.

NOT glossy, not neon, not a sci-fi HUD, not a busy interface, no plastic 3D render, no gradient
background. Absolutely NO legible text, no words, no letters, no numbers, no labels, no
watermark, no logo anywhere. Only abstract UI shapes: speech bubbles, code-line bars, the cursor,
the arrow. Balanced, minimal, high contrast between the calm light left and the working dark
right.
```

## Why the prompt is shaped this way

**The contrast IS the scroll stop.** A calm light chat panel beside a dark working terminal reads
in half a second as "one side talks, the other ships" - which is the whole argument of the
material, made visually before a single word is read. A grid of feature rows makes that argument
in twelve small lines nobody stops for.

**Pure white, stated twice.** The band and footer take the MODE colour of the picture (32), so
white here is what makes the whole card white, as the operator asked, enforced by the image rather
than by a hardcoded value.

**No text at all.** The labels are the payload and they may not be gibberish, so they are
composited in HTML over the empty white margins the prompt reserves.

**The right half is deliberately more dominant.** Slightly larger, darker, with the rising arrow:
the material's verdict is that the building side compounds, and the composition says so.

## Then

    python3 content/_seedream.py "<the prompt above>" \
      --out content/ig/chatgpt-vs-claude/picture-raw.jpg --size 2048x2048
    python3 content/_board01pic.py          # composites the labels, writes picture.png
    python3 content/_reveal.py content/ig/chatgpt-vs-claude/picture.png \
      "People who use" "ChatGPT" --split "vs people who use" "Claude" --accent Claude \
      --pic-h 1080 --foot-h 108 --out chatgpt-vs-claude --render
