# Brief for the parallel session

You are a second Claude session working on this repo at the same time as another one. This file
is your complete brief. Read it fully before touching anything.

The other session is doing **short-form R&D** (the reaction format, Three.js, the renderer).
**You are doing run-board films and their captions.** The split below is what keeps you from
colliding. It is not advisory.

---

## 1. READ THESE, IN THIS ORDER, BEFORE YOU BUILD ANYTHING

Everything you need to reach the same standard is already written down. Read, do not skim.

| # | Path | What it gives you |
|---|---|---|
| 1 | `CLAUDE.md` | **The binding config.** Brand, voice, dimensions, safe zones, caption rules, and 30, which is the accumulated list of every mistake already made. This is the shared memory. |
| 2 | `analysis/virality-principles.md` | What the operator's own analytics proved about saves, comments and hooks |
| 3 | `analysis/reels-virality.md` | Researched IG guidance: vary the interrupt, change ~1s, loop, sends carry 3-5x likes |
| 4 | `analysis/reaction-format.md` | How a posted reel was measured and what killed it |
| 5 | `analysis/film-10-proposal.md` | The worked example of a film proposal. Match this shape. |
| 6 | `content/maybe-film-10.html`, `content/inbound-film-11.html`, `content/contract-film-12.html` | The three most recent films. **12 is the newest and carries every fix.** Build from it. |
| 7 | `content/ig/film-12-contract/caption.md` and `content/li/film-12-contract/caption.md` | The two caption standards. Reel form and LinkedIn form are different. |
| 8 | `content/_film.py`, `content/_retention.py`, `content/_licut.py`, `content/_scrub.py` | The tools. Read their docstrings, they explain the reasoning. |

The single most important read is **CLAUDE.md 30**. Every rule in it was paid for with a
rejected material. Not re-reading it is how you repeat one.

---

## 2. WHAT YOU OWN, AND WHAT YOU MUST NOT TOUCH

### Yours to write
```
content/<slug>-film-13.html      content/<slug>-film-14.html      ... 13 and up
content/<slug>-film-NN-vo.mp3    content/<slug>-film-NN-vo.align.json
content/<slug>-film-NN.mp4
content/ig/film-13-<kw>/         content/li/film-13-<kw>/         ... and up
analysis/film-13-proposal.md     ... and up
```

### DO NOT TOUCH - the other session is editing these live
```
content/_film.py           <- being modified for a Three.js clock RIGHT NOW
content/_reaction.py       content/_reelscan.py      content/vendor/
content/reaction-*.html    content/reaction-*.mp4
content/_clay*.py          content/_deck*.py         content/_carousel.py
analysis/reaction-format.md          analysis/reels-virality.md
```

**You RUN `content/_film.py`, you never EDIT it.** If you hit a bug in it, write the diagnosis
into your commit message and carry on with a workaround in your own file. The other session
will apply the fix. Two sessions editing the renderer will corrupt both your renders.

### Shared, append-only
`CLAUDE.md` - you may APPEND a new rule if the operator gives you one, at the end of the
relevant section. Never rewrite an existing rule, never reflow the file. Conflicts here are
painful because both sessions read it as memory.

---

## 3. GIT

Ask the operator to confirm your branch name before your first push. Suggested:
`claude/parallel-films-2` off the same base as `claude/educational-materials-voice-gml260`.

- Never push to the other session's branch.
- Never `git add -A` from the repo root. Stage **your own paths explicitly**, or you will
  commit the other session's in-progress renderer edits and break them.
  ```
  git add content/<slug>-film-13.html content/ig/film-13-* content/li/film-13-* analysis/film-13-*
  ```
- Leak-check every commit, the credentials are real:
  ```
  git diff --cached | grep -cE "sk_1193|vThC6vX|ELEVENLABS_API_KEY="    # must print 0
  ```
- No PR unless the operator asks.

---

## 4. CREDITS - COORDINATE OR YOU WILL BURN THE OPERATOR'S QUOTA

ElevenLabs credentials live **outside the repo**, in the session scratchpad
`eleven.env`. Ask the operator for the path; never commit them, never echo them.

**One VO take per film. Never re-record to fix a visual.** The alignment cache
(`<film>-vo.align.json`) reuses the take as long as the script is byte-identical, so:
- finalise the script BEFORE the first render
- `--vo-only` first to get the marks, then re-time the page, then render
- if you edit one word of VO, you have paid for a whole new take

Silent films cost nothing: `--no-audio`. Use it for every layout iteration.

---

## 5. THE DELIVERABLE STANDARD

A film is not done until **all** of this is true. This is the bar the last three met.

**Build**
- [ ] Proposal written first, in the shape of `analysis/film-10-proposal.md`, and the subject
      checked against every shipped film for collision
- [ ] Built FROM `content/contract-film-12.html`, so its fixes carry
- [ ] **Head object differs from every other film's opener.** 05 dial, 10 week strip, 11 card
      fan, 12 document. CLAUDE.md 30 forbids a fifth opening on any of them.
- [ ] Every row's headline and sub-line is ONE line. Rows are fixed height; longer copy clips.
- [ ] Canvas 1080x1920, everything inside the 300..1590 safe band

**Timing - the rule that has bitten three times**
- [ ] `--vo-only` first, read the real beat marks
- [ ] **Re-derive every delay measured from a late beat.** 12's b5-to-b6 gap was 6.26s; if
      yours differs, the payoff and CTA offsets are wrong and the payoff will flash and vanish
- [ ] The film does not end on a held frame

**Verify**
- [ ] `python3 content/_retention.py content/<film>.html` -> ALL PASS against episode 04.
      Source the VO env first or it measures a page with no hook and lies to you.
- [ ] Frames sampled across the beats and actually LOOKED AT before delivery
- [ ] `grep -nE '—|–|…' ` on every .md -> 0 results

**Ship**
- [ ] `content/ig/film-NN-<kw>/` with `reel.mp4`, `cover.png` (scrubbed), `caption.md`
- [ ] `python3 content/_licut.py content/ig/film-NN-<kw>/reel.mp4 content/li/film-NN-<kw>/ --thumb <s>`
- [ ] `content/ig/INDEX.md` updated, newest first
- [ ] Delivered to the operator with SendUserFile. **Never describe a material without
      attaching it.**

**Captions - two different forms, both validated**
- Reel (`content/ig/...`): CLAUDE.md 15.6 short form, one beat per paragraph
- LinkedIn (`content/li/...`): CLAUDE.md 15 - **400-470 words**, five blocks, arrow list, the
  fixed CTA, plus **80-150 word ALT** and **40-80 word first comment**
- Both: zero em/en dashes, zero curly quotes, exactly the five hashtags, and **no agent names**

---

## 6. THE RULES THAT COST US THE MOST, IN SHORT

Full detail is in CLAUDE.md 30. These are the ones you will trip over.

1. **No agent names. Ever.** Claude, AI, Ultron - nothing else. Say what it does, not which
   agent does it. (21, rewritten 2026-08-06.)
2. **The elapsed time must be the FOUNDER's, never the machine's.** 48h of outbound is real
   because replies take days. 40 minutes to read a contract is not - the machine takes
   seconds, so the number reads as the product being slow. Ask whose clock it is.
3. **A wall may never outlive its hook.** If the film uses an opaque `.hkscrim`, it must finish
   clearing by `--hookgone`. This cost two episodes their opening.
4. **The board is legible from the seam.** Rows at .34 opacity from the start, brightening on
   their span. Hiding them leaves an empty frame right after the scroll-stop.
5. **Numbers are real or they do not appear.** Operator-scale, from the docs, never invented.
   No close rates, no benchmarks, no fabricated research.
6. **Nothing sends itself.** The founder approves and sends. It is true and it is the better
   line.
7. **Show every render.** SendUserFile, always.
8. **Fix ONE element at a time** when the operator names something specific.

---

## 7. SUBJECT QUEUE - TAKE THESE IN ORDER, THEY ARE COLLISION-CHECKED

Shipped: 01 research, 02 overnight, 03 model routing, 04 governance, 05 outbound 48h,
06 the GTM role, 07 how founders use Claude wrong, 08 the AI Act sender rule, 09 the pitch,
10 the stalled deal, 11 the inbound hour, 12 the contract.

| Film | Subject | Keyword | Why it is clean |
|---|---|---|---|
| **13** | The week after they pay. Onboarding, and the churn that starts on day one. | `WEEK` | The whole post-sale side is unfilmed. Check what the product genuinely does here before committing - do not overclaim. |
| **14** | Per-seat pricing, and why it punishes the buyer who adopts fastest. | `SEATS` | The backlog's strongest unspent entry. It is an ARGUMENT, not a run - it needs a different shape from the run board, so propose that shape first. |
| **15** | The competitor you found out about from a customer. | `RIVAL` | Wait - `RIVAL` is already taken (CLAUDE.md 6, script 33). Pick a free keyword and check the table. |

Always check a proposed keyword against the CLAUDE.md 6 table AND every shipped film folder
before you commit to it.

---

## 8. WHEN TO STOP AND ASK

- The subject touches a claim you cannot source from the docs
- A guard fails and the fix would change something the operator approved
- You want to edit anything in the DO NOT TOUCH list
- You are about to spend a VO take on a script you are not certain of
