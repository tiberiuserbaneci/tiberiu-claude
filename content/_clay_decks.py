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
from _clay import build, dial, cards, badge, stack3, phone, grid2, rail

DECKS = []


def D(slug, title, kw, slides, run):
    DECKS.append(dict(slug=slug, title=title, kw=kw, slides=slides, run=run))


def cta(kw, sub, body, badge_title):
    return dict(eyebrow="COMMENT", h=kw, sub=sub, body=body,
                obj=badge("ALL ACCESS", badge_title, "ACCESS: GRANTED", "51ULTRON.COM"))


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
       obj=badge("THE SWITCH", "FROM DOING<br>TO DIRECTING", "DECISIONS: YOURS", "EXECUTION: NOT")),
  cta("CEO", "and I will send you the 24 hour switch.",
      "The three things to keep, and how to hand over the rest.", "THE 24 HOUR SWITCH"),
], run="dial,cards,stack3,grid2,phone,badge,badge")

# ---------------------------------------------------------------- 02 LAUNCH
R2 = ["BRIEF", "BUILD", "LIVE", "SELL"]
D("clay-02-launch", "LAUNCH IN 24H", "LAUNCH", [
  dict(eyebrow="ZERO CODE", h="LAUNCH YOUR<br>PRODUCT IN<br>24 <em>HOURS.</em>",
       sub="Not a mockup. A link you can send a customer tonight.",
       body="You have had the idea for months. The gap was never the idea.",
       obj=dial("24", "HOURS")),
  dict(eyebrow="HOUR 1", h="DESCRIBE IT<br><em>ONCE.</em>",
       sub="One paragraph. What it does, and who it is for.",
       body="No repo to clone. No stack to choose. No developer to wait on.",
       obj=badge("THE BRIEF", "ONE PARAGRAPH", "REPO: NONE", "DEV: NONE")),
  dict(eyebrow="HOUR 2 - 10", h="IT <em>BUILDS</em><br>THE WHOLE<br>THING.",
       sub="Pages, copy, the signup, the payment link.",
       body="Written in your voice from things you already said, not from a template.",
       obj=cards([dict(n="01", b="The page", i="layout, copy, states"),
                  dict(n="02", b="The signup", i="wired to somewhere real", acc=True),
                  dict(n="03", b="The payment", i="so it can actually take money")]),
       rail=rail(R2, 1)),
  dict(eyebrow="HOUR 11 - 16", h="IT GOES<br><em>LIVE.</em>",
       sub="A real address, then it opens the page and checks it works.",
       body="Not a preview that expires. A URL that loads on your phone.",
       obj=stack3([dict(b="DEPLOYED", u="a real address"),
                   dict(b="OPENED AND CHECKED", u="it renders, the form fires", acc=True),
                   dict(b="THEN DONE", u="not before", inset=True)]),
       rail=rail(R2, 2)),
  dict(eyebrow="HOUR 17 - 24", h="YOU SEND<br>THE <em>LINK.</em>",
       sub="To a customer. Not to a designer for feedback.",
       body="Changes are another sentence, not another two weeks.",
       obj=grid2([dict(u="BEFORE", b="3 wks", i="brief, wait, review, wait"),
                  dict(u="AFTER", b="1 day", i="describe, ship, send", acc=True),
                  dict(u="AGENCY", b="0", i="no invoice"),
                  dict(u="CODE", b="0", i="you wrote none")]),
       rail=rail(R2, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="YOU STOPPED<br><em>WAITING</em> ON<br>SOMEONE ELSE.",
       sub="The bottleneck was never the product.",
       body="It was the three weeks between deciding and having something real to show.",
       obj=phone([(14,0),(36,0),(66,1),(96,1)], "STATUS", "LIVE")),
  cta("LAUNCH", "and I will send you the 24 hour build.",
      "How to brief it, and how it checks its own work.", "THE 24 HOUR LAUNCH"),
], run="dial,badge,cards,stack3,grid2,phone,badge")

# ---------------------------------------------------------------- 03 48H
R3 = ["FIND", "REACH", "SHOW", "CLOSE"]
D("clay-03-48h", "FIRST CUSTOMER", "48H", [
  dict(eyebrow="THE 48 HOUR RUN", h="YOUR FIRST<br>PAYING <em>CUSTOMER</em><br>IN 48 HOURS.",
       sub="No list bought. No team. No agency.",
       body="Two days is enough to find them, reach them, show them and ask.",
       obj=dial("48", "HOURS")),
  dict(eyebrow="HOUR 1 - 4", h="FIND <em>WHO</em><br>WOULD BUY.",
       sub="Forty companies, and the person whose budget it comes out of.",
       body="Not a scraped list. A short one that knows why now, and who signs.",
       obj=grid2([dict(u="WHO", b="40 firms", i="inside your ICP, not near it"),
                  dict(u="WHOM", b="1 name", i="the one who signs", acc=True),
                  dict(u="WHY NOW", b="A signal", i="funding, hiring, a launch"),
                  dict(u="ORDER", b="Ranked", i="who to work first")]),
       rail=rail(R3, 0)),
  dict(eyebrow="HOUR 5 - 12", h="REACH <em>THEM</em><br>LIKE A HUMAN.",
       sub="One trigger, one question, under sixty words.",
       body="Written from what they actually posted, not a template with their name in it.",
       obj=cards([dict(n="01", b="One specific trigger", i="the reason you write today"),
                  dict(n="02", b="An ask, not a pitch", i="answerable in one line", acc=True),
                  dict(n="03", b="You approve each one", i="nothing sends without you")]),
       rail=rail(R3, 1)),
  dict(eyebrow="HOUR 13 - 30", h="GIVE THEM<br>SOMETHING<br>TO <em>OPEN.</em>",
       sub="A page built for this offer, live by the time they reply.",
       body="Most first replies die because there is nothing on the other end of the link.",
       obj=stack3([dict(b="A REAL PAGE", u="not a deck attachment"),
                   dict(b="THEIR PROBLEM ON IT", u="in their words", acc=True),
                   dict(b="A WAY TO PAY", u="live, today", inset=True)]),
       rail=rail(R3, 2)),
  dict(eyebrow="HOUR 31 - 48", h="ASK FOR<br>THE <em>MONEY.</em>",
       sub="The objection you were about to walk past, answered first.",
       body="Most first deals are lost to silence, not to a no.",
       obj=phone([(30,0),(48,0),(46,1),(80,1)], "FIRST SALE", "$49"),
       rail=rail(R3, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="YOU STOPPED<br><em>PLANNING</em><br>THE LAUNCH.",
       sub="Two days of doing it beats two months preparing to.",
       body="Nobody validates an idea in a document. They validate it when someone pays.",
       obj=badge("THE RUN", "FIND, REACH,<br>SHOW, ASK", "DAYS: 2", "TEAM: 1")),
  cta("48H", "and I will send you the exact 48 hour run.",
      "The order, the words, and where you approve.", "THE 48 HOUR RUN"),
], run="dial,grid2,cards,stack3,phone,badge,badge")

# ---------------------------------------------------------------- 04 NIGHT
R4 = ["23:47", "02:14", "05:30", "07:02"]
D("clay-04-night", "WAKE UP SHIPPED", "NIGHT", [
  dict(eyebrow="ONE NIGHT", h="CLOSE THE<br>LAPTOP AT 11.<br>WAKE UP <em>SHIPPED.</em>",
       sub="Your company stops when you stop. It does not have to.",
       body="Eight hours a night you were never going to use anyway.",
       obj=dial("8", "HOURS")),
  dict(eyebrow="23:47", h="ONE LINE<br>BEFORE <em>BED.</em>",
       sub="Not a spec. Not a ticket. One sentence of what you want.",
       body="Nobody to brief in the morning, and no standup to book.",
       obj=badge("THE BRIEF", "ONE SENTENCE", "SPEC: NONE", "MEETINGS: 0")),
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
       obj=stack3([dict(b="IT SHIPS", u="to a real address"),
                   dict(b="IT OPENS IT", u="and confirms it renders", acc=True),
                   dict(b="THEN IT STOPS", u="not before", inset=True)]),
       rail=rail(R4, 2)),
  dict(eyebrow="07:02", h="YOU WAKE UP<br>TO A <em>RESULT.</em>",
       sub="Three things done, sized and waiting for a yes.",
       body="The page live, this week's posts queued, the video cut.",
       obj=cards([dict(n="01", b="The page is live", i="open it on your phone"),
                  dict(n="02", b="The week is queued", i="posts sized and slotted", acc=True),
                  dict(n="03", b="The video is cut", i="ready to publish")]),
       rail=rail(R4, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="THE DAY STOPPED<br>ENDING WHEN<br><em>YOU</em> DID.",
       sub="You did not find more hours. You stopped being what they depended on.",
       body="The list you never get to is the list that gets done overnight.",
       obj=phone([(10,0),(30,0),(64,1),(97,1)], "DONE BY 07:02", "3")),
  cta("NIGHT", "and I will send you the overnight setup.",
      "How to brief it at night, and how it verifies before it stops.", "THE OVERNIGHT RUN"),
], run="dial,badge,cards,stack3,cards,phone,badge")

# ---------------------------------------------------------------- 05 POSTS
R5 = ["ANGLES", "HOOKS", "CUTS", "QUEUE"]
D("clay-05-posts", "30 DAYS IN AN HOUR", "POSTS", [
  dict(eyebrow="ONE HOUR", h="30 DAYS OF<br>POSTS IN<br>ONE <em>HOUR.</em>",
       sub="Not thirty posts. Thirty days you never have to think about.",
       body="You stop posting on day four because every post starts from a blank page.",
       obj=dial("30", "DAYS")),
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
       obj=stack3([dict(b="30 OPENING LINES", u="written and ranked first"),
                   dict(b="THE SURVIVORS", u="the ones worth writing", acc=True),
                   dict(b="THEN THE POSTS", u="under a line that works", inset=True)]),
       rail=rail(R5, 1)),
  dict(eyebrow="MINUTE 26 - 45", h="ONE IDEA.<br>THREE <em>CUTS.</em>",
       sub="A carousel, a short video and a written post are not one post resized.",
       body="Each one is cut for the place it is going, from the same idea.",
       obj=cards([dict(n="01", b="The carousel", i="the one people save"),
                  dict(n="02", b="The short video", i="the one that travels", acc=True),
                  dict(n="03", b="The written post", i="the one that starts arguments")]),
       rail=rail(R5, 2)),
  dict(eyebrow="MINUTE 46 - 60", h="A MONTH,<br><em>QUEUED.</em>",
       sub="Slotted for your window, waiting on one approval.",
       body="You say yes once instead of thirty times, then stop thinking about it.",
       obj=badge("THE QUEUE", "30 DAYS SCHEDULED", "APPROVALS: 1", "POSTS: 30"),
       rail=rail(R5, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="CONSISTENCY<br>STOPPED BEING<br><em>DISCIPLINE.</em>",
       sub="Nobody posts daily on willpower.",
       body="They post daily because it was written before the day started.",
       obj=phone([(16,0),(28,0),(60,1),(95,1)], "POSTS THIS MONTH", "30")),
  cta("POSTS", "and I will send you the one hour content run.",
      "Angles, thirty hooks, the cuts and the queue.", "THE 30 DAY QUEUE"),
], run="dial,grid2,stack3,cards,badge,phone,badge")

# ---------------------------------------------------------------- 06 72H
R6 = ["MON", "TUE", "WED", "THU"]
D("clay-06-72h", "IDEA TO REVENUE", "72H", [
  dict(eyebrow="ONE WEEK", h="IDEA <em>MONDAY.</em><br>REVENUE<br><em>THURSDAY.</em>",
       sub="The whole arc, inside one working week.",
       body="Most ideas die in the gap between having them and having something to show.",
       obj=dial("72", "HOURS")),
  dict(eyebrow="MONDAY", h="TEST IT<br>BEFORE YOU<br><em>BUILD</em> IT.",
       sub="Who has this problem, and do they pay for anything near it today.",
       body="An afternoon of checking beats a month of building the wrong thing.",
       obj=cards([dict(n="01", b="Who has it", i="and how many of them there are"),
                  dict(n="02", b="What they pay now", i="the budget already exists", acc=True),
                  dict(n="03", b="Why it is open", i="what the current answer misses")]),
       rail=rail(R6, 0)),
  dict(eyebrow="TUESDAY", h="BUILD THE<br>SMALLEST <em>REAL</em><br>VERSION.",
       sub="Live, takes money, does one thing properly.",
       body="Not a waitlist. Not a landing page with a form. Something that works.",
       obj=stack3([dict(b="ONE PROMISE", u="the thing it actually does"),
                   dict(b="ONE PAGE", u="live, on a real address", acc=True),
                   dict(b="ONE PRICE", u="it can take money today", inset=True)]),
       rail=rail(R6, 1)),
  dict(eyebrow="WEDNESDAY", h="PUT IT IN<br>FRONT OF<br>FORTY <em>PEOPLE.</em>",
       sub="Named, reachable, and picked for a reason.",
       body="Forty right people beats four hundred addresses, every time.",
       obj=badge("WEDNESDAY", "FORTY NAMED<br>PEOPLE", "SCRAPED: 0", "APPROVED BY: YOU"),
       rail=rail(R6, 2)),
  dict(eyebrow="THURSDAY", h="THE FIRST<br>ONE <em>PAYS.</em>",
       sub="Not validation. Money, from someone you did not know on Monday.",
       body="One paying customer tells you more than a hundred conversations did.",
       obj=phone([(24,0),(44,0),(52,1),(86,1)], "FIRST REVENUE", "DAY 4"),
       rail=rail(R6, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="YOU STOPPED<br><em>RESEARCHING</em><br>AND SHIPPED.",
       sub="The week was never the constraint.",
       body="The constraint was how long it took to find out you were wrong.",
       obj=badge("THE WEEK", "TEST, BUILD,<br>SEND, CHARGE", "DAYS: 4", "TEAM: 1")),
  cta("72H", "and I will send you the four day run.",
      "What to test Monday, and what to ship Tuesday.", "IDEA TO REVENUE"),
], run="dial,cards,stack3,badge,phone,badge,badge")

# ---------------------------------------------------------------- 07 TEN
R7 = ["09:00", "10:30", "12:00", "13:00"]
D("clay-07-ten", "TEAM OF TEN", "TEN", [
  dict(eyebrow="FOUR HOURS", h="WORK FOUR<br>HOURS. SHIP<br>LIKE <em>TEN.</em>",
       sub="Not a productivity trick. A different number of things running at once.",
       body="One person can only do one job at a time. That was always the ceiling.",
       obj=dial("11", "AT ONCE")),
  dict(eyebrow="09:00", h="YOU START<br><em>ELEVEN</em> JOBS.",
       sub="In about four minutes. One line each, plain English.",
       body="Research, outreach, a page, this week's posts, the contract, the follow ups.",
       obj=cards([dict(n="01", b="You describe them", i="one line per job, no forms"),
                  dict(n="02", b="They start together", i="not one after another", acc=True),
                  dict(n="03", b="You leave", i="none of them need you present")]),
       rail=rail(R7, 0)),
  dict(eyebrow="10:30", h="THEY RUN<br><em>WITHOUT</em><br>YOU.",
       sub="No standup, no handover, nobody waiting on your reply to continue.",
       body="The work that used to queue behind you now runs beside itself.",
       obj=grid2([dict(u="RUNNING", b="Research", i="the accounts you named"),
                  dict(u="RUNNING", b="Outreach", i="drafted, held for you", acc=True),
                  dict(u="RUNNING", b="The page", i="built and verified"),
                  dict(u="RUNNING", b="The week", i="posts written and cut")]),
       rail=rail(R7, 1)),
  dict(eyebrow="12:00", h="THEY HAND<br>OFF TO <em>EACH</em><br>OTHER.",
       sub="What the research found is what the outreach is written from.",
       body="A team of freelancers never does this, and it is the whole difference.",
       obj=stack3([dict(b="WHAT IT FOUND", u="feeds what it writes"),
                   dict(b="WHAT IT WROTE", u="feeds what it builds", acc=True),
                   dict(b="ONE CONTEXT", u="held across all of it", inset=True)]),
       rail=rail(R7, 2)),
  dict(eyebrow="13:00", h="YOU <em>APPROVE</em><br>AND CLOSE<br>THE LAPTOP.",
       sub="Eleven finished things, one review pass, four hours.",
       body="It arrives checked, so reviewing is reading, not redoing.",
       obj=badge("THE DAY", "11 JOBS, 4 HOURS", "STARTED: 09:00", "DONE: 13:00"),
       rail=rail(R7, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="YOU STOPPED<br>BEING THE<br><em>QUEUE.</em>",
       sub="Everything used to wait its turn behind you.",
       body="Your day was never too short. It was single threaded.",
       obj=phone([(12,0),(34,0),(68,1),(98,1)], "JOBS IN PARALLEL", "11")),
  cta("TEN", "and I will send you the four hour day.",
      "The eleven jobs, and how to start them all at once.", "THE FOUR HOUR DAY"),
], run="dial,cards,grid2,stack3,badge,phone,badge")

# ---------------------------------------------------------------- 08 INVESTORS
R8 = ["NUMBERS", "STORY", "ROOM", "REPLY"]
D("clay-08-investors", "THEY CALL BACK", "INVESTORS", [
  dict(eyebrow="48 HOURS", h="BECOME THE<br>FOUNDER THEY<br><em>CALL BACK.</em>",
       sub="Nobody passes because the deck was ugly.",
       body="They pass because the answer to the second question was not ready.",
       obj=dial("48", "HOURS")),
  dict(eyebrow="HOUR 1 - 6", h="YOUR OWN<br><em>NUMBERS</em><br>FIRST.",
       sub="Pulled from what actually happened, not from a memory of it.",
       body="Growth, retention, what a customer costs you and what they are worth.",
       obj=grid2([dict(u="GROWTH", b="Monthly", i="the real curve, not the good months"),
                  dict(u="RETENTION", b="By cohort", i="where they leave, and when", acc=True),
                  dict(u="COST", b="To acquire", i="all in, not just ad spend"),
                  dict(u="VALUE", b="Per customer", i="over the life, not the first month")]),
       rail=rail(R8, 0)),
  dict(eyebrow="HOUR 7 - 20", h="THE <em>STORY</em><br>THOSE NUMBERS<br>TELL.",
       sub="Not the story you wish they told.",
       body="Where you are early, where you are strong, and what the money buys.",
       obj=stack3([dict(b="WHAT IS WORKING", u="with the number under it"),
                   dict(b="WHAT IS NOT YET", u="said before they find it", acc=True),
                   dict(b="WHAT THE ROUND BUYS", u="one specific thing", inset=True)]),
       rail=rail(R8, 1)),
  dict(eyebrow="HOUR 21 - 36", h="THE ROOM<br>THEY <em>ASK</em><br>FOR NEXT.",
       sub="The one you scramble to build after the first good call.",
       body="Financials, cohorts, contracts, cap table. Assembled while the call is still warm.",
       obj=grid2([dict(u="THE MODEL", b="Defensible", i="assumptions you can stand behind"),
                  dict(u="THE COHORTS", b="Charted", i="the one they always request", acc=True),
                  dict(u="THE PAPER", b="In order", i="contracts and cap table"),
                  dict(u="THE ASK", b="Specific", i="what the money actually buys")]),
       rail=rail(R8, 2)),
  dict(eyebrow="HOUR 37 - 48", h="THE <em>QUESTION</em><br>BEFORE THEY<br>ASK IT.",
       sub="Twenty objections, answered in writing, before the second call.",
       body="The one that kills the round is never the one you rehearsed.",
       obj=badge("THE PREP", "20 OBJECTIONS<br>ANSWERED", "REHEARSED: ALL", "SURPRISED: NONE"),
       rail=rail(R8, 3)),
  dict(eyebrow="WHAT ACTUALLY CHANGED", h="YOU STOPPED<br>SOUNDING<br><em>EARLY.</em>",
       sub="Same company. Same numbers. A different conversation.",
       body="Being prepared reads as being further along, because it usually is.",
       obj=phone([(20,0),(42,0),(66,1),(94,1)], "SECOND CALLS", "+3x")),
  cta("INVESTORS", "and I will send you the 48 hour prep.",
      "The numbers to pull, and the twenty questions.", "THE 48 HOUR PREP"),
], run="dial,grid2,stack3,grid2,badge,phone,badge")


def main():
    seen = {}
    for d in DECKS:
        if d["run"] in seen:
            sys.exit(f"{d['slug']} repeats the object run of {seen[d['run']]}")
        seen[d["run"]] = d["slug"]
    for d in DECKS:
        p = build(d["slug"], d["title"], d["slides"])
        print(f"  {p.name:22} {len(d['slides'])} slides  {d['kw']:8} {d['run']}")
    print(f"{len(DECKS)} decks, every object run unique")


if __name__ == "__main__":
    main()
