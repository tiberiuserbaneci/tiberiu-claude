# VEO 3 PROMPTING SKILL (in-repo) — learned from DeepMind guide + GitHub Veo3 repos
# (snubroot/Veo-3-Prompting-Guide, jax-explorer/awesome-veo3-videos, shijincai/veo3-prompt-generator).

## Professional 7-component structure (write the prompt in these fields)
1. **Subject** — the thing, with specific attributes.
2. **Action** — exact movement/behavior with timing.
3. **Scene** — environment, props, lighting setup, atmosphere.
4. **Style** — shot type + angle + camera movement + lighting approach + aesthetic + aspect + grade.
5. **Dialogue** — usually none for us.
6. **Sounds** — specify explicitly to stop audio hallucination (or "no music, quiet").
7. **Technical (negative)** — "no subtitles, no watermark, no artifacts, no warped text/logos".

## MULTIPLE camera angles (operator asked; a single 8s clip = one move)
- Reliable pro method = **multi-shot cut**: generate 2-3 short segments, each a DIFFERENT shot
  (angle + framing + lighting), then cut on the beat. This is how you get real angle variety.
- Per segment use ONE primary move (dolly-in / crane-down / orbit / pan). Never stack moves (=muddy).
- **Camera trick:** append **"(that's where the camera is)"** after the camera position — it triggers
  camera-aware processing and sharply improves results.
- Shots vocabulary: EWS, WS, MS, CU, ECU; low-angle, high-angle, top-down; dolly-in, tracking, crane,
  orbit/360, pan, tilt, handheld.

## Varied lighting (operator asked)
- Give each shot a DIFFERENT setup: three-point (warm key + fill + rim), Rembrandt (triangular
  shadow), golden-hour, chiaroscuro (stark light/shadow), soft window light. State it per shot.

## Logos / text (operator: Veo can stylize/animate them; but keep the REAL mark)
- The REAL Claude 3D mark lives in-repo: `content/_templates/tiktok/lib/claude-logo-3d-{matte,glossy,metal,extruded}.png`
  (an ~11-ray coral sunburst). Do NOT let Veo invent a different burst. For a faithful logo, inject
  the real 3D logo into the seed (image-to-video) OR reference it exactly. "Fable 5" wordmark also injected.
- Palette: **Claude light** — cream/off-white paper, soft coral #D97757, warm tan, charcoal ink.
  NO bright red, NO dark sci-fi.

## Length / cost
- Veo 3 single clip ~8s; extend for longer. Veo 3 Fast for iteration (~$1.2/8s), Veo 3 full for finals.
- Multi-shot movie = a few short segments cut together; iterate on Fast, finalize on full.
