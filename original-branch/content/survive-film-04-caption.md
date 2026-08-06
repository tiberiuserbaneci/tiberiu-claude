# ULTRON STACK 04 - SURVIVE

Film: `survive-film-04.mp4` (1080x1920, ~36.5s, narrated, REALNUMBERS cream flipping to Dark Ultron)
Keyword: **SURVIVE**

First material in the series built to a measured retention target rather than to taste. See
`content/_retention.py` and the note at the bottom.

## Every number is cited. Do not edit one without its source.

| Claim | Source | Note |
|---|---|---|
| 88% of AI agent proofs of concept never reach broad production | IDC, 2026 | cited in Cognizant's EMEA AI unit launch, 28 July 2026 |
| 33 pilots started, 4 reach live operation | IDC, same | the 88% expressed as a cohort |
| ~60% success on a single run, 25% across eight consecutive runs at production load | enterprise agent benchmarks, 2026 | the strongest number in the film |
| Evaluation gaps 64%, governance friction 57%, model reliability 51% | Forrester / Anaconda, 2026 | ranked blockers |
| ~130 real agentic vendors in a field of thousands; "agent washing" | Gartner | press release dated **25 June 2025**, re-circulating July 2026 |
| >40% of agentic AI projects cancelled by end of 2027 | Gartner, same release | as above |

**The Gartner material is a June 2025 primary that went viral again last week.** It is fair to
cite and unfair to call new. Nothing in the caption claims it is this week's research.

**These are enterprise-scale numbers and the ICP is 2 to 50 employees.** No eight-person
company runs 33 pilots. The film states the research as research, then lands beat 5 on founder
scale. The caption does the same. Do not restate the enterprise framing as if it were the
reader's own experience.

**The three survival behaviours are Ultron's and all three were filmed in episode 02**, from
the operator's own console recording: shell exec to a live URL, a browser opened against the
deployed page, and HUMAN GATE holding the send. Nothing here is a roadmap promise.

**No operator-confession hook.** The numbers belong to IDC and Gartner, so "I watched 33
pilots die" would be a fabricated result under CLAUDE.md 21. The authority comes from naming
the sources on screen. This is the one film in the series that cannot use the section 26
"I plus a number" opener, and that is deliberate.

---

## INSTAGRAM REELS CAPTION (short)

Cover frame: `survive-film-04-cover.png`.

Most AI agents do not fail. They pass the demo and then quietly stop being opened.

IDC put a number on it: 88% of agent pilots never reach production. 33 start, 4 go live.

The reason is not intelligence, it is repetition. Six in ten on one run becomes one in four
across eight, and a demo is one run.

The ones that survive ship to a real address, check their own work, and keep a human on the
send.

Comment SURVIVE and I will send you the exact setup.

#claude #ai #founder #startup #buildinpublic

---

## LINKEDIN CAPTION

Your AI agent is not going to fail loudly.
It will pass the demo, and then you will quietly stop opening it.

- - -

IDC put a number on the thing everyone suspects: 88% of agent proofs of concept never reach
broad production. For every 33 a company starts, four go live. I have watched founders read
that stat and assume it is an enterprise problem. It is not. At eight people the same failure
looks like the AI workflow you set up in January and stopped opening in March, with a sample
size of one.

- - -

→ The reason is not intelligence, it is repetition. An agent that succeeds six times in ten
on a single run drops to one in four across eight consecutive runs at production load.

→ A demo is one run. That is the whole trick. A rebranded chatbot and a real agent are
indistinguishable until the second attempt, which is why Gartner counts only about 130 real
agentic vendors in a field of thousands and calls the rest agent washing.

→ Ranked by the teams who actually ran them, three things kill agents: evaluation gaps at 64%,
governance friction at 57%, model reliability at 51%. Note that two of the three are not model
problems at all.

→ Gartner expects more than 40% of agentic AI projects to be cancelled by the end of 2027.
That forecast is from June 2025 and it has aged into a description rather than a prediction.

→ The ones that make it out do three unglamorous things: they ship to a real address, they
check their own work before calling it done, and a human approves before anything sends.

- - -

The uncomfortable read is that the winning behaviours are not intelligence features. Shipping
to a real URL, verifying your own output, and holding the send for a person are governance,
and governance is the 57% almost nobody built. An agent that is right three times in four does
not need more autonomy, it needs someone on the send button. Output you still have to check is
not finished work, it is homework.

- - -

Follow for one AI system for founders every day.
Comment SURVIVE and I will send you the exact Claude setup we used.

---

## FIRST COMMENT

The number that should worry founders is not 88%. It is that six in ten on one run becomes one
in four across eight, because every demo you have ever been shown was one run.

Two of the three things that kill agents are governance, not intelligence. Ship to a real
address, verify your own output, keep a human on the send.

Drop SURVIVE below and I will send you the exact setup.

---

## VIDEO DESCRIPTION / ALT

Vertical film that changes brand system halfway through. It opens on cream with the line '88%
of AI agents never leave the demo' filling the frame, with 88% and DEMO on solid book-orange
blocks. A headline reading 88% of agent pilots never reach broad production, sourced to IDC
2026, sits above a grid of 33 tiles labelled PILOT 01 to PILOT 33. Twenty-nine of them turn
black one after another while four stay lit in book-orange and read live, over a tally of 33
started, 4 reached live operation, 29 never left the demo. Next, eight full-height columns
labelled RUN 1 to RUN 8 show the surviving share in orange collapsing from 60% to 25% while
the black failed share takes over the frame. Three ranked bars follow: evaluation gaps 64%,
governance friction 57%, model reliability 51%. A field of small marks then shows roughly 130
real vendors among thousands, beside notes on agent washing and Gartner's 40% cancellation
forecast. The whole frame then flips to near-black Dark Ultron for the closing section, headed
12% make it out, with three numbered rules: it ships to a real address, tagged SENTINEL; it
checks its own work, tagged SENTINEL; a human approves the send, tagged HUMAN GATE. Closes on
'output you verified, not homework', a Comment SURVIVE call to action and the Ultron logo.

---

## WHY THIS ONE IS BUILT DIFFERENTLY

Episode 01 posted and held over half its traffic through second three, then fell to 10-12%
from second four at an 80%+ skip rate. `content/_retention.py` measured the frames and found
the cause: coverage collapsed 70% the moment the hook left, and the scenes never recovered
past 71% of it. The graphic really was too thin, and now it is a number rather than a feeling.

Episode 04 is the first built against that measurement:

| | ep 01 | ep 04 |
|---|---|---|
| hook coverage | 0.069 | 0.076 |
| body coverage | 0.030 to 0.049 | 0.093 to 0.132 |
| body as share of hook | 43% to 71% | 122% to 173% |
| largest dead band | 583px (ep 02 pre-fix) | 3px |
| retention guard | FAIL | PASS |

The frame gets fuller as the film runs instead of emptier. Two design rules came out of it and
are now in FILM-SERIES.md: a full-bleed sheet rather than a centred card, and never fade
content to grey to retire it, because a state that dims is a state that measures empty. The
killed pilots and the failed run share both go black on cream, which raises coverage and reads
harder at the same time.
