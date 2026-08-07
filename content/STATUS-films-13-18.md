# Status: Films 13-18

Date: 2026-08-07
Branch: ultron/read-parallel-session-md-in-d688b5
Owner: parallel session (films 13+)

---

## Films structurally complete (awaiting VO)

| Film | Model | Keyword | Head Object | LI Words | Preflight |
|---|---|---|---|---|---|
| 13 WEEK | run-board | WEEK | customer profile | 464 | PASS |
| 14 SEATS | argument | SEATS | invoice | 471 | PASS |
| 15 FIELD | argument | FIELD | message bubbles | 491 | PASS |
| 16 PIPELINE | run-board | PIPELINE | pipeline bar | 441 | PASS |
| 17 DRAFT | run-board | DRAFT | paper stack | 405 | PASS |
| 18 NUDGE | argument | NUDGE | message thread | 420 | PASS |

All six: HTML, proposal, IG caption, LI caption, INDEX entry.
All keywords collision-checked clean.
No em-dashes, no smart quotes, no ellipsis in any file.
All 25 shipped MP4s remain intact.

## Blocker

`ELEVEN_VOICE_ID` not in environment. `--vo-only` needed for beat marks.

## Finish command

```bash
export ELEVEN_VOICE_ID=<your-voice-id>
for film in week-film-13 seats-film-14 field-film-15 pipeline-film-16 draft-film-17 nudge-film-18; do
  python3 content/_film.py content/$film.html --vo-only
  python3 content/_film.py content/$film.html --no-audio
  python3 content/_retention.py content/$film.html
  python3 content/_film.py content/$film.html
done
```
