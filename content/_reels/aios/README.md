# aios — Instagram motion reel (Fable 5 in action)

The Instagram deliverable for THE AI OPERATING SYSTEM is a single 9:16 motion reel
(15.3s). TikTok keeps the static 3D carousel unchanged.

## Pipeline
1. `build_veo_shots.py` — renders 3 clean shot-seeds (Claude cream palette):
   - seed-A-logo (real Claude 3D starburst + Fable 5 wordmark, warm rim light)
   - seed-B-code (agent program fills the editor window, side window light)
   - seed-C-done (coral check + DONE / shipped in 6.2s / READY TO PUBLISH)
2. `veo_i2v.py` + `veo_bc_stable.py` — Veo 3 Fast image-to-video on each seed, ONE
   camera move per clip (A dolly-in; B/C stable push-in so text does not drift).
   -> veoA-logo.mp4, veoB-code.mp4, veoC-done.mp4
3. `assemble_fable_movie.py` — cuts the CLEAN early window of each clip into one
   13.0s movie (logo -> code -> DONE), hard cuts, NO LOOP. -> fable5-movie.mp4
4. `build_motion_reel.py aios fable5-movie.mp4 <out>` — composites the reel:
   hook top (2.9s) + video centred@t0 descending to fill the bottom half +
   8 elements scrolling the top band (eyebrow+hook, 1.1s beat, spring+motion-blur) +
   CTA overlay on the dimmed video (2.5s). IG safe zones enforced. -> aios-ig-reel.mp4

## Live location
Monolith vault, IG row "THE AI OPERATING SYSTEM (Instagram)"; R2 ultron-reels.
