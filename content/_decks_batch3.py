#!/usr/bin/env python3
"""Batch 3. Guard-shaped again: black, then white with the break, then black.

  G  TURNED  verdict black          what I said no to, and what it bought back
  H  2AM     console white  break   the questions I was too embarrassed to ask a person
  I  MONDAY  ledger  black          the seven numbers I check before the week starts

H is the break AND the AI moment, because the break slot and the product window are now the
same design. `stamp` proved that thin does not stop a scroll - the audience skips empty as
fast as it skips repetitive - so the interrupt is the most arresting frame in the set rather
than the emptiest.

Reactions come from `_reactions.py`, sourced off measured reels. Subjects stay founder-led:
the things turned down, the 2am questions, the numbers checked before the week. Ultron
arrives as what fixed it, never as the subject of slide one, and every cover names Claude in
the frame so the viewer never has to guess what "it" is.
"""
import importlib.util, pathlib

REPO = pathlib.Path("/home/user/tiberiu-claude")


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


FONTS = load("_fonts").embedded_css()
DK = load("_glassdeck")
CSS = load("_deck_css").CSS

# ------------------------------------------------------------- G: verdict / black
G = {
    "id": "deck-g-turned", "design": "verdict", "theme": "black", "keyword": "TURNED",
    "family": "sayingno",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "ai_line": "Claude, running as Ultron",
    "reaction_pattern": "future-regret",
    "reaction_text": "Say yes to all of it<br>and you will own<br><em>none</em> of it.",
    "reaction_say": "Seven things I turned down last quarter, and what each one bought back. "
                    "The last one was the hardest.",
    "reaction_kick": "What I said no to",
    "eyebrow": "Every yes was reasonable. Together they were a year I would not get back.",
    "hook": "7 things<br>I turned down<br><em>last quarter</em>",
    "badge": "7", "badge_l": "reasonable offers I said no to, and what each one bought back",
    "rail_l": "every no bought a week back",
    "cta_eye": "All seven, with the exact line I used to say no",
    "cta_line": "I will send you the seven, and the wording I use to decline without burning it.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"h": "The customer who wanted a different product",
         "cn": "3 mo", "cl": "of building a second product for one logo",
         "x": "Say yes, it is revenue",
         "xw": "One contract, and a roadmap that now belongs to somebody else.",
         "y": "Say no, and say why in one line",
         "yw": "Claude drafted the no. It kept the relationship and it kept the roadmap, "
               "which is the part I would have lost."},
        {"h": "The partnership that was a meeting series",
         "cn": "11", "cl": "calls, no signature, and it was on my calendar every week",
         "x": "Take the meeting, see where it goes",
         "xw": "It goes to another meeting. It always goes to another meeting.",
         "y": "Ask for the decision date first",
         "yw": "If there is no date there is no deal. That question ends half of them "
               "in the first reply, which is the point."},
        {"h": "The feature every prospect asked about",
         "cn": "0", "cl": "of the people who asked for it had signed anything",
         "x": "Build what they ask for",
         "xw": "Asked for is not paid for. The gap between them is most of a roadmap.",
         "y": "Ask who has already paid",
         "yw": "Ranked by who signed, not by who spoke loudest. The list looks completely "
               "different and it is the honest one."},
        {"h": "The conference that cost a week",
         "cn": "1 wk", "cl": "gone, for a badge and a folder of business cards",
         "x": "Go, everyone will be there",
         "xw": "Two useful conversations, five days, and no follow up because you got home tired.",
         "y": "Write to the twenty people first",
         "yw": "The ones actually worth meeting, contacted before anyone books a flight. "
               "Same outcome without the week."},
        {"h": "The advisor who wanted equity for introductions",
         "cn": "0.5%", "cl": "for a warm intro I could have written myself",
         "x": "Take the help, it is only half a point",
         "xw": "Half a point is permanent. The introductions were three emails.",
         "y": "Write the three emails",
         "yw": "The research and the first line take an afternoon now. Equity does not "
               "come back and an afternoon does."},
        {"h": "The rebuild that would fix everything",
         "cn": "2 mo", "cl": "of rewriting instead of selling, for a problem nobody reported",
         "x": "Rebuild it properly first",
         "xw": "Nobody churned over the thing you are about to rewrite. Check.",
         "y": "Ask what customers actually reported",
         "yw": "The complaints, ranked by how many people made them. The rebuild was not "
               "on the list and it never is."},
        {"h": "The hire I wanted because I was tired",
         "cn": "1", "cl": "person, hired to fix a feeling, not to do a job",
         "x": "Hire, you cannot keep going like this",
         "xw": "Loneliness is not a skills gap, and equity is the most expensive way to buy "
               "company.",
         "y": "Name the job first, then decide",
         "yw": "Written down, most of it was work that runs without a person now. What was "
               "left did not need a full time hire yet."},
    ],
}

# ------------------------------------------------------------- H: console / white / BREAK
H = {
    "id": "deck-h-2am", "design": "console", "theme": "white", "keyword": "2AM",
    "family": "worry", "break": True,
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "ai_line": "Claude, running as Ultron",
    "window": "ULTRON  ·  02:14  ·  NOBODY ELSE AWAKE",
    "reaction_pattern": "anticlimax",
    "reaction_text": "The questions I was<br>too embarrassed<br>to ask a <em>person</em>.",
    "reaction_say": "I typed all seven of them at two in the morning. "
                    "That is really it. No framework, no course.",
    "reaction_kick": "02:14, month eleven",
    "eyebrow": "No framework. No course. Seven things I typed at 2am and what came back.",
    "hook": "What I asked<br>at <em>2am</em>",
    "cta_eye": "All seven questions, word for word, with what came back",
    "cta_line": "I will send you the seven questions exactly as I typed them.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "Am I late", "h": "Am I <em>too late</em>",
         "in": "Four companies do what I do and three are funded. Am I too late?",
         "out": ["Name what you know about this buyer that they do not",
                 "Funded means they must grow fast, not that they serve well",
                 "Late matters in a race. This is not one, it is a fit question"],
         "note": "the honest answer  <span>-></span>  not the encouraging one"},
        {"t": "Is it real", "h": "Is any of this <em>real</em>",
         "in": "Of my open deals, which would you still work on Monday?",
         "out": ["22 have not moved in a month and nobody said no",
                 "10 are a person who likes me and cannot sign",
                 "9 are real, and one is closer than everything above it"],
         "note": "it ranks, I decide  <span>-></span>  it forecasts nothing"},
        {"t": "What am I missing", "h": "What am I <em>not</em> seeing",
         "in": "Argue against my own plan. What would make me wrong?",
         "out": ["The three assumptions the whole thing rests on, named",
                 "Which one is cheapest to test this week",
                 "What evidence would actually change my mind"],
         "note": "it argues back  <span>-></span>  that is the useful part"},
        {"t": "Say the hard thing", "h": "How do I say the <em>hard</em> thing",
         "in": "I have to tell a customer we are not building their feature.",
         "out": ["What they actually need underneath the request",
                 "The no, in my words, without the apology spiral",
                 "What to offer instead so the relationship survives"],
         "note": "I send it  <span>-></span>  it never sends anything"},
        {"t": "Price it", "h": "Am I charging <em>too little</em>",
         "in": "Nobody has pushed back on my price. What does that tell you?",
         "out": ["Zero pushback is a signal, and it is not a good one",
                 "What the buyer is comparing you against, not what you cost to build",
                 "The test: raise it on the next three and watch"],
         "note": "no benchmarks  <span>-></span>  your buyers, your evidence"},
        {"t": "Where did it go", "h": "Where did the <em>week</em> go",
         "in": "Here is my calendar. What did I actually do this week?",
         "out": ["Hours by what it moved, not by what it was called",
                 "The recurring meeting that has produced nothing in six weeks",
                 "The one block that was the only work only I could do"],
         "note": "it counts  <span>-></span>  and counting is the whole intervention"},
        {"t": "Should I stop", "h": "Should I <em>stop</em>",
         "in": "Give me the case for shutting this down.",
         "out": ["The strongest version of the argument against continuing",
                 "What would have to be true in ninety days for it to work",
                 "Which of those you can actually influence"],
         "note": "it will make the case  <span>-></span>  the decision is still yours"},
    ],
}

# ------------------------------------------------------------- I: ledger / black
I = {
    "id": "deck-i-monday", "design": "ledger", "theme": "black", "keyword": "MONDAY",
    "family": "dashboard",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "ai_line": "Claude, running as Ultron",
    "reaction_pattern": "small-input",
    "reaction_text": "Seven numbers.<br>Twenty minutes.<br><em>Sunday night.</em>",
    "reaction_say": "That is the whole review. Seven numbers, and if any of them is wrong "
                    "I know exactly what Monday is for.",
    "reaction_kick": "Before the week starts",
    "eyebrow": "Twenty minutes on a Sunday. Seven numbers, and each one names a decision.",
    "hook": "7 numbers<br>I check before<br><em>Monday</em>",
    "cta_eye": "The seven, with the threshold that means act this week",
    "cta_line": "I will send you the seven numbers and what each one means when it moves.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "Deals that moved this week",
         "h": "Movement, not <em>volume</em>",
         "b": "Not how many are open. How many did something a person can point to. "
              "Everything else is a list you are carrying.",
         "a": "zero moved  ->  the week was admin, not selling"},
        {"t": "Deals with a named signer",
         "h": "Who can actually <em>sign</em>",
         "b": "A contact is not a buyer. If nobody in the thread can sign, the deal has "
              "not started yet whatever the notes say.",
         "a": "no signer named  ->  it is a conversation, not a deal"},
        {"t": "Days since the oldest open deal moved",
         "h": "The <em>oldest</em> one is the tell",
         "b": "The number nobody wants to look at. Past thirty days it is not pending, "
              "it is finished, and it is holding a slot.",
         "a": "over 30 days  ->  close it or restart it, not both"},
        {"t": "First replies this week",
         "h": "Did anyone <em>answer</em>",
         "b": "Not sends. Replies. Sends measure effort and effort is not the constraint. "
              "Replies measure whether the first line worked.",
         "a": "sends up, replies flat  ->  the message is wrong, not the volume"},
        {"t": "Hours on work only I could do",
         "h": "Was I the <em>bottleneck</em>",
         "b": "Out of the week, how much was judgement and relationships. If it is near "
              "zero I spent the week being staff at my own company.",
         "a": "under 5 hours  ->  something upstream should be running without you"},
        {"t": "What the AI spend actually bought",
         "h": "Cost per thing that <em>shipped</em>",
         "b": "Not the total. What it produced. If the number is climbing and the output "
              "is flat, it is routing, not usage.",
         "a": "cost up, output flat  ->  wrong tier, not too much use"},
        {"t": "One thing I will not do next week",
         "h": "The <em>subtraction</em>",
         "b": "The only number that is a sentence. If nothing comes off the list, next "
              "week is this week with more on it.",
         "a": "nothing removed  ->  you did not plan, you accumulated"},
    ],
}

if __name__ == "__main__":
    import re
    GD = load("_deckguard")
    RC = load("_reactioncard")
    RX = load("_reactions")
    SPECS = (G, H, I)
    for spec in SPECS:
        GD.register(spec)
        (REPO / f"content/{spec['id']}.html").write_text(DK.build(spec, CSS, FONTS))
        plain = re.sub(r"<[^>]+>", " ", spec["reaction_text"]).replace("  ", " ").strip()
        d = REPO / f"content/decks/{spec['id']}"; d.mkdir(parents=True, exist_ok=True)
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
        print(f"{spec['id']:18} {spec['design']:8} {spec['theme']:6} "
              f"{'BREAK' if spec.get('break') else '':6}  {plain}")
    for mode in ("preview", "alpha"):
        (REPO / f"content/reactions3-{mode}.html").write_text(RC.page(SPECS, FONTS, mode))
