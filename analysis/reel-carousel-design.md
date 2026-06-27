# Fast-Flip Reel-Carousel Design Rules

> Reference for 9:16 (1080x1920) Dark Ultron carousels that auto-advance every 0.5-1s in a reel.
> Each slide = fixed eyebrow + headline at the top, one 3D "object" (rendered UI panel) grounded
> in a fixed middle zone. Built for a library of ~100 reusable 3D shells with text injected by code.
> Added to the learning set 2026-06-27. Extends CLAUDE.md S9 (safe zones), S26 (virality), S27 (density).
> Sources at the bottom.

## North star

When slides flip in 0.5-1s the eye never re-reads, it pattern-matches: it locks onto whatever sits
in the SAME screen position as the last frame and treats everything else as motion. So the sequence
must behave like one continuous scene with a few fixed anchors and exactly one thing changing per
beat (the "object"). Lock the eyebrow, headline baseline, object center, and footer to identical
pixel coordinates on every slide; vary only the object and the headline words. Use serial dependence
and Gestalt continuity in your favor (the brain auto-stitches frames that share position, color and
direction); fight them and the deck reads as disconnected posts that "jump." Judge a slide by what
survives a single 0.5-1s glance: one anchored shape, one bold word, one accent.

## A. Fixed anchor points and alignment across slides

- Lock 4 anchors to identical pixel coords on EVERY slide: eyebrow top, headline first-baseline,
  3D-object center, footer baseline. These never move frame to frame. This is the single most
  important rule for a fast flip.
- Object center is the master anchor: pin it to canvas X-center (540px) and ONE fixed Y on every
  slide (matches CLAUDE.md S30 "same fixed Y on every slide"). Vary the object's size/shape inside
  the zone, never its center. A panel that drifts up/down between slides is the #1 jarring failure.
- Use an 8pt grid: every margin, gap and offset is a multiple of 8. Side padding ~90px (already the
  TikTok norm in S9). Inner gutter 20-24px.
- Snap headline and eyebrow to a left edge that is constant across slides; do not re-center text per
  slide (centering shifts the left edge and the eye sees it twist).
- Keep all content inside the safe band: top inset 300px, bottom 330px, left 70px, right 130px
  (CLAUDE.md S9). The visible working band is ~1080x1290; design only inside it, keep the 1920 canvas.
- Reserve a FIXED object zone (a constant box) and frame every panel to that box. Frame a panel by
  its difference from its own corner background (most-inclusive bbox before the soft vignette), then
  scale it to fill the zone and center it, so no panel sits higher/lower/wider than another.
- Headline area is a fixed height block (e.g. 2-line max box). Reserve space for 2 lines even when a
  slide uses 1, so the object below never shifts up. Text grows/shrinks inside the box, the box is fixed.

## B. Visual rhythm and the one-thing-varies principle

- ONE thing varies per slide: the object plus its headline. Eyebrow style, type sizes, colors,
  positions, footer stay identical. This is what makes a flip feel like turning pages, not channel-surfing.
- Identical typography across all slides: same headline size, same eyebrow size, same weight. Do NOT
  resize the headline to "fit" longer copy; shorten the copy instead.
- Constant background and border on every slide visually binds the set (Gestalt: similarity +
  common region). Same charcoal #191919, same dot-grid texture, same atmospheric glow placement.
- Maintain a steady beat: one object per slide, never two competing focal elements (one focal rule
  also in S30). Two objects on one fast slide reads as noise.
- Do NOT spread sparse content with space-between or flex:1 to fill the zone (S27 hard rule). A thin
  object in a big zone reads airy and skippable. Scale the object to fill, or pick a denser shell.
- Vary objects so no two CONSECUTIVE slides repeat the same model/shape (S30: each object distinct
  and on-topic). Rhythm = same frame, changing content; monotony = same content; chaos = changing frame.
- Keep object SIZE within a tight band slide to slide (roughly same footprint). Wild size swings break
  the rhythm even when the center is fixed; let shape and internal detail carry the variation.

## C. Scenario / narrative arc across a sequence

- Structure as cover -> build -> payoff -> CTA. Every fast deck needs a spine the flip rides along,
  or fast advance feels random.
- COVER (slide 1): the most important asset. Stop the scroll + state the promise + open a curiosity
  gap that only the payoff closes. Hook text under ~40 characters so it lands in one glance.
  Per S30: title centered, brand mark below the hook, no sub-hook line.
- OPEN LOOP: pose the question/tension on slide 1, reveal the answer only on the payoff slide (5-7).
  The unresolved loop is what pulls the swipe (or the eye) to the end.
- BUILD (middle slides): each adds ONE new beat (new object + new line). New information every beat,
  never a restated point. Order from most surprising first if not strictly sequential.
- PAYOFF: put the single most valuable number / punchline EXCLUSIVELY on the last content slide. Do
  not leak it earlier.
- CTA: one clear CTA on the final slide. Per CLAUDE.md S30 the CTA slide reuses one of the 3 fixed 3D
  pills (OPERATOR / FOUNDER / BUILDER), keyword aligned to the pill word. Optional soft nudge mid-deck.
- Slide count: 5-7 slides is the save/share sweet spot; 8-12 max for educational. Completion drops
  hard after slide 12. Fewer strong slides beat many weak ones on a fast flip.
- Aim for completion: a deck where ~60-80% reach the last slide gets pushed by the algorithm. The arc
  is an engineering target, not decoration.

## D. Symmetry and balance of a single 3D object in its zone

- Center the object on the canvas X-axis (540px) by its true optical center, not its bounding box.
  Soft shadow/glow margins are uneven, so centering the raw crop shifts it visually; center the panel.
- Give the object a stable visual weight: it should read as grounded (sitting in the zone), not
  floating. A consistent ground shadow / base on every panel keeps the eye from re-hunting it.
- Treat the zone as a rule-of-thirds field: the object's mass sits on the central third; let detail or
  a single highlight fall near a thirds intersection rather than dead-center-flat.
- Keep one dominant axis per object (vertical panel, horizontal card) and rotate that axis slowly
  across the arc if at all; do not flip orientation every slide.
- Show the COMPLETE element, scaled, never trimmed (S30 hard rule). A cut edge breaks symmetry and
  reads as a glitch on a fast flip. If it looks cut, the crop is wrong, fix the crop.
- Balance the object against the headline: headline mass top-left, object mass center, footer mast
  bottom. This top-center-bottom triad is the fixed composition for every slide.
- The object must illustrate its OWN slide's hook (writing hook -> a writing/content panel), and be
  full-frame and distinct, never the generic seed dashboard (S30).

## E. Fast-flip-specific rules (what survives a 0.5-1s glance)

- A frame on screen ~0.5-1s allows ONE fixation: one shape + one bold word + one accent. Anything
  needing a second look is wasted. Design each slide to be "gotten" in under one second.
- Text budget per slide: a headline readable in ~1s. Keep it to one short line (ideally < 6-8 words,
  cover < 40 chars). Reels best practice is 1-2s per text element; at 0.5s you must be even tighter.
- Position continuity beats content: because the eye tracks the last position, keeping the anchor
  fixed lets the viewer read the NEW word instantly instead of re-locating it. Movement of a fixed
  element costs a whole fixation.
- Common-fate / continuity: keep any implied motion or reading direction consistent (left-to-right,
  top-to-bottom) across slides so the frames feel like one moving scene, not cuts.
- No fine print, no dense tables meant to be read on a fast slide (dense is for LinkedIn single-image,
  S27). On a flip, density = an object with rich internal texture the eye reads as "substantial,"
  not literal rows to parse.
- One accent action per slide (one glowing element, one highlighted value). Two glows split the
  fixation and nothing registers.
- Re-earn the glance every slide: swipe/attention drops fast (median card1->card2 ~62%, ~22% by
  card 5 on ad carousels). The fixed frame + one fresh object is how you keep the eye from leaving.
- Add a constant swipe/advance cue (e.g. a right-edge hint or progress ticks) in the SAME spot on
  every slide so orientation never costs a fixation.

## F. Color / contrast accent rhythm

- Background, ivory text and footer color are CONSTANT on every slide. Only the accent moves the eye.
- Accent rhythm: rotate the warm accent across the Dark Ultron set (--book #CC785C, --book-dark
  #C84623, --kraft #D4A27F) by SECTION/beat, not randomly (matches S27 "different palette accent per
  section"). E.g. build slides on --book, the payoff slide on --book-dark for a contrast pop.
- Exactly ONE high-contrast hit per slide: the headline keyword OR the object's live value in accent,
  never both maxed. The single hottest pixel is where the eye lands first, control it.
- Keep contrast ratio of headline-on-charcoal high and identical every slide (ivory #FAFAF7 on
  #191919). Do not dim the headline on some slides; constant contrast = constant readability at speed.
- Accent area should be roughly constant frame to frame (small, ~5-10% of the slide). A slide that
  suddenly floods with accent breaks the rhythm and reads as a different brand.
- Reserve the strongest accent (--book-dark) for the payoff and the CTA pill so color itself signals
  "this is the moment," reinforcing the arc.
- No forbidden colors (S7): no neon orange, green, saturated red, peach, purple, blue (logo blue
  excepted). Off-palette on one slide shatters the binding.

## Apply checklist (run before exporting a fast-flip deck)

- [ ] Eyebrow top, headline baseline, object center (540px X + fixed Y), footer baseline IDENTICAL on every slide
- [ ] Only the object + headline words change slide to slide; type sizes/colors/positions constant
- [ ] Object centered by optical center, grounded, COMPLETE (never trimmed), fills the zone (no airy gap)
- [ ] No two consecutive slides repeat the same object model; each object matches its own hook
- [ ] Arc present: cover (hook < 40 chars, open loop) -> build (1 new beat each) -> payoff (best number, last) -> CTA pill
- [ ] 5-7 slides (max 12); designed so most viewers reach the end
- [ ] Each slide readable in one ~0.5-1s fixation: one shape, one bold word, one accent
- [ ] One accent hit per slide; accent rotates by beat; payoff/CTA on --book-dark
- [ ] Constant background/border/charcoal + constant ivory headline contrast on every slide
- [ ] Safe band respected (top 300 / bottom 330 / left 70 / right 130), 1920 canvas kept, 8pt grid
- [ ] Constant swipe/advance cue in the same spot every slide
- [ ] grep -nE '-|-|...' clean (no em/en dash or ellipsis char); DM Sans/DM Mono only; no forbidden colors

## Sources

- TryMyPost, Instagram Carousel Algorithm 2026: https://www.trymypost.com/blog/instagram-carousel-algorithm-2026-guide
- UseVisuals, Best Grid Systems for Social Media Templates: https://usevisuals.com/blog/best-grid-systems-social-media-templates
- Evolve, From Rotation to Swipe: the hidden logic of carousel design: https://medium.com/@evolvebypaperclip/from-rotation-to-swipe-the-hidden-logic-of-carousel-design-be2eace326ff
- Marketing Agent, Mastering Instagram Carousel Strategy 2026 (swipes not scrolls): https://marketingagent.blog/2026/01/03/mastering-instagram-carousel-strategy-in-2026-the-algorithm-demands-swipes-not-just-scrolls/
- Toptal, Gestalt Principles for UI/UX: https://www.toptal.com/designers/ui/gestalt-principles-of-design
- NCBI, The perceived stability of scenes: serial dependence in ensemble representations: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5434007/
- OpusClip, Ideal Instagram Reels Length and Format for Retention: https://www.opus.pro/blog/ideal-instagram-reels-length
- MotionEdits, The Art of Pacing: https://motionedits.com/the-art-of-pacing-how-we-edit-for-maximum-engagement/
- Larry Jordan, Nailing Down the Anchor Point: https://larryjordan.com/articles/nailing-down-the-anchor-point-in-final-cut-pro/
