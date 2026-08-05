# ULTRON PAPER - the light carousel series

Ten decks, six slides each, 1080x1920, REALNUMBERS light system. PDF carousel per deck plus
per-slide PNGs in `content/paper/`.

Built from the Ultron documentation already in this repo (the `docs-01` to `docs-13` series and
its source copy), cut as founder job stories rather than as feature tours. The decks are data
in `content/_decks_data.py`; the layout primitives and the design system live once in
`content/_deck.py`. Seventy hand-typed slides drift, and by deck four nothing lines up with
deck one.

```bash
python3 content/_fonts.py                       # (re)bake the embedded webfonts
python3 content/_decks_data.py                  # write the ten decks into content/
python3 content/_carousel.py content/paper-*.html   # PNGs + PDF, scrubbed
python3 content/_carousel.py content/paper-01-chat.html --check   # geometry only
```

## The ten

| # | Deck | Keyword | Angle | Source |
|---|---|---|---|---|
| 01 | ONE BOX | CHAT | one composer carries twelve jobs | docs-03 |
| 02 | THE WORKFORCE | AGENTS | seven agents, one router, zero gaps | docs-04, CLAUDE.md 1 |
| 03 | THE BRAIN | BRAIN | memory that survives the tab | docs-06 |
| 04 | BACKGROUND JOBS | JOBS | brief it, close the laptop | docs-05 |
| 05 | THE COMPUTER | COMPUTER | it runs the code, it does not describe it | docs-09 |
| 06 | SESSIONS | CONTEXT | pick it up where you dropped it | docs-10 to 12 |
| 07 | THE BUILDER | BUILDER | a sentence to a live URL | docs-07 |
| 08 | AI-NATIVE INDEX | INDEX | scored on what runs, not what is installed | docs-08 |
| 09 | SHARED WORK | SHARED | send the thread, not the file | docs-13 |
| 10 | THE ROUTING MAP | ROUTING | eight GTM jobs, one AI wins one | docs-02 |

## No two decks read alike, and it is enforced

Each deck declares its run of layout primitives (`cover, rows, grid, split, chart, stack, cta`)
and the builder **exits** if two decks share a run. Anti-repetition stops being a thing someone
remembers to check.

Every deck: `cover` first, `cta` last, four different middles in a different order.

## What this fixes about the reference deck

The `ultron_24h_startup.html` reference performs, and five things about it do not survive
contact with this pipeline:

1. **It loads Tailwind and Google Fonts from a CDN.** The export renderer has no network, so
   that page renders unstyled and cannot be exported at all. See the fonts note below, because
   this bit turned out to be worse than it looked.
2. **`aspect-ratio: 9/16; max-width: 480px` is a preview, not a canvas.** These are 1080x1920
   exactly, asserted per slide at render time; a slide that is off size produces an error, not
   a quietly letterboxed upload.
3. **Its footer sits at `bottom: 6%`**, which is 115px on a 1920 frame and well inside
   TikTok's caption band. CLAUDE.md 9 puts the bottom inset at 330px. Every footer here clears
   it, and `_carousel.py` reports anything painted outside the safe box.
4. **Its accent is `#F27A45`**, which is in neither brand system. These run REALNUMBERS
   (CLAUDE.md 8): `#EFEBE0` ground, `#C84623` accent, `#23211E` for the dark blocks.
5. **Its content area centres a small object in a large empty box.** These pack the band. The
   guard reads 37 to 49% empty rows with a largest dead band of 58 to 68px, against a 120px
   limit.

## The fonts were never loading. In anything.

Every material in this repo links Google Fonts with a `<link>` tag. Headless Chromium here has
no network, so `document.fonts` comes back **empty** and Anton, DM Sans, DM Mono and Instrument
Serif all fall back to the same default grotesque. Measured: the string "ONE BOX" at 100px sets
at 456px in the fallback and 308px in real Anton, a 32% difference in width, and every material
built on the four-register type system has been shipping in one face at four sizes.

`_preflight.py` reported "fonts: 4 families" throughout, because it was reading the `@import`
line, which lists whatever you typed whether or not a byte of it arrived.

`content/_fonts.py` fixes it the same way `_img.py` handles images (CLAUDE.md 18): curl reaches
the internet through the agent proxy even though the renderer does not, so it fetches the CSS
with a browser user agent to get woff2, pulls each file, verifies the magic bytes, and rewrites
the URLs to data URIs. Latin subsets only. The result is `content/assets/fonts.css`, 531 KB, ten
faces, inlined into every deck.

**Any new material should embed that stylesheet rather than link Google Fonts**, and the older
materials are worth re-rendering for the same reason.

## Slide anatomy

```
top 300px      TikTok status bar + tabs + search
  mast         ULTRON PAPER . <deck>            <KEYWORD>
  body         one layout primitive, packed
  foot         logo . brand line                    NN/06
bottom 330px   caption, username, progress bar
left 70 / right 130
```
