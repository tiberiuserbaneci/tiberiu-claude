#!/usr/bin/env python3
"""Batch 1: three decks, three designs, both themes. Validation set before serial execution.

Every subject is pegged to something dated inside the last 30 days, because the operator's
rule is that an older subject is a stale subject:

  20 Jul 2026  AMD commits up to $5B to Anthropic and deploys chips
  16 Jul 2026  Claude Code called the hottest piece of software in the world
  09 Jul 2026  Anthropic opens IPO investor meetings

Model names are current on purpose. A deck that says Opus 4.x in August 2026 reads as a
repost of somebody else's post, so the tiers named here are Opus 5, Sonnet 5 and Haiku 4.5,
and their prices are the published ones rather than invented.

Each spec carries `reaction` - the line that goes over the operator's own face before slide 1
- and it is deliberately NOT the slide 1 hook. Repeating it would spend the second where
attention is highest saying the same thing twice.
"""
import importlib.util, pathlib

REPO = pathlib.Path("/home/user/tiberiu-claude")


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


FONTS = load("_fonts").embedded_css()
DK = load("_glassdeck")
CSS = load("_deck_css").CSS

# ---------------------------------------------------------------- deck A: verdict / black
A = {
    "id": "deck-a-wrong", "design": "verdict", "theme": "black", "keyword": "WRONG",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction": "Claude Code is the hottest software on earth right now. "
                "Most founders are still using it like Google.",
    "eyebrow": "It got called the hottest software on earth in July. "
               "Most people still type one line into it.",
    "hook": "7 things<br>you are doing<br><em>backwards</em>",
    "badge": "7", "badge_l": "habits that cost you a week, and what replaces each one",
    "rail_l": "each one costs you a day",
    "cta_eye": "The full seven, with the exact wording for each",
    "cta_line": "I will send you all seven, written out, ready to paste.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"h": "One line in, one answer out",
         "cn": "2x", "cl": "the work, because you do it once with it and once yourself",
         "x": "Ask it a question",
         "xw": "You get an answer, you read it, you do the work anyway.",
         "y": "Give it the job and the constraints",
         "yw": "Who it is for, what done looks like, what it must not do. "
               "The answer arrives finished."},
        {"h": "You are paying the top tier to look things up",
         "cn": "5x", "cl": "the price, for an answer the small model also gets right",
         "x": "Everything on the biggest model",
         "xw": "Opus 5 is $5 per million in, $25 out. A lookup does not need it.",
         "y": "Route the job to the tier it needs",
         "yw": "Haiku 4.5 is $1 and $5. Same answer on a lookup, a fifth of the bill."},
        {"h": "A fresh chat forgets you every time",
         "cn": "10 min", "cl": "of re-explaining, every session, forever",
         "x": "Start a new chat each time",
         "xw": "You re-explain the company, the customer and the tone. Every session.",
         "y": "Write the context once",
         "yw": "Who you sell to, how you write, what you have already tried. "
               "It stops guessing."},
        {"h": "Draft means you still have the work",
         "cn": "80%", "cl": "of the task still sitting with you when the draft arrives",
         "x": "Ask for a draft",
         "xw": "A draft is a task you have not finished. You still have to sit with it.",
         "y": "Ask for the finished thing",
         "yw": "Name the format, the length and where it is going. Then you edit, not write."},
        {"h": "It cannot check what it cannot see",
         "cn": "1", "cl": "confident wrong answer is all it takes, and it reads like the right one",
         "x": "Trust the first output",
         "xw": "It sounds right. Sounding right is not the same as being right.",
         "y": "Make it show its work",
         "yw": "Ask what it assumed and what would make it wrong. The weak part names itself."},
        {"h": "Copy and paste is not a workflow",
         "cn": "0", "cl": "of it survives the week, because it lives in a chat nobody reopens",
         "x": "Do it by hand each time",
         "xw": "The good result lives in a chat window nobody can find again.",
         "y": "Turn the good one into a run",
         "yw": "Same input shape, same output, every week, without you being in the room."},
        {"h": "Nothing should send itself",
         "cn": "100", "cl": "people get the bad line, with your name on it, in one click",
         "x": "Let it send",
         "xw": "One bad line goes to a hundred people with your name on it.",
         "y": "Approve, then send",
         "yw": "It drafts, ranks and queues. You read it once. That is the whole gate."},
    ],
}

# ---------------------------------------------------------------- deck B: receipt / white
B = {
    "id": "deck-b-bill", "design": "receipt", "theme": "white", "keyword": "BILL",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction": "AMD just put five billion dollars into the company that makes Claude. "
                "Your AI bill is still wrong.",
    "eyebrow": "AMD committed up to $5B to Anthropic in July. "
               "Compute got cheaper. Your bill did not.",
    "hook": "Where the<br>money actually<br><em>goes</em>",
    "badge": "5x", "badge_l": "PRICE GAP, TOP TIER TO BOTTOM",
    "receipt_head": "ONE MONTH  ·  PUBLISHED LIST PRICE  ·  PER MILLION TOKENS",
    "cta_eye": "The routing table, per job, with the tier each one needs",
    "cta_line": "I will send you the table I use to decide which tier gets which job.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "Opus 5, input", "v": "$5.00",
         "h": "The top tier is <em>five times</em> the bottom",
         "b": "Opus 5 costs $5 in and $25 out per million. It is worth it for hard "
              "judgement and nothing else."},
        {"t": "Opus 5, output", "v": "$25.00",
         "h": "Output is <em>five times</em> input",
         "b": "You are billed most for what it writes. Long rambling answers are the "
              "line item nobody looks at."},
        {"t": "Sonnet 5, input", "v": "$3.00",
         "h": "The default is <em>not</em> the expensive one",
         "b": "Sonnet 5 at $3 and $15 handles almost everything a founder asks in a day."},
        {"t": "Sonnet 5, output", "v": "$15.00",
         "h": "Same job, <em>40 percent</em> less",
         "b": "Moving standard work off the top tier takes 40 percent off it without "
              "changing the answer."},
        {"t": "Haiku 4.5, input", "v": "$1.00",
         "h": "A lookup costs <em>one dollar</em>",
         "b": "Classification, extraction, tagging, routing. High volume, low judgement. "
              "This is the tier for it."},
        {"t": "Haiku 4.5, output", "v": "$5.00",
         "h": "The cheap tier is <em>not</em> the weak tier",
         "b": "On a job with one right answer, the small model gets it. You are paying "
              "for judgement you did not need."},
        {"t": "The wrong tier", "v": "the whole gap",
         "h": "Most of the bill is <em>the wrong tier</em>",
         "b": "Not usage. Routing. The fix is deciding per job instead of picking a "
              "model once and forgetting."},
    ],
}

# ---------------------------------------------------------------- deck C: trace / black
C = {
    "id": "deck-c-24h", "design": "trace", "theme": "black", "keyword": "24H",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction": "Stop spending six months building a startup. "
                "Here is what twenty four hours looks like now.",
    "eyebrow": "Anthropic opened IPO meetings in July. "
               "The tools that got them there are the ones on your laptop.",
    "hook": "One founder.<br>One day.<br><em>Nobody hired</em>",
    "badge": "24h", "badge_l": "start to first reply, and what happened in each block",
    "cta_eye": "The whole run, hour by hour, with what goes in at each step",
    "cta_line": "I will send you the run, block by block, with the input for each one.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"v": "00:00", "t": "Who would actually buy this",
         "h": "Hour zero. <em>Not</em> a list",
         "b": "Forty companies with a reason to care this quarter, and the person who "
              "signs at each one. Ranked, not alphabetised."},
        {"v": "02:00", "t": "What each of them said out loud",
         "h": "The trigger is <em>public</em>",
         "b": "A hire, a launch, a post, a funding line. One real thing per company, "
              "which is what makes the first line land."},
        {"v": "04:00", "t": "Forty first emails, none of them a template",
         "h": "Forty emails, <em>forty</em> openings",
         "b": "Each one built on that company's trigger. Under sixty words. The ask is "
              "a question, because a question gets answered."},
        {"v": "06:00", "t": "You read them and press send",
         "h": "It drafts. <em>You</em> send",
         "b": "Nothing leaves without you reading it. That is not a limitation, it is "
              "the reason your name survives the campaign."},
        {"v": "11:00", "t": "The first replies come back",
         "h": "The polite ones are <em>the objections</em>",
         "b": "Interesting, but we already have something. That is not a no, and it is "
              "not interest either. It is the deal asking a question."},
        {"v": "16:00", "t": "The answer to the one you would have missed",
         "h": "Answer the <em>quiet</em> one",
         "b": "The soft line you read as friendly. It decides the deal more often than "
              "the loud objection does."},
        {"v": "24:00", "t": "A ranked list of who is actually real",
         "h": "Twenty four hours, <em>one</em> real call",
         "b": "Not forty conversations. One meeting worth taking, and the reason it is "
              "the one, written down."},
    ],
}

if __name__ == "__main__":
    for spec in (A, B, C):
        html = DK.build(spec, CSS, FONTS)
        out = REPO / f"content/{spec['id']}.html"
        out.write_text(html)
        print(f"{spec['id']:14} {spec['design']:8} {spec['theme']:6} "
              f"{len(html):>10,} chars   -> {out.name}")
        print(f"               reaction: {spec['reaction']}")
