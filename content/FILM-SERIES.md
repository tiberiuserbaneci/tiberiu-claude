# ULTRON STACK - narrated film format

Vertical explainer films for TikTok, Reels and LinkedIn video. One agent, one constraint,
one payoff, 26 seconds. Reverse engineered from the reference clip, rebuilt on the
REALNUMBERS light system (CLAUDE.md 8).

---

## How the format actually works

There is no motion design tool in this pipeline. Every object on screen is a CSS or SVG
primitive drawn in an HTML page: browser cards, input fields, data rows, terminal windows,
pill chips. The camera never moves. There is no 3D. Motion is only `opacity`,
`translateY` and `scale`, staggered so a new object lands every 1 to 2 seconds.

The page is not screen recorded. `_film.py` freezes the CSS clock and steps it by hand:

```js
document.getAnimations().forEach(a => { a.pause(); a.currentTime = t_ms })
```

Every element carries its own `animation-delay` on one shared wall clock, so seeking that
clock puts the whole scene at an exact moment. Same input, same bytes out, every run. No
dropped frames, and any beat can be re-timed by editing one number.

## The six beats

The spine is a **constraint reveal**: open on a limitation everyone accepts, then take it
apart. Roughly 50 spoken words across 26 seconds.

| Beat | Window | Job | Episode 01 |
|------|--------|-----|-----------|
| 1 | 0.0 - 5.6s | The constraint everyone lives with | Research eats the first hour |
| 2 | 5.6 - 9.8s | The one action that changes it | You paste one domain |
| 3 | 9.8 - 15.3s | Mechanism A, shown not claimed | CORTEX reads the company |
| 4 | 15.3 - 19.0s | Mechanism B, going deeper | And the person who signs |
| 5 | 19.0 - 22.5s | The payoff, named and granular | One ranked brief |
| 6 | 22.5 - 25.5s | CTA | COMMENT CORTEX |

Those windows are measured off episode 01's take, not chosen. Write the script first, let
the recording place the cuts.

Rules that carry the format:

- **One sentence per beat.** One word per sentence in book orange.
- **Never let the frame go still.** A new object every 1 to 2 seconds inside a beat.
- **Beat 1 is the longest.** The constraint needs room to land before the turn.
- **The dominant block is packed** (CLAUDE.md 30). A lone object floating in the stage
  reads as skippable. Fill it with the real rows, or with what the agent removes.
- **Content is real.** Fields come from the confirmed ICP and the documented agent
  behaviour. Demo data uses an obviously fictional company.

## Making episode 02

1. Copy `cortex-film-01.html`. Name it `<agent>-film-NN.html`, keeping `-film-` in the
   name so the guard targets `#film` at 1080x1920.
2. Rewrite the `FILM-META` block at the top: the six `vo` lines and their beat marks. The
   page is the single source of truth, the renderer never needs editing.
3. Rebuild the six scenes with objects specific to that agent. **Do not reuse episode 01's
   objects** (CLAUDE.md 30, every material is bespoke). Vary the treatment per beat.
4. Check composition without paying for a full render:
   `python3 content/_film.py content/<file>.html --still 13.5`
5. Run the guard: `python3 content/_preflight.py content/<file>.html`
6. Render: `python3 content/_film.py content/<file>.html`

## Renderer

```
python3 content/_film.py <file>.html            # narrated mp4 next to the html
                         --still 13.5           # single PNG at that second
                         --to 3                 # partial render, timing probe
                         --no-audio             # silent
                         --vo-only              # just build the voiceover
                         --png                  # lossless frames, 8x slower
```

Voiceover needs `ELEVENLABS_API_KEY` and `ELEVEN_VOICE_ID` in the environment. **Never
commit them.** Without them the film still renders, silent, on the authored beat marks.

## The voice drives the picture

The narration is **one unbroken take**, not six clips stitched together. Stitched clips each
carry their own lead-in and tail silence, roughly a second of dead air across six cuts, and
the seams are audible. One take also lets the voice carry prosody across sentence
boundaries.

So the picture follows the voice rather than the other way round. ElevenLabs returns
character-level timestamps, `_film.py` reads off when each beat's sentence actually starts,
and writes those into the page's `--b1..--b6` beat clock. Every animation delay is expressed
against that clock:

```css
.h3{animation:rise .7s var(--e) both calc(var(--b3) + .55s), ...}
```

A line that runs long moves its own cut with it. The visual for a sentence can never appear
before the sentence is spoken, and the film's length is set by the take (last word plus a
0.7s tail), so it never outlives the narration or clips it.

## Kinetic type, not a caption track

The narration is part of the film, not an overlay on it, so no line is set at one size. Every
word is weighed and typeset accordingly, which is the whole difference between a subtitle and
a title sequence:

| Weight | What earns it | Typeface | Hook / band size | Entrance |
|---|---|---|---|---|
| `fn` | glue words (the, of, and, is) | **Instrument Serif italic**, muted | 86 / 46px | drift up, 0.22s |
| `mid` | ordinary content words | **DM Sans 700** | 124 / 56px | rise, or in from left or right, 0.34s |
| `key` | long words, caps, numbers | **DM Sans 900** | 170 / 82px | drop or pop, 0.48s |
| `hero` | the episode's `accent` list | **Anton**, uppercase, book orange | 210 / 118px | blur in, 0.72s |

**Three typefaces, each with a different job.** An italic serif for the glue, a grotesque for
the body of the line, a heavy condensed face for the words that land. That is a real change
of voice mid-sentence, which one family at four sizes can never give you.

The single-family rule was lifted by the operator on 2026-08-04 and CLAUDE.md 7 now permits
any font. `_preflight.py` reports the families a material loads rather than rejecting them,
and flags anything past four registers: display, body, glue and meta, the last being DM Mono
on the UI chrome. Give each family a distinct job; two faces that are nearly the same look
worse than one used well.

Declare the episode's hero words in FILM-META as `"accent":[...]`. Everything else is decided
by `weigh()` in `_film.py`, so a new episode gets the treatment for free.

### The band composes on three lines

The caption band is 404px, which is three lines, and using one of them is what makes a
subtitle rail. Phrases are chunked long enough to fill the band (up to 8 words, breaking at a
clause only once there are 4), then `layout_lines()` breaks them with a rhythm rather than
wrapping them:

- a **hero word gets its own line**, so nothing competes with it
- everything else groups into runs of up to 3 words or 18 characters
- **a new idea always starts at the left margin**, then steps right as it continues: left,
  indented, right. This is not decoration, it is reading order. Cycling the anchor by chunk
  index instead threw the opening words of a phrase ("the", "All of it") small and to the
  right, and the reader had to hunt for where the sentence began. Variety comes from the type
  weights and from how many lines a phrase takes, **never** from moving its first word off
  the left.

```
All of it            Then the one
    RANKED               person who
        into one page,       SIGNS,
```
Left, then indented 104px, then 208px. Every phrase begins flush left, no exceptions.

**The step is a bounded indent, not `flex-end`.** Right-aligning the last line threw a short
closing word ("already", "posted.", "cold.") to the far margin, and it stopped reading as part
of the sentence it belongs to. A fixed indent keeps the staircase while keeping the word near
its phrase.

### The caption takes the half the visual is not using

Declare it per beat in FILM-META, `"zones":["bot","top","bot","top","bot"]`, and give each
scene the matching `capbot` or `captop` class so it keeps clear of that half.

**Phrases are chunked within a beat, never across one.** This is what makes zones safe rather
than a source of collisions. A phrase that straddles a cut keeps the zone of the beat it
started in while the picture has already moved on, so the caption and the incoming card both
claim the same half and overlap. Chunking per beat segment makes that impossible by
construction instead of guarding against it after the fact. Alternating it
works the type across the whole frame, which is what the good creators do, without ever
letting a line land on a card. Random placement would collide; placement tied to the beat
cannot.

### Margins

The safe box is inset **104px left / 152px right**, not the 70/130 minimum from CLAUDE.md 9.
At 70px a 118px display word looks clipped to the edge of a phone screen. Verified by
measuring the leftmost glyph in the browser rather than by eye.

**Depth through speed** (choreography rules): the line carrying a hero or key word is
foreground and lands at full speed; supporting lines sit back and take 1.2x as long. Combined
with the **1/3 elements rule**, only one line is ever in active motion, because the words
arrive on the voice.

**Motion identity: Premium** (from the `motion-design` skill). One signature curve
`cubic-bezier(.4,0,.2,1)` for most moves, `cubic-bezier(.05,.7,.1,1)` for entrances that must
be noticed, and **zero overshoot** anywhere. Bouncy easing reads as playful, which is the
opposite of the suspense this format wants.

**All three motion layers must be present**, or the result reads flat no matter how good the
timing is:
- *Primary*: the word arriving.
- *Secondary*: the highlighter chasing a hero word in 70ms behind it, and its tracking
  settling from `.06em` to `-.03em` after it lands.
- *Ambient*: a slow warm breath under the whole frame on an 11s loop, so a held word is never
  a frozen frame.

Exits accelerate and run shorter than entrances (0.14s against 0.22s). What arrives matters
more than what leaves.

### Reveal a row of four as a set, then move the selection

Three cards can be revealed one per spoken clause. Four cannot: at 152px of usable width per
column, three empty slots for two seconds reads as a half built table, which is exactly the
airiness CLAUDE.md 27.9 rejects. Episode 03 lands all four in a **120ms micro cascade** and
moves the voice sync onto the *selection* instead, so the row is complete at every frame and
each card brightens as the narration names it.

The second animation on a card must fill **forwards**. A later `both` filled animation
back-fills its `0%` keyframe to t=0 and wins, which shows every card on the opening frame.
Same trap as the scene fills, and it looks like a rendering bug rather than a CSS mistake.

**Size the panel to its tallest state.** Episode 03's body was 513px against states of 152
to 351px, leaving 59 to 158px of empty panel above and below every one of them. Measure the
content height of each `.st` in the browser, set `min-height` to the tallest plus padding,
then push the panel's travel distance out by however much it shrank so it still lands in the
same place. 513 to 420 took the worst dead band from 158px to 41px, and the guard's own
reading from a passing but soft number to 36px.

## Word budget

**Measure the voice before writing the script.** The Tibi voice runs about **3.3 words per
second, 200 wpm**, so a film needs roughly **3.3 words for every second** you want covered.
Episode 01 is 92 words over 28 seconds.

Coming in under budget is the failure mode. 43 words left the first cut of episode 01 at 45%
speech and it read as unfinished; 92 words puts it at 94%. Run `--vo-only` and check the
reported w/s before committing to a render.

**Punctuation sets the pauses, not word count.** ElevenLabs takes a long breath at a full
stop, so a period between two beats is worth roughly a second of dead air. Episode 01 had a
0.96s hole at one beat boundary that no amount of extra words would close. Ending that beat
on a comma and opening the next with `and` cut it to 0.17s.

Check the result rather than assuming:

```bash
ffmpeg -i content/<film>-vo.mp3 -af silencedetect=noise=-40dB:d=0.35 -f null - 2>&1 \
  | grep silence_duration
```

Pauses of 0.3 to 0.5s are rhythm and worth keeping, especially the one before the CTA.
Anything approaching a second is a hole. Aim for 90%+ speech coverage.

**Re-check the beat windows after recording.** The take decides them, so a beat whose line
runs long gets a longer window, and its objects can finish early and leave the frame static.
Beat 3 of episode 01 stretched to 7.2s while its card finished building in 3.6s, so its rows
were respread to land across the whole window.

The same lever measured again on the episode 03 rewrite: a beat listing four models as four
sentences ran the whole take at **195 wpm over 41.2s**; joining them into one sentence with
commas took it to **219 wpm over 36.8s** with identical wording. Four full stops cost 4.4
seconds. Write lists as one comma sentence unless the pause is doing real work.

**Sync the picture to the measured word, not to a guess.** Dump the word timings out of the
alignment cache and read the offsets straight off it:

```python
words = words_from(json.load(open("content/<film>-vo.align.json"))["alignment"])
[(w, round(s - b4, 2)) for w, s, _ in words if w.strip(".,").lower() in NAMES]
```

Episode 03's four tier cards pulse at b4+2.10 / +4.00 / +6.00 / +8.45 against spoken
Haiku 2.00 / Sonnet 3.93 / Opus 5.91 / Fable 8.18. Landing 0.1s behind the word reads as the
picture confirming the narration; landing ahead of it reads as a mistake.

The renderer calls `_scrub.py` last, which strips MP4 metadata and stamps operator
authorship (CLAUDE.md 28). Never ship a freshly rendered file that skipped it.

## Retention is measurable, so measure it

Episode 01 posted, held over half its traffic through second three, and fell to 10-12% from
second four at an 80%+ skip rate. Two hypotheses were live, weak graphic or weak sentence.
`content/_retention.py` settles that class of argument by reading the frames:

```bash
python3 content/_retention.py content/<film>.html --to 8 --step 0.2
```

It reports **ink**, the share of the frame carrying an edge, and **motion**, the change in the
busiest tile since the last sample. Both had to be defined carefully to be worth anything:

- ink is edge energy, never brightness. These films run cream on cream and ivory on graphite,
  so any absolute threshold measures the background and calls a blank canvas full.
- motion is the busiest **tile**, never the frame mean. A question mark popping in is 0.05% of
  the pixels and averages to nothing while the eye goes straight to it. The global version
  called all three finished films dead in a window where two of them were fine.
- the cliff reference is the hook measured **before the sheet joins it**. A film that overlaps
  its hook with the incoming scene, which every film should, briefly double exposes and posts
  a peak that never exists as a state. Comparing against that inflated peak fails good work.

What it found in episode 01: coverage collapsed from 0.0685 to 0.0206 in 0.15s when the hook
left, and the scenes never recovered past 71% of it. The operator's first hypothesis was
right, and it is now a number.

### Two rules that came out of it

**Full bleed, not a centred card.** A card with margins cannot carry the visual mass the hook
just had. Episode 04's sheet fills the safe band edge to edge and measures 0.093 to 0.132
against a 0.076 hook: 122% to 173%, where episode 01 ran 43% to 71%. The frame gets fuller as
the film runs instead of emptier.

**Never fade content to grey to retire it.** Episode 04's first cut dimmed its dead pilots to
`opacity:.34` with a grayscale filter, which is the obvious way to say "this one died" and
measurably empties the frame: ink fell from 0.088 to 0.043 exactly as the tiles died. Dead
things now go **black on cream**, the same tone as the failed share of every run column. It
raises coverage and reads harder at the same time, which is the rare change that costs
nothing.

A full bleed sheet has no free half to give the caption, so it reserves one: 330px off the
edge that beat's zone claims, against a 300px caption band. The extra 30px is not a fudge, it
absorbs the sheet's own slow push, which scales it 2.2% and puts content outside a box that
padding alone cannot see. Verified by asserting zero caption/content rectangle overlap across
the whole film, not by looking at a still.

**Furnish a state before you animate it.** A bar chart whose bars start at zero height is an
empty frame wearing a headline. Hairline tracks do not fix it either: a 1px border averages
away at viewing size, and the guard is right to ignore it. Draw the thing the bars are
eating into.

## Performance

PNG frame encoding costs 863ms at 1080x1920 against 113ms for JPEG, measured. Frames are
only an intermediate on the way into h264, so JPEG 95 is the default and a full 26s film
renders in about two minutes instead of twenty. The paper texture carries 5% noise, which
dithers the gradients and keeps them from banding. `--png` exists for a pristine master.

The static layers (paper, blurred desk shapes, grid, noise, vignette) live inside one
`.bg` element with `contain:paint`, so the blurs rasterise once rather than recompositing
on all 780 frames. That element also clips them: a rotated box contributes its **rotated**
bounding box to scrollable overflow, which silently pushed the canvas to 2020px and failed
the dimension guard until it was clipped.

## Design skills installed for this series

In `.claude/skills/`, curated from five upstream repos rather than installed wholesale:

| Skill | Why it earns its place here |
|---|---|
| `design-dna` | Reverse engineers layout, type and palette from a reference. This is the manual work that produced episode 01 from the reference clip. |
| `genjutsu/_jutsu/css-native` | Zero-dependency CSS animation, which is exactly this pipeline. |
| `genjutsu/_jutsu/motion-principles` | Timing, easing, enter and exit patterns. |
| `genjutsu/_jutsu/ui-ux-pro-max` | 84 styles, 192 palettes, 74 font pairings. Feeds the bespoke-per-material rule. |
| `genjutsu/_jutsu/design-audit` | Motion gaps and consistency checklist before a render. |
| `genjutsu/_jutsu/canvas-generative` | Particles, flow fields, noise, for backgrounds beyond the CSS paper. |
| `genjutsu/cast`, `genjutsu/paint` | The orchestrators over the above. |
| `gsap-core`, `gsap-timeline`, `gsap-utils`, `gsap-performance` | `timeline.seek(t)` is a deterministic clock like the one here, but with far more expressive sequencing. The upgrade path when CSS delays stop being enough. |
| `motion-design` | Lottie and keyframe workflow. |

**Deliberately not installed.** All eleven `threejs-*` skills: this format is flat editorial on
paper, and 3D would break both the brand and the frame-stepped capture. `gsap-react`,
`gsap-frameworks` and `gsap-scrolltrigger`: there is no framework and no scroll here. The
genjutsu `compose-*`, `swiftui-*`, `mobile-principles` and `desktop-principles` skills are
native app UX, not video. Adding them would only make the right skill harder to trigger.

## Gotcha that will bite you

Two animations on one element, both with `fill-mode: both`, do not behave the way they
read. The second one backwards-fills its `from` keyframe all the way to t=0 and, being
later in the list, wins. Every scene and headline was visible from the first frame because
of it. **Out animations take `forwards`, not `both`:**

```css
.h1{animation:rise .7s var(--e) both .95s, scout .4s ease-in forwards 6.30s;}
```

## The other gotcha, which is worse because it looks like nothing

FILM-META lives inside a CSS comment, so **any `*/` inside it closes that comment early.**
Everything after it becomes garbage CSS, error recovery swallows the whole `:root` block, and
every custom property in the film silently becomes empty. The page still renders, just
unstyled and unanimated, and Python parses the JSON perfectly the whole time, so nothing
warns you.

An accent-marker syntax of `*word*` with `/` as a line separator produced exactly that, via
`*eats*/`. Line separators are `|` now, and `read_meta` refuses to load a meta block
containing `*/`.

The symptom to recognise: rules using `var()` compute to `animation: none` while rules
without it still work.
