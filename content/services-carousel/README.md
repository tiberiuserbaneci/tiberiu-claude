# Ultron Services Carousel (TikTok / Instagram)

Motion carousel reel, **1080×1450 source slides → 1080×1350 (4:5) reel**, 39.2s, voiced.
New TikTok/Instagram direction (operator, 2026-06-24): **Ultron-forward hook, services not GTM.**
Redesign of the first TikTok REVIEW post ("Tool Engine Editorial45"), rebuilt on the
**Vertex cream 3D template** generated this cycle.

## What it is
- **5 slides:** cover hook (static) → Collections, Proposals, Support (each with motion) → CTA (static).
- Each service slide shows the same premium dark console: a single ask in, five steps routed to real
  apps, and a final **gate row that waits for your yes** before anything spends money or hits send.
- **Design = Vertex** (`gemini-3-pro-image`, 2K, 4:5). All 5 rendered in one batch with the cover as
  the style anchor, so the set is one coherent generation.
- **Motion = composited on top of the Vertex pixels** (no rebuild): the clean design shows from frame 1,
  then each row lights up in sequence (orange fire + scan line + check pings), the gate pulses, a swipe
  arrow nudges. Slide 1 (hook) and slide 5 (CTA) stay static.
- **Voice:** Cloud TTS `en-US-Studio-Q` (male). **Captions:** burned-in subtitles, synced.

## Files
- `services-carousel-45.mp4` — the final reel (the deliverable; in the Monolith vault, tagged Review · TikTok + Instagram).
- `slides/slide-1..5.png` — the Vertex slide designs (scrubbed, operator authorship).
- `poster.jpg` — vault thumbnail (cover frame).
- `caption.md` — TikTok/Instagram caption (CTA-first, Ultron-forward, 5 hashtags).
- `_build/` — reproducible pipeline: `run-deck2.mjs` + `decks/serviceinfo.json` (Vertex render),
  `detect.py` (console detection), `build_slide.py` (per-slide motion), `build_reel.py` (voice + stitch).

## Reproduce
1. `TOKENFILE=gcp_token.txt PROJECT=<gcp> DECK=decks/serviceinfo.json node _build/run-deck2.mjs` → 5 Vertex slides.
2. `python3 _build/build_reel.py` → synth voice, composite motion, burn captions, stitch the reel.

Storage: Monolith vault (live library) + this repo (reference/model copy).
