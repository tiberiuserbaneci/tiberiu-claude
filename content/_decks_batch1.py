#!/usr/bin/env python3
"""Batch 1: three decks, three designs, both themes. Validation set before serial execution.

SUBJECTS ARE FOUNDER-LED, NEVER NEWS (operator, 2026-08-08: "nu putem sa facem din profilul
meu un canal de stiri"). The first pass of this file got that exactly backwards: it made AMD's
investment and Anthropic's IPO the SUBJECT of the material. Nobody follows an operator account
for a funding round. The themes are the ones the audience is actually there for - founder led,
operator, work hack, first founder, wanna-be founder, tips for growth - and a news item is at
most a peg inside a line, never the thing the deck is about.

WHAT ACTUALLY TRAVELS ON THOSE THEMES. Pulled off Instagram the day this was written:

  2.7M  "That's really it"                                    personal admission
  2.0M  ten startup ideas for 2026                            countable list
  1.5M  quit a high-paying job at 23                          the life decision
  1.3M  "Comment 'get' to get the prompt"                     keyword CTA
  764K  "14 rules for startups, comment any I missed"         list plus an invitation to argue
  515K  "In 1995, Elon Musk faced over $100,000 in debt"      origin story with one number

None of them is an industry update. Every one is somebody's life, or a list you can act on
tonight. So each deck below is a confession or a run the operator can stand behind, and Ultron
arrives at the end as the thing that fixed it - never as the subject of the first slide.

The 30-day rule still binds, but on FACTS INSIDE the copy rather than on topics: prices,
model names and any claim have to be current. Opus 5, Sonnet 5 and Haiku 4.5 at published
list price. A deck naming Opus 4.x in August reads as somebody else's repost.

Each spec carries `reaction` - the line over the operator's own face before slide 1 - and it
is deliberately NOT the slide 1 hook. Repeating it spends the second where attention is
highest saying the same thing twice.
"""
import importlib.util, pathlib

REPO = pathlib.Path("/home/user/tiberiu-claude")


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


FONTS = load("_fonts").embedded_css()
DK = load("_glassdeck")
CSS = load("_deck_css").CSS

# --------------------------------------------- deck A: verdict / black / first-founder regret
A = {
    "id": "deck-a-year", "design": "verdict", "theme": "black", "keyword": "YEAR",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction": "Office ends at five. Mine ended at eleven. For a year. "
                "And almost none of it was the work that mattered.",
    "eyebrow": "Year one, eleven at night, every night. Here is what I was actually doing.",
    "hook": "7 things<br>that cost me<br><em>a year</em>",
    "badge": "7", "badge_l": "mistakes I made in year one, and what I would do instead",
    "rail_l": "every one of these cost me months",
    "cta_eye": "All seven, written out, with what I do instead of each",
    "cta_line": "I will send you the seven, and the exact thing that replaced each one.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"h": "I built for nine months before I sold anything",
         "cn": "9 mo", "cl": "of building for a customer who did not exist yet",
         "x": "Build it, then find who wants it",
         "xw": "Every feature felt like progress. None of it was evidence.",
         "y": "Find who wants it, then build that",
         "yw": "Forty companies with a reason to care this quarter, and the person who "
               "signs at each. Then you know what to build."},
        {"h": "I did everything, so nothing got done properly",
         "cn": "0", "cl": "of it was the work only I could have done",
         "x": "Do all of it yourself",
         "xw": "Research, outreach, follow up, invoices, the deck. All of it, badly.",
         "y": "Keep only what needs you",
         "yw": "The judgement calls and the relationships. Everything upstream of those "
               "is a run that goes without you in the room."},
        {"h": "I waited until it was ready. It never was",
         "cn": "4 mo", "cl": "of polish nobody asked for and nobody noticed",
         "x": "Ship when it is ready",
         "xw": "Ready is a feeling, and the feeling never arrives on its own.",
         "y": "Ship when someone is waiting",
         "yw": "Get one person who wants it by Friday. The deadline stops being yours "
               "and the polish stops being infinite."},
        {"h": "I chased every lead that answered",
         "cn": "41", "cl": "open deals, and nine of them were real",
         "x": "Work every lead that replies",
         "xw": "A reply feels like a deal. Quiet feels like alive. Neither is true.",
         "y": "Rank them before you work them",
         "yw": "Who can sign, who has a reason this quarter, who moved in the last "
               "two weeks. The rest is a list you are carrying, not a pipeline."},
        {"h": "I started from zero every single morning",
         "cn": "10 min", "cl": "re-explaining my own company, every session, forever",
         "x": "Open a blank page each day",
         "xw": "You explain who you sell to and how you write. Again. And again.",
         "y": "Write the context once",
         "yw": "Who the buyer is, how you sound, what you already tried. Written down "
               "once, it stops guessing and you stop repeating yourself."},
        {"h": "I confused being busy with being early",
         "cn": "60 h", "cl": "a week, and the hours were the only thing scaling",
         "x": "Work more hours",
         "xw": "Eleven at night is not commitment. It is the absence of leverage.",
         "y": "Build the run once",
         "yw": "The thing that worked, turned into something that happens again next "
               "week without you being awake for it."},
        {"h": "I nearly automated my own name into the ground",
         "cn": "1", "cl": "bad line, sent to a hundred people, with your name on it",
         "x": "Let the tool send it",
         "xw": "Volume is easy. Getting your name back afterwards is not.",
         "y": "It drafts, you send",
         "yw": "Everything queued, ranked and written. You read it once and press send. "
               "That gate is the whole difference."},
    ],
}

# --------------------------------------------- deck B: receipt / white / the money
B = {
    "id": "deck-b-bill", "design": "receipt", "theme": "white", "keyword": "BILL",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction": "Stop paying for AI like it is a Netflix subscription. "
                "This is what it actually costs.",
    "eyebrow": "I checked what I was actually paying for. "
               "Most of it was one decision I never made.",
    "hook": "Where the<br>money actually<br><em>goes</em>",
    "badge": "5x", "badge_l": "PRICE GAP, TOP TIER TO BOTTOM",
    "receipt_head": "PUBLISHED LIST PRICE  ·  PER MILLION TOKENS  ·  AUGUST 2026",
    "cta_eye": "The routing table, per job, with the tier each one needs",
    "cta_line": "I will send you the table I use to decide which tier gets which job.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "Opus 5, input", "v": "$5.00",
         "h": "The top tier is <em>five times</em> the bottom",
         "b": "It is worth it for hard judgement. It is not worth it for anything "
              "you could have looked up yourself."},
        {"t": "Opus 5, output", "v": "$25.00",
         "h": "You pay most for what it <em>writes</em>",
         "b": "Output costs five times input. A long rambling answer is a line item, "
              "and it is the one nobody reads."},
        {"t": "Sonnet 5, input", "v": "$3.00",
         "h": "The default is <em>not</em> the expensive one",
         "b": "Almost everything a founder asks in a day sits here. Drafting, "
              "summarising, planning, replying."},
        {"t": "Sonnet 5, output", "v": "$15.00",
         "h": "Same answer, <em>40 percent</em> less",
         "b": "Moving your standard work down one tier takes forty percent off the "
              "bill and changes nothing you would notice."},
        {"t": "Haiku 4.5, input", "v": "$1.00",
         "h": "A lookup costs <em>one dollar</em>",
         "b": "Sorting, tagging, extracting, routing. High volume, one right answer. "
              "This is the tier that exists for it."},
        {"t": "Haiku 4.5, output", "v": "$5.00",
         "h": "Cheap is <em>not</em> the same as weak",
         "b": "On a job with one correct answer the small model gets it. You were "
              "paying for judgement the job never needed."},
        {"t": "Picking one model and forgetting", "v": "the whole gap",
         "h": "It is not usage. It is <em>one decision</em>",
         "b": "You chose a model once, months ago, and every job since has run on it. "
              "That single default is most of the bill."},
    ],
}

# --------------------------------------------- deck C: trace / black / the 24 hour build
C = {
    "id": "deck-c-dayone", "design": "trace", "theme": "black", "keyword": "DAYONE",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction": "Stop spending six months building a startup. "
                "This is day one, hour by hour.",
    "eyebrow": "Not the version where you quit your job first. "
               "The version that fits in one day.",
    "hook": "Day one.<br>Start to first<br><em>real reply</em>",
    "badge": "24h", "badge_l": "idea to a person answering you, and what happens in each block",
    "cta_eye": "The whole day, block by block, with what goes in at each step",
    "cta_line": "I will send you day one, hour by hour, with the input for every block.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"v": "00:00", "t": "Name who has this problem today",
         "h": "Hour zero. <em>Not</em> an idea",
         "b": "Not a market. Forty companies with a reason to care this quarter, and "
              "the person who signs at each one."},
        {"v": "02:00", "t": "Find what each of them said out loud",
         "h": "The trigger is <em>public</em>",
         "b": "A hire, a launch, a post, a funding line. One real thing per company. "
              "That is what makes a first line land instead of bounce."},
        {"v": "04:00", "t": "Write forty first lines, none of them a template",
         "h": "Forty emails, <em>forty</em> openings",
         "b": "Each built on that company's own trigger. Under sixty words. The ask is "
              "a question, because a question is the thing people answer."},
        {"v": "06:00", "t": "Read them yourself and press send",
         "h": "It drafts. <em>You</em> send",
         "b": "Nothing leaves without you reading it. That is not a limitation, it is "
              "why your name still works next month."},
        {"v": "11:00", "t": "The first replies land while you eat",
         "h": "The polite ones <em>are</em> the objections",
         "b": "Interesting, but we already have something. That is not a no and it is "
              "not interest. It is the deal asking you a question."},
        {"v": "16:00", "t": "Answer the one you would have walked past",
         "h": "Answer the <em>quiet</em> one",
         "b": "The soft line you read as friendly. It decides more deals than the loud "
              "objection ever does, and it is the one founders skip."},
        {"v": "24:00", "t": "One person who actually wants to talk",
         "h": "One day, <em>one</em> real conversation",
         "b": "Not forty threads. One call worth taking tomorrow, and the reason it is "
              "that one, written down where you can check it."},
    ],
}

if __name__ == "__main__":
    for spec in (A, B, C):
        html = DK.build(spec, CSS, FONTS)
        out = REPO / f"content/{spec['id']}.html"
        out.write_text(html)
        print(f"{spec['id']:16} {spec['design']:8} {spec['theme']:6} -> {out.name}")
        print(f"                 REACTION: {spec['reaction']}")
