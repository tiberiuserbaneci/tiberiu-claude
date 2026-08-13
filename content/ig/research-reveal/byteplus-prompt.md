# BytePlus prompt: the picture for "15 ChatGPT prompts for research"

Square, 1:1, **no title anywhere in the image** - the title lives in the white band that gets
composited on top, so any text the model puts at the top would collide with it.

## The prompt

```
A clean flat-vector infographic poster, square 1:1, on a warm cream paper background (#FAF6EE)
with a soft grain. A radial hub-and-spoke diagram: one green circular emblem at the centre,
fifteen thin spokes radiating outward to fifteen small numbered circles, 01 to 15, evenly
spaced around the hub. At the end of every spoke sits a small rounded rectangular label card
in white with a soft shadow, each carrying one short heading in bold dark grey.

The fifteen headings, in order: Research Plan, Brainstorm Topics, Study Review, Question
Builder, Research Timeline, Dataset Helper, Find Gaps, Method Design, Check Credibility,
Trend Insights, Ethics Review, Abstract Summary, Hypothesis Ideas, Cross-Topic Links,
Quiz Generator.

Alternating accent colours on the numbered circles and label headers: muted terracotta
(#C84623), warm ochre (#B8873F), soft sage grey. A tiny line icon beside each label. Balanced
composition, generous white space, editorial infographic style, crisp vector lines, no
photographic elements, no gradients on the type.

Absolutely no title, no headline, no heading text at the top or bottom of the image. No
watermark, no logo, no signature, no border.
```

## Why the prompt is shaped this way

**Short headings only, never the prompt bodies.** The source infographic carries three lines of
body copy per card. No image model renders fifteen paragraphs legibly, and at reel size nobody
reads them anyway - the operator's own model video carries a sixteen row table whose labels are
tool names, not sentences. Give the model fifteen two-word headings and it can hold them.

**No title, stated twice and in two ways.** "No title" and "no heading text at the top" both
appear, because the band is composited over rows 282 to 468 and anything the model draws up
there is destroyed or, worse, half visible under the band.

**No OpenAI mark by name.** Asking for the ChatGPT logo gets a mangled approximation of a
trademarked knot, which is the same defect that got the hand-drawn logos rejected on the
creator toolkit. A plain green circular emblem reads as the right family without pretending
to be the mark.

## Then

    python3 content/_reveal.py <generated.png> "15 ChatGPT PROMPTS" "that do your research" \
      --accent PROMPTS --out research-reveal --render
