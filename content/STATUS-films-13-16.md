# Status: Films 13 WEEK, 14 SEATS, 15 FIELD, 16 PIPELINE

Date: 2026-08-07
Branch: ultron/read-parallel-session-md-in-d688b5
Owner: parallel session (films 13+)

---

## Film 13 WEEK — run-board model

- `analysis/film-13-proposal.md` | `content/week-film-13.html`
- IG: `content/ig/film-13-week/caption.md` | LI: `content/li/film-13-week/caption.md`
- Preflight: PASS | Silent render: 1020 frames, 34s, 2.4MB | LI: 464 words
- Keyword: WEEK — collision-clean
- Head object: customer profile avatar

## Film 14 SEATS — argument model

- `analysis/film-14-proposal.md` | `content/seats-film-14.html`
- IG: `content/ig/film-14-seats/caption.md` | LI: `content/li/film-14-seats/caption.md`
- Preflight: PASS | Silent render: 1020 frames, 34s, 2.3MB | LI: 471 words
- Keyword: SEATS — collision-clean
- Head object: invoice receipt
- Shape corrected from initial run-board draft to argument model

## Film 15 FIELD — argument model

- `analysis/film-15-proposal.md` | `content/field-film-15.html`
- IG: `content/ig/film-15-field/caption.md` | LI: `content/li/film-15-field/caption.md`
- Preflight: PASS | Silent render: 1020 frames, 34s, 1.8MB | LI: 491 words
- Keyword: FIELD — collision-clean (RIVAL taken in CLAUDE.md 6)
- Head object: message bubbles

## Film 16 PIPELINE — run-board model

- `analysis/film-16-proposal.md` | `content/pipeline-film-16.html`
- IG: `content/ig/film-16-pipeline/caption.md` | LI: `content/li/film-16-pipeline/caption.md`
- Preflight: PASS | LI: 441 words
- Keyword: PIPELINE — collision-clean
- Head object: pipeline bar with stages

---

## Blocker

`ELEVEN_VOICE_ID` not in environment. `--vo-only` needed for beat marks before final render.

**One command per film to finish:**
```bash
export ELEVEN_VOICE_ID=<your-voice-id>
for film in week-film-13 seats-film-14 field-film-15 pipeline-film-16; do
  python3 content/_film.py content/$film.html --vo-only
  python3 content/_film.py content/$film.html --no-audio
  python3 content/_retention.py content/$film.html
  python3 content/_film.py content/$film.html
done
```
