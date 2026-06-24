# Virality Principles — derived from real LinkedIn performance

> Built from the top 10 posts in the Mar 4 – Jun 1 2026 export, with per-post analytics
> (impressions, reach, reactions, comments, reposts, **saves**, sends) for each.
> North-star (operator-set): **viral = impressions+reach → saves → comments**, in that order.
> Raw data: `post-performance-join.csv`. Last updated: 2026-06-01.

## Basis & honest caveat
- **n = 10** posts (the reach top-5 + the resonance winner + 4 requested mid-tier).
- **9 of 10 are the same topic family** ("AI model routing for founder GTM"), almost all dark
  "legacy" brand. So **topic and brand are partly confounded** — I cannot fully separate
  "this topic wins" from "this brand wins."
- What survives the confound: the **three engagement levers** below hold across topic, brand and
  format, so treat them as robust. **Reach magnitude** is the noisy, low-control variable.

---

## Conclusion 1 — Reach is a lottery; ship for consistency, not for the spike
**Evidence:** the same formula (routing topic + "I + number" hook + dense infographic) produced
reach from **893 to 11,619 impressions — a 13x swing** (4/29 vs 5/7, near-identical recipe).
**Apply:**
- Do not judge a post by its reach. Keep the format and cadence; expect ~1 in N to spike.
- Optimize what you control (saves + comments), not what you don't (which post goes big).

## Conclusion 2 — SAVES are the controllable lever (operator metric #2)
**Evidence:**
- #2 (model-comparison matrix, **no** save ask) → **1 save** (0.02%).
- #4 (the **same** matrix format **+ "Save this routing map"** + reusable framing) → **25 saves** (0.65%).
  Same content type; the ask + framing alone moved saves ~25x.
- Carousel (4/9, copy-paste prompts + "Save this") → **0.87% save rate, the highest of all 10**.
**Apply (to win saves):**
1. Make the asset **reference-grade**: a *named* map / routing sheet / numbered system / prompt list the reader will reuse.
2. End with an explicit **"Save this [name the asset]."** — literally name it ("Save this routing map").
3. For pure save-bait, a **carousel** of copy-paste items beats a single image.
- Expected: **0.45–0.90% save rate** when you do this; **~0.02%** when you skip it.

## Conclusion 3 — COMMENTS scale with keyword lead-magnet CTAs (operator metric #3)
**Evidence:** "Comment [KEYWORD] and I'll send the Claude workflow" → **TERRITORY 34, GTM 29,
BLUEPRINT 23**. Open/soft prompts ("leave your task in the comments") → **3–19**.
**Apply:** end with **"Comment [KEYWORD] and I will send you the exact Claude [workflow/system]."**
Name a specific, desirable lead magnet. (This is also the CLAUDE.md §15 CTA format — it works.)

## Conclusion 4 — Hook template: "I + a concrete number"
**Evidence:** nearly every winner opens this way — "I wasted $420/mo", "I sourced $127K",
"I gave Claude 12,400 accounts. It picked 847.", "I cancelled $7,200", "I almost hired 6 GTM roles."
Present in both the reach winners and the resonance winner.
**Apply:** open the **visual** hook with **"I [verb] [concrete $ or count]."**
**Overrides CLAUDE.md §14** ("don't start with I", "zero statistics in the hook") for the visual hook —
the data shows the opposite is what wins.

## Conclusion 5 — Your reach lane is "AI model routing for founder GTM"
**Evidence:** 9/10 top posts are this theme (Claude vs ChatGPT vs Gemini/Perplexity routing,
GTM-cost-collapse, agent-replacement, decision-board). It matches the demographics (founders,
IT/software/consulting) that the audience rewards with reach.
**Apply:** for **reach**, stay in this lane — "which model/agent for which GTM job", dense infographic.
The one off-lane post (Claude-products carousel) still won on **saves**, so the save/comment levers
travel to other topics; **reach** is the lane-dependent part.

## Conclusion 6 — Format: carousel for saves, single image for reach
**Evidence:** 9/10 reach winners are single-image infographics; the 1 carousel had the **best save
rate (0.87%)** but only **mid reach (2,190)**.
**Apply:** single dense infographic = **reach** play; carousel of copy-paste items = **save** play.
**Refines CLAUDE.md §22** ("PDF carousel > PNG single image") — true for **saves**, not demonstrated for reach.

---

## Apply-in-context checklist (pick the goal, pull the lever)
- **Goal = REACH** → routing-lane topic + "I + number" visual hook + single dense infographic. Accept the variance.
- **Goal = SAVES** → reference-grade asset *or* carousel + **"Save this [named asset]."**
- **Goal = COMMENTS** → **"Comment [KEYWORD] and I'll send the exact Claude workflow."**
- **Always** → real numbers, named tools (Claude / SPECTER / STRIKER / CORTEX / PULSE / SENTINEL), one dominant idea, operator voice.

## CLAUDE.md reconciliation (what this analysis overrides)
| Config rule | Data verdict |
|---|---|
| §14 — no "I" start, no stats in hook | **OVERRIDE** — "I + concrete number" hooks are the consistent winners |
| §22 — "PDF carousel > PNG single image" | **REFINE** — carousel wins **saves**; reach not shown to favor it |
| §15 — caption hook must differ from visual hook | **NOT predictive** — the #1-reach post used near-duplicate hooks |
| §21 — no emoji in copy | **NOT predictive** — the emoji caption (5/12) performed well |

## What would sharpen this further (not yet available)
- **Off-lane winners** (non-routing topics that did well) to break the topic/brand confound.
- **More carousels** — only 1 in the sample, so the format read is a single data point.
- **The full post list** (export caps at top-50), to learn from posts that failed, not only winners.

---

## BEST-PERFORMER DECOMPILE (2026-06-24) - post 7473683676527071232 ("routing/engine")

Hook: "Your AI tool sends your prompt to a model..." (6/19, 2 PM). Best performer since this workspace started.
Single-post analytics: 1,939 impressions / 1,147 reached. Engagement 62 = **35 comments**, 26 reactions, **1 save**, 0 reposts, 0 sends. 5 profile views, 5 followers.
Audience: 46% Founder/Co-Founder/CEO/Owner, 66% Owner/CXO/Senior, 57% at <=50-employee IT/software/consulting (exact ICP).

Reverse-engineered - what made it click:
1. **COMMENTS play, not saves/design.** 35 comments vs 1 save; comment:reaction ratio >1 is rare. The keyword comment-CTA was the engine, NOT the visual (saves ~0). On this lane, optimise the CTA for comments, not the design for saves.
2. **Hook = hidden mechanic.** "Your AI [invisible thing it does]" - a curiosity gap about how it works under the hood. This is the reach lane that travels.
3. **Topic = the engine under the hood** (routing / which model). A reveal, not a tip. The topic self-selected the ICP.

Formula to repeat: hidden-mechanic "Your AI..." hook -> dense single-image infographic -> **keyword comment-CTA** -> "how it actually works" topic.
First application: the **tool-engine** set (tool routing = the next layer of the same engine), keyword ENGINE.
