# TikTok carousel — two distinct working models (saved 2026-06-25)

Two operator-approved ways to build a TikTok/IG carousel. Both share: Dark-Ultron
charcoal `#191919`, DM Sans / DM Mono, hook orange `#C8643F`, big ghosted page
numbers, swipe on slide 1 / progress on 2..N-1 / Ultron-logo + `51ultron.com`
footer on the last slide, and the **genuine Claude sunburst** logo
(`claude_logo_genuine.png` — vector trace: filled core + 11 tapered rays, Claude
orange `#EE7141`; regenerate from `claude_logo_v2.html`). TikTok = Claude-forward;
Ultron lives in the hook + footer.

Target format: **9:16, 1080×1920, full-coverage** (no letterbox bars on IG).
The 3D model = ONE example per slide; vary treatment, never all the same.

---

## MODEL A — TikTok 2D (coded)  ·  the "skill"
**File:** `build_docs_carousel.py` (whole slide = one HTML doc, rendered 2× with Playwright).

- Each slide's focal element is a **real coded HTML/CSS UI card** (docs-style: slash
  palette, active-plan, agents list, file list, ranked-accounts, model routing,
  comments) — pixel-perfect, legible, zero AI artefacts. This is the
  `app.51ultron.com/docs` design language, in code.
- Chrome (eyebrow + headline + description + progress/footer) is all CSS → titles
  are automatically identical across slides.
- Small **3D Claude sunburst** accent above the eyebrow on each slide (optional, not mandatory).
- Highest fidelity + fully controllable. Use this as the default.

## MODEL B — TikTok 3D (Vertex-generated images)
Chrome rendered in PIL (locked typography); Vertex renders ONLY the focal 3D model;
composited into a fixed zone. Two sub-variants:

- **B1 tilted three-quarter** — `gen_models.py` (models). Each slide a *different* 3D
  shape (phone, card cluster, dashboard, stat tiles, node flow, comment card) at a
  three-quarter angle.
- **B2 front-on framed** — `gen_front.py` (models_front). Same elements viewed
  **straight-on (orthographic front, no tilt)**, each cropped + alpha-keyed (charcoal
  → transparent, so NO visible frame/box) into one fixed invisible zone, with a soft
  grounding drop-shadow so it doesn't look "dropped in".

**Page builders:** `build_3d916.py <models_dir> <out_dir>` renders the 9:16 (1080×1920)
page for EITHER model set, reusing the existing model images (no Vertex regen needed to
re-page or reformat). `build_slides.py` / `build_front.py` are the older 4:5 pagers.
`reupload_916.py <out_dir> <prefix>` pushes a rebuilt page to an existing vault item.

### Vertex pro 3D-render formula (learned from Google's Nano Banana guide)
> `[Subject] + [PBR material] + [lighting] + [camera/view] + [color] + [background]`

Copy-ready keywords that make Vertex output a *premium 3D render* not a flat image:
- **Render:** "high-fidelity 3D PRODUCT RENDER, Octane / Cinema 4D quality, physically-based rendering"
- **Material:** "soft-touch MATTE, subtly BEVELED rounded edges, visible THICKNESS / extrusion"
- **Lighting:** "three-point SOFTBOX studio setup, ambient occlusion, soft RIM light, soft CONTACT SHADOW beneath"
- **View:** tilted → "tasteful three-quarter angle"; front-on → "straight-on ORTHOGRAPHIC front view, no perspective distortion"
- **Negatives:** "NOT a flat 2D screenshot, NOT chunky cartoon 3D, NOT plastic-toy, NOT AI-ish, NOT an illustration"
- Seed Vertex with the gold dashboard (`GOLD-dashboard`) ONLY as a quality bar; describe a DIFFERENT shape per slide.

Source: https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana

---

## Shipped examples (Monolith vault, owner tiberiu@nexitynetwork.org, tag TikTok) — all 9:16
- `OPERATOR STACK (9:16 docs)` — Model A → `content/services-rollout/operator-docs/`
- `OPERATOR STACK (3D Vertex · 9:16)` — Model B1 tilted → `content/services-rollout/operator-stack/`
- `OPERATOR STACK (front-framed · 9:16)` — Model B2 front-on → `content/services-rollout/operator-front/`

> NOTE: build scripts use this session's scratchpad paths + read credentials
> (`adc.json` for Vertex, `cfenv` for Cloudflare) that are NEVER committed. They are
> saved here as the reference implementation of each model.
