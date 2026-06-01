# Analysis — Post Performance Join

Goal: reverse-engineer the **virality principles already working** by correlating real LinkedIn
performance with the content attributes of each post.

## Source
`post-performance-join.csv`, built from the LinkedIn export `Content_20260304_20260601` (Mar 4 – Jun 1, 2026).
62 distinct posts (LinkedIn caps the export at the top 50 by each metric):
- **38** posts have BOTH impressions + engagements (the strong join set)
- **12** are engagement-only (made top-50 by engagement, not by impressions)
- **12** are impressions-only (made top-50 by impressions, not by engagement)

## Pre-filled columns (do not edit)
| Column | Meaning |
|---|---|
| `post_date` | publish date (M/D/2026) from the export |
| `post_url` | LinkedIn activity URL |
| `impressions` | blank if the post wasn't in the top-50-by-impressions table |
| `engagements` | lump total; blank if not in the top-50-by-engagement table |
| `engagement_rate_pct` | engagements ÷ impressions × 100 (only when both are known) |

## Columns to fill (controlled values — keep them exact)
| Column | Allowed values |
|---|---|
| `publish_time` | `HH:MM` Romania time (to test the 10–11 AM claim) |
| `format` | `image` · `pdf-carousel` · `text` · `video` · `document` · `repost` |
| `script_file` | repo filename (e.g. `script-41-linkedin-v1.html`) or `not-in-repo` |
| `brand` | `dark-ultron` · `legacy` · `other` |
| `campaign` | `realnumbers` · `series1` · `series2` · `standalone` |
| `hook_style` | `A` (Operator Confession) · `B` (Counter-intuitive) · `C` (Number/Question reveal) · `D` (Mix/Challenge) · `other` |
| `topic_tag` | AGENT MATH · FOUNDER PAIN · GTM TRUTH · TOOL AUDIT · REAL NUMBERS · PRICING LAW · or free |
| `cta_keyword` | the post's keyword (OPERATOR, SIGNAL, STACK, …) |
| `reactions` `comments` `reposts` `saves` | integers from per-post analytics (**saves = #1 signal**) |
| `notes` | anything relevant |

## What's still missing for a full picture
1. **The fill columns above** — especially `format` and `saves` (the two biggest levers).
2. **The full post list**, not just the top 50, to learn from posts that *failed* (avoid survivorship bias).
3. **North-star metric** — define "viral": reach (impressions) vs resonance (ER/saves/comments) vs
   follower growth vs DM conversions. The data shows these diverge sharply, so the principles differ.

## How to fill
Edit the CSV directly on GitHub (or locally) and commit. Once `format` + `saves` + `hook_style`
are in for the 38-post join set, the correlations become meaningful.
