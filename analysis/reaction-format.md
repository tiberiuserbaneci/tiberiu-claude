# The reaction reel, measured - and what replaces the slideshow

Operator, 2026-08-07: the reaction opener is one of the few virals. The slideshow after it
"uneori prinde alteori imi omoara complet audienta", and two of our carousels run this way did
not pass 200 views. Reference clip measured with `content/_reelscan.py`, 13.87s, 1440x2560.

---

## 1. What the measurement says

Ink is the fraction of the frame carrying an edge. Motion is the busiest tile between samples.

| segment | ink mean | motion mean | dead samples |
|---|---|---|---|
| live plate (0 to 3.7s) | 0.0902 | 0.1665 | 3 of 15 (20%) |
| slideshow (3.7s on) | 0.0888 | 0.1299 | **23 of 40 (57%)** |

**The slides are not empty.** Ink is within 2% of the face. Every instinct says "the slides are
weak" and the frame disagrees: they carry as much as a human head at close range.

**The slideshow is dead 57% of the time.** And the mean hides it - a 22% drop in average motion
looks survivable. The distribution is the story, and it is a sawtooth:

    swipe .27  |  0.0000  0.0000  0.0000  |  swipe .26  |  0.0000  0.0000  0.0000  | ...

Eight times. Motion is not low between slides, it is **exactly zero** - the frame is a held
still. The eye follows change; between swipes there is nothing to follow.

**The last 1.75 seconds are one frozen frame.** From 11.75s to the end, eight consecutive dead
samples. That is the COMMENT slide - the frame that is supposed to convert is the most dead
thing in the video, sitting there while the thumb is already moving.

**Three of the cuts pass through black.** Ink hits 0.0000 at 2.75s and again at 7.00s, near-zero
at 9.75s. A black frame is the worst single frame you can put in a feed: it reads as "over".

**The plate freezes before it ends.** 3.25 to 3.75s is already still - the last frame held while
the caption sat there. The reaction is really 3.0s of motion plus 0.75s of dead hold.

## 2. So the diagnosis is not "the slides are weak"

It is that **a slideshow gives the viewer nothing to watch and too much to read, at the same
time.** Each slide carries roughly 25 words of body copy under the title. At 2s a slide, a
viewer reads about 6 words while also deciding whether to stay. The body copy is never read by
anyone - it only signals "this is dense", which is a reason to leave.

Text budget for the animated part, at ~3 words per second of readable attention: **about 30
words total.** The reference carries about 120 after the plate.

## 3. The format

**LIVE GROUND.** The plate does not cut away. It becomes the ground and keeps playing.

    0.0 - 3.0s   operator plate, full frame, one gesture, no speech.
                 Caption card is ours, not the iOS default box.
    3.0 - 3.5s   the footage does not cut. It darkens and pushes back - brightness and scale
                 down, a grade over it - and stays underneath. Nothing is replaced.
    3.5 - 13.5s  the board builds over the live footage, only ever accumulating.
                 The CTA lands on the same ground. There is never a cut in the whole piece.

Why this and not "animate the slides":

- **It cannot hit the still floor.** Real footage of a person never stops moving. The metric
  that killed the slideshow is structurally unreachable.
- **It never cuts to black**, because it never cuts.
- **It keeps a face on screen**, which is the highest-retention object in any feed, instead of
  spending the strongest asset in the first three seconds and then throwing it away.
- **It answers the operator's own objection to episode 09.** Photography as a ground was
  rejected as fake - it was stock. The operator's own reaction footage is the opposite of
  stock, and it is the one image in this system that is unarguably real.

Second option if a plate long enough is not available: **PERSISTENT CORNER** - the plate shrinks
to a corner card at 3.0s and keeps playing there while the board takes the frame. Weaker, but it
still never cuts and still holds a face.

## 4. What the board does, and the rules it inherits

The run-board model (episodes 05, 10, 11, 12) already solves the accumulate-never-replace
problem, and it ports here with three changes:

1. **No voice.** No VO means no ElevenLabs beat marks and no credits spent, so the clock is
   authored. That is a feature at this length: 10s does not need narration, and the operator
   does not speak on camera anyway.
2. **A continuously running counter**, not a stepped one. One element that moves through the
   entire ten seconds guarantees motion between every row entrance. The reference restates its
   clock on three separate slides; one clock that runs is both cheaper and unbroken.
3. **Titles only.** Row headline plus a two or three word result. No body paragraph. That is
   what gets the piece under the 30 word budget.

Timing, against a 10s board: four rows at ~2.2s, counter running throughout, payoff at ~11.5s,
CTA over the same ground with the counter landing on its final number.

## 5. What has to be true to build it

- A plate of **at least 14s** of usable footage. The reference has 13.87s total and freezes at
  3.25s, so the existing clip is a hook, not a ground. One continuous take, no speech, minimal
  movement after the opening gesture, is enough - it only has to not be still.
- Shot at 1080x1920 or larger, which the reference already is at 1440x2560.
- `content/_reelscan.py` runs on the output before delivery, same as `_retention.py` does for
  the films. The bar to clear is the reference's own live plate: **under 20% dead samples across
  the whole piece**, and zero samples at exactly 0.0000.
