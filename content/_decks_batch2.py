#!/usr/bin/env python3
"""Batch 2. The guard chose the shape of this batch, not me.

Run before this: verdict/black/regret, receipt/white/money, trace/black/speedrun. So the
guard required the next deck to be white, a design that is not trace, a family not used in
the last four, and - because none of the first three were - a BREAK. That is D. E and F then
follow the same alternation and take the two designs that had never shipped.

  D  STOPPED  stamp   white  break     the thin one, read in half a second
  E  RULES    ledger  black            list-and-argue, invites the correction out loud
  F  HIRE     score   white            the scorecard, roles against what already covers them

Every reaction is drawn from `_reactions.py`, which is sourced off real reels rather than
written by me, and every subject is founder-led: what somebody stopped doing, the rules they
run on, the hire they keep almost making. None of it is an industry update.
"""
import importlib.util, pathlib

REPO = pathlib.Path("/home/user/tiberiu-claude")


def load(n):
    s = importlib.util.spec_from_file_location(n, REPO / f"content/{n}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


FONTS = load("_fonts").embedded_css()
DK = load("_glassdeck")
CSS = load("_deck_css").CSS

# ------------------------------------------------- D: stamp / white / THE BREAK
D = {
    "id": "deck-d-stopped", "design": "stamp", "theme": "white", "keyword": "STOPPED",
    "family": "stopped", "break": True,
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction_pattern": "anticlimax",
    "reaction_text": "I got faster by<br>doing <em>less</em>.",
    "reaction_say": "Seven things I stopped doing completely. That is really it. "
                    "No new tool, no new system.",
    "reaction_kick": "Seven things, gone",
    "eyebrow": "No new tool. No new system. Seven things I stopped doing.",
    "hook": "7 things<br>I do not do<br><em>any more</em>",
    "cta_eye": "All seven, and what I replaced each one with",
    "cta_line": "I will send you the seven, and the one thing that replaced each.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "Checking email first", "mark": "&times;",
         "b": "The inbox is somebody else's list. Mine now starts with the one thing "
              "only I can do that day."},
        {"t": "Rewriting what it drafted", "mark": "&times;",
         "b": "If I am rewriting it, the brief was wrong. I fix the brief once instead "
              "of the output every time."},
        {"t": "Chasing every reply", "mark": "&times;",
         "b": "A reply is not a deal. Nine of my forty one were real and the other "
              "thirty two were a list I was carrying."},
        {"t": "Starting from a blank chat", "mark": "&times;",
         "b": "The context is written down once. It stops guessing and I stop "
              "explaining my own company every morning."},
        {"t": "Working past ten", "mark": "&times;",
         "b": "Eleven at night was never commitment. It was the absence of anything "
              "that ran without me."},
        {"t": "Paying top tier for lookups", "mark": "&times;",
         "b": "One routing decision I never made was most of the bill. Same answers, "
              "a fifth of the cost."},
        {"t": "Letting anything send itself", "mark": "&times;",
         "b": "It drafts, ranks and queues. I read it once and press send. That gate "
              "is not a limitation, it is the whole reason my name still works."},
    ],
}

# ------------------------------------------------- E: ledger / black
E = {
    "id": "deck-e-rules", "design": "ledger", "theme": "black", "keyword": "RULES",
    "family": "rules",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction_pattern": "list-and-argue",
    "reaction_text": "7 rules I run<br>my week on.<br><em>Tell me one is wrong.</em>",
    "reaction_say": "I mean it. If one of these is wrong for your business, "
                    "say which one and why.",
    "reaction_kick": "Founder operating rules",
    "eyebrow": "Not advice. The seven I actually run on, and I want the argument.",
    "hook": "7 rules<br>I run my<br><em>week</em> on",
    "cta_eye": "All seven, written out, plus the two I dropped",
    "cta_line": "I will send you the seven, and the two I stopped believing.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "One thing only I can do, first",
         "h": "Monday starts with <em>one</em> thing",
         "b": "Before anything else, name the single task nobody else could have done. "
              "That is the day. The rest is arrangeable.",
         "a": "if you cannot name it  ->  the day is already somebody else's"},
        {"t": "Nothing goes out unread",
         "h": "It drafts. <em>I</em> send",
         "b": "Everything is written, ranked and queued. I read it once. The gate costs "
              "ten minutes and it is why the name still works.",
         "a": "the gate  ->  ten minutes, every time"},
        {"t": "Quiet is not alive",
         "h": "Quiet is <em>not</em> alive",
         "b": "Nobody says no any more. A deal that has not moved in a month is not "
              "pending, it is finished, and it is taking a slot.",
         "a": "a month with no reply  ->  it is closed, mark it"},
        {"t": "Fix the brief, not the output",
         "h": "Rewriting means the <em>brief</em> was wrong",
         "b": "If I am editing heavily, I did not say what done looks like. I fix that "
              "once rather than the output every single time.",
         "a": "editing heavily  ->  go back one step, not forward"},
        {"t": "Write the context once",
         "h": "Say it <em>once</em>, not daily",
         "b": "Who the buyer is, how I sound, what I already tried. Written down, it "
              "stops guessing and I stop repeating myself.",
         "a": "one page  ->  every session after it"},
        {"t": "Match the job to the tier",
         "h": "Not everything needs the <em>big</em> one",
         "b": "A lookup has one right answer. Judgement does not. Deciding per job "
              "rather than once, months ago, is most of the bill.",
         "a": "per job  ->  same answer, a fifth of the price"},
        {"t": "If it worked, make it a run",
         "h": "The good result must <em>repeat</em>",
         "b": "A win that lives in a chat window nobody reopens did not happen. Turn "
              "it into something that runs next week without me awake.",
         "a": "it worked once  ->  make it happen without you"},
    ],
}

# ------------------------------------------------- F: score / white
F = {
    "id": "deck-f-hire", "design": "score", "theme": "white", "keyword": "HIRE",
    "family": "hiring",
    "mast": "ULTRON <em>/</em> AI FOR FOUNDERS",
    "reaction_pattern": "qualifying-question",
    "reaction_text": "About to make your<br><em>first hire</em>?",
    "reaction_say": "Seven roles founders hire too early, and what already covers each "
                    "one until the work is real.",
    "reaction_kick": "Before you post the job",
    "eyebrow": "Seven roles founders hire first. Not one of them is wrong forever, "
               "and not one of them is right yet.",
    "hook": "7 hires<br>you do not<br>need <em>yet</em>",
    "badge": "7", "badge_l": "roles founders fill too early, and what covers each until then",
    "col0": "THE ROLE",
    "cols": ["NEEDED NOW", "COVERED", "HIRE WHEN"],
    "cta_eye": "All seven, with the trigger that means it is finally time",
    "cta_line": "I will send you the seven, each with the signal that says hire now.",
    "cta_sub": "no link in the caption  <span>-></span>  it comes to your DMs",
    "items": [
        {"t": "SDR", "m": ["no", "yes", "yes"],
         "h": "The first <em>SDR</em>",
         "b": "You do not have a repeatable message yet. Hiring someone to send one you "
              "have not found makes the not-finding faster."},
        {"t": "Researcher", "m": ["no", "yes", "no"],
         "h": "A <em>researcher</em>",
         "b": "Forty companies, who signs at each, what changed this quarter. This is "
              "the one that never comes back as a hire."},
        {"t": "Content writer", "m": ["no", "yes", "yes"],
         "h": "A <em>writer</em>",
         "b": "Nobody can write in your voice from a brief. They can once your voice "
              "exists in writing, and that is the part to do first."},
        {"t": "Sales ops", "m": ["no", "yes", "yes"],
         "h": "<em>Ops</em>, before there are operations",
         "b": "A process you have not written down cannot be operated by anyone. Write "
              "it, run it twice, then hire it."},
        {"t": "Chief of staff", "m": ["no", "no", "yes"],
         "h": "A <em>chief of staff</em>",
         "b": "This is the one that is genuinely a hire. It is also the one people make "
              "at twelve people, not at three."},
        {"t": "Legal counsel", "m": ["no", "yes", "yes"],
         "h": "<em>Counsel</em> on retainer",
         "b": "Reading a contract and flagging what is not standard is not the same as "
              "advising you. Get the flags now, get the lawyer when you sign big."},
        {"t": "Second founder", "m": ["no", "no", "yes"],
         "h": "A <em>second founder</em>",
         "b": "Loneliness is not a skills gap. If the reason is that you are tired, the "
              "answer is leverage, and equity is the most expensive way to buy it."},
    ],
}

if __name__ == "__main__":
    import re, subprocess
    GD = load("_deckguard")
    RC = load("_reactioncard")
    RX = load("_reactions")
    SPECS = (D, E, F)
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
        (REPO / f"content/reactions2-{mode}.html").write_text(RC.page(SPECS, FONTS, mode))
