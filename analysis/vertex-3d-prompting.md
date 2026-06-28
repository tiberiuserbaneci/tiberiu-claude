# Vertex 3D Object Prompting - the premium-congruent render formula

> How we prompt **Vertex AI `gemini-3-pro-image-preview`** to generate the 3D "object" panels for the
> 9:16 carousels, so they do NOT drift, do NOT garble words, and come out as premium, congruent 3D
> (same palette, same edges, same lighting on every object). Re-validated against Google's official
> docs 2026-06-28. The live formula is embedded in `content/_hitl-src/gen_*.py` (`MBASE`/`MTAIL`);
> this file is the durable reference so the knowledge survives container recycles.
> Sources at the bottom.

## API call (exact config we use)

- **Model:** `gemini-3-pro-image-preview` (Google: "designed for professional asset production" - use
  the Pro image model, NOT a faster one, when text must render correctly).
- **Endpoint:** `https://aiplatform.googleapis.com/v1/projects/<P>/locations/global/publishers/google/models/gemini-3-pro-image-preview:generateContent`
- **Project:** `project-c28b1276-8b53-430a-a7a`. **Auth:** ADC refresh_token in `scratchpad/adc.json`
  exchanged for an access token at `oauth2.googleapis.com/token` (see `monolith/README.md` pattern).
- **generationConfig:** `{"responseModalities":["IMAGE"],"imageConfig":{"aspectRatio":"4:5","imageSize":"2K"}}`
  - 4:5 portrait object, 2K so the panel stays crisp when scaled into the slide zone.
- **Style anchor (the #1 congruence lever):** pass a previously-approved object PNG as the FIRST part
  (`inlineData` image) before the text part. Every object in a set inherits its palette / lighting /
  bevel / material from the same seed image, so the deck looks like one family. This is our use of
  Google's "input images for consistency" (up to 3 style references, up to 10 object references).
- **Retry:** backoff on HTTP 429 (20s x attempt) and on empty `candidates` (check `finishReason`);
  up to ~7 attempts. Image gen is non-deterministic - regenerate until it passes (Google: "you might
  have to regenerate images until you achieve the look you want").

## The MBASE formula (what every object prompt contains)

Structure each prompt as **subject + context + style** (Google's core framework), in this fixed order:

1. **Medium + quality first:** "A HIGH-FIDELITY 3D PRODUCT RENDER (Octane / Cinema 4D quality,
   physically-based rendering) of a premium UI panel." Lead with the medium so the model commits to
   3D, not a flat screenshot. Quality boosters Google endorses: 4K/2K, high-detail, "by a professional".
2. **Camera + geometry:** "viewed STRAIGHT-ON in ORTHOGRAPHIC FRONT VIEW, upright and perfectly
   symmetric, no perspective tilt." Fixed camera = objects that line up slide-to-slide.
3. **Material + lighting (explicit, per Google):** "soft-touch MATTE panel with subtly BEVELED rounded
   edges and visible THICKNESS, lit by a three-point SOFTBOX studio setup with ambient occlusion and a
   SOFT CONTACT SHADOW beneath it." Material + three-point softbox are the exact knobs Google lists.
4. **Anti-flat guard:** "NOT a flat 2D screenshot, NOT a sticker, NOT an illustration."
5. **Background + framing for our crop pipeline:** "On a COMPLETELY FLAT #191919 dark charcoal
   background, vertical 4:5, a panel about 3:2 in the MIDDLE at ~70% width so there is a GENEROUS EMPTY
   CHARCOAL MARGIN on ALL FOUR sides." The flat charcoal + margin is what lets `crop_obj()` key the
   background out cleanly and frame the WHOLE panel.
6. **Whole-object rule (our recurring failure if dropped):** "the panel is rendered WHOLE and COMPLETE
   - all four rounded corners and the full left/right/top/bottom edges visible inside the frame; NOTHING
   cropped or running past the frame edge." A generated-whole object is why a later trim is always OUR
   crop bug, never the object (CLAUDE.md S30).
7. **Palette lock:** "ALL accents (buttons, chips, icons, checks, dots) use the SAME warm terracotta
   orange (muted burnt-sienna). Only charcoal, white, muted grey and that one warm orange." Matches the
   Dark Ultron tokens (#191919 / #FAFAF7 / #CC785C). No green/blue/purple.
8. **Anti-garble text rule:** "Real legible text, EXACT words, no garbled text. Do NOT render any hex
   code or colour code as visible text; no raw code, no snake_case, no prices."
9. **Tail:** "The whole panel is exactly this, centred, front-on. No other panels. No code, no hex text."

## Anti-drift / anti-garble (the part that keeps it congruent)

- **Keep visible text SHORT - Google's hard rule: <= 25 characters per text element, and at most
  2-3 distinct phrases per image.** Our panels with many rows are the main garble risk. Per object,
  keep each label a few words; if a panel needs more, cut it or split across rows, never a paragraph.
- **Specify font *style*, not exact font.** The image model gives "creative interpretations, not
  precise font matching." Ask for "clean sans-serif label", not "DM Sans 900" - the DM type lives in
  the coded text layer, not inside the rendered object.
- **Negative prompts: state omissions plainly, do not use "no/don't".** Google: write "wall, frame"
  not "no walls". Our "NO green, NO blue" works in practice but the cleaner form is a short
  "charcoal, white, grey, warm-orange only" positive palette statement; keep both belt-and-braces.
- **Style-anchor image > words for congruence.** When two objects in a set look different, the fix is
  feeding the better one back as the seed, not adding adjectives.
- **One object, one job.** Each object must illustrate ITS OWN slide's hook and be distinct from the
  neighbours (CLAUDE.md S30). Vary the seed/wording so Vertex does not collapse every panel to the
  generic dashboard.
- **Regenerate, then verify.** Non-deterministic: loop until the object passes (palette, complete
  edges, legible exact words). The crop pipeline (`crop_obj` + `place_in_zone`) then frames the WHOLE
  panel and centres it at canvas X + fixed zone-Y on every slide.

## Reuse note (paths to fix before re-running gen_*.py)

The `gen_*.py` scripts hardcode the OLD session scratchpad (`.../27326f10-.../scratchpad`) for `SP`,
`TE`, `adc.json` and the seed image. Before regenerating, repoint:
- `SP` / `adc.json` -> `scratchpad/adc.json` (this session)
- seed image -> a committed approved object under `content/_hitl-src/models_*`
- output dirs -> a working dir under the current scratchpad.
The committed `models_*` objects already exist, so most builds reuse them with NO Vertex call.

## Sources

- Vertex AI - Imagen prompt guide (official): https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide
- Gemini API - Image generation (official): https://ai.google.dev/gemini-api/docs/image-generation
