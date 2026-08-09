#!/usr/bin/env python3
"""Batch 5. Black, then white with a new break, then black.

  M  PRICE      verdict black          three years, three prices, all wrong differently
  N  SEVENTEEN  grid    white  break   the seventeen nos before the first yes
  O  SPLIT      score   black          which jobs still need me and which do not

N is the THIRD break shape. Two shapes alternating is still a pattern, and after console,
meter, console, meter the audience knows what the interrupt is going to be. `grid` reads
proportion by COUNTING rather than by bar length: the whole set of rejections sits on screen
at once and how few of them were real is visible before a word is read.

O is the deck that answers the operator's own complaint from two batches ago - that a reader
could not tell AI was involved at any point. It does not mention AI in the hook and it does
not have to, because the entire material is the division of labour: three jobs that still
need him, two that do not, two that are shared. Naming what it CANNOT do is the most credible
way to say what it does.

Subjects found, not assigned, and none of them is a news item: getting the price wrong,
counting the rejections, and admitting which parts of the week are no longer his.
"""
import importlib.util, pathlib

REPO = pathlib.Path("/home/user/tiberiu-claude")


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


FONTS = load("_fonts").embedded_css()
DK = load("_glassdeck")
CSS = load("_deck_css").CSS

# ------------------------------------------------------------- M: verdict / black
M = {
    "id": "deck-m-price", "design": "verdict", "theme": "black", "keyword": "PRICE",
    "family": "pricing",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction_pattern": "ignorance-reveal",
    "reaction_text": "Your price was set<br>by <em>fear</em>,<br>not by maths.",
    "reaction_say": "Mine was, three times, in three different directions. Every one of them "
                    "cost more than the last.",
    "reaction_kick": "Three years of pricing",
    "eyebrow": "Three years, three prices, and each one wrong in a different direction. Here "
               "is all of it.",
    "hook": "3 times<br>I priced it<br><em>wrong</em>",
    "badge": "4x", "badge_l": "the gap between what it cost me and what the buyer was "
                              "already paying to do it badly",
    "rail_l": "every one of these cost a quarter",
    "cta_eye": "All seven, with the one question I ask before naming a number",
    "cta_line": "I will send you the seven, and the question I ask before I name a price.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"h": "I priced from <em>my costs</em>",
         "cn": "4x", "cl": "what they were already paying to get it done badly",
         "x": "Work out your costs, add a margin",
         "xw": "The buyer has never seen your costs and does not care what they are.",
         "y": "Price against what it replaces",
         "yw": "What are they paying today to get this done badly. That number is the "
               "ceiling, and it was four times what I had been asking."},
        {"h": "Nobody <em>pushed back</em>",
         "cn": "0", "cl": "objections in eleven months, which I read as a compliment",
         "x": "No pushback means the price is right",
         "xw": "Zero objections is a signal and it is not a good one. It means you are not "
               "in the conversation they are actually having.",
         "y": "Raise it on the next three and watch",
         "yw": "Three conversations is enough to know. It costs nothing you were going to "
               "get anyway, and it is the cheapest test in the company."},
        {"h": "I discounted to <em>close</em>",
         "cn": "-30%", "cl": "on the first three, and quietly on everything after them",
         "x": "Discount to get the logo",
         "xw": "The first price you accept becomes the price. They talk to each other, and "
               "so do their finance teams.",
         "y": "Give anything except the number",
         "yw": "A longer term, a case study, an earlier start. The number is the only thing "
               "you cannot take back afterwards."},
        {"h": "I had <em>one</em> price",
         "cn": "1", "cl": "price, for two buyers who were nothing like each other",
         "x": "Keep it simple, one price",
         "xw": "Simple for you. Two buyers paying for two different jobs, and one of them "
               "was always wrong.",
         "y": "Price the job, not the software",
         "yw": "Claude ranked which deals belonged to which job. Written down, the split was "
               "obvious, and it had been sitting in the pipeline for a year."},
        {"h": "I <em>explained</em> the price",
         "cn": "9", "cl": "paragraphs on a pricing page that answered nothing",
         "x": "Justify it with features",
         "xw": "Every line of justification tells them you expect an argument, so they go "
               "and look for the argument.",
         "y": "Say what it replaces, in one line",
         "yw": "What they stop paying for or stop doing. The page stopped needing an "
               "explanation the day it said that instead of listing what is included."},
        {"h": "I moved it <em>quietly</em>",
         "cn": "2", "cl": "changes nobody was told about, and both got noticed",
         "x": "Change it and hope nobody asks",
         "xw": "Existing customers find out. Finding out on their own is worse than any "
               "increase you were afraid to announce.",
         "y": "Tell them first, with the reason",
         "yw": "The reason, the date, and what stays the same. Nobody left. The ones who "
               "would have left had already gone."},
        {"h": "I sold on <em>price</em>",
         "cn": "1", "cl": "customer who chose me for being cheapest, and left for the same reason",
         "x": "Win on being cheaper",
         "xw": "Whoever arrives for the price leaves for the price, and usually inside a "
               "quarter.",
         "y": "Win on the thing they cannot get elsewhere",
         "yw": "Say what only you do, out loud, in the first line. The people who need that "
               "specific thing stop leading with what it costs."},
    ],
}

# --------------------------------------------------------- N: grid / white / BREAK
N = {
    "id": "deck-n-seventeen", "design": "grid", "theme": "white", "keyword": "SEVENTEEN",
    "family": "rejection", "break": True,
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "unit": "nos", "win": "YES",
    "reaction_pattern": "anticlimax",
    "reaction_text": "Only <em>two</em> of them<br>actually<br>meant no.",
    "reaction_say": "Seventeen people said no before anyone said yes. I sorted all of them "
                    "and only two were real. That is genuinely it.",
    "reaction_kick": "Before the first yes",
    "eyebrow": "Seventeen people said no before anyone said yes, and I kept every one of them.",
    "hook": "17 nos<br>before the<br>first <em>yes</em>",
    "cta_eye": "All seventeen, sorted, with what each kind of no actually means",
    "cta_line": "I will send you the seventeen, sorted, and what each type of no really means.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"n": 4, "t": "NOT NOW",
         "h": "Four said <em>not now</em>",
         "b": "The most common no and the least useful, because it is not a no. Four people, "
              "no budget cycle named, no date attached. Three of the four never came back.",
         "a": "no date attached  ->  it was a no"},
        {"n": 3, "t": "WE BUILT IT",
         "h": "Three had <em>built it</em>",
         "b": "Internally, badly, and not about to admit that to a stranger. This is the no "
              "that becomes a yes eighteen months later, when the person who built it leaves.",
         "a": "built internally  ->  come back when they hire"},
        {"n": 3, "t": "WRONG PERSON",
         "h": "Three were the <em>wrong person</em>",
         "b": "Interested, encouraging, and unable to sign anything. Three of my seventeen "
              "were not rejections at all. They were me writing to whoever answered.",
         "a": "a fan is not a buyer"},
        {"n": 2, "t": "TOO EXPENSIVE",
         "h": "Two said <em>too expensive</em>",
         "b": "Only two, which surprised me, because price is the objection founders fear "
              "most. Both meant it was not worth it, which is a value problem in a price "
              "costume.",
         "a": "price named  ->  usually value unclear"},
        {"n": 2, "t": "NO REPLY",
         "h": "Two never <em>replied</em> again",
         "b": "After a good call. That is the one that keeps you awake, and the honest "
              "answer is that something changed on their side that had nothing to do with me.",
         "a": "silence after a good call  ->  not about you"},
        {"n": 2, "t": "REAL REASON",
         "h": "Two had a <em>real</em> reason",
         "b": "A funding round and a round of redundancies. Both said so plainly and both "
              "said when to come back. One of them is a customer now, fourteen months later.",
         "a": "a real reason arrives with a date"},
        {"n": 1, "t": "MY MISTAKE",
         "h": "One was just <em>wrong for it</em>",
         "b": "That company should never have been on the list. My error, not their no. "
              "Claude reading all seventeen together is how the pattern surfaced, and the "
              "list stopped producing that kind of no.",
         "a": "one bad no  ->  a fixable list"},
    ],
}

# ------------------------------------------------------------- O: score / black
O = {
    "id": "deck-o-split", "design": "score", "theme": "black", "keyword": "SPLIT",
    "family": "whodoeswhat",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "col0": "THE JOB", "cols": ["ME", "IT", "BOTH"],
    "reaction_pattern": "cautionary",
    "reaction_text": "Hand over the<br><em>wrong</em> job<br>and you find out.",
    "reaction_say": "Seven jobs in my week. I handed over four of them, and the three I kept "
                    "are the reason the company is still mine.",
    "reaction_kick": "What still needs me",
    "eyebrow": "Seven jobs in my week. Three still need me, two do not, and two are shared.",
    "hook": "What still<br>needs <em>me</em>",
    "badge": "7", "badge_l": "jobs in a founder's week, and which of them I am still doing",
    "cta_eye": "All seven, with the exact point where each one hands over",
    "cta_line": "I will send you the seven, and where the handover actually happens on each.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "Finding who to write to", "m": ["no", "yes", "no"],
         "h": "Finding who: <em>not me</em>",
         "b": "Forty companies with a reason to care this quarter and the person who signs "
              "at each. It was an afternoon a week and it is the cleanest handover here."},
        {"t": "Writing the first line", "m": ["no", "no", "yes"],
         "h": "The first line: <em>both</em>",
         "b": "It drafts forty, each from a real trigger. I read them and I press send. The "
              "gate costs ten minutes and it is the reason my name still works."},
        {"t": "Deciding what a reply means", "m": ["yes", "no", "no"],
         "h": "Reading a reply: <em>me</em>",
         "b": "It can tell me what they are protecting. It cannot tell me whether I want "
              "this customer, and that second question is the entire job."},
        {"t": "Reading the contract", "m": ["no", "no", "yes"],
         "h": "The contract: <em>both</em>",
         "b": "Three clauses that are not market and why each matters to me. I sign it. It "
              "does not, and none of it is legal advice."},
        {"t": "Ranking the pipeline", "m": ["no", "yes", "no"],
         "h": "The pipeline: <em>not me</em>",
         "b": "What moved, who can sign, what is stale. Four hours a week to produce a "
              "number, and now the number is there before I sit down on a Sunday."},
        {"t": "Saying no to a customer", "m": ["yes", "no", "no"],
         "h": "Saying no: <em>me</em>",
         "b": "It writes a better no than I do when I am tired. It cannot decide which "
              "relationship is worth keeping, and that decision is the whole point of the no."},
        {"t": "Deciding what we build next", "m": ["yes", "no", "no"],
         "h": "What we build: <em>me</em>",
         "b": "It ranks the complaints by how many people made them, which is genuinely "
              "useful. Choosing between two good options on incomplete information is not "
              "a job anybody can hand over."},
    ],
}

SPECS = (M, N, O)

if __name__ == "__main__":
    import re
    GD = load("_deckguard")
    RC = load("_reactioncard")
    RX = load("_reactions")

    def plain_of(html):
        s = re.sub(r"<br\s*/?>", " ", html)
        s = re.sub(r"<[^>]+>", "", s)
        return re.sub(r"\s+([.,;:?!])", r"\1", re.sub(r"\s+", " ", s)).strip()

    for spec in SPECS:
        GD.register(spec)
        plain = plain_of(spec["reaction_text"])
        d = REPO / f"content/decks/{spec['id']}"
        d.mkdir(parents=True, exist_ok=True)
        (d / "reaction.md").write_text(
            f"# Reaction opener - {spec['id']}\n\n"
            f"**Kicker (small, above)**  {spec['reaction_kick']}\n\n"
            f"**ON SCREEN** (what they read, keep it short)\n\n> {plain}\n\n"
            f"**YOU SAY** (over the same shot)\n\n> {spec['reaction_say']}\n\n"
            f"**Then** slide 1, which does NOT repeat this line.\n\n"
            f"**Pattern** {RX.cite(spec['reaction_pattern'])}\n\n"
            f"> {RX.BY_ID[spec['reaction_pattern']]['src']}\n\n"
            f"{RX.BY_ID[spec['reaction_pattern']]['why']}\n\n"
            f"**Keyword** {spec['keyword']}\n\n"
            f"Files: `reaction-overlay.png` drops straight over your footage "
            f"(transparent), `reaction-preview.png` is how it reads.\n")
        for variant in ("reel", "carousel"):
            out = REPO / f"content/build/{spec['id']}-{variant}.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(DK.build(spec, CSS, FONTS, variant))
        print(f"{spec['id']:18} {spec['design']:8} {spec['theme']:6} "
              f"{'BREAK' if spec.get('break') else '':6}  {plain}")
    for mode in ("preview", "alpha"):
        (REPO / f"content/reactions5-{mode}.html").write_text(RC.page(SPECS, FONTS, mode))
