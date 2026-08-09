#!/usr/bin/env python3
"""Batch 7. Black, then white, then black with the break.

  S  QUICK   receipt black          what a two day feature actually costs
  T  FOLLOW  verdict white          seven follow ups that got ignored
  U  OPENS   meter   black  break   what I actually open in a week

All three designs change ground at once, which has not happened before. `receipt` had only
ever been white, `verdict` had only ever been black across three decks, and `meter` had only
been white. Flipping all three means the batch is built entirely from familiar shapes and not
one of them looks like anything already in the feed - cheaper than inventing three designs and
better, because a shape that has earned its layout does not need replacing, it needs relighting.

U carries a constraint worth stating: no third party product is ever named. CLAUDE.md 21 allows
Claude, AI and Ultron and nothing else, so the tools are described by the job they do - the
CRM, the tracker, the dashboard. That is also the more honest version, because the point is
never which vendor it was, it is that the most expensive seat is the least opened one.
"""
import importlib.util, pathlib

REPO = pathlib.Path("/home/user/tiberiu-claude")


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


FONTS = load("_fonts").embedded_css()
DK = load("_glassdeck")
CSS = load("_deck_css").CSS

# ------------------------------------------------------------- S: receipt / black
S = {
    "id": "deck-s-quick", "design": "receipt", "theme": "black", "keyword": "QUICK",
    "family": "featurecost",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "receipt_head": "ONE QUICK FEATURE  ·  QUOTED AT TWO DAYS  ·  ACTUAL",
    "reaction_pattern": "future-regret",
    "reaction_text": "Quick features<br>bill you <em>monthly</em>.<br>Forever.",
    "reaction_say": "I quoted two days. Here is what it actually cost, itemised, including "
                    "the line that never stops.",
    "reaction_kick": "The two day feature",
    "eyebrow": "I said two days. Here is the itemised version, including the line that never "
               "stops arriving.",
    "hook": "What a<br><em>two day</em><br>feature costs",
    "badge": "2d", "badge_l": "WHAT I QUOTED",
    "total": "7.5d", "total_l": "plus a day a month, forever",
    "cta_eye": "The whole bill, and the question I ask before agreeing to anything",
    "cta_line": "I will send you the itemised version and the question I ask before agreeing.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "Building the thing itself", "v": "2d",
         "h": "Two days <em>building</em>",
         "b": "The only part I estimated, and the only part I got right. Everything under it "
              "is what I was not thinking about while saying yes on a call."},
        {"t": "The spec I did not write", "v": "1d",
         "h": "One day of <em>rework</em>",
         "b": "Built the wrong version, because the request was one sentence in a call and "
              "nobody wrote down what done meant. Heavy editing always means the brief was "
              "wrong."},
        {"t": "Testing it properly", "v": "1d",
         "h": "One day <em>testing</em>",
         "b": "Not the happy path, the other ones. Skipped, this line does not disappear. It "
              "moves to a customer finding it on a Friday afternoon."},
        {"t": "Explaining it to everybody", "v": "0.5d",
         "h": "Half a day <em>explaining</em>",
         "b": "The changelog, the two customers who asked, and the one who did not ask and "
              "needed it. Every feature comes with a small permanent audience to keep "
              "informed."},
        {"t": "Supporting it, every month", "v": "1d/mo",
         "h": "A day a month, <em>forever</em>",
         "b": "This is the line that changes the arithmetic. It never ends, it grows with "
              "the customer count, and it is completely invisible on the day you agree."},
        {"t": "The next feature working around it", "v": "3d",
         "h": "Three days <em>working around it</em>",
         "b": "Everything built afterwards has to account for it. That is what a feature "
              "actually is: not a thing you add, a constraint you agree to keep."},
        {"t": "What I did not build instead", "v": "the real one",
         "h": "The one I <em>did not</em> build",
         "b": "Seven and a half days went to one customer's request while the thing three "
              "customers had asked for waited another month. Claude ranks requests by how "
              "many people made them, which is the only number that should decide this."},
    ],
}

# ------------------------------------------------------------- T: verdict / white
T = {
    "id": "deck-t-follow", "design": "verdict", "theme": "white", "keyword": "FOLLOW",
    "family": "followup",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction_pattern": "qualifying-question",
    "reaction_text": "Still sending<br><em>just checking in</em>?",
    "reaction_say": "Seven follow ups that got ignored, and the one line that replaced each "
                    "of them. The first one is the one everybody sends.",
    "reaction_kick": "The follow up",
    "eyebrow": "Forty follow ups, no replies, and not one of them was about them. Here is "
               "what replaced each.",
    "hook": "7 follow ups<br>that got<br><em>ignored</em>",
    "badge": "0", "badge_l": "replies from forty of the first kind, and what replaced each one",
    "rail_l": "every one of these was a deal I already had",
    "cta_eye": "All seven, with the exact line that replaced each",
    "cta_line": "I will send you the seven and the exact line I use instead of each one.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"h": "<em>Just checking in</em>",
         "cn": "0", "cl": "replies from forty of these, over four months",
         "x": "Just checking in on this",
         "xw": "It gives them nothing to answer, so replying is pure cost with no reason "
               "attached.",
         "y": "Send something they can use",
         "yw": "One thing you have found since you spoke, about them. Then the question. "
               "The difference in reply rate is not close."},
        {"h": "I followed up in <em>three days</em>",
         "cn": "3d", "cl": "after the call, before anything could possibly have changed",
         "x": "Follow up fast, stay top of mind",
         "xw": "Nothing has changed in three days except that you now look anxious.",
         "y": "Follow up when something changed",
         "yw": "Theirs or yours. A new customer like them, a thing they asked about shipping, "
               "a piece of news. The trigger is the message."},
        {"h": "The <em>five email</em> sequence",
         "cn": "5", "cl": "emails, and all five of them were about me",
         "x": "Set up a five step sequence",
         "xw": "Five messages that could have gone to anybody, arriving on a schedule that is "
               "obviously a schedule.",
         "y": "Two, both specific",
         "yw": "Written from what they actually said on the call. Claude drafts them off my "
               "notes, so it takes minutes rather than being the thing I skip."},
        {"h": "I attached the deck <em>again</em>",
         "cn": "2", "cl": "attachments, zero opens, both times",
         "x": "Resend the deck in case they missed it",
         "xw": "They did not miss it. They did not open it, which is different and worse.",
         "y": "Send one line and one number",
         "yw": "The single thing in the deck that applies to them. If it cannot survive as "
               "one sentence, the deck was never going to save it."},
        {"h": "<em>Any updates?</em>",
         "cn": "0", "cl": "new information offered, every single time I sent it",
         "x": "Ask whether there are any updates",
         "xw": "You are asking them to do the work of moving your deal forward.",
         "y": "Tell them the update",
         "yw": "What changed on your side, and what you need by when. Deals move because "
               "somebody moves them, and it is not going to be them."},
        {"h": "I chased the <em>wrong person</em>",
         "cn": "6 wk", "cl": "of following up with somebody who could not sign anything",
         "x": "Keep working your champion",
         "xw": "A champion who cannot sign is a friend. Six weeks of friendship is not a "
               "pipeline.",
         "y": "Ask who else needs to see this",
         "yw": "In the follow up, plainly. It is not rude and it saves everybody a quarter. "
               "If the answer is nobody, that is also an answer."},
        {"h": "I gave up after <em>two</em>",
         "cn": "2", "cl": "attempts, when the yes usually arrives on the fifth",
         "x": "Two follow ups, then move on",
         "xw": "Two is where most people stop, and it is exactly where the pile of unworked "
               "deals begins.",
         "y": "Five, if each one carries something",
         "yw": "Not five reminders. Five different reasons to reply. The moment you cannot "
               "think of a new one, that is the actual signal to stop."},
    ],
}

# ------------------------------------------------------- U: meter / black / BREAK
U = {
    "id": "deck-u-opens", "design": "meter", "theme": "black", "keyword": "OPENS",
    "family": "toolaudit", "break": True,
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "axis": "WHAT IT IS", "unit": "OPENS / WEEK",
    "reaction_pattern": "life-contrast",
    "reaction_text": "Seven tools.<br>I open <em>three</em>.",
    "reaction_say": "I counted every open for a month. The most expensive one is the one I "
                    "opened least, and one of them I had forgotten I pay for.",
    "reaction_kick": "The stack, counted",
    "eyebrow": "I counted every time I opened every tool I pay for, for a month. Then I "
               "looked at the bill.",
    "hook": "What I <em>actually</em><br>open in<br>a week",
    "cta_eye": "The whole audit, and the three questions I ask before renewing",
    "cta_line": "I will send you the audit and the three questions I ask before I renew.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "The thing I actually work in", "v": 22, "d": "22",
         "h": "Twenty two: the <em>real</em> one",
         "b": "Opened every working day, several times a day. One tool does most of the work, "
              "and it is never the one with the most expensive plan on it.",
         "a": "most opens  ->  smallest invoice"},
        {"t": "Scheduling", "v": 6, "d": "6",
         "h": "Six: <em>scheduling</em>",
         "b": "Six opens a week to find a time. Not the meetings. Finding the time for the "
              "meetings, which is a job I did not know I had bought a tool for.",
         "a": "six opens  ->  three hours"},
        {"t": "The CRM", "v": 4, "d": "4",
         "h": "Four: the <em>CRM</em>",
         "b": "Four opens, and three of them were me updating it rather than reading it. A "
              "system you maintain and never consult is a chore with a login screen.",
         "a": "updated three times  ->  read once"},
        {"t": "The project tracker", "v": 3, "d": "3",
         "h": "Three: the <em>tracker</em>",
         "b": "Bought when I thought the problem was visibility. The problem was that there "
              "were two of us and we were sitting in the same room.",
         "a": "solves a problem I did not have"},
        {"t": "The analytics dashboard", "v": 2, "d": "2",
         "h": "Two: the <em>dashboard</em>",
         "b": "Two opens a week, both on a Monday, both to look at a number I could have been "
              "handed. Claude sends me the seven that matter and I stopped opening it.",
         "a": "a number I should be sent"},
        {"t": "The design tool", "v": 1, "d": "1",
         "h": "One: the <em>design tool</em>",
         "b": "The most expensive seat on the list, opened once a week, kept because "
              "cancelling feels like admitting something. That is not a tool cost, it is an "
              "identity cost.",
         "a": "highest price  ->  lowest use"},
        {"t": "The one I forgot I pay for", "v": 0, "d": "0",
         "h": "Zero: the one I <em>forgot</em>",
         "b": "Not opened once in the month I spent counting. I found it on the card "
              "statement rather than in my head, which is the entire reason this exercise "
              "exists.",
         "a": "zero opens  ->  eleven months paid"},
    ],
}

SPECS = (S, T, U)

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
        (REPO / f"content/reactions7-{mode}.html").write_text(RC.page(SPECS, FONTS, mode))
