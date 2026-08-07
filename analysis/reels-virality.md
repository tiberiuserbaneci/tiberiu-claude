# Reels virality principles, and what they say about our format

Researched 2026-08-07 at the operator's instruction, after R1 measured clean on dead frames and
was still correctly rejected as "prea monotona si prea plictisitoare fara voce". Sources at the
bottom. What follows is only the part that changes what we build.

## 1. Watch time INCLUDING replays is the top signal

Instagram counts total seconds watched rather than 3-second views, so a 15s reel watched three
times outranks a 60s watched once. Rewatching is read as proof the thing is worth showing to
more people, and viewers replay looped videos without noticing.

**So:** short and loopable beats long. The close should resemble the open closely enough that a
replay has no visible seam. Length is a budget, not a target.

## 2. Sends carry 3 to 5x the weight of likes for unconnected reach

A send is read as a high-trust signal and is the strongest lever for reaching non-followers.

**So:** the piece needs one frame worth sending to someone - a complete, legible artifact. In
the run format that is the assembled board, and it may not be a half-second flash. R2 v1 held
it for 0.4s; it now holds for 2.2s, which is also the "dramatic pause" the pacing guidance puts
between the fast development and the close.

## 3. Vary the interrupt, or it stops working

Repeating one interrupt type - always a zoom, always the same text animation - makes it
predictable, and a predictable interrupt is not an interrupt.

**This is what R1 got wrong.** It ran the same row-entry animation four times. R2 uses seven
distinct treatments (scale slam, horizontal wipe, rise, mask up, rotate-pop, defocus, snap) and
never repeats an entrance back to back.

## 4. Change every ~1s, and keep moving BETWEEN the changes

Guidance is a visual change every 1.5-3s for measured content, tightening to ~0.5s in the final
acceleration, with the "5-second rule": any block where nothing changes is a leak.

**Both halves matter, and each half alone fails.** Measured on our own builds:

| | motion mean | dead samples after the plate |
|---|---|---|
| reference viral | 0.130 | 23/40 (57%) |
| R1, slow board, continuous drift | 0.034 | 0/46 (0%) |
| R2 v1, 1s beats, static between | 0.090 | 17/44 (39%) |
| **R2 final, 1s beats + per-beat drift** | **0.112** | **2/49 (4%)** |

R1 was continuous but inert - the metric said "moving" while the thing looked like nothing was
happening, which is exactly the operator's complaint and a real limit of the measurement. R2 v1
was dynamic but reverted to a slideshow, just a faster one. Only the combination is right: the
frame changes about every second AND the content inside each beat keeps drifting.

The drift has to live on an inner wrapper. A third transform animation on the scene element
replaces its in/out pair rather than adding to it - the same trap recorded in CLAUDE.md 30.

## 5. Kinetic type carries a silent reel

Most feed viewing is sound-off, and animated text is a working substitute for narration: one
idea at a time, entering and leaving, no voiceover needed.

**So:** the segment needs no VO, which also means it costs no credits and can be iterated
freely. Text budget stays at roughly 3 words per second of readable attention.

## What is still unproven

Ink mean is 0.042 against the reference's 0.089 - big type on a dark ground carries fewer edges
than dense light slides. The metric cannot tell "impactful" from "empty", so this is a judgement
call the numbers do not settle, and it is the first thing to look at if R2 underperforms.

Sources:
- https://www.creatorscope.io/blog/how-to-use-pattern-interrupts-to-boost-retention-on-reels
- https://edicionvideopro.com/en/professional-instagram-reels-editing-high-retention/
- https://joyspace.ai/pattern-interrupt-reset-attention-span
- https://blog.hootsuite.com/instagram-algorithm/
- https://www.dataslayer.ai/blog/instagram-algorithm-2025-complete-guide-for-marketers
- https://www.yansmedia.com/blog/kinetic-typography-marketing-videos
- https://reelwords.ai/blog/animated-captions
