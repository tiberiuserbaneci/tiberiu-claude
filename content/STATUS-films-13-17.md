# Status: Films 13-17

Date: 2026-08-07

---

## Films structurally complete (awaiting VO)

| Film | Model | Keyword | Head Object | LI Words | Status |
|---|---|---|---|---|---|
| 13 WEEK | run-board | WEEK | customer profile | 464 | preflight PASS, silent render 2.4MB |
| 14 SEATS | argument | SEATS | invoice | 471 | preflight PASS, silent render 2.3MB |
| 15 FIELD | argument | FIELD | message bubbles | 491 | preflight PASS, silent render 1.8MB |
| 16 PIPELINE | run-board | PIPELINE | pipeline bar | 441 | preflight PASS |
| 17 DRAFT | run-board | DRAFT | paper stack | 405 | preflight PASS |

All five: HTML, proposal, IG caption, LI caption, INDEX entry.

## Blocker

`ELEVEN_VOICE_ID` not in environment. `--vo-only` needed for beat marks.

## Finish command

```bash
export ELEVEN_VOICE_ID=<your-voice-id>
for film in week-film-13 seats-film-14 field-film-15 pipeline-film-16 draft-film-17; do
  python3 content/_film.py content/$film.html --vo-only
  python3 content/_film.py content/$film.html --no-audio
  python3 content/_retention.py content/$film.html
  python3 content/_film.py content/$film.html
done
```
