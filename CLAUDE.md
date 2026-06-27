# CLAUDE.md — Ultron Content Operating Config

> Binding config for this repo. Adapted from the Ultron Teams workspace system prompt
> (exported from a previous personal-git session) and rebuilt for **this** environment.
> Active brand system: **Dark Ultron** (primary) + **REALNUMBERS** (parallel, lead magnets).
> Single deviation from the source config: **canvas is 1080×1450px** (see §9).
> Last rebuilt: 2026-06-01

---

## 0. GOVERNANCE (read first)

These meta-rules sit above everything else in this file:

1. **Any rule here can be overridden** by the operator's explicit request, typically off the
   back of a temporary analysis we run together. **Once a rule is rewritten, the new version
   becomes the single source of truth** and is the only rule in force until changed again.
   Update this file when that happens — do not keep stale rules around.
2. **Propose before executing.** For every generated material (poster, caption, PDF, etc.),
   surface the improvements you'd make and get a go-ahead before producing the final output.
3. **Fix one element at a time.** When asked to fix something specific, change only that — never
   touch unrelated elements in the same pass.
4. **Blunt, direct communication.** Push back on generic, salesy, or off-brand output. No hedging.
5. **`content/tokens.css` is LEGACY**, not the binding palette. It uses Inter/JetBrains/Fraunces +
   `#D97757` + a 1450 reference, which conflicts with Dark Ultron. The binding tokens are the
   Dark Ultron CSS variables in §7. Do not import `tokens.css` into new posters.
6. **The 72 uploaded materials predate this config.** They use forbidden fonts (Inter/Fraunces/
   JetBrains/Bricolage/etc.), `#D97757`, and were built at 1450px. Treat them as **rebuild
   candidates** to the Dark Ultron standard (keeping 1450px), not as the brand reference.

---

## 1. PROJECT CONTEXT

**Ultron** is an AI-powered GTM operating system for founders. URL: 51ultron.com · App: app.51ultron.com.

**Founder & operator:** Tibi Serbaneci (CEO Ultron, NexityNetwork). Co-founder Catalin Fetean. InnovX accelerator cohort.

**Seven Ultron agents** (each callable by name with a slash command, or auto-routed):
- **CORTEX** (`/cortex`) — research: profiles people, companies and markets into one ranked brief
- **SPECTER** (`/specter`) — outbound: cold emails, follow-ups and multi-step sequences
- **STRIKER** (`/striker`) — deals: qualification, discovery, objection handling, proposals, close plans
- **PULSE** (`/pulse`) — content: posts, launches, newsletters and thought-leadership in your voice
- **SENTINEL** (`/sentinel`) — code: reads, writes, tests and ships code, opens the PR
- **AMPLIFY** (`/amplify`) — publishing: formats and schedules each asset per channel and time zone
- **COUNSEL** (`/counsel`) — legal: drafts and reviews NDAs, MSAs and term sheets, flags risk

Plus the **ROUTER** (the composer): type plain English and it routes to the agent that owns the job, picks the model tier, and lets agents hand off to and compose with each other.
Plus **HUMAN GATE**: human approval before anything sends.

**Model tiers (the router picks one per turn):** Lite = Haiku (quick lookups), Smart = Sonnet (default), Deep = Opus (hard judgement). Free plan = Lite only; paid = credits via OpenRouter.

> Roster updated 2026-06-04 (operator-confirmed): supersedes the earlier five-agent list (CORTEX=ICP / SPECTER=research / PULSE=routing). PULSE is now the content agent; the ROUTER does routing and model selection.

**Pricing tiers:**
- Starter: free
- Max: $19/mo + pay-as-you-go AI credits
- Enterprise: $297/mo per user

**Tech stack:** Next.js, Supabase, Vercel, Claude/Anthropic as AI backbone, OpenRouter as middleware for per-user credit provisioning.

**Confirmed resources (real links — do NOT invent others):**
- app.51ultron.com/resources
- app.51ultron.com/resources#blueprints
- app.51ultron.com/techniques
- app.51ultron.com/docs
- app.51ultron.com/docs/architecture
- app.51ultron.com/enterprise
- app.51ultron.com/bcp
- app.51ultron.com/creators
- work.51ultron.com/calculator

**Confirmed ICP (90-day analytics):** Founder/Co-Founder/CEO at 2–50 employee companies, IT services / software / consulting, US and UK.

---

## 2. GIT WORKFLOW (rebuilt for this environment)

> **STORAGE MOVED TO MONOLITH (operator, 2026-06-24 — binding, per §0.1; supersedes the GitHub
> Pages / `main` publishing rule below and the portal auto-push rules in §29):** material storage is
> now **exclusively the Monolith account vault** — Cloudflare D1 `opencut-vault` (binding `VAULT_DB`),
> owner `x5SELCqkIRk7HmZmJrQGzrgRP9hSzxk3` = **tiberiu@nexitynetwork.org**, media in R2
> `ultron-reels/imports/`. Items are tagged by channel: **LinkedIn / TikTok / Instagram**, titles
> status-marked (`Posted …` / `Review …` / `Revision …`), caption = caption + first comment (ALT
> dropped). The GitHub Pages portal + Codespace auto-push are **disabled** (they cost money and were
> unreliable) — do **not** run the always-on portal or push its manifest. The cost was the *hosted
> portal* (Codespace compute + Pages), NOT plain repo commits. **Every material built IS committed to
> the work branch as a reference/model copy (operator, 2026-06-24): the git repo is the reference
> archive; the Monolith vault is the live library.** New builds: wire the asset into the vault (R2 +
> `vault_items`) AND commit the source (HTML/PNG/caption) to the work branch so it exists as a model.

This repo is **not** the old personal `ultron-content` repo. The original config referenced
`tiberiuserbaneci/ultron-content`, a remote named `ultron-content`, and a `GH_PAT` env var —
**none of that applies here.** Use the values below.

- **Repo:** `NexityNetwork/tiberiu-claude`
- **Remote:** `origin` (managed by the Claude Code web environment via local proxy — **no PAT, no token to set or commit**)
- **Work branch:** `claude/epic-davinci-eGOGS` — develop here
- **`main`:** holds the reference content (the 72 uploaded materials live in `content/`)
- **Push:** `git push -u origin <branch-name>` (retry with backoff on network errors only)
- **To main:** the operator authorized publishing to `main` (2026-06-12) — `main` is the branch
  **GitHub Pages serves** (the always-on secure portal + the materials its downloads point to).
  Develop on the work branch, then fast-forward / merge to `main` to publish. Still no PR unless asked.
- **PRs:** do not open a PR unless explicitly asked

There is no token to provision. Do not add remotes for, or attempt to reach, any other repo —
this session is scoped to `NexityNetwork/tiberiu-claude` only.

---

## 3. FILE STRUCTURE

**Current (actual) layout** — flat, everything in `content/`:

```
content/
├── script-XX-linkedin-vN.html      # LinkedIn posters
├── script-XX-tiktok.html           # TikTok posters
├── docs-XX-[topic]-linkedin-vN.html# Docs Series posters
├── logos-reference.html            # logo reference sheet
├── tokens.css                      # LEGACY token set — do not use (see §0.5)
├── ultron-logo.png                 # real Ultron logo (base64-inline it for exports, see §7)
├── script-22/23/24-*.png           # exported PNGs
└── .gitkeep
```

**Target organization** (config's intended structure — adopt only when the operator asks; do NOT
reorganize the 72 files unilaterally):

```
content/
├── html/        # posters
├── captions/    # script-XX-caption.md
├── ig/          # highlights/ (6 covers 1080x1920) + stories/ (6 stories 1080x1920)
├── pdfs/        # lead-magnet PDFs (REALNUMBERS)
└── assets/      # logo + shared assets
```

**Dimensions:**
- LinkedIn portrait: **1080×1450px** (operator standard for this project)
- Instagram story / IG highlight cover: **1080×1920px**
- TikTok poster: **1080×1920px**

**Universal scaler (in every poster HTML), tuned for 1450px:**
```css
.scaler>.canvas{
  transform-origin:top center;
  transform:scale(calc(min(100vw / 1130, (100vh - 48px) / 1510)));
}
```

---

## 4. POSTED SCRIPTS — DO NOT REDESIGN

- **Series 1 posted (no redesign):** 02, 06, 10, 19, 24
- **Series 2 posted (no redesign):** 15, 23, 26, 37
- **Active in production:** REALNUMBERS campaign (20 posts total).

---

## 5. REALNUMBERS CAMPAIGN

**Activation safety word:** REALNUMBERS

**Structure: 20 posts** = 10 (Template A) + 4 (Template B) + 6 (Template C)
- **Template A:** dark text hero (10 posts)
- **Template B:** infographic + optional quote zone (4 posts)
- **Template C:** carousel PDF (6 posts)

**6 thematic tags:**
1. AGENT MATH
2. FOUNDER PAIN
3. GTM TRUTH
4. TOOL AUDIT
5. REAL NUMBERS
6. PRICING LAW

**4 voices:** GTM / AI / Founder / Pain — all framed "I…" (operator debrief).

**Campaign routing:**
- **6 lead-magnet posts** (triggers: STACK / FOCUS / AUDIT / ICP / 100) → PDF
- **14 direct-Ultron posts** (agents: CORTEX / SPECTER / STRIKER / PULSE / SENTINEL / AMPLIFY / COUNSEL)
- **Post 17 EXCLUDED** from campaign

**CTA rule:** never reference invented documents. Only real links to confirmed Ultron techniques or lead-magnet PDFs that already exist.

---

## 6. CTA KEYWORDS

| Script | Keyword | Script | Keyword |
|--------|---------|--------|---------|
| 01 | OPERATOR | 14 | MANIFESTO |
| 02 | SIGNAL | 27 | GTM |
| 03 | STACK | 29 | CYCLE |
| 04 | TOOLS | 33 | RIVAL |
| 05 | SDR | 36 | OVERNIGHT |
| 06 | FUNNEL | 41 | **WINNERS** |
| 07 | GATE | 53 | PROOF |
| 08 | DECAY | 54 | KILL |
| 09 | LEVELS | docs-01 | ENGINE |
| 10 | ICP | | |
| 11 | AGENTS | | |
| 12 | COMPOUND | | |
| 13 | ACTIVITY | | |

**REALNUMBERS lead-magnet keywords:** STACK / FOCUS / AUDIT / ICP / 100 / RESOURCES / SIGNAL / INBOX / PROMPTS / TOKENS — all route to `app.51ultron.com/resources` or `app.51ultron.com/techniques` depending on post theme.

**CTA rules:**
- Keyword in CAPS, the rest lowercase
- CTA ends with "connect" to enable DM capability
- Links **never** in post body — first comment only
- Calculator: work.51ultron.com/calculator
- Short.io for shortlinks (e.g. 51ultron.com/stack/)

---

## 7. BRAND SYSTEM — DARK ULTRON (primary)

The system for LinkedIn posts, Instagram highlights/stories, and docs visuals.

### Colors (CSS variables — these are the binding tokens)
```css
:root{
  --slate-dark:  #191919;     /* canvas background */
  --slate-med:   #262625;     /* card backgrounds */
  --ivory-light: #FAFAF7;     /* text primary */
  --book:        #CC785C;     /* accent primary - Book Cloth */
  --book-dark:   #C84623;     /* accent strong */
  --kraft:       #D4A27F;     /* accent secondary warm */
  --cloud-med:   #919180;     /* muted text */

  /* opacity variants */
  --book-lo: rgba(204,120,92,.10);
  --book-bd: rgba(204,120,92,.32);
  --ink-70:  rgba(250,250,247,.72);
  --ink-46:  rgba(250,250,247,.46);
  --ink-30:  rgba(250,250,247,.30);
  --ink-14:  rgba(250,250,247,.14);
  --rule:    rgba(250,250,247,.10);
  --kraft-lo:rgba(212,162,127,.10);
  --kraft-bd:rgba(212,162,127,.30);
}
```

**FORBIDDEN in Dark Ultron:** orange neon (#ff801f, #ed7f4a), green (#4ade80, #76d39a), saturated red (#c0392b), peach (#ffe0c2), purple, blue (exception: the Ultron logo, which has blue in the sphere).

### Typography
**Only accepted family:**
```
@import 'https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700;9..40,800;9..40,900&family=DM+Mono:wght@400;500&display=swap'
```

- **DM Sans 400/500/700/800/900** — all text (hooks, body, labels, numbers)
- **DM Mono 400/500** — mast/footer labels, monospace meta, tags

**FORBIDDEN:** Fraunces, Inter, Inter Tight, Instrument Serif, Bricolage Grotesque, JetBrains Mono, Space Grotesk, Caveat, Kalam, Arial, Roboto, Helvetica.

### Background textures
```css
/* Dot grid */
.canvas::before{
  content:'';position:absolute;inset:0;pointer-events:none;z-index:0;
  background-image:radial-gradient(rgba(204,120,92,.05) 1.2px,transparent 1.3px);
  background-size:26px 26px;
}
/* Atmospheric warm glow */
.atm{
  position:absolute;inset:0;pointer-events:none;z-index:1;
  background:
    radial-gradient(ellipse 60% 40% at 92% 2%,rgba(204,120,92,.16) 0%,transparent 64%),
    radial-gradient(ellipse 44% 30% at 6% 99%,rgba(212,162,127,.08) 0%,transparent 62%);
}
```

### Ultron logo (PNG, base64 embedded)
Real logo = blue/orange sphere on black. Source file in this repo: **`content/ultron-logo.png`**.
Exports run headless and external URLs 403, so the logo must be **base64-inlined**:
```html
<img src="data:image/png;base64,[BASE64_OF_ultron-logo.png]" class="ftr-logo">
```
Workflow: read `content/ultron-logo.png`, base64-encode it, substitute it into the `LOGO_URI`
token in the poster before export. (The old config kept this in `content/assets/logo-b64.txt`;
here the source of truth is the PNG itself — generate the base64 from it on demand.)

**Fallback gradient (only if the PNG is unavailable):**
```css
background:
  radial-gradient(circle at 72% 22%,rgba(255,140,80,.95) 0%,rgba(220,80,30,.3) 22%,transparent 36%),
  radial-gradient(circle at 22% 76%,rgba(55,170,255,.95) 0%,rgba(30,130,220,.3) 22%,transparent 38%),
  radial-gradient(circle at 38% 38%,rgba(30,30,50,1) 0%,#060810 55%,#000 100%);
```

### Claude logo (SVG embedded)
Claude sunburst logo for posts where Claude is the main mention. Full SVG path stored in the
template. 115–130px in hero, bottom-right, drop-shadow:
```css
.hero-claude{
  position:absolute;bottom:0;right:0;
  width:115px;height:115px;z-index:3;
  filter:drop-shadow(0 0 24px rgba(204,120,92,.45));
}
```

> See `content/logos-reference.html` for the logo reference sheet.

---

## 8. BRAND SYSTEM — REALNUMBERS (parallel, for lead magnets)

Light system for lead-magnet PDFs and PDF carousels. Coexists with Dark Ultron, does NOT replace it.

### Colors
- **Cream:** `#F5ECE3` (primary bg)
- **Dark orange:** `#BE4628`
- **Ultron orange:** `#C84623`
- **Editorial orange:** `#D26446`
- **Dark:** `#111`
- Background alternatives: `#EFEBE0` / `#FAF9F7` (lightest)

### Typography
- **DM Sans** for editorial
- **DM Mono / JetBrains Mono** for REALNUMBERS asset meta

### Components
- **Browser frame** mockup with `app.51ultron.com` as the URL bar
- **Grid + noise overlay**
- **Footer with border accent**
- All with the Ultron logo embedded

### REALNUMBERS output checklist
Each REALNUMBERS visual includes:
1. HTML visual
2. Caption
3. First comment
4. ALT text
5. DM template

---

## 9. CANVAS & LAYOUT RULES

### Dimensions (STRICT)
- LinkedIn portrait: **1080 × 1450px**
- Instagram story / IG cover: **1080 × 1920px**
- TikTok photo-carousel, editorial 4:5 format: **1080 × 1350px** (operator, 2026-06-12 — the
  top-performer reference format; filenames carry `-45-` or `editorial45` so the guard targets
  1350; photo mode has no 300px safe-zone inset, keep ~90px side padding; bottom-bleed visuals
  are part of the format, dims are checked on the canvas box)

### Safe zones — vertical 1080×1920 (TikTok / IG story) (operator, 2026-06-04 — binding)
TikTok and IG overlay their UI on every edge of the frame. Keep ALL content inside this safe box.
The mast/title must sit BELOW the top inset. `top:150px` was too small (top tabs covered the mast); `top:250px` still let the TikTok search/header bar cover the carousel header (operator, 2026-06-10), so the inset is now 300px.
- **top: 300px** (status bar + For You / Following tabs + search/header bar; 250 was confirmed covering the carousel header)
- right: 130px (the like / comment / share rail)
- bottom: 330px (caption, username, progress bar)
- left: 70px
```css
.safe{position:absolute;top:300px;left:70px;right:130px;bottom:330px;display:flex;flex-direction:column;}
```
Every vertical carousel slide and story uses these insets. Pre-flight: verify the mast top ≥ 300px before export.

**Canvas vs visible band (operator, 2026-06-10 — binding):** the canvas MUST stay 1080×1920. 9:16 is the TikTok/IG upload format; anything shorter gets cropped or letterboxed unpredictably. Content is NOT spread across the full 1920 - it lives only inside the safe box, a visible band of about **1080×1290** after the 300 top / 330 bottom insets. Design to that band; keep the 1920 canvas. Research basis: TikTok organic safe area is roughly 960×1386 centered, top UI band ~200px, right rail ~120px, bottom caption/CTA ~330–480px.

### Canvas CSS base
```css
.canvas{
  width:1080px;height:1450px;
  background:var(--slate-dark);
  padding:30px 44px 22px 44px;
  display:flex;flex-direction:column;
  position:relative;overflow:hidden;
}
```

### Padding budget (1450px)
- Vertical available: 1450 − 30 − 22 = **1398px** for content
- Horizontal: 1080 − 44 − 44 = **992px** for content
- Mandatory CSS comment at top, e.g.:
  `/* BUDGET: 1398px vertical — sections: mast 24 + hero 240 + grid 384 + ... = 1398 */`

### Flex layout — dead-space rule
- **Exactly one dominant section** per poster with `flex-grow:1; min-height:0`
- **Everything else:** `flex-shrink:0`
- **Never** `flex-grow:1` on two sibling sections
- Absorb bottom space with `margin-top:auto` on the stat-strip or equivalent
- Variable-content grids: either fixed height or `justify-content:space-between`
- Cards as `display:flex;flex-direction:column;gap:Xpx` with `margin-top:auto` on the card foot to pin it to the bottom

### Pre-flight checklist (mandatory before any export)
1. `grep -nE '—|–' file.html` → 0 results (NO em/en dashes)
2. Footer visible, single row, logo + URL present
3. Mast: single row, keywords left, meta right
4. Total container height = exactly **1450px** (verify with `scrollHeight` in Playwright)
5. Budget CSS comment written and respected
6. All fonts are DM Sans / DM Mono (REALNUMBERS exception aside)
7. All colors from the Dark Ultron palette (or REALNUMBERS)

---

## 10. HEADER (mast) — standard

```css
.mast{
  flex-shrink:0;display:flex;align-items:center;justify-content:space-between;
  padding-bottom:12px;border-bottom:1px solid var(--rule);
}
.mast-kw{
  font-family:'DM Mono',monospace;font-size:9.5px;font-weight:500;
  letter-spacing:.18em;text-transform:uppercase;
  color:var(--ink-46);white-space:nowrap;overflow:hidden;line-height:1;
}
.mast-kw .sep{color:var(--book);margin:0 7px;}
.mast-r{
  font-family:'DM Mono',monospace;font-size:9.5px;font-weight:500;
  letter-spacing:.16em;text-transform:uppercase;color:var(--ink-70);
  white-space:nowrap;flex-shrink:0;padding-left:18px;
}
.mast-r em{color:var(--book);font-style:normal;}
```

**Mast rules:**
- Single row. Border-bottom on `.mast` directly (NOT a separate `.mast-rule` div)
- Keywords left: topic keywords (AI OUTBOUND, FOUNDER GTM, AI AGENTS, COLD EMAIL, etc.). NEVER script number / post count / session duration
- Meta right: SCRIPT XX / N=XXX / TIMEFRAME
- NEVER a second row under the mast (no eyebrow line, no hero-eye in mast)
- Separator: `<span class="sep">·</span>` (middle dot, NOT em-dash)

---

## 11. FOOTER — standard

```css
.ftr{
  flex-shrink:0;margin-top:12px;padding-top:12px;
  border-top:1px solid var(--rule);
  display:flex;align-items:center;justify-content:space-between;gap:16px;
}
.ftr-l{display:flex;align-items:center;gap:11px;min-width:0;}
.ftr-logo{width:30px;height:30px;border-radius:50%;object-fit:cover;flex-shrink:0;}
.ftr-txt{
  font-family:'DM Mono',monospace;font-size:9.5px;font-weight:400;
  letter-spacing:.14em;text-transform:uppercase;color:var(--ink-70);
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
}
.ftr-txt strong{color:var(--ivory-light);font-weight:500;}
.ftr-url{
  font-family:'DM Sans',sans-serif;font-weight:900;
  font-size:15px;letter-spacing:-.4px;color:var(--ivory-light);flex-shrink:0;
}
.ftr-url em{color:var(--book);font-style:normal;}
```

**Footer rules:**
- Single row: Ultron logo left + brand text + URL `51ultron.com` right
- URL syntax: `51ultron<em>.</em>com` (dot in book color)
- NEVER a keyword strip in the footer
- NEVER two rows
- Brand text format: `<strong>ULTRON</strong> · AI OPERATOR FOR FOUNDERS · [CONTEXT]`

---

## 12. CTA chip — standard

```css
.cta-block{
  flex-shrink:0;margin-top:12px;
  display:flex;align-items:stretch;
  border:1px solid var(--book);border-radius:4px;overflow:hidden;
}
.cta-txt{
  flex:1;padding:14px 18px;
  display:flex;flex-direction:column;justify-content:center;gap:5px;
  background:rgba(204,120,92,.07);
}
.cta-l{
  font-family:'DM Sans',sans-serif;
  font-size:13.5px;font-weight:500;color:rgba(250,250,247,.82);line-height:1.35;
}
.cta-l strong{color:var(--ivory-light);font-weight:800;}
.cta-chip{
  flex-shrink:0;padding:0 24px;gap:9px;
  background:var(--book);
  display:flex;align-items:center;
  font-family:'DM Sans',sans-serif;
  font-size:14px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;
  color:#1a0f0a;
  box-shadow:inset 0 0 0 1px rgba(250,255,247,.12), 0 0 30px rgba(204,120,92,.35);
}
.cta-chip svg{width:17px;height:17px;stroke:#1a0f0a;stroke-width:2.6;fill:none;stroke-linecap:round;stroke-linejoin:round;}
```

**CTA chip content:**
- Solid Book Cloth chip with arrow `→` (SVG arrow)
- Text format: `COMMENT [KEYWORD]` with arrow
- Book Cloth glow drop shadow

---

## 13. SCORING FRAMEWORK (GO/REBUILD decision)

Before publishing any poster, score on 4 dimensions, each /100:

| Dimension | Checks |
|-----------|--------|
| **Virality** | Scroll-stop hook in the first 2 lines of the LinkedIn preview |
| **Save-Worthy** | Reader can concretely implement something from it (saves = #1 algorithm signal) |
| **Visual** | Brand consistency, clear hierarchy, zero dead space, exactly 1450px |
| **System Thinking** | Real numbers, specifically named tools, numbered layers with validation |

**Publish threshold: minimum 70/100 overall.**

Off-brand outputs with the wrong palette score 73–79. Dark Ultron implemented correctly scores 90+.

**GO/REBUILD logic:**
- 90+: GO directly
- 80–89: GO with minor adjustments
- 70–79: REBUILD — probably off-brand or weak hook
- <70: full REBUILD

---

## 14. HOOK STYLES (4 proven techniques)

### Style A: Operator Confession
"I [verb past]. I expected X. Y happened."
Example: "I told Claude to write 200 cold emails. I expected 50 to convert. Seven did."

### Style B: Direct contradiction (counter-intuitive)
"The [common thing] never failed. The [unexpected thing] did."
Example: "The AI never failed. 100 founders did."

### Style C: Question reframe
"Why did X happen and Y not? I read all of them to find out."

### Style D: Direct reader challenge (useful anti-pattern)
"Stop reading X. Start reading Y."
Example: "Stop reading why your cold emails failed. Start reading why the rare ones worked."

**Universal hook rules:**
- Max 12 words
- Zero statistics in the hook (numbers go in the stack/graphic, NOT in the hook text)
- Operator debrief voice ("I ran/built/killed/sent/tested")
- Do not start with "I" as the first word
- Must contain "AI" or "Claude" explicitly in the first 2 lines (algorithm + audience)

---

## 15. CAPTION / ALT TEXT / FIRST COMMENT

Complete rules for the 3 text pieces that accompany every LinkedIn poster. Write them in the
order given by the Copywriting Process (§15.4).

### 15.1 CAPTION

**Length**
- Standard: 400–470 words (model: post KILL); 2,400–2,800 characters
- NOT under 350 words (missing the context needed for save-worthy)
- NOT over 500 words (pushes past "see more", breaks continuity)

**Structure (5 mandatory blocks)**

*Block 1 — Hook text (2 lines, NOT a visual duplicate)*
- Acts as scroll-stop in the feed (the first 2 lines are the only ones visible before "see more")
- Use a different angle than the poster's visual hook; do not reuse its words
- Must contain "AI" or "Claude" explicitly in the first 2 lines (no click without visible AI)
- Pick one of the 4 caption hook styles below — NOT the same one used for the visual hook:
  - **A — Operator Confession:** "I told Claude to write 200 cold emails. I expected 50 to convert. Seven did."
  - **B — Counter-intuitive reveal:** "The 7 cold emails that booked meetings had nothing to do with copy quality."
  - **C — Number reveal not shown in the visual:** "11 minutes. That is how long Claude needed to find the pattern I spent two days hunting by hand."
  - **D — Confession + counter-intuitive mix (strongest):** "I told Claude to write 200 cold emails. I expected 50 to convert. Seven did. What those 7 had in common had nothing to do with copy quality."

*Block 2 — Context/story (3–4 sentences)*
- Why you ran the experiment; what you thought initially vs what you found
- Operator voice mandatory ("I ran/built/sent/tested"); establish authority, no hedging

*Block 3 — Body, numbered list with `→` (3–5 items)*
- Each starts with `→` and describes one concrete behavior/pattern/finding
- Specific numbers in each (exact figures, NOT "many"/"most"); name the tools (Claude, SPECTER, STRIKER, etc.)
- Sequencing: most surprising finding first

*Block 4 — Bridge insight*
- 2–3 sentences linking the findings to an underlying lesson
- Do NOT repeat the findings — extract the principle; connect to product/system subtly (no hard sell)

*Block 5 — Fixed CTA (exactly this form)*
```
Follow for one AI system for founders every day.
Comment [KEYWORD] and I will send you the exact Claude [workflow/audit prompt/system] we used.
```

**Visual separators**
- Between blocks: `- - -` (three standard-keyboard dashes, NOT em-dashes)
- Body items: `→` arrows; sub-list bullets `•` (rare); NO emoji
- NO bold/italic markdown (LinkedIn does not render it)

**Punctuation** (see also §21): standard keyboard characters only; "every day" not "every week";
"Claude workflow"/"Claude audit prompt"/"Claude system" not generic "prompt"/"framework";
"It will" not "it might"; "Most teams" not "some teams".

**Caption anti-patterns (do NOT)**
- Generic hook that says nothing ("Here is what I learned about AI")
- Caption hook duplicating the visual hook
- List of 8+ items (max 5); fictional quotes attributed to others; mentioning unreal products
- Promising an invented PDF/document (the CTA points only to confirmed lead magnets)
- Hedging language; starting the hook with "I"; statistics in the hook; emoji; hashtags in the body (the §15.6 five-set on the last line is allowed)

### 15.2 ALT TEXT

Structural description of the poster for accessibility + the LinkedIn algorithm.

**Length:** 80–150 words, one continuous paragraph (not under 60, not over 200 — LinkedIn truncates).

**Structure (in order)**
1. **Open:** theme + palette (1 sentence) — e.g. "Dark editorial visual on slate background."
2. **Hero** (2–3 sentences): the layout (3-up stack / text-led / split-screen / funnel), key numbers with their roles, the visual hook quoted in single quotes, Claude logo present/absent
3. **Body sections** (2–3 sentences): main sections in visual order, key numbers/patterns — only what communicates the visual jump, not everything
4. **Footer/CTA closure** (1 sentence): "Closes with a Comment [KEYWORD] call to action and the Ultron logo."

**ALT rules**
- Use Ultron color names (book-orange, kraft, slate, ivory), NOT hex codes
- Quote numbers exactly, not rounded; visual hook in single quotes `'...'` (not double)
- No emotional descriptors ("striking", "powerful"); no font/CSS technical detail; no "image of…" opener

**Canonical example (script-41 final):**
> "Dark editorial visual on slate background. Hero shows a vertical stack on the left, separated by a book-orange line: the number 7 in large book-orange labeled 'Converted · Booked Meetings', the number 200 in mid-size kraft labeled 'Sent · AI Cold Emails', and 3.5 percent in white labeled 'Rate · Over 10 Days.' Headline on the right reads 'Stop reading why your cold emails failed. Start reading why the rare ones worked.' Sub-headline notes 200 emails written by Claude over 10 days, 7 turned into meetings. Claude sunburst logo bottom right. Below, a grid of 200 dots represents each send, with 7 dots highlighted in book-orange and numbered 1 to 7. Three structural pattern cards: One Specific Trigger, The Ask Is A Question Not A CTA, Fewer Than 62 Words. Closes with a Comment WINNERS call to action and the Ultron logo."

### 15.3 FIRST COMMENT

Where the links + hook restatement live. The author's first comment sits right under the post, so
it's the only place external links do NOT penalize reach.

**Length:** 3–5 sentences (40–80 words). Not under 30, not over 100 (passes the mobile fold).

**Structure (3 pieces)**
1. **Hook restatement + key stats** (1–2 sentences) — a different angle than the visual/caption hook; include the key number + Claude/tool mention
2. **Concrete lead-magnet promise** (1 sentence) — what they get if they comment; specific, not "useful stuff"
3. **Explicit CTA with the real link** (1–2 sentences) — "Drop [KEYWORD] below and I will send you…"; link as plain-text URL (LinkedIn doesn't render markdown links); points to a confirmed lead magnet, never an invented document

**First comment rules**
- Real link always — never an invented document (absolute REALNUMBERS rule)
- DM lead-magnet posts: NO link, just the trigger word ("Drop WINNERS below")
- Existing PDF lead magnet: direct link to `app.51ultron.com/...`; shortlink posts: `51ultron.com/stack/` (via Short.io)
- Two blank lines between pieces for spacing; [KEYWORD] in caps; no emoji; no hashtags

**Canonical example (script-41):**
> "200 cold emails written by Claude. 10 days. 7 booked a meeting. I read every single one looking for what the 7 winners had that the 193 failures did not.
>
> Three patterns showed up in all 7 and in zero of the 193. None of them were 'write better copy.'
>
> Drop WINNERS below and I will send you the exact Claude audit prompt I used to score the 200."

**Restricted DM workflow:** when a user comments but you cannot DM them (first-degree restriction),
approved public reply: "DM failed. Let's connect and I'll send it over."

### 15.4 COPYWRITING PROCESS (write in this order)

1. **Visual hook first** — pick style A/B/C/D (§14), max 12 words, no statistics
2. **Visual sub-hook** — put the numbers here (200 emails, 10 days, 7 meetings), 18–25 words, mention Claude/AI
3. **Caption hook (different angle)** — different from the visual hook, use one of the remaining 3 styles, 2 lines max
4. **Caption body (Blocks 2–4)** — Context → Findings (`→` list) → Bridge
5. **Fixed CTA (Block 5)** — copy the standard form, change only [KEYWORD] and workflow/prompt/system
6. **ALT text** — after the visual is final; structural, with the exact numbers from the visual
7. **First comment last** — a different angle than the caption hook; add the real link or DM trigger
8. **Pre-flight** — `grep -nE '—|–|…' *.md *.html` → 0 results; confirm the 3 hooks (visual/caption/first comment) are worded differently; [KEYWORD] consistent across all 3; first-comment link is real

### 15.5 TEXT-PIECE CHECKLIST (caption + ALT + first comment)

- [ ] Caption 400–470 words; 5 blocks (Hook / Context / Body `→` / Bridge / CTA)
- [ ] Caption hook DIFFERENT from the visual hook; contains "AI"/"Claude" in the first 2 lines; does not start with "I"
- [ ] Block 3 has 3–5 `→` items with exact numbers
- [ ] Fixed CTA exact: "Follow for one AI system for founders every day. Comment [KEYWORD]…"
- [ ] ALT text 80–150 words, structural, exact numbers, Ultron color names
- [ ] First comment 40–80 words, 3 pieces, real link OR DM trigger (never an invented document), different angle than caption hook
- [ ] [KEYWORD] consistent across caption + first comment + visual
- [ ] `grep -nE '—|–|…' file.md` → 0 results; zero emoji and markdown; hashtags only the §15.6 five-set on the last line

---

### 15.6 SOCIAL CAPTION FORMAT + HASHTAGS (operator, 2026-06-04 — binding; supersedes the hashtag bans elsewhere in this file)

**Paragraph format (TikTok and any social caption):** one beat per paragraph, 1–2 sentences max,
a blank line between every paragraph (scannable, 360Brew style).

**CTA-FIRST (operator, 2026-06-19 — binding, per §0.1; supersedes the earlier CTA-last order below):**
**Every TikTok caption OPENS with the CTA on line 1**, in the exact form
`Comment KEYWORD and I will send you [the specific asset].` Then the body, then hashtags last.
Order:
1. CTA — "Comment KEYWORD and I will send you…" — **the first line, always**
2. Hook — the reframe, its own paragraph ("Most people X." / "You X. Operators Y.")
3. The shift — "Now I…" (1–2 sentences)
4. Setup — one line
5. Body — the dense mechanics paragraph OR itemized beats ("Label: one-line description", one per paragraph)
6. Closing punch — a short imperative ("Stop running Claude on default.") OR the product line ("This is X on the Ultron platform…")
7. Hashtags — the last line

**HASHTAGS — exactly 5, only these, no more, no fewer, no substitutes:**
`#claude #ai #founder #startup #buildinpublic`
Broad tags shared across TikTok, Twitter and LinkedIn. NEVER niche tags (#aiagents, #anthropic,
#gtm, #saas, #aiworkflow, #claudeai, etc.). NEVER in the body — only the last line. Emoji still forbidden.

---

## 16. PROVEN LAYOUTS (active templates)

### Layout 1: Hero 3-up stack (script-41)
Hero left: 3 numbers stacked vertically with a book border-left.
- Large number in book (the result)
- Medium number in kraft (scale)
- Small number in ivory (rate)
Typographic hook on the right + sub-hook.

### Layout 2: Hero text-led (decision map, script-53 final)
Huge 88px ivory hook with a book accent on the key word + 48px kraft sub-stat.
- Use when you want maximum scroll-stop on pure text
- No hero image, just text + Claude logo bottom-right

### Layout 3: Hero hub + nodes (decision map)
Hero number + rotated vertical label + horizontal label + diagram below.

### Layout 4: Funnel / process diagram
- 100/200 founders/runs at the top
- Branches via SVG connectors
- 3 outcome cards at the bottom with dominant numbers
- Best for cohort analysis, GTM postmortems

### Layout 5: Dot-grid evidence (200 dots, 7 highlighted — script-41)
- Use ONLY when the grid communicates scale + rare events
- Do NOT repeat this layout if a recent material already used it

### Layout 6: Split-screen comparison (rejected for script-53)
- Number left vs number right with a vertical VS
- For direct contrast, but the **kicker must be ABOVE the split, not below it**

---

## 17. INSTAGRAM HIGHLIGHTS SYSTEM

6 highlights covers + 6 info-dense stories for the `tiberiu.ai` profile.

### Highlights covers (1080×1920)
Specs:
- WHITE background `#FFFFFF` (NOT slate — Instagram crops circular on white)
- Large liquid-glass circle (720px) with premium effect:
  - Interior cream radial gradient
  - Specular highlight top-left
  - Warm bounce right
  - Warm rim shadow bottom
  - Exterior 3D drop shadow
- Book Cloth icon inside with a vertical 3D gradient (light top → deep bottom)
- Top-edge highlight on edges (gloss overlay)
- Darkened side faces (book-side)
- Layered drop shadow under the icon

### 6 highlights mapping
| Highlight | URL | Icon |
|-----------|-----|------|
| BLUEPRINTS | app.51ultron.com/resources#blueprints | 5-block architectural grid |
| DOCS | app.51ultron.com/docs | Document with corner fold (Ultron-logo gradient) |
| ENTERPRISE | app.51ultron.com/enterprise | 2 corporate 3D towers with windows |
| TECHNIQUES | app.51ultron.com/techniques | 3 sparkles/stars (techniques = insights) |
| BCP | app.51ultron.com/bcp | Central hub + 6 orbital nodes (identity layer) |
| CREATORS | app.51ultron.com/creators | 3 numbered circles 1-2-3 (Create/Post/Get paid) |

**BCP NOTE:** BCP = **Business Common Profile** (directory layer for the agentic web). NOT "Business Continuity Plan". Icon is hub-and-spokes, NOT a shield.

**CREATORS NOTE:** UGC fidelization program (Create → Post → Get paid). Icon is a 1-2-3 process, NOT a camera.

### Stories (1080×1920, info-dense)
Same slate background as the LinkedIn posters (consistency).
Layout:
- Small icon at top + eyebrow (highlight name in DM Mono)
- Huge title (110px) + book accent on the key word
- 3 numbered bullets with a book border-left
- Solid book CTA chip at the bottom with arrow: `OPEN [NAME] →`
- TAP hint: `TAP → 51ULTRON.COM/[name]`

### Instagram workflow
1. Upload the matching story
2. Add Link Sticker → paste URL
3. Position the link sticker over the orange "OPEN [NAME] →" chip
4. Post the story
5. Highlights → Edit Cover → upload from ig/highlights/
6. Name the highlight (max 16 chars)

---

## 18. PLAYWRIGHT EXPORT WORKFLOW

Export PNG/PDF from HTML with headless Chromium (Playwright).

### PNG export (1080×1450 LinkedIn / 1080×1920 Instagram)
```python
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width':1080,'height':1450}, device_scale_factor=2)
    pg.goto('file:///home/user/tiberiu-claude/content/poster.html')
    pg.wait_for_timeout(1800)
    pg.eval_on_selector('#export-bar','e=>e.style.display="none"')
    pg.eval_on_selector('.scaler>.canvas','e=>e.style.transform="none"')
    pg.eval_on_selector('body','e=>e.style.padding="0"')
    pg.locator('#artifact').screenshot(path='output.png')
    b.close()
```

### Multi-page PDF carousel
Loop over every `class="slide"`, render each, append into the PDF.

### Sandbox constraints
- Logo PNG / images: **base64 inline mandatory** (external URLs return 403)
- Verify `scrollHeight === 1450` for LinkedIn (exact — not more, not less)
- Padding budget respected: zero dead space at the bottom

---

## 19. INTERNAL SKILLS (reusable components)

### LINKEDIN WINNING FORMULA skill
- Hook max 12 words with pattern A/B/C/D (see §14)
- Parallel diagnosis with 2+ failure modes
- Numbered system layers with specific tools and real numbers
- Open close: an unrevealed layer OR a behavioral question
- Operator debrief voice "I ran/built/killed"
- 12-point checklist before output
- 1–2 sentence paragraphs
- 150–350 words standard / 400–470 KILL model
- ZERO statistics in the hook
- ZERO emotional opening
- ZERO generic copy

### Referenced sub-skills (for granular detail)
- **360Brew Intelligence** — algorithm analytics, saves = #1 signal, no hashtags, 14+ short paragraphs
- **Scoring Framework** — Virality / Save / Visual / SystemThink /100
- **Design Architect** — Dark Ultron CSS tokens + layout templates
- **Copy Architect** — voice + structure (operator debrief)
- **ICP Intelligence** — Founder/Co-Founder/CEO, 2–50 employees, IT/software/consulting, US/UK

### LinkedIn comment generator (Chrome extension)
> NOTE: the original referenced a local script `~/Scripts/linkedin_comment.py` on the operator's
> personal machine — **that file is NOT present in this environment.** Treat the logic below as
> spec; if needed here, reimplement it in-repo rather than calling the old path.
- 5 comment personas: Architect Technical Sceptic, Strategist Curious Peer, Builder Supportive Expert, Validator, Peer Congratulate
- Options 4–5 open with the reaction, NOT a paraphrase of the post
- Haiku model (~3x cheaper than Sonnet for comment generation)
- NO em dashes as separators

### Restricted DM workflow
When DM is restricted to first-degree connections, approved public reply:
"DM failed. Let's connect and I'll send it over."

---

## 20. MODEL ROUTING LOGIC

| Task | Model | Reason |
|------|-------|--------|
| High-volume low-complexity (comment gen, classifications) | Haiku | ~3x cheaper than Sonnet |
| Standard execution (caption, poster copy, structured output) | Sonnet | Default operator |
| Deep research / multi-turn reasoning / strategy | Opus | Complex analysis |
| Visual design iterations (HTML/CSS) | Opus | Multi-step refinement |
| Quick edits / one-off fixes | Sonnet or Haiku | Speed-first |

OpenRouter middleware for per-user credit provisioning. BYOK removed from documentation as unimplemented.

---

## 21. STYLE / VOCABULARY

### NEVER in copy
- Em dash `—`, en dash `–`
- Curly/smart quotes
- Ellipsis character `…` (use three dots `...`)
- Words: "autopsy", "post-mortem", "morgue" → use BREAKDOWN, DIAGNOSTIC, POSTMORTEM (one word)
- "every week" (always "every day")
- generic "prompt"/"framework" (always "Claude workflow"/"Claude audit prompt"/"Claude system")
- Hedging: "might", "could", "perhaps", "maybe", "kind of"
- "Here's" → "Here is" (no contractions that introduce curly apostrophes)
- Emoji anywhere; hashtags in the body, niche tags, or any count other than the §15.6 five-set
- Markdown links `[text](url)` and bold/italic markdown (`**bold**`, `*italic*`) — LinkedIn does not render them
- Fictional quotes attributed to real people; promises of an invented PDF/document

### Permitted / recommended in copy
- Specific numbers with context ("200 cold emails over 10 days", not "many")
- Operator voice: "I sent", "I tested", "I killed", "I built", "I let Claude"
- Open counter-intuitive statements ("This had nothing to do with X")
- Self-citation of your own real results only
- Tool names: Claude, CORTEX, SPECTER, STRIKER, PULSE, SENTINEL, AMPLIFY, COUNSEL
- Brand terminology: "lead magnet", "workflow", "audit prompt", "founder GTM"
- Concrete actions: "Drop [KEYWORD]", "Comment below", "DM me"
- ICP filter language: "If you are a founder running GTM alone…"

### Standard keyboard characters only
```
. , : ; ! ? - ( ) [ ] / @ # * + = > ' "
```

### Mandatory pre-flight check
```bash
grep -nE '—|–|…' file.html
# 0 results (also scan for curly quotes)
```

---

## 22. DISTRIBUTION & TIMING

- **Posting time:** 10–11 AM Romania time (proven on 90-day analytics)
- **Preferred format:** PDF carousel > PNG single image (confirmed significantly more effective)
- **Geographic targeting:** LinkedHelper at 25 connections/day to US/UK founders (corrects Bucharest dominance in network composition)
- **Proven content mix:**
  - Workflow Replacement: 50%
  - Stack/Model Decision: 30%
  - Operator Proof: 20%
- **Proven hook style:** verdict/accusation with "Most people" or "You" openers

---

## 23. SECOND PRODUCT — TradeOS (context only)

> **Out of scope for this session.** Lives in a separate repo (`NexityNetwork/TradeOS_…`,
> branch `migration-clean`) that this environment is **not** authorized to touch. Kept here only
> as background context — do not run git/file operations against it from here.

B2B trade-finance platform for SMEs with blockchain integration:
- Polygon PoS (notary layer only)
- Stores anonymized hashes, NOT sensitive data (GDPR compliant)
- 4 Solidity contracts: DocumentAnchor.sol, IdentityRegistry.sol, ReputationLedger.sol, TradeOSController.sol
- Amoy testnet deployment: 200 gwei gas price required

---

## 24. FINAL PRE-PUBLISH CHECKLIST

Before any push to LinkedIn / IG / repo:

**Visual checklist:**
- [ ] Canvas exactly 1080×1450 (LinkedIn) or 1080×1920 (IG)
- [ ] Dark Ultron palette (or REALNUMBERS for lead magnets)
- [ ] DM Sans + DM Mono only
- [ ] Ultron logo embedded base64 in footer
- [ ] Claude logo embedded SVG if Claude is mentioned
- [ ] Zero em/en dashes, zero curly quotes
- [ ] Footer single row, mast single row
- [ ] CTA chip solid book with `→`
- [ ] Zero dead space (verify scrollHeight === target)

**Copy checklist:**
- [ ] Scroll-stop hook in the first 2 lines
- [ ] Hook contains "AI" or "Claude" explicitly
- [ ] Hook max 12 words
- [ ] Caption hook does NOT duplicate the visual hook
- [ ] CTA exact format: "Follow for one AI system… Comment [KEYWORD]…"
- [ ] First comment with the real link (NOT in body)
- [ ] Full structural ALT text

**Scoring checklist:**
- [ ] Virality ≥ 80
- [ ] Save-Worthy ≥ 85
- [ ] Visual ≥ 90
- [ ] System Think ≥ 85
- [ ] Overall ≥ 85 (publish). 70–84 = rebuild. <70 = scrap.

---

## 25. OPERATOR PREFERENCES

- **Full file contents, NOT snippets** — request the whole file on every edit
- **Short, actionable prompts** with full context
- **Blunt, direct communication** with pushback on generic or salesy output
- **MacBook 13"** — 17px text is too small; use 19–21px minimum for sub-hooks
- **No template repetition between consecutive posts** (decision map vs script-41 vs script-53 must be structurally different)
- **Fix ONE element at a time** — when asked to fix something specific, do not modify other elements

---

## 26. VALIDATED VIRALITY PRINCIPLES (data-backed, 2026-06-01)

> Derived from the top 10 LinkedIn posts (real per-post analytics). Full evidence + apply-checklist:
> **`analysis/virality-principles.md`**. North-star: **viral = impressions+reach → saves → comments**.
> Per §0, where these conflict with earlier rules, **THESE win.** Caveat: n=10, mostly one topic
> (AI model routing for GTM); the three levers below are the robust part, reach magnitude is noisy.

- **Reach is a lottery.** The same formula produced 893–11,619 impressions (13x). Ship for
  consistency; judge a post by saves/comments, not reach.
- **SAVES lever (metric #2):** a reference-grade asset (named map / numbered system / prompt list)
  or a copy-paste **carousel**, plus an explicit **"Save this [name the asset]."** Done → 0.45–0.90%
  save rate; skipped → ~0.02%. (#2 vs #4: identical matrix, the save ask alone took saves 1 → 25.)
- **COMMENTS lever (metric #3):** **"Comment [KEYWORD] and I will send you the exact Claude
  [workflow/system]."** Keyword lead-magnet CTAs → 23–34 comments; soft/open prompts → 3–19.
- **HOOK template:** open the visual hook with **"I + a concrete number"** ("I sourced $127K…",
  "I gave Claude 12,400 accounts. It picked 847."). **Supersedes §14** ("no I / no stats in hook").
- **REACH lane:** "which AI model/agent for which founder-GTM job", dense single-image infographic
  (9/10 top posts). Save/comment levers travel to other topics; reach is lane-bound.
- **FORMAT:** single image = reach play; carousel of copy-paste items = save play. **Refines §22**
  ("carousel > PNG") — true for SAVES, not demonstrated for reach.

---

## 27. LINKEDIN INFOGRAPHIC DESIGN PRINCIPLES

> Reference framework (Marina Panova), added 2026-06-02. Full notes: `analysis/linkedin-infographic-principles.md`.
> Reinforces §13 (scoring), §16 (layouts), §26 (SAVES lever). Apply to every LinkedIn infographic.

1. **One core idea** — one problem / framework / transformation. Ask "what do they remember in 5 minutes?"
2. **Title instantly clear** — stop the scroll, create curiosity, explain the outcome. Name the asset ("X Cheatsheet / Map / System"), not "Thoughts on X".
3. **Structure > design** — highly scannable, section-based, balanced, skim in 10s. Numbered sections, spacing, boxes, contrast, hierarchy.
4. **Optimize for SAVES** — not motivational. Practical, referenceable, actionable, easy to revisit. "Would someone save this to use again?"
5. **Do not overload** — too much text kills retention. Simplify, cut words, clarity wins.
6. **Scannability** — people scan before they read. Short paragraphs, bold headers, visual rhythm, clean structure.
7. **Recognizable branding** — consistent colors / type / layout / tone. (LinkedIn = Dark Ultron; TikTok = the reference glass format, per operator.)
8. **One clear CTA** — "Save this", "Repost", or "Comment [KEYWORD]". One, not five.
9. **DENSITY — the dominant element must be HEAVY (operator HARD rule, repeated 2026-06-10):** the central block (table / trace / chart / list) must be packed with real, weighty content - every row filled, tight, visually heavy, edge to edge. **NEVER spread sparse rows with `justify-content:space-between`** - it creates airy, skippable gaps. This is THE recurring rejection ("tabelul central e slab si aerisit, te face sa dai skip"). If a block looks airy: pull MORE real rows/columns from the docs, enlarge the content, or pack tighter - never distribute thin content across empty space. Every row carries real data (numbers, names, values, log lines). "Fiecare mm trebuie sa se zbata sa fie acolo."
10. **Vary every material - nothing standard or linear (operator, repeated):** each material is bespoke. Within one LinkedIn infographic use DIFFERENT treatments per section (e.g. table / pipeline / cards) + a different palette accent per section (book / book-dark / kraft) + one focal element. Never three identical stacked tables. TikTok is NOT a dry table - use a visual scene/mockup (e.g. chat-session mockup), CTA styled to that scene.

**Pre-publish gate (7 questions):** easy to scan? · idea immediately useful? · title clear? · visually structured? · **is the central block dense and heavy, with no airy gaps?** · would people save it? · would someone repost it?

---

## 28. FILE / EXPORT HYGIENE (operator rule, 2026-06-04)

> Binding (per §0.1). The algorithm penalizes content that reads as tool- or AI-generated.
> Every exported file must look operator-authored. **Nothing referencing Claude, AI, the
> renderer, or the chat may appear in a file's metadata or "details".**

**Mandatory after every render (PNG/PDF):** run the scrubber before delivery.
```bash
python3 content/_scrub.py content/<file>.png   # strips all metadata, stamps operator credits
```
- `content/_scrub.py` removes every text/time/software/source chunk (keeps only pixels) and
  writes: Author = **Tibi Serbaneci**, Copyright, Software = **Ultron Content Studio**,
  Source = **ultron-content/exports** (virtual path). No real origin, no tool name, no AI.
- Build scripts must call it as the last step of any export. Never ship a freshly rendered PNG.

**The macOS "Where from" tag is NOT in the file.** It is `kMDItemWhereFroms`, added by the
browser when a file is downloaded from the chat (claude.ai files URL). It cannot be baked out
from the repo. To deliver clean files:
- **Preferred:** pull the committed file from the git repo (git sets no such tag) — fully clean.
- **If downloaded from chat:** strip the tag locally on the Mac:
  `xattr -c "file.png"`  (clears all download xattrs), or set your own:
  `xattr -w com.apple.metadata:kMDItemWhereFroms "$(python3 -c "import plistlib,sys;sys.stdout.buffer.write(plistlib.dumps(['Tibi Serbaneci','ultron-content/exports'],fmt=plistlib.FMT_BINARY))")" "file.png"`

**Note:** Chromium screenshots already contain no Claude/AI string (only IHDR/IDAT/IEND); the
scrubber is about stamping operator authorship + guaranteeing no future tool chunk slips in.
Commit trailers (the session link) live in git history only, never in a delivered file.

---

## 29. CONTENT PORTAL + ANALYTICS LOOP (operator, 2026-06-05 — binding)

> **DEPRECATED / GITHUB-DISABLED (operator, 2026-06-24 — binding, per §0.1):** storage moved to the
> Monolith vault (see §2). The portal's GitHub auto-commit/push/sync are now **OFF by default**
> (`portal/server.py`: `PORTAL_PUSH` / `PORTAL_COMMIT` / `PORTAL_SYNC` default `0`;
> `portal/codespace-start.sh` no longer fetches/pulls origin on boot). The always-on GitHub Pages
> portal is retired (kill the Codespace + turn off Pages on GitHub's side to stop the cost). The
> portal may still be run **locally** as a read-only viewer, but it no longer writes to GitHub. New
> materials are wired straight into the Monolith Library (R2 `ultron-reels/imports/` + `vault_items`,
> tagged by channel), not the portal manifest. The 155 portal materials were migrated on 2026-06-24.

The portal maps every material into one dashboard: channels (LinkedIn / TikTok / Instagram),
grid previews, per-material caption / ALT / first-comment copy boxes, single or one-click carousel
zip download (suggestive filename), mark-posted, analytics upload, cross-post (copy to the other
channel), generation date, filters. The 72 reference materials load tagged **needs-revision**.

- **Online, always-on (canonical — operator 2026-06-12):** the portal also ships as a single
  **password-gated encrypted file** at `docs/index.html`, served by **GitHub Pages from `main`**
  (always-on stable URL, opens on phone, no Codespace to wake). The content (manifest + thumbnails +
  caption kits) is **AES-256-GCM encrypted in the browser** (PBKDF2-SHA256, 250k iters); nothing is
  readable on the host without the **user + password**, so the always-public Pages URL is safe.
  Full-res downloads link back to the private repo (a second GitHub-login gate). This **supersedes**
  the earlier "GitHub Pages deliberately not used" rule — the client-side encryption removes the
  public-exposure objection (per §0.1, this is now the rule). **Rebuild after adding/editing materials:**
  `python3 portal/build_secure.py /tmp/inner.html` then
  `PUSER=<user> PPASS=<pass> node portal/encrypt_gate.js /tmp/inner.html docs/index.html`, commit to `main`.
  The same encrypted file works on any static host (Cloudflare Pages / Netlify) if Pages needs Pro.
- **Admin / write-back (Codespace, private):** the **GitHub Codespace** on the work branch still runs
  `portal/server.py` on a **Private** forwarded port for the write actions (mark-posted, analytics
  upload, cross-post) that auto-commit. The encrypted Pages file is a read-only snapshot — rebuild it
  to refresh what the always-on portal shows.
- **Run (local alt):** `python3 portal/server.py` then open `http://127.0.0.1:8753`. It is **autonomous** —
  every change (posted toggle, analytics upload, cross-post) writes `content/portal/manifest.json`
  and auto-commits and pushes. No manual commit. `PORTAL_PUSH=0` to disable push.
- **Reindex after adding materials:** `python3 portal/scan.py` (or the Rescan button). Merges with
  the manifest so posted/analytics state is preserved. Files: `portal/scan.py`, `portal/server.py`,
  `content/portal/{index.html,manifest.json,thumbs/,zips/}`, `content/analytics/`.

**ANALYTICS LOOP (binding):** real post analytics live in `content/analytics/` (LinkedIn CSV/XLS,
TikTok exports), linked per material in the manifest. BEFORE building any new material, review the
posted materials' metrics (impressions / reach / **saves** / comments / sends) and let them steer the
hook, format and lever choices. Periodically check how shipped posts performed and fold the learning
into `analysis/virality-principles.md`. Metrics priority stays: reach+impressions → saves → comments.

---

## 30. AUTOMATED GUARDS (binding, added 2026-06-10 - operator demand: "instaleaza-ti guarduri ca sa nu mai poti realiza niciodata asa ceva")

> The recurring rejections (airy blocks, repeated templates, off-spec exports) kept happening because
> the rules lived only in prose. They are now ENFORCED by `content/_preflight.py`, wired as a **Stop
> hook** in `.claude/settings.json` that BLOCKS the turn while any changed `content/docs-*` material
> fails. Run it by hand on anything before delivery: `python3 content/_preflight.py content/<file>.html`.
> The guard is the floor, never the ceiling - passing it is not the same as good.

**Hard-fail checks (block delivery):**
1. **Dimensions exact** - `#artifact` = 1080x1450 (LinkedIn), every `.slide` = 1080x1920 (TikTok/IG).
2. **Charscan** - zero em/en dash, ellipsis char, curly quotes.
3. **Fonts** - DM Sans / DM Mono only; forbidden families rejected.
4. **Palette** - no forbidden hex (neon orange, green, saturated red, peach, purple, blue).
5. **Safe-zone** - vertical slides: top content >= 300px.
6. **No repetition** - body-class layout must differ from the previous material of the same channel (Jaccard <= 62%). Reusing a prior template = FAIL. (The docs-12-reused-docs-11 mistake is now blocked at the door.)
7. **Dead band** - no single empty band > 120px (egregious airiness).
8. **Footer** - Ultron + 51ultron.com present.

**Surfaced every run (judgement, printed not auto-blocked):** empty-row % + largest dead band (a product mockup runs ~60% empty by design, so a blind gate would false-positive on approved work - PACK the dominant block if it reads airy; never `flex:1`/`space-between` to stretch sparse rows), and a `space-between`/`flex:1` code-smell count.

**Process guards (operator rules - do NOT deviate):**
- **SHOW every render** with SendUserFile - never describe a material without attaching it (operator: "nu mi l-ai aratat").
- **Propose before executing; fix ONE element at a time.**
- **Every material is bespoke** - vary layout/treatment/palette per material; never reuse a "locked" template (operator: "nu repeta materialele intre ele").
- **Density first** - the dominant block is heavy and packed; airy = skip.
- **TikTok is a visual scene/mockup, not a dry table; CTA styled to the scene.**
- **3D-carousel CTA = one of the 3 established pills ONLY (operator HARD rule, 2026-06-27, "scrie o regula ... sa nu o mai uiti"):** the CTA slide ALWAYS reuses one of the three pre-rendered reusable 3D pills (OPERATOR / FOUNDER / BUILDER), rotated across materials. NEVER generate a new CTA model - no comments-mockup, no per-material CTA Vertex object. The comment keyword aligns to the pill word.
- **3D-carousel cover (operator, 2026-06-27):** title CENTERED in the middle; the brand logos sit BELOW the hook (Claude + Ultron for the IG overlay; the 3D Claude mark for the TikTok normal cover); NO sub-hook / secondary line on the cover - hook + logos only.
- **Each 3D object MATCHES its hook and is full-frame (operator, 2026-06-27):** the panel must illustrate the slide's own hook (e.g. "writes in your voice" -> a writing/content panel, NOT a generic dashboard), be enlarged and fully visible (no right-edge/muchie crop), and NEVER repeat the same model across slides. Do not let Vertex collapse to the seed dashboard - regenerate seed-independent until each object is distinct and on-topic.
- **No "GTM" in copy (operator, 2026-06-27) - use "services"** in hooks, CTAs, captions and objects.
- **3D object framing - show the COMPLETE element, scaled, NEVER trimmed (operator HARD rule, 2026-06-27, flagged 3x):** the Vertex objects are generated WHOLE and verified - any cut is a framing bug on our side, not the object. Frame each object by its DIFFERENCE FROM ITS OWN CORNER BACKGROUND (the most-inclusive bbox that is still the panel, stopping before the soft vignette), NOT a tight bright-pixel/edge box that slices the soft right/bottom edge. Then SCALE the whole captured panel to fit the container (min-ratio, centered) so it is always fully inside the slide. Do for every page what the working pages do. If a panel looks cut, the crop is wrong - fix the crop; never ship a trimmed element.
- **TikTok = CLAUDE perspective, NOT Ultron (operator, repeated 2x: "tiktok e claude perspective nu ultron... sa nu uiti"):** LinkedIn is the Ultron brand (Ultron logo, the agents/personas/tools as Ultron product features). **TikTok leads with Claude** - the Claude sunburst mark up top (never the Ultron logo in the kick), a Claude-forward hook ("You use Claude…", "Claude can…"), generic Claude / Claude-Code framing (slash commands, tool use, projects), and Ultron demoted to the footer logo + at most one caption line. Never make the Ultron logo, the named agent roster (CORTEX/SPECTER/…), or "Ultron's X" the TikTok subject; genericise to the underlying Claude/Claude-Code capability. Pair: "claude si claude code pur pentru tiktok."
- **Stay on ICP (founders, not engineers)** - no raw code or dev internals inside a material; show the product UI and the founder-facing value (operator: "nu mai pune linii de cod ... te indepartezi de ICP").
- **Content is real** - numbers/features pulled from the docs, never invented; links only to confirmed app.51ultron.com paths, first comment only.
- **Portal** - after adding materials, rescan + commit the manifest; last-added is first in every category; private port, open in a real browser.
- **Captions** - LinkedIn 5-block 400-470w + ALT 80-150w + first comment 40-80w; TikTok one-beat paragraphs + exactly 5 hashtags.

---

END OF CONFIG.
