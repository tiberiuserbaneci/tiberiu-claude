#!/usr/bin/env python3
"""Batch 6. White, then black with the break, then white.

  P  CALL     ledger  white          the first ten minutes of a sales call
  Q  LOST     console black  break   what I asked after losing a customer
  R  MORNING  trace   white          what happens before 8am

Two designs move theme for the first time. `ledger` has only ever run black (E, I) and `trace`
has only ever run black (C, K), so putting both on the light ground makes two familiar shapes
read as new without inventing anything. And Q is the first BREAK on a dark theme - every
previous one has been white, so the interrupt now varies by ground as well as by shape.

Q is also the third console, and a third console needs a different frame or it is just the
same window with new words in it. D was what he types on a Monday and H was what he types at
2am; this one is a single relationship, eleven months of it, pasted in at the point where it
is already over. Same object, completely different weather.

R deliberately breaks the customer-lifecycle cluster that P and Q would otherwise make. Three
decks in a row about customers is not caught by the family guard and would still read as one
long post.
"""
import importlib.util, pathlib

REPO = pathlib.Path("/home/user/tiberiu-claude")


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


FONTS = load("_fonts").embedded_css()
DK = load("_glassdeck")
CSS = load("_deck_css").CSS

# ------------------------------------------------------------- P: ledger / white
P = {
    "id": "deck-p-call", "design": "ledger", "theme": "white", "keyword": "CALL",
    "family": "discovery",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction_pattern": "imperative",
    "reaction_text": "Stop pitching.<br>Start <em>diagnosing</em>.",
    "reaction_say": "Seven things I do in the first ten minutes of a call, and not one of "
                    "them is saying what we do.",
    "reaction_kick": "First ten minutes",
    "eyebrow": "Seven things I do before I have said what we do. The call is decided in here.",
    "hook": "The first<br>10 minutes<br>of a <em>call</em>",
    "cta_eye": "All seven, with the exact wording for the two nobody does",
    "cta_line": "I will send you the seven, and the exact wording for the two nobody does.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "Ask what made them take the call",
         "h": "Why did they take <em>this</em> call",
         "b": "Not how are you. Something happened recently that made a stranger's email "
              "worth twenty minutes, and whatever that is, that is the deal. Claude hands me "
              "what changed at their company this month, so I ask about the right thing.",
         "a": "no trigger named  ->  no urgency, no deal"},
        {"t": "Find out who else is in the room",
         "h": "Who else has to <em>agree</em>",
         "b": "Asked in minute three, not week three. If the answer is vague, this is a "
              "conversation rather than a deal, and I stop selling and start mapping.",
         "a": "no named signer  ->  it has not started"},
        {"t": "Ask what they do about it today",
         "h": "What are they doing <em>today</em>",
         "b": "Every problem already has a solution, usually a person and a spreadsheet. That "
              "is the competitor, not the other software, and it is what I am priced against.",
         "a": "the spreadsheet is the competitor"},
        {"t": "Make them say the number",
         "h": "Get them to say the <em>number</em>",
         "b": "How many hours, how many deals, how much. If they cannot put a number on it, "
              "it is an irritation rather than a problem, and irritations do not get budget.",
         "a": "no number  ->  no budget"},
        {"t": "Say the thing that disqualifies",
         "h": "Say what makes it <em>wrong</em> for them",
         "b": "Out loud, early. It costs one bad fit deal and it buys every good one, because "
              "the moment you name a real limitation people start believing the rest of it.",
         "a": "one honest limit  ->  the rest becomes credible"},
        {"t": "Shut up for longer than is comfortable",
         "h": "Say <em>nothing</em> for four seconds",
         "b": "The second thing they say is the true one. The first is the version they "
              "prepared on the way in. Four seconds of silence is the cheapest question in "
              "sales and almost nobody can hold it.",
         "a": "the second answer  ->  the real one"},
        {"t": "Agree the next step before you hang up",
         "h": "Book it <em>on the call</em>",
         "b": "Not I will follow up. A date, a person, and what has to be true by then. "
              "Everything I have ever left to email has died in email.",
         "a": "left to email  ->  it dies in email"},
    ],
}

# ------------------------------------------------------ Q: console / black / BREAK
Q = {
    "id": "deck-q-lost", "design": "console", "theme": "black", "keyword": "LOST",
    "family": "churn", "break": True,
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "window": "ULTRON  ·  ELEVEN MONTHS, ONE THREAD",
    "reaction_pattern": "origin-number",
    "reaction_text": "Month nine.<br>One customer.<br><em>Gone</em>.",
    "reaction_say": "I pasted eleven months of the relationship in and asked what I missed. "
                    "The answer was in month three.",
    "reaction_kick": "The one that left",
    "eyebrow": "One customer, eleven months, and the month it ended was not the month they "
               "cancelled.",
    "hook": "What I asked<br>after losing<br>a <em>customer</em>",
    "cta_eye": "The seven questions, and the three signals I watch for now",
    "cta_line": "I will send you the seven questions and the three signals I watch for now.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "When did it end", "h": "When did it <em>actually</em> end",
         "in": "Here is eleven months of the thread. When did this actually end?",
         "out": ["Month three, on the ticket that took nine days",
                 "Every message after it is shorter than the one before",
                 "The cancellation in month eleven was admin, not a decision"],
         "note": "the date I would have named  <span>-></span>  was eight months late"},
        {"t": "What did I miss", "h": "What did I <em>miss</em>",
         "in": "What did they tell me that I read as a compliment?",
         "out": ["Twice they said no rush, which meant it had stopped mattering",
                 "Once they asked whether there was a cheaper plan",
                 "Nobody new from their side ever joined the thread"],
         "note": "three signals  <span>-></span>  not one of them a complaint"},
        {"t": "Who stopped", "h": "Who stopped <em>replying</em> first",
         "in": "Who on their side went quiet, and when?",
         "out": ["The person who signed left the thread in month five",
                 "Everything after that was a user, not a buyer",
                 "Nobody replaced them and I never once asked"],
         "note": "the signer left  <span>-></span>  the deal left with them"},
        {"t": "Was it price", "h": "Was it ever about <em>price</em>",
         "in": "They said it was budget. Was it budget?",
         "out": ["Budget is the polite exit, and it was said once, at the end",
                 "Usage had been flat for four months before that",
                 "They renewed two other tools in the same quarter"],
         "note": "budget named at the end  <span>-></span>  it was not budget"},
        {"t": "Where in the product", "h": "Where did they <em>stop</em>",
         "in": "Where in the product did they stop, and when?",
         "out": ["Three weeks in, at the step that needs their own data",
                 "They never got past it and never said so",
                 "The setup assumed a person they did not have"],
         "note": "one step  <span>-></span>  eleven months of not mentioning it"},
        {"t": "Who else looks like this", "h": "Who else looks like <em>them</em>",
         "in": "Which current customers look like this one did in month three?",
         "out": ["Two, on the same shape of usage curve",
                 "Both have gone quiet in the last three weeks",
                 "Both still have the signer in the thread, which is the difference"],
         "note": "the same pattern  <span>-></span>  found while it is still fixable"},
        {"t": "What do I change", "h": "What do I <em>change</em>",
         "in": "What would have kept them?",
         "out": ["Answer the first slow ticket as if it is the whole relationship",
                 "Ask who signs again every quarter, not once at the start",
                 "Nine days is the number that mattered, and it was never the price"],
         "note": "one number to watch  <span>-></span>  days to first answer"},
    ],
}

# ------------------------------------------------------------- R: trace / white
R = {
    "id": "deck-r-morning", "design": "trace", "theme": "white", "keyword": "MORNING",
    "family": "morning",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction_pattern": "small-input",
    "reaction_text": "The first hour<br>is <em>triage</em>,<br>not routine.",
    "reaction_say": "Six twenty to eight. Seven blocks, and most of the hour is reading what "
                    "already ran while I was asleep.",
    "reaction_kick": "Before eight",
    "eyebrow": "Six twenty to eight. Not a routine, a triage, and most of it is reading what "
               "already ran.",
    "hook": "What happens<br>before <em>8am</em>",
    "badge": "1h40", "badge_l": "from waking to the first real decision, and most of it is "
                                "reading rather than doing",
    "cta_eye": "The whole hour, block by block, plus what runs before I wake up",
    "cta_line": "I will send you the hour block by block, and what runs before I am awake.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"v": "06:20", "t": "The phone stays shut",
         "h": "06:20, the phone stays <em>shut</em>",
         "b": "Twenty minutes. Not discipline, arithmetic: whatever is in there was already "
              "there at 4am and none of it improves by being read while I am half awake."},
        {"v": "06:40", "t": "What ran overnight",
         "h": "06:40, what ran <em>overnight</em>",
         "b": "One page. What went out, what came back, what needs me. Claude assembles it "
              "while I am asleep, which is the only reason this block is four minutes rather "
              "than forty."},
        {"v": "06:45", "t": "The one thing only I can do",
         "h": "06:45, name the <em>one thing</em>",
         "b": "Written down before anything else is opened. If I cannot name it, the day "
              "already belongs to somebody else and I will find that out at 11am."},
        {"v": "07:00", "t": "Replies, in one pass",
         "h": "07:00, replies in <em>one pass</em>",
         "b": "Everything that came back overnight, answered once, in order of who can sign. "
              "Not the inbox. The seven that matter, drafted and waiting on me to read them."},
        {"v": "07:25", "t": "The hard one, first",
         "h": "07:25, the <em>hard</em> one",
         "b": "The conversation I am avoiding goes here, while I still have the appetite for "
              "it. Moved to the afternoon it becomes tomorrow, and tomorrow it becomes next "
              "week."},
        {"v": "07:45", "t": "Nothing new before eight",
         "h": "07:45, nothing <em>new</em>",
         "b": "No new ideas, no new tools, no new tabs. Anything arriving now gets written "
              "down and read after lunch, because a new idea at 7:45 is not urgency, it is "
              "avoidance wearing a good suit."},
        {"v": "08:00", "t": "The day starts already decided",
         "h": "08:00, already <em>decided</em>",
         "b": "One hour forty from waking. Nothing in it was creative and nothing in it was "
              "optional, and the whole difference is that by nine I am doing the work rather "
              "than choosing it."},
    ],
}

SPECS = (P, Q, R)

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
        (REPO / f"content/reactions6-{mode}.html").write_text(RC.page(SPECS, FONTS, mode))
