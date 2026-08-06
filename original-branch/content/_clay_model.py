#!/usr/bin/env python3
"""Model deck for the ULTRON CLAY direction: the time-boxed transformation genre.

Not a feature tour. The promise is an outcome with a clock on it, the middle is the run, and
the payoff is the identity change: you did the work of a team you never hired.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _clay import build, dial, cards, badge, stack3, phone, grid2, rail

STEPS = ["2H", "6H", "24H", "48H"]

SLIDES = [
 dict(eyebrow="THE 48 HOUR RUN",
      h="48 HOURS.<br>ONE PAYING<br><em>CUSTOMER.</em>",
      sub="No team. No code. No agency invoice.",
      body="While the plan is still in a doc, this one has already sent, "
           "built and closed.",
      obj=dial("48", "HOURS", pip=True), rail=""),

 dict(eyebrow="HOUR 1 - 2",
      h="FIND<br><em>THEM.</em>",
      sub="Forty accounts, ranked before the coffee goes cold.",
      body="CORTEX reads the company, the person who signs and the signal "
           "that says now, in one pass.",
      obj=cards([
        dict(n="01", b="Reads the company", i="sector, size, region, the stack they pay for"),
        dict(n="02", b="Finds who signs", i="what they own and what they posted", acc=True),
        dict(n="03", b="Ranks the forty", i="one page, before you open a tab"),
      ]), rail=rail(STEPS, 0)),

 dict(eyebrow="HOUR 3 - 6",
      h="REACH<br><em>THEM.</em>",
      sub="Every message written on what CORTEX just found.",
      body="SPECTER writes the first touch and the follow ups. You approve. "
           "Nothing sends without you.",
      obj=stack3([
        dict(b="THE TRIGGER", u="why now, in one line"),
        dict(b="THE ASK", u="a question, not a pitch", acc=True),
        dict(b="THE GATE", u="you approve before it sends", inset=True),
      ]), rail=rail(STEPS, 1)),

 dict(eyebrow="HOUR 7 - 24",
      h="BUILD<br><em>IT.</em>",
      sub="The page they land on ships while you sleep.",
      body="SENTINEL writes the files, runs the deploy, opens a browser and "
           "checks its own work before it calls it done.",
      obj=grid2([
        dict(u="WRITES", b="Files", i="pages, copy, the form"),
        dict(u="RUNS", b="Deploy", i="shell exec to a live URL", acc=True),
        dict(u="OPENS", b="Browser", i="checks the page renders"),
        dict(u="SHIPS", b="The PR", i="branch, commit, opened"),
      ]), rail=rail(STEPS, 2)),

 dict(eyebrow="HOUR 25 - 48",
      h="CLOSE<br><em>THEM.</em>",
      sub="The objection you were about to walk past, surfaced.",
      body="STRIKER runs qualification, handles the objection and drafts the "
           "close plan. You are the one who says yes.",
      obj=phone([(34, False), (52, False), (44, True), (78, True)],
                "FIRST SALE", "$49"),
      rail=rail(STEPS, 3)),

 dict(eyebrow="WHAT ACTUALLY CHANGED",
      h="YOU DID NOT<br>WORK <em>HARDER.</em>",
      sub="You ran a team you never hired.",
      body="Seven agents, one operator, one gate. The work of a GTM team, "
           "and the payroll of none of it.",
      obj=cards([
        dict(n="0", b="Hires", i="no roles to define, no onboarding"),
        dict(n="7", b="Agents", i="research, outbound, deals, content, code", acc=True),
        dict(n="1", b="Operator", i="you, holding the send button"),
      ]), rail=""),

 dict(eyebrow="COMMENT",
      h="48H",
      sub="and I will send you the exact run.",
      body="The prompts, the order, and where the human gate sits. "
           "Same system, your next 48 hours.",
      obj=badge("ALL ACCESS", "THE 48 HOUR RUN",
                "ACCESS: GRANTED", "51ULTRON.COM"), rail=""),
]

if __name__ == "__main__":
    p = build("clay-01-48h", "48 HOUR RUN", SLIDES)
    print(f"  {p.name}  {len(SLIDES)} slides")
