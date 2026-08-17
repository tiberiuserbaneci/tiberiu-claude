# Brand mark library

Local, offline, permanent. The renderer has no network (CLAUDE.md 18), so every mark a poster or
a film inlines has to be a file on disk. This is that file set, plus the index that tells a
material which variant to use.

Built and maintained by **`content/_logos.py`**. Nothing here is hand drawn: an approximated mark
inside an infographic about that exact product is the first thing a reader notices.

```
content/assets/logos/
├── mono/<slug>.svg        3453 marks, Simple Icons, one path, monochrome, tint it any colour
├── ai/<name>.svg           903 marks, Lobe icons, the AI model set, colour and mono variants
├── color/<slug>.svg         84 full colour marks for the tools we actually name
├── png/<slug>-1024.png     111 raster exports, plus -w white variants, for a video editor
├── logos.json              the index: slug, brand hex, files, source, measured flags
└── library-sheet.png       contact sheet of the working set

content/assets/icons/       THE WORKING SET, what _stack.py and _layouts.py already read
├── <slug>.svg              mono mark
├── <slug>-color.svg        colour mark
└── <slug>-wordmark.svg     the brand's wordmark, when that is all it has
```

Two tiers on purpose: a material wants one obvious file per tool, the library wants everything.
The working set keeps the naming the existing scripts expect, so they picked the new marks up
with no code change.

## What is in it

| | count |
|---|---|
| colour mark | 84 |
| monochrome only | 16 |
| no vector mark anywhere | 41 |
| library, monochrome | 3453 |
| library, AI models | 903 |

## Sources

All four reachable through the agent proxy, measured 2026-08-17. `cdn.jsdelivr.net`, `unpkg.com`,
`cdn.simpleicons.org` and `api.iconify.design` are all still refused on the CONNECT tunnel, which
is why these four and not the obvious CDNs.

| key | source | what it is | licence |
|---|---|---|---|
| `si` | `simple-icons` npm tarball | 3453 monochrome marks plus the official brand hex | CC0 |
| `lobe` | `@lobehub/icons-static-svg` npm | 903 AI model marks, colour and mono | MIT |
| `gil` | `gilbarbara/logos` raw.github | official full colour artwork | CC0 |
| `dash` | `homarr-labs/dashboard-icons` raw.github | app marks, colour | MIT |

The icon **files** are freely licensed. The **trademarks** are not: a third party mark in a
commercial piece needs the operator's approval (CLAUDE.md 18), which the tool stack materials
have. Naming a product in copy and stamping its logo on a frame are two different permissions.

## The two measured flags, and why a material must read them

`logos.json` carries what a filename cannot tell you. Both numbers come off the rendered PNG,
not off the markup, so they describe what the viewer will actually see.

**`dark` (41 marks).** The mark is near black artwork: 26 of them measure a luminance of exactly
0.000. On the slate card `#191919` they are invisible. Vercel, Cursor, ChatGPT, GitHub, Instagram,
X, CapCut, Ideogram, Manus, Recraft, Runway, Suno and Vercel are all in this class. Two correct
fixes: use `png/<slug>-1024-w.png` or tint the mono mark white, or put the colour mark on a light
chip the way a real product tile does. The contact sheet does the second, which is why a third of
its tiles are white.

**`wide_ink` (Cal.com 4.77:1, Gusto 2.63:1).** The drawing is a band, not a tile. A viewBox says
nothing here, because Simple Icons draws every mark inside a 24x24 square, wordmarks included.
Dropped into an 84px square tile a 4.8:1 wordmark is 17px tall and unreadable.

`wordmark` names a separate file for the eight brands whose only colour artwork was a wordmark
(Pipedrive 4.4:1, Webflow 4.0, Zapier 3.7, HubSpot 3.4, Mixpanel 3.1, Gusto 2.6, Flux 2.5,
Stripe 2.4). Those keep their square mono mark in the tile and the wordmark stays available for a
wide slot.

## Two mistakes the builder now refuses to make

**A mark for the wrong company.** `gilbarbara/logos` "apollostack" is Apollo GraphQL, not
Apollo.io the sales tool. Simple Icons "fathom" is usefathom.com the analytics company, not
Fathom the meeting notetaker. Both were installed on the first pass and both would have gone out
on a card next to a description of the other product. Anyone who uses the tool sees it instantly,
so both are now declared missing and render as a monogram tile. `Fathom Analytics` is a separate,
correct entry.

**A stub that passes every structural check.** Lobe's `zapier-color.svg` is a valid 198 byte SVG
holding one 21 character path, and it rendered on the card as a small orange dash. The gate now
measures the drawing, calibrated against the real simple marks it has to let through:

```
stub  zapier-color   198 b   21 ink   1 element   <- reject
real  framer (gil)   405 b   95 ink   1 element
real  trello (gil)   829 b    0 ink   3 elements  <- geometry in rects, no path data at all
real  clickup (dash)1520 b  197 ink   2 elements
```

## No vector mark in any source

41 tools, almost all of them the newest AI startups. Each renders as a monogram tile until a real
file is dropped into `content/assets/icons/`, which is a working outcome, not a blocker.

Apollo, Attio, Beehiiv, Bolt, Clay, Deel, Dropcontact, Elicit, Fathom, FigJam, Fireflies, Gamma,
Granola, Gumloop, Height, Heygen, Higgsfield, Hunter, Instantly, Lemlist, Limitless, Lindy, Mem,
Mercury, Metricool, Motion, Otter, Outreach, Pipedrive, Readwise, Reclaim, Rippling, Salesloft,
Shortwave, Smartlead, Superhuman, Superwhisper, Synthesia, Tana, Whimsical, Wispr Flow.

To add one: drop `<slug>.svg` or `<slug>-color.svg` into `content/assets/icons/` and re-run
`--install`. A local file that none of the four sources carry is kept and recorded as
`local:<file>`, which is how Canva is already in the set.

## Commands

```bash
python3 content/_logos.py --sync            # refresh the source cache, about 9 MB, gitignored
python3 content/_logos.py --install         # library + working set + logos.json
python3 content/_logos.py --png 1024        # raster exports, brand colour and white
python3 content/_logos.py --sheet           # rebuild library-sheet.png
python3 content/_logos.py --find granola    # search all four sources by name
python3 content/_logos.py --report          # what is installed, what is missing
```

`.logocache/` holds the downloaded sources and is gitignored: it is rebuildable in one command,
and the marks themselves are committed, so a fresh container needs no network to render.
