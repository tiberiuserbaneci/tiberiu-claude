# Design upgrade notes (operator: "LinkedIn 3/10, IG/TT 6/10, basic si monoton") - 2026-07-02

Research: pineable.com carousel best practices, linkboost/meet-lea LinkedIn carousel guides,
postnitro/resont IG hook guides, dark-glassmorphism 2026 trend pieces, Chris Do / Lara Acosta
carousel breakdowns + INTERNAL reference: app.51ultron.com landing (operator-approved bar).

## Why v2 scored 3/10 (root causes)
1. **Monochrome monotony**: every block = same dark grey card (#1f1f1e) + 1px hairline border.
   No color fields, no pattern interrupts. The eye has nothing to land on.
2. **Timid typography**: 54px hooks, 34px stats. Top creators run display type at 4em vs 1.5em
   body (2.6x+ ratio); the site runs ~80px light display on mobile width.
3. **No focal "money" element** per poster: everything equal weight = nothing scroll-stops.
4. **No real-world texture**: zero real logos in LinkedIn, no photographic/3D element = "template" feel.

## The v3 design system (from the site + research)
- **Color-field cards**: SOLID terracotta gradient blocks (site's "Pre-built primitives" card) and
  **IVORY cards with dark text** (site's white pills scaled up) as the pattern interrupt on dark.
  Rule: every poster gets >=1 solid accent block + >=1 ivory block. Hairline cards only as tertiary.
- **Display type**: hooks 62-72px, key numbers 96-150px, tight tracking, sentence case + period.
  Hierarchy ratio >=2.5x between display and body. Body >=15px (mobile-legible at 5in).
- **Glow blooms**: radial warm glows behind the focal number/element (site's light-burst language).
- **White pills**: CTA chips = white pill + dark text (site button language), not outlined boxes.
- **Real 3D logos**: Vertex-rendered glossy tool tiles wherever tools are named (mixed-media beats
  flat vector; the UNFAIR ADVANTAGE bar).
- **One idea per slide / one focal per poster**: the money element takes 35-50% of the canvas.
- **First slide = 2-second audition**: hook 5-8 words + the distinctive visual; specificity + contrast.

## IG cover overlay (operator correction)
Overlay must NOT block the video: NO full-bleed card. Hook + KEYED floating logo stack (transparent
bg, tiles float over the video) + small brand marks. Play hook and stack as one composition.
