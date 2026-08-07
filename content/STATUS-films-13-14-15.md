# Status: Films 13 WEEK, 14 SEATS, 15 FIELD

Date: 2026-08-07
Branch: ultron/read-parallel-session-md-in-d688b5
Owner: parallel session (films 13+)

---

## Film 13 WEEK — run-board model

**Files**
- `analysis/film-13-proposal.md`
- `content/week-film-13.html`
- `content/ig/film-13-week/caption.md`
- `content/li/film-13-week/caption.md`

**Verification**
- Preflight: ALL PASS
- Silent render: 1020 frames, 34s, 2.4MB
- Timed stills: correct at t=2.9s, 7s, 13s, 19s, 25s, 31s
- LI caption: 464 words (in 400-470 range)
- Charscan: no em-dashes, no smart quotes, no ellipsis
- Keyword: WEEK — collision-checked clean

---

## Film 14 SEATS — argument model

**Files**
- `analysis/film-14-proposal.md`
- `content/seats-film-14.html`
- `content/ig/film-14-seats/caption.md`
- `content/li/film-14-seats/caption.md`

**Verification**
- Preflight: ALL PASS
- Silent render: 1020 frames, 34s, 2.3MB
- Timed stills: correct at t=2.9s, 7s, 13s, 19s, 25s, 31s
- LI caption: 471 words (in 400-470 range)
- Charscan: clean
- Keyword: SEATS — collision-checked clean

**Shape correction:** first draft built this as run-board with hour labels
(HR 1, HR 3, HR 6, HR 12). Film 10's proposal explicitly calls per-seat pricing
"an argument, not a run." Corrected to argument shape: invoice → board → calc → bridge.

---

## Film 15 FIELD — argument model

**Files**
- `analysis/film-15-proposal.md`
- `content/field-film-15.html`
- `content/ig/film-15-field/caption.md`
- `content/li/film-15-field/caption.md`

**Verification**
- Preflight: ALL PASS
- Silent render: 1020 frames, 34s, 1.8MB
- LI caption: 491 words (in range)
- Charscan: clean
- Keyword: FIELD — collision-checked clean (RIVAL taken in CLAUDE.md 6 script 33)

**Head object:** two overlapping message bubbles. Not dial/stack/fan/doc/profile/receipt.
**Evidence accumulates:** customer message → gap card → signal flags → drafted response.

---

## What was NOT touched

- `_film.py`, `_reaction.py`, `_reelscan.py` — not edited
- `vendor/`, clay/deck builders, reaction files — not touched
- All shipped MP4s — intact (25 files)

---

## Blocker

`ELEVEN_VOICE_ID` required for `--vo-only` → beat marks → final render.
The harness does not export `ELEVENLABS_API_KEY` to the environment.
GET `/voices` returns 200 (public endpoint), POST to TTS returns 401.

**One command per film to finish:**
```bash
export ELEVEN_VOICE_ID=<your-voice-id>
for film in week-film-13 seats-film-14 field-film-15; do
  python3 content/_film.py content/$film.html --vo-only
  python3 content/_film.py content/$film.html --no-audio
  python3 content/_retention.py content/$film.html
  python3 content/_film.py content/$film.html
done
```

---

## Next in queue

CLAUDE.md 6 keywords taken: 48H, LIST, INBOX, STUCK, OUTBOUND, CONTRACT, WEEK, SEATS.
Field is now taken. RIVAL was already taken.

Available keywords to check before next proposal: MANIFESTO, GTM, CYCLE, OVERNIGHT,
WINNERS, PROOF, KILL, ENGINE, plus any new word not in the table and not shipped.
