# BytePlus prompt: the picture for "Claude for solopreneurs, 25 commands that run a one-person business"

Square, 1:1, **no title, no headline, no numbers anywhere** - the hook lives in the white band
that is composited on top (CLAUDE.md 32). Line taken from the three operator reference models:
warm editorial, one central object, function nodes around it, thin orange connectors, very little
text. More visual than text, decent graphic, deliberately NOT a glossy 3D render or AI slop.

## The prompt

```
A clean editorial flat-vector infographic, square 1:1, on a warm cream paper background (#F5ECE3)
with a very fine paper grain. A calm radial command-center layout: at the centre, one softly
glowing rounded-square tile in warm terracotta holding a single minimal four-point starburst
emblem in cream. Six rounded rectangular tiles arranged in an even ring around the centre, each
tile off-white with a soft low shadow, each holding one simple monoline icon above one short
word.

The six tiles, evenly spaced clockwise from top: a coin icon labelled MONEY, a handshake icon
labelled SALES, a megaphone icon labelled MARKETING, a document icon labelled CONTENT, a gear
icon labelled OPS, a magnifier icon labelled RESEARCH.

Thin terracotta dotted connector lines run from the central tile out to each of the six tiles.
Accent palette limited to warm terracotta (#C84623) and soft ochre (#B8873F) for the icons and
connectors, dark charcoal (#1a1a1a) for the six words. Generous white space, balanced symmetric
composition, premium editorial infographic style, crisp clean monoline icons, subtle soft
shadows only.

Absolutely flat 2D editorial illustration, NOT a 3D render, not glossy, not plastic, no bevels,
no photographic elements, no gradients on the type. No title, no headline, no heading text, no
numbers or digits anywhere, no watermark, no logo, no signature, no border. Only the six single
words appear as text, nothing else.
```

## Why the prompt is shaped this way

**One central object, six nodes - the model-4 line, stripped of numbers.** The reference dashboard
carries a wall of figures (34 deals, $312K, 1h 12m). The operator's brief here is more visual and
less text, so the composition is kept and the numbers are dropped: centre = one AI, ring of six =
the whole business. That is a two-second read, which is what a seven-second reveal needs.

**Six one-word labels, and the count is stated twice.** Seedream mangles long strings and invents
extra ones; six short real words is the safe amount, and "only the six single words appear" plus
"no numbers or digits" fences off the gibberish that numbering produced on the research picture
(07, 11, 13 twice, no 12 or 14).

**No Claude mark by name.** Asking for the Claude logo returns a mangled sunburst. A plain
four-point starburst emblem reads as the right family - it is the mark's own geometry - without
pretending to be the trademark, the same fix used on the research picture's green emblem.

**Flat, not 3D, stated four ways.** "NOT a 3D render, not glossy, not plastic, no bevels" is the
whole guard against the vulgar-3D / AI-slop failure the operator named. The three reference models
are all flat editorial; matching that line is the point.

## Then

    python3 content/_seedream.py "<the prompt above>" --out content/ig/solopreneur/picture.jpg
    # validate the picture with the operator, then, with the chosen hook:
    python3 content/_reveal.py content/ig/solopreneur/picture.jpg "line one" "line two" \
      --accent WORD --out solopreneur --render
