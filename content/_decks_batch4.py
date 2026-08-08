#!/usr/bin/env python3
"""Batch 4. White with a new break, then black, then white.

  J  TEN     meter   white  break   where the first ten customers actually came from
  K  LAUNCH  trace   black          the week after I launched, day by day
  L  HOURS   receipt white          the seven jobs nobody invoices you for

J introduces the SECOND break shape. `console` was the only one, which made the break itself
predictable: after two of them the audience knows the interrupt is a product window, and a
predictable interrupt is not an interrupt. A chart is the right second shape because it is
simple to read and heavy to look at, which is the pair `stamp` failed - and the bar lengths
carry the argument before a word is read. The longest bar is the channel that cannot be
repeated, and you see that first.

L reuses the receipt with a declared twist. Deck B's bill was dollars on a card. This one is
hours, the payer is the founder, and the total is a week of his life. Same shape, different
unit and different victim, which is the "mic twist" the operator asked for when two materials
rhyme rather than a pretence that they do not.

Subjects stay founder-led and found rather than assigned: where the first customers came from,
the week after a launch nobody noticed, and the work that never appears on an invoice. Every
one is countable, personal, and none of them is a news item.
"""
import importlib.util, pathlib

REPO = pathlib.Path("/home/user/tiberiu-claude")


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


FONTS = load("_fonts").embedded_css()
DK = load("_glassdeck")
CSS = load("_deck_css").CSS

# ------------------------------------------------------- J: meter / white / BREAK
J = {
    "id": "deck-j-first10", "design": "meter", "theme": "white", "keyword": "TEN",
    "family": "firstcustomers", "break": True,
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "axis": "SOURCE", "unit": "CUSTOMERS",
    "reaction_pattern": "origin-number",
    "reaction_text": "Ten customers.<br>Four already<br><em>knew me</em>.",
    "reaction_say": "I counted where every one of the first ten actually came from. The two "
                    "channels everybody recommends produced zero between them.",
    "reaction_kick": "The first ten",
    "eyebrow": "Ten customers, seven sources. The two channels everybody recommends produced "
               "nothing at all.",
    "hook": "Where my<br>first 10<br><em>came from</em>",
    "cta_eye": "All ten, the source of each, and the two I would run first now",
    "cta_line": "I will send you the ten, where each one came from, and what I would run first.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "People who already knew me", "v": 4, "d": "4",
         "h": "Four already<br><em>knew me</em>",
         "b": "Four of ten came out of a network I spent eight years building and cannot "
              "build again this quarter. It is the best channel I have and the only one "
              "that does not scale.",
         "a": "great number  ->  terrible strategy"},
        {"t": "One post that worked", "v": 2, "d": "2",
         "h": "Two came from<br><em>one post</em>",
         "b": "Not forty posts. One. It named a problem in the first line, and everything "
              "else I published that month named me instead.",
         "a": "one post about them  ->  beat thirty about me"},
        {"t": "A customer who told someone", "v": 2, "d": "2",
         "h": "Two came from<br><em>one referral</em>",
         "b": "Both from the same customer, unprompted, in month four. I had no system for "
              "asking and I am not convinced that asking would have worked.",
         "a": "one happy customer  ->  two more"},
        {"t": "Cold email", "v": 1, "d": "1",
         "h": "One came from<br><em>cold email</em>",
         "b": "One out of roughly four hundred, sent by hand between other jobs. That is "
              "not a channel failing. It is a channel I never ran, because doing it "
              "properly cost an evening per ten. Claude does the reading and the first "
              "line now.",
         "a": "400 by hand  ->  1 signed"},
        {"t": "An event I almost skipped", "v": 1, "d": "1",
         "h": "One came from<br><em>a room</em>",
         "b": "A meetup I nearly cancelled, a conversation by the door, a customer six "
              "weeks later. Unrepeatable, and I count it honestly rather than calling it "
              "strategy afterwards.",
         "a": "luck is real  ->  it is not a plan"},
        {"t": "Inbound from the website", "v": 0, "d": "0",
         "h": "The website<br>brought <em>nobody</em>",
         "b": "Eleven months live, a contact form, and zero. It was a brochure for a "
              "product you had to already understand. Claude rewrote it from the problem "
              "instead of the features and it stopped being a brochure.",
         "a": "zero  ->  and I had redesigned it twice"},
        {"t": "Paid ads", "v": 0, "d": "0",
         "h": "Paid ads brought<br><em>nothing</em>",
         "b": "The channel every guide opens with, and the only one that produced nothing "
              "at all for a product this specific. I stopped in month two. I do not regret "
              "the money, only the two months of hoping.",
         "a": "spent  ->  learned  ->  stopped"},
    ],
}

# ------------------------------------------------------------- K: trace / black
K = {
    "id": "deck-k-launchweek", "design": "trace", "theme": "black", "keyword": "LAUNCH",
    "family": "launchweek",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction_pattern": "life-contrast",
    "reaction_text": "Launch day.<br>41 visitors.<br>Seven were <em>me</em>.",
    "reaction_say": "That was day one. Here is every day of the week that followed, and the "
                    "one that actually changed it was not the first.",
    "reaction_kick": "The week after launch",
    "eyebrow": "Forty one visitors on day one and seven of them were me. Here is every day "
               "that followed.",
    "hook": "The week<br>after I<br><em>launched</em>",
    "badge": "7", "badge_l": "days after launch, and the one that changed it was not day one",
    "cta_eye": "The seven days, plus the twelve messages I sent on day three",
    "cta_line": "I will send you the week day by day, and the message I wrote to the twelve.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"v": "DAY 1", "t": "I posted it and refreshed the page",
         "h": "Day one was <em>refreshing</em>",
         "b": "Forty one visitors, seven of them me. Four months of building and one "
              "afternoon of telling people. The launch was not the marketing. It was the "
              "end of the building."},
        {"v": "DAY 2", "t": "Silence, and the first bad instinct",
         "h": "Day two I wanted to <em>rebuild</em>",
         "b": "Nobody signed up, so I opened the code. Rebuilding is what founders do when "
              "they are frightened, because it is the part they are good at. I closed it "
              "again."},
        {"v": "DAY 3", "t": "Twelve messages, written by hand",
         "h": "Day three I <em>asked</em>",
         "b": "Twelve individual messages, no template. Nine replied. Not one of them had "
              "seen the post. Reach is not distribution and a post is not a launch."},
        {"v": "DAY 4", "t": "The first real objection",
         "h": "Day four somebody said <em>no</em>",
         "b": "And told me why, which is worth more than the yes I was hoping for. It was "
              "the pricing page. It explained what the product does and never once what it "
              "replaces."},
        {"v": "DAY 5", "t": "I rewrote the page from the objection",
         "h": "Day five I rewrote the <em>page</em>",
         "b": "Claude read every reply from the twelve and wrote the page from their words "
              "instead of mine. Same product. It stopped needing an explanation."},
        {"v": "DAY 6", "t": "A signup from somebody I did not know",
         "h": "Day six, a <em>stranger</em>",
         "b": "One person, nobody I had ever met. That is the whole difference between a "
              "demo and a business, and it happened on the version written from somebody "
              "else's objection."},
        {"v": "DAY 7", "t": "I stopped calling it a launch",
         "h": "Day seven it stopped being a <em>launch</em>",
         "b": "A launch is a day. Distribution is a habit. The week that worked was the one "
              "where writing to people came before opening anything else."},
    ],
}

# ------------------------------------------------------------- L: receipt / white
L = {
    "id": "deck-l-unpaid", "design": "receipt", "theme": "white", "keyword": "HOURS",
    "family": "unpaidwork",
    "twist": "same receipt shape as deck B's tool bill, but the unit is hours and the payer "
             "is the founder, so the total is a week of his life rather than a card charge",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "receipt_head": "UNBILLED  ·  ONE WEEK  ·  FOUNDER, SOLE OPERATOR",
    "reaction_pattern": "wrong-tool",
    "reaction_text": "Nobody invoices you<br>for the <em>other</em><br>34 hours.",
    "reaction_say": "I itemised the week nobody bills me for. Thirty four hours, seven line "
                    "items, and the biggest one was not the one I expected.",
    "reaction_kick": "The unbilled week",
    "eyebrow": "Nobody invoices you for any of these. You pay all of them, every week, in "
               "the only currency you cannot make more of.",
    "hook": "Seven jobs<br>you never<br><em>hired</em> for",
    "badge": "34h", "badge_l": "PER WEEK, UNBILLED",
    "total": "34h", "total_l": "unbilled, one week",
    "cta_eye": "The whole bill, and the four lines that came off it first",
    "cta_line": "I will send you the seven line bill and the four I stopped paying, in order.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "Chasing people who went quiet", "v": "6h",
         "h": "Six hours <em>chasing</em>",
         "b": "Not selling. Following up on people who already said they were interested "
              "and then stopped replying. Six hours a week of writing just checking in, in "
              "slightly different words."},
        {"t": "Answering the same five questions", "v": "5h",
         "h": "Five hours on the <em>same five</em>",
         "b": "The same five questions from every new person, typed fresh every time, "
              "because the answers lived in my head and nowhere anybody else could reach."},
        {"t": "Reading up before every call", "v": "7h",
         "h": "Seven hours <em>reading up</em>",
         "b": "The company, the person, what they posted last week. Twenty minutes a call, "
              "and it decides whether the call is good or wasted, so it never gets cut. "
              "Claude does the reading now and I get the three lines that matter."},
        {"t": "Writing the follow up", "v": "4h",
         "h": "Four hours on <em>follow ups</em>",
         "b": "The email after the call, which decides whether the call counted at all. "
              "Written late, written tired, and written last."},
        {"t": "Working out what actually moved", "v": "4h",
         "h": "Four hours finding out <em>what moved</em>",
         "b": "Reading my own pipeline to discover what changed this week. Four hours to "
              "produce a number Claude hands me in the time it takes to make coffee."},
        {"t": "Scheduling", "v": "3h",
         "h": "Three hours <em>scheduling</em>",
         "b": "Three hours a week finding a time. Not the meeting. Finding the time for "
              "the meeting."},
        {"t": "The admin nobody sees", "v": "5h",
         "h": "Five hours of <em>admin</em>",
         "b": "Invoices, contracts, expenses, the form somebody needs signed. Not work, the "
              "tax on having customers, and it is a full working day every fortnight."},
    ],
}

SPECS = (J, K, L)

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
        (REPO / f"content/reactions4-{mode}.html").write_text(RC.page(SPECS, FONTS, mode))
