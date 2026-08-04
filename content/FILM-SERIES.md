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
| 1 | 0.0 - 6.5s | The constraint everyone lives with | Research eats the first hour |
| 2 | 6.5 - 10.0s | The one action that changes it | You paste one domain |
| 3 | 10.0 - 15.5s | Mechanism A, shown not claimed | CORTEX reads the company |
| 4 | 15.5 - 19.0s | Mechanism B, going deeper | And the person who signs |
| 5 | 19.0 - 23.0s | The payoff, named and granular | One ranked brief |
| 6 | 23.0 - 26.0s | CTA | COMMENT CORTEX |

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
commit them.** Without them the film still renders, silent, with beat timings unchanged.
Each beat is a separate request laid onto a silent bed at its declared mark, so picture and
voice stay locked: a sentence that runs long never pushes the visuals.

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

## Gotcha that will bite you

Two animations on one element, both with `fill-mode: both`, do not behave the way they
read. The second one backwards-fills its `from` keyframe all the way to t=0 and, being
later in the list, wins. Every scene and headline was visible from the first frame because
of it. **Out animations take `forwards`, not `both`:**

```css
.h1{animation:rise .7s var(--e) both .95s, scout .4s ease-in forwards 6.30s;}
```
