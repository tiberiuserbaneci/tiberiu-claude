#!/usr/bin/env python3
"""ULTRON CLAY decks: fast-reward promises, told in the founder's own words.

Operator, 2026-08-05, after two rejected rounds. The rules, in the order they were learned:

1. FAST REWARD. The register is "become a CEO in 24 hours" and "launch your product in 24
   hours". The viewer has to feel they could have it by tomorrow, so the clock is 24 to 72
   hours and never a month. Thirty days is a plan, not a promise.
2. NO AGENT NAMES, EVER. CORTEX, SPECTER, STRIKER, PULSE, SENTINEL, AMPLIFY and COUNSEL mean
   nothing outside this company, and a post in the movie format has already been killed for
   leaning on one. No internal mechanics as headlines either: no router, no gate, no tiers,
   no memory layer. Describe what happens in plain words.
3. GAIN, NOT AVOIDANCE. The operator cut every negatively framed theme (fire, never, cancel)
   and kept every gain (become, launch, first customer, wake up shipped, revenue). Efficiency
   does not convert at this speed; identity, revenue and a launch do.
4. THE PROMISE IS THE RUN, NOT A GUARANTEE. These describe what the system does in the time
   given. Numbers on the slides are real or plainly illustrative, never a fabricated result
   presented as measured (CLAUDE.md 21).

Object runs are asserted unique at build time, so no two decks read alike.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _clay import (build, rail, obj_name, OBJECTS, dial, cards, badge, stack3, phone, grid2,
                    bars, timeline, orbit, slip, calendar, funnel, chat, meter,
                    stamp, versus, stepper, chips, inbox, counter)

DECKS = []

# What each deck is supposed to render, in order. This is the declared intent; the run is
# read back off the built slides and checked against it, so swapping an object without
# updating this line fails the build instead of passing quietly.
MATRIX = {
    "clay-01-ceo":       ["dial", "cards", "stack3", "grid2", "phone", "versus", "badge"],
    "clay-02-launch":    ["meter", "chips", "chat", "timeline", "slip", "counter", "stamp"],
    "clay-03-48h":       ["counter", "inbox", "funnel", "chat", "phone", "stepper", "badge"],
    "clay-04-night":     ["orbit", "stepper", "cards", "calendar", "grid2", "meter", "stamp"],
    "clay-05-posts":     ["calendar", "grid2", "bars", "chips", "timeline", "counter", "badge"],
    "clay-06-72h":       ["stepper", "funnel", "versus", "slip", "inbox", "dial", "stamp"],
    "clay-07-ten":       ["chips", "orbit", "inbox", "bars", "stack3", "calendar", "badge"],
    "clay-08-investors": ["slip", "meter", "chat", "cards", "orbit", "funnel", "stamp"],
}


def D(slug, title, kw, slides):
    DECKS.append(dict(slug=slug, title=title, kw=kw, slides=slides,
                      run=[obj_name(s["obj"]) for s in slides]))


def cta(kw, sub, body, badge_title, form="badge"):
    """The ask alternates between a plaque and a seal. Eight decks closing on one identical
    pill is the saturation CLAUDE.md 30 now forbids."""
    obj = (badge("ALL ACCESS", badge_title, "ACCESS: GRANTED", "51ULTRON.COM")
           if form == "badge" else stamp(kw, badge_title))
    return dict(eyebrow="COMMENT", h=kw, sub=sub, body=body, obj=obj)


# ---------------------------------------------------------------- 01 CEO
R = ["06:00", "12:00", "18:00", "24:00"]
D("clay-01-ceo", "BECOME A CEO", "CEO", [
  dict(eyebrow="ONE DAY", h="BECOME A<br><em>CEO</em> IN<br>24 HOURS.",
       sub="You already have the title. You do not have the job.",
       body="A CEO decides and reviews. You are still doing all the work in between.",
       obj=dial("24", "HOURS")),
  dict(eyebrow="HOUR 1", h="WRITE DOWN<br>WHAT ONLY<br><em>YOU</em> CAN DO.",
       sub="It is a shorter list than you think, and it is always the same three things.",
       body="Decide, sell, say no. The rest of your calendar is delegated work you kept.",
       obj=cards([dict(n="01", b="Decide", i="the calls only you can make"),
                  dict(n="02", b="Sell", i="the rooms that need your face", acc=True),
                  dict(n="03", b="Say no", i="the thing nobody else may do")]),
       rail=rail(R, 0)),
  dict(eyebrow="HOUR 2 - 8", h="HAND OVER<br>THE <em>REST.</em>",
       sub="You describe each job once, in plain English. It runs from there.",
       body="Research, first drafts, follow ups, the page, the paperwork. Briefed, not done by you.",
       obj=stack3([dict(b="YOU DESCRIBE IT", u="one line, no forms"),
                   dict(b="IT RUNS IT", u="start to finish, unattended", acc=True),
                   dict(b="YOU APPROVE IT", u="nothing goes out without you", inset=True)]),
       rail=rail(R, 1)),
  dict(eyebrow="HOUR 9 - 20", h="IT WORKS<br>WHILE YOU<br><em>DECIDE.</em>",
       sub="You are in the two meetings that matter. Eleven other jobs are running.",
       body="None of them need you present. All of them wait for you to say yes.",
       obj=grid2([dict(u="RUNNING", b="Research", i="the accounts you named"),
                  dict(u="RUNNING", b="Outreach", i="drafted, held for you", acc=True),
                  dict(u="RUNNING", b="The page", i="built and checked"),
                  dict(u="WAITING", b="Your yes", i="the only blocker left")]),
       rail=rail(R, 2)),
  dict(eyebrow="HOUR 21 - 24", h="YOU <em>REVIEW.</em><br>YOU DO NOT<br>REBUILD.",
       sub="Twenty minutes of approvals instead of a second working day.",
       body="It arrives finished and checked, not as a draft that moves the work back to you.",
       obj=phone([(90,0),(64,0),(30,1),(9,1)], "HOURS EXECUTING", "-80%"),
       rail=rail(R, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="YOU STOPPED<br>BEING YOUR OWN<br><em>EMPLOYEE.</em>",
       sub="Same company. Same day. A different job inside it.",
       body="Founders do not burn out from deciding. They burn out executing what they decided.",
       obj=versus(dict(u="BEFORE", b="DOING", i="every job on your own desk"),
                  dict(u="AFTER", b="DIRECTING", i="you decide, it executes"))),
  cta("CEO", "and I will send you the 24 hour switch.",
      "The three things to keep, and how to hand over the rest.", "THE 24 HOUR SWITCH"),
])

# ---------------------------------------------------------------- 02 LAUNCH
R2 = ["BRIEF", "BUILD", "LIVE", "SELL"]
D("clay-02-launch", "LAUNCH IN 24H", "LAUNCH", [
  dict(eyebrow="ZERO CODE", h="LAUNCH YOUR<br>PRODUCT IN<br>24 <em>HOURS.</em>",
       sub="Not a mockup. A link you can send a customer tonight.",
       body="You have had the idea for months. The gap was never the idea.",
       obj=meter(72, "24h", "IDEA TO URL")),
  dict(eyebrow="HOUR 1", h="DESCRIBE IT<br><em>ONCE.</em>",
       sub="One paragraph. What it does, and who it is for.",
       body="No repo to clone. No stack to choose. No developer to wait on.",
       obj=chips([dict(t="a repo to clone", off=True), dict(t="a stack to choose", off=True),
                  dict(t="a dev to wait on", off=True), dict(t="one paragraph", acc=True)])),
  dict(eyebrow="HOUR 2 - 10", h="IT <em>BUILDS</em><br>THE WHOLE<br>THING.",
       sub="Pages, copy, the signup, the payment link.",
       body="Written in your voice from things you already said, not from a template.",
       obj=chat([dict(t="build the page, the signup and a way to pay"),
                 dict(t="writing the pages and the copy in your voice", you=True),
                 dict(t="signup wired, payment link live", you=True)]),
       rail=rail(R2, 1)),
  dict(eyebrow="HOUR 11 - 16", h="IT GOES<br><em>LIVE.</em>",
       sub="A real address, then it opens the page and checks it works.",
       body="Not a preview that expires. A URL that loads on your phone.",
       obj=timeline(["WRITE", "DEPLOY", "OPEN", "CONFIRM"], 3),
       rail=rail(R2, 2)),
  dict(eyebrow="HOUR 17 - 24", h="YOU SEND<br>THE <em>LINK.</em>",
       sub="To a customer. Not to a designer for feedback.",
       body="Changes are another sentence, not another two weeks.",
       obj=slip(("THE BILL", "24 HOURS"),
                [("Agency brief and revisions", "0"), ("Developer time", "0"),
                 ("Lines of code you wrote", "0"), ("Weeks of waiting", "0")],
                "TOTAL", "1 day"),
       rail=rail(R2, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="YOU STOPPED<br><em>WAITING</em> ON<br>SOMEONE ELSE.",
       sub="The bottleneck was never the product.",
       body="It was the three weeks between deciding and having something real to show.",
       obj=counter("STATUS", "LIVE", "sendable today")),
  cta("LAUNCH", "and I will send you the 24 hour build.",
      "How to brief it, and how it checks its own work.", "THE 24 HOUR LAUNCH", "stamp"),
])

# ---------------------------------------------------------------- 03 48H
R3 = ["FIND", "REACH", "SHOW", "CLOSE"]
D("clay-03-48h", "FIRST CUSTOMER", "48H", [
  dict(eyebrow="THE 48 HOUR RUN", h="YOUR FIRST<br>PAYING <em>CUSTOMER</em><br>IN 48 HOURS.",
       sub="No list bought. No team. No agency.",
       body="Two days is enough to find them, reach them, show them and ask.",
       obj=counter("FROM COLD LIST TO", "1", "paying customer")),
  dict(eyebrow="HOUR 1 - 4", h="FIND <em>WHO</em><br>WOULD BUY.",
       sub="Forty companies, and the person whose budget it comes out of.",
       body="Not a scraped list. A short one that knows why now, and who signs.",
       obj=inbox([dict(b="Northwind Systems", i="hiring two AEs this month", t="TIER 1", acc=True),
                  dict(b="Bellhaven Group", i="raised in March", t="TIER 1"),
                  dict(b="Calder and Vine", i="new ops lead, week two", t="TIER 2")]),
       rail=rail(R3, 0)),
  dict(eyebrow="HOUR 5 - 12", h="REACH <em>THEM</em><br>LIKE A HUMAN.",
       sub="One trigger, one question, under sixty words.",
       body="Written from what they actually posted, not a template with their name in it.",
       obj=funnel([dict(b="Forty written", v="40"), dict(b="You approved", v="40"),
                   dict(b="Replied", v="6")]),
       rail=rail(R3, 1)),
  dict(eyebrow="HOUR 13 - 30", h="GIVE THEM<br>SOMETHING<br>TO <em>OPEN.</em>",
       sub="A page built for this offer, live by the time they reply.",
       body="Most first replies die because there is nothing on the other end of the link.",
       obj=chat([dict(t="interesting, send me something"),
                 dict(t="here is the page", you=True),
                 dict(t="that is exactly our problem")]),
       rail=rail(R3, 2)),
  dict(eyebrow="HOUR 31 - 48", h="ASK FOR<br>THE <em>MONEY.</em>",
       sub="The objection you were about to walk past, answered first.",
       body="Most first deals are lost to silence, not to a no.",
       obj=phone([(30,0),(48,0),(46,1),(80,1)], "FIRST SALE", "$49"),
       rail=rail(R3, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="YOU STOPPED<br><em>PLANNING</em><br>THE LAUNCH.",
       sub="Two days of doing it beats two months preparing to.",
       body="Nobody validates an idea in a document. They validate it when someone pays.",
       obj=stepper(["FIND", "REACH", "SHOW", "ASK"], 3)),
  cta("48H", "and I will send you the exact 48 hour run.",
      "The order, the words, and where you approve.", "THE 48 HOUR RUN"),
])

# ---------------------------------------------------------------- 04 NIGHT
R4 = ["23:47", "02:14", "05:30", "07:02"]
D("clay-04-night", "WAKE UP SHIPPED", "NIGHT", [
  dict(eyebrow="ONE NIGHT", h="CLOSE THE<br>LAPTOP AT 11.<br>WAKE UP <em>SHIPPED.</em>",
       sub="Your company stops when you stop. It does not have to.",
       body="Eight hours a night you were never going to use anyway.",
       obj=orbit("8h", "UNATTENDED",
                 [dict(t="23:47<br>brief"), dict(t="02:14<br>build", acc=True),
                  dict(t="05:30<br>verify"), dict(t="07:02<br>done", acc=True)])),
  dict(eyebrow="23:47", h="ONE LINE<br>BEFORE <em>BED.</em>",
       sub="Not a spec. Not a ticket. One sentence of what you want.",
       body="Nobody to brief in the morning, and no standup to book.",
       obj=stepper(["TYPE IT", "SLEEP", "IT RUNS", "READ IT"], 0)),
  dict(eyebrow="02:14", h="IT DOES THE<br>WORK YOU<br><em>POSTPONED.</em>",
       sub="Reading the sources, writing the files, running the build.",
       body="The job you have moved to tomorrow four times, finished while you sleep.",
       obj=cards([dict(n="01", b="Reads what it needs", i="sources, and your own past work"),
                  dict(n="02", b="Writes the files", i="into the project, not a chat", acc=True),
                  dict(n="03", b="Runs the build", i="and fixes it when it breaks")]),
       rail=rail(R4, 1)),
  dict(eyebrow="05:30", h="IT <em>CHECKS</em><br>ITS OWN WORK.",
       sub="Opens what it made and confirms it actually works.",
       body="Work you still have to verify is not finished. It is homework with extra steps.",
       obj=calendar(("THE NIGHT", "8 HOURS UNATTENDED"), 22, 30),
       rail=rail(R4, 2)),
  dict(eyebrow="07:02", h="YOU WAKE UP<br>TO A <em>RESULT.</em>",
       sub="Three things done, sized and waiting for a yes.",
       body="The page live, this week's posts queued, the video cut.",
       obj=grid2([dict(u="LIVE", b="The page", i="open it on your phone"),
                  dict(u="QUEUED", b="The week", i="sized and slotted", acc=True),
                  dict(u="CUT", b="The video", i="ready to publish"),
                  dict(u="TYPED", b="1 line", i="at 23:47")]),
       rail=rail(R4, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="THE DAY STOPPED<br>ENDING WHEN<br><em>YOU</em> DID.",
       sub="You did not find more hours. You stopped being what they depended on.",
       body="The list you never get to is the list that gets done overnight.",
       obj=meter(88, "3", "DONE BY 07:02")),
  cta("NIGHT", "and I will send you the overnight setup.",
      "How to brief it at night, and how it verifies before it stops.", "THE OVERNIGHT RUN", "stamp"),
])

# ---------------------------------------------------------------- 05 POSTS
R5 = ["ANGLES", "HOOKS", "CUTS", "QUEUE"]
D("clay-05-posts", "30 DAYS IN AN HOUR", "POSTS", [
  dict(eyebrow="ONE HOUR", h="30 DAYS OF<br>POSTS IN<br>ONE <em>HOUR.</em>",
       sub="Not thirty posts. Thirty days you never have to think about.",
       body="You stop posting on day four because every post starts from a blank page.",
       obj=calendar(("ONE HOUR OF WORK", "30 DAYS QUEUED"), 30, 30)),
  dict(eyebrow="MINUTE 1 - 10", h="IT READS<br>WHAT YOU<br>ALREADY <em>SAID.</em>",
       sub="Your posts, your decisions, your numbers.",
       body="It writes in your voice because it read your voice, not because you described it.",
       obj=grid2([dict(u="YOUR POSTS", b="What worked", i="the ones that already landed"),
                  dict(u="YOUR CALLS", b="What changed", i="decisions, and why", acc=True),
                  dict(u="YOUR NUMBERS", b="Real ones", i="not rounded, not invented"),
                  dict(u="YOUR VOICE", b="Read", i="not imitated")])),
  dict(eyebrow="MINUTE 11 - 25", h="THIRTY <em>HOOKS</em><br>BEFORE ONE POST.",
       sub="The first line is the whole thing. Write those first.",
       body="Only the lines that stop a scroll earn a body underneath them.",
       obj=bars([dict(k="Lines written", p=100, v="30"),
                 dict(k="Worth a body", p=37, v="11", acc=True),
                 dict(k="Posted", p=30, v="9", acc=True)]),
       rail=rail(R5, 1)),
  dict(eyebrow="MINUTE 26 - 45", h="ONE IDEA.<br>THREE <em>CUTS.</em>",
       sub="A carousel, a short video and a written post are not one post resized.",
       body="Each one is cut for the place it is going, from the same idea.",
       obj=chips([dict(t="carousel, saved", acc=True), dict(t="short video, travels"),
                  dict(t="written, argued about"), dict(t="one idea", acc=True)]),
       rail=rail(R5, 2)),
  dict(eyebrow="MINUTE 46 - 60", h="A MONTH,<br><em>QUEUED.</em>",
       sub="Slotted for your window, waiting on one approval.",
       body="You say yes once instead of thirty times, then stop thinking about it.",
       obj=timeline(["WRITE", "CUT", "SLOT", "APPROVE"], 3),
       rail=rail(R5, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="CONSISTENCY<br>STOPPED BEING<br><em>DISCIPLINE.</em>",
       sub="Nobody posts daily on willpower.",
       body="They post daily because it was written before the day started.",
       obj=counter("POSTS THIS MONTH", "30", "one hour of work")),
  cta("POSTS", "and I will send you the one hour content run.",
      "Angles, thirty hooks, the cuts and the queue.", "THE 30 DAY QUEUE"),
])

# ---------------------------------------------------------------- 06 72H
R6 = ["MON", "TUE", "WED", "THU"]
D("clay-06-72h", "IDEA TO REVENUE", "72H", [
  dict(eyebrow="ONE WEEK", h="IDEA <em>MONDAY.</em><br>REVENUE<br><em>THURSDAY.</em>",
       sub="The whole arc, inside one working week.",
       body="Most ideas die in the gap between having them and having something to show.",
       obj=stepper(["TEST", "BUILD", "SEND", "CHARGE"], 3)),
  dict(eyebrow="MONDAY", h="TEST IT<br>BEFORE YOU<br><em>BUILD</em> IT.",
       sub="Who has this problem, and do they pay for anything near it today.",
       body="An afternoon of checking beats a month of building the wrong thing.",
       obj=funnel([dict(b="Companies like this", v="900"),
                   dict(b="Already paying for near", v="240"),
                   dict(b="Underserved", v="61")]),
       rail=rail(R6, 0)),
  dict(eyebrow="TUESDAY", h="BUILD THE<br>SMALLEST <em>REAL</em><br>VERSION.",
       sub="Live, takes money, does one thing properly.",
       body="Not a waitlist. Not a landing page with a form. Something that works.",
       obj=versus(dict(u="A WAITLIST", b="0", i="collects emails, proves nothing"),
                  dict(u="LIVE AND PRICED", b="1", i="can take money today")),
       rail=rail(R6, 1)),
  dict(eyebrow="WEDNESDAY", h="PUT IT IN<br>FRONT OF<br>FORTY <em>PEOPLE.</em>",
       sub="Named, reachable, and picked for a reason.",
       body="Forty right people beats four hundred addresses, every time.",
       obj=slip(("WEDNESDAY", "THE SEND LIST"),
                [("Named people", "40"), ("Scraped addresses", "0"),
                 ("Written from a real signal", "40"), ("Approved by you", "40")],
                "SENT", "40"),
       rail=rail(R6, 2)),
  dict(eyebrow="THURSDAY", h="THE FIRST<br>ONE <em>PAYS.</em>",
       sub="Not validation. Money, from someone you did not know on Monday.",
       body="One paying customer tells you more than a hundred conversations did.",
       obj=inbox([dict(b="Payment received", i="your first customer", t="DAY 4", acc=True),
                  dict(b="Reply from Bellhaven", i="asking for a call", t="DAY 3"),
                  dict(b="Page went live", i="a real address", t="DAY 2")]),
       rail=rail(R6, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="YOU STOPPED<br><em>RESEARCHING</em><br>AND SHIPPED.",
       sub="The week was never the constraint.",
       body="The constraint was how long it took to find out you were wrong.",
       obj=dial("4", "DAYS")),
  cta("72H", "and I will send you the four day run.",
      "What to test Monday, and what to ship Tuesday.", "IDEA TO REVENUE", "stamp"),
])

# ---------------------------------------------------------------- 07 TEN
R7 = ["09:00", "10:30", "12:00", "13:00"]
D("clay-07-ten", "TEAM OF TEN", "TEN", [
  dict(eyebrow="FOUR HOURS", h="WORK FOUR<br>HOURS. SHIP<br>LIKE <em>TEN.</em>",
       sub="Not a productivity trick. A different number of things running at once.",
       body="One person can only do one job at a time. That was always the ceiling.",
       obj=chips([dict(t="research", acc=True), dict(t="outreach"), dict(t="the page", acc=True),
                  dict(t="the week's posts"), dict(t="the contract", acc=True),
                  dict(t="follow ups")])),
  dict(eyebrow="09:00", h="YOU START<br><em>ELEVEN</em> JOBS.",
       sub="In about four minutes. One line each, plain English.",
       body="Research, outreach, a page, this week's posts, the contract, the follow ups.",
       obj=orbit("11", "AT ONCE",
                 [dict(t="research"), dict(t="outreach", acc=True),
                  dict(t="the page"), dict(t="the week", acc=True)]),
       rail=rail(R7, 0)),
  dict(eyebrow="10:30", h="THEY RUN<br><em>WITHOUT</em><br>YOU.",
       sub="No standup, no handover, nobody waiting on your reply to continue.",
       body="The work that used to queue behind you now runs beside itself.",
       obj=inbox([dict(b="Research", i="40 accounts ranked", t="DONE", acc=True),
                  dict(b="Outreach", i="drafted, held for you", t="WAITING"),
                  dict(b="The page", i="built and verified", t="DONE", acc=True)]),
       rail=rail(R7, 1)),
  dict(eyebrow="12:00", h="THEY HAND<br>OFF TO <em>EACH</em><br>OTHER.",
       sub="What the research found is what the outreach is written from.",
       body="A team of freelancers never does this, and it is the whole difference.",
       obj=bars([dict(k="Alone, in a queue", p=100, v="1 a time"),
                 dict(k="Together, handing off", p=44, v="11 at once", acc=True)]),
       rail=rail(R7, 2)),
  dict(eyebrow="13:00", h="YOU <em>APPROVE</em><br>AND CLOSE<br>THE LAPTOP.",
       sub="Eleven finished things, one review pass, four hours.",
       body="It arrives checked, so reviewing is reading, not redoing.",
       obj=stack3([dict(b="WHAT IT FOUND", u="feeds what it writes"),
                   dict(b="WHAT IT WROTE", u="feeds what it builds", acc=True),
                   dict(b="ONE CONTEXT", u="held across all of it", inset=True)]),
       rail=rail(R7, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="YOU STOPPED<br>BEING THE<br><em>QUEUE.</em>",
       sub="Everything used to wait its turn behind you.",
       body="Your day was never too short. It was single threaded.",
       obj=calendar(("A WORKING MONTH", "4 HOUR DAYS"), 21, 30)),
  cta("TEN", "and I will send you the four hour day.",
      "The eleven jobs, and how to start them all at once.", "THE FOUR HOUR DAY"),
])

# ---------------------------------------------------------------- 08 INVESTORS
R8 = ["NUMBERS", "STORY", "ROOM", "REPLY"]
D("clay-08-investors", "THEY CALL BACK", "INVESTORS", [
  dict(eyebrow="48 HOURS", h="BECOME THE<br>FOUNDER THEY<br><em>CALL BACK.</em>",
       sub="Nobody passes because the deck was ugly.",
       body="They pass because the answer to the second question was not ready.",
       obj=slip(("THE ASK", "48 HOURS OUT"),
                [("Numbers pulled, not remembered", "yes"), ("Cohorts charted", "yes"),
                 ("Cap table in order", "yes"), ("Objections answered", "20")],
                "READY", "48h")),
  dict(eyebrow="HOUR 1 - 6", h="YOUR OWN<br><em>NUMBERS</em><br>FIRST.",
       sub="Pulled from what actually happened, not from a memory of it.",
       body="Growth, retention, what a customer costs you and what they are worth.",
       obj=meter(64, "4", "NUMBERS THEY ASK FOR")),
  dict(eyebrow="HOUR 7 - 20", h="THE <em>STORY</em><br>THOSE NUMBERS<br>TELL.",
       sub="Not the story you wish they told.",
       body="Where you are early, where you are strong, and what the money buys.",
       obj=chat([dict(t="what is not working yet?"),
                 dict(t="churn above 40 seats, here is the cohort", you=True),
                 dict(t="good, most founders hide that")]),
       rail=rail(R8, 1)),
  dict(eyebrow="HOUR 21 - 36", h="THE ROOM<br>THEY <em>ASK</em><br>FOR NEXT.",
       sub="The one you scramble to build after the first good call.",
       body="Financials, cohorts, contracts, cap table. Assembled while the call is still warm.",
       obj=cards([dict(n="01", b="The model", i="assumptions you can stand behind"),
                  dict(n="02", b="The cohorts", i="the chart they always request", acc=True),
                  dict(n="03", b="The paper", i="contracts and cap table, in order")]),
       rail=rail(R8, 2)),
  dict(eyebrow="HOUR 37 - 48", h="THE <em>QUESTION</em><br>BEFORE THEY<br>ASK IT.",
       sub="Twenty objections, answered in writing, before the second call.",
       body="The one that kills the round is never the one you rehearsed.",
       obj=orbit("20", "ANSWERED",
                 [dict(t="market"), dict(t="churn", acc=True),
                  dict(t="moat"), dict(t="team", acc=True)]),
       rail=rail(R8, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="YOU STOPPED<br>SOUNDING<br><em>EARLY.</em>",
       sub="Same company. Same numbers. A different conversation.",
       body="Being prepared reads as being further along, because it usually is.",
       obj=funnel([dict(b="First calls", v="12"), dict(b="Second calls", v="7"),
                   dict(b="Term sheets", v="2")])),
  cta("INVESTORS", "and I will send you the 48 hour prep.",
      "The numbers to pull, and the twenty questions.", "THE 48 HOUR PREP", "stamp"),
])


def main():
    """Enforce the graphic-variety rule (CLAUDE.md 30) on what the decks actually render."""
    fail, seen, openers, used = [], {}, {}, set()
    for d in DECKS:
        slug, run = d["slug"], d["run"]
        want = MATRIX.get(slug)
        if want and run != want:
            fail.append(f"{slug} renders {','.join(run)}, the matrix declares {','.join(want)}")
        # inside one deck: a form may not come back, so the viewer never scrolls past a repeat
        dupes = {o for o in run if run.count(o) > 1}
        if dupes:
            fail.append(f"{slug} reuses {', '.join(sorted(dupes))} within the deck")
        key = ",".join(run)
        if key in seen:
            fail.append(f"{slug} repeats the object run of {seen[key]}")
        seen[key] = slug
        # across the set: two materials opening on the same form is the saturation complaint
        if run[0] in openers:
            fail.append(f"{slug} opens on {run[0]}, same as {openers[run[0]]}")
        openers[run[0]] = slug
        used.update(run)
    if fail:
        sys.exit("GRAPHIC VARIETY:\n  " + "\n  ".join(fail))

    for d in DECKS:
        p = build(d["slug"], d["title"], d["slides"])
        print(f"  {p.name:22} {len(d['slides'])} slides  {d['kw']:9} {','.join(d['run'])}")
    idle = sorted(set(OBJECTS) - used)
    print(f"{len(DECKS)} decks, {len(used)} of {len(OBJECTS)} forms in use, "
          f"every run unique, no form repeats inside a deck"
          + (f"\nunused: {', '.join(idle)}" if idle else ""))


if __name__ == "__main__":
    main()
