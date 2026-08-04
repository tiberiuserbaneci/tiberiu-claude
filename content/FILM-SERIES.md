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

The renderer calls `_scrub.py` last, which strips MP4 metadata and stamps operator
authorship (CLAUDE.md 28). Never ship a freshly rendered file that skipped it.

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
