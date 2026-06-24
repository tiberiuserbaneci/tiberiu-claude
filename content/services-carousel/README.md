# Ultron Services Carousel (TikTok / Instagram)

New TikTok/Instagram direction (operator, 2026-06-24): **Ultron-forward hook, services not GTM.**
Vertex-designed, **4:5 full-bleed (1080×1350)**, voiced + captioned.

## What it is
- **5 slides, each a distinct composition** (Vertex owns the design; brand system is the only guardrail):
  1. **Hook** — the Ultron orb hero, mixed service objects swirling in. "You run every service by hand. Ultron runs it for you."
  2. **Collections** — the real app icons (accounting, Gmail, CRM, Calendar, Slack, payments), invoices + coins flowing the lines.
  3. **Proposals** — a central proposal document being assembled from its app pieces (Docs, Sheets, e-sign, CRM).
  4. **Support** — a vertical ticket queue clearing into an empty inbox (Gmail, helpdesk, orders, tracker, Slack).
  5. **CTA** — "One ask. Every service runs." + COMMENT SERVICES.
- The **orb appears only on the hook**; service slides carry their real tools. Orange **51ultron.com** footer on every slide, consistent typography.
- **Motion (Instagram movie):** model-generated frames (image-to-image, seeded from each slide) where the app icons float/glow and the objects travel the flow lines / assemble / clear — crossfaded into loops, headline + footer locked so text never drifts. Cover + CTA static.
- **Voice:** Azure Neural `en-US-Andrew:DragonHDLatestNeural` via the Monolith's `/api/tts` (the same engine the Remix/revoice feature uses), normal rate. **Captions:** word-by-word karaoke, burned in.
- **TikTok = the 5 static slides (carousel). Instagram = the movie.**

## Files
- `services-movie-45.mp4` — the 42.8s Instagram movie (in the vault, Review · Instagram).
- `slides/slide-1..5.png` — the 5 static slides, 1080×1350, scrubbed (the TikTok carousel; vault Review · TikTok).
- `poster.jpg` — Instagram video thumbnail.
- `caption.md` — caption (CTA-first, Ultron-forward, 5 hashtags).
- `_build/` — reproducible pipeline: `gen_creative.py` (design direction) · `gen_apps.py`/`gen_fix.py` (Vertex slides) · `add_footer.py` (orange footer) · `gen_motion_all.py`/`gen_34_lite.py` (motion frames) · `stitch_motion.py` (loops) · `build_movie45.py` (voice + karaoke + stitch) · `detect.py`/`rows.py` helpers.

## Notes
- Design = Vertex `gemini-3-pro-image` (2K). Motion frames at 1K to stay in budget.
- Storage: Monolith vault (live library) + this repo (reference/model copy).
- Supersedes the earlier console-table version (this replaces it).
