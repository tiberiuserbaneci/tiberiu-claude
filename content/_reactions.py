#!/usr/bin/env python3
"""Reaction hook library. Every pattern here was measured on Instagram, not invented.

Operator, 2026-08-08: "nu doar cele date de mine ca exemplu - acolo ti am dat cateva sugestii
- tu gasesti reactii virale tot pe materialele pe care le scoutuiesti." Right. His examples
were the brief, not the source. So the openers below are pulled off real reels with their
view counts and accounts attached, and each one carries the RULE that makes it work plus the
Ultron adaptation. A reaction that cannot name the pattern it came from is a guess.

Read it as: this shape earned these views, therefore this shape is the container. The content
poured into it is the operator's own life, per the founder-led rule.

CAUTION on the top of the range. The 65M and 46.7M entries are a different genre - sponsored
interview and luxury-flex content - and their pull comes from the subject, not the sentence.
They are logged for completeness and marked unusable rather than quietly copied, because
lifting a shape whose engine is a Ferrari onto a GTM post gets a shape and no engine.
"""

# pattern, verbatim source hook, views, account, why it works, how it maps to Ultron
PATTERNS = [
    {
        "id": "cautionary",
        "src": "What happens when you let AI manage your production infrastructure? "
               "One developer found out the hard way.",
        "views": "11.0M", "who": "#claudeai",
        "why": "A question about a risky choice, then a person who already paid for the "
               "answer. The viewer is not being taught, they are being warned, and a warning "
               "is the one thing nobody scrolls past.",
        "map": "The risky choice is the founder's own habit. He is the developer who found "
               "out, which is the only honest way to run it.",
    },
    {
        "id": "small-input",
        "src": "20 mins a day, and solid consistency is all it takes",
        "views": "15.3M", "who": "@jadablue_designs",
        "why": "A tiny input against a large outcome. It is credible because the number is "
               "small enough to try tonight.",
        "map": "One day, one hour, one input. Never 'transform your business'. The unit has "
               "to be something the viewer could start before bed.",
    },
    {
        "id": "ignorance-reveal",
        "src": "Most people have no idea how much of their personal information is sitting "
               "on the internet right now.",
        "views": "457K", "who": "@aigeneralist.vs",
        "why": "Names a thing already true about the viewer that they have not looked at. "
               "Not an accusation, a blind spot, which is why it does not put them on the "
               "defensive.",
        "map": "The bill, the pipeline, the calendar. Something they own and have not opened.",
    },
    {
        "id": "wrong-tool",
        "src": "Comment CODES and I'll send 7. Most people use Claude like a basic "
               "search engine.",
        "views": "2.5M", "who": "#claudeai",
        "why": "A wrong belief stated flatly, with the keyword in the hook rather than "
               "saved for the end. The ask arrives while they still care.",
        "map": "Founders using a tool at a fraction of what it does. Keyword goes in the "
               "first line, not only on slide 9.",
    },
    {
        "id": "qualifying-question",
        "src": "Building in 2026? Then these 5 AI tools should already be in your workflow.",
        "views": "706K", "who": "@10xoperator",
        "why": "Filters the audience in the first three words and implies they are already "
               "behind. The viewer self-selects and then has to check.",
        "map": "Founder? Then this should already be true for you. Works with a count.",
    },
    {
        "id": "future-regret",
        "src": "If you ignore these skills in 2026, don't complain about your salary in 2027.",
        "views": "233K", "who": "@saumya1singh",
        "why": "Puts a dated price on inaction. It is a threat with a receipt attached, "
               "and the date makes it feel like a countdown.",
        "map": "Ignore this now and here is the specific thing it costs by a named point.",
    },
    {
        "id": "origin-number",
        "src": "In 1995, Elon Musk faced over $100,000 in student debt",
        "views": "515K", "who": "@startupbell",
        "why": "One year, one number, one person. The story is already moving before the "
               "sentence ends.",
        "map": "The operator's own year and his own number. Never a borrowed founder myth.",
    },
    {
        "id": "list-and-argue",
        "src": "14 rules for startups - comment any I missed",
        "views": "764K", "who": "@imad.json",
        "why": "A countable list plus an explicit invitation to disagree. The comment ask "
               "is the content, not a bolt-on, so it reads as confidence rather than farming.",
        "map": "Any numbered deck can carry it. Invite the correction out loud.",
    },
    {
        "id": "imperative",
        "src": "Upload your raw video to Claude.",
        "views": "251K", "who": "@soravjain",
        "why": "No setup at all. An instruction as the first frame, so the viewer is already "
               "mid-task before deciding whether to watch.",
        "map": "One concrete action the founder could do in the next minute.",
    },
    {
        "id": "anticlimax",
        "src": "That's really it",
        "views": "2.7M", "who": "@chrispathway",
        "why": "Implies the reveal already happened and was smaller than expected. It works "
               "on curiosity rather than promise, which is why it survives.",
        "map": "Use on a run the audience assumes is complicated. Sparingly - it earns "
               "nothing on its own if the payoff is not genuinely small.",
    },
    {
        "id": "life-contrast",
        "src": "Office end at 5 pm. Me at 11 pm",
        "views": "operator's own example", "who": "operator",
        "why": "Two clock times, no verb, no claim. The gap is the whole hook and the "
               "viewer closes it themselves.",
        "map": "Any two facts about the operator's life with a gap between them.",
    },
    # logged, deliberately not used
    {
        "id": "luxury-flex", "unusable": True,
        "src": "The Ferrari BILLIONAIRE / This is the ultimate flex",
        "views": "46.7M / 5.0M", "who": "@theschoolofhardknockz, @netkohen",
        "why": "The pull is the subject, not the sentence. Sponsored interview and "
               "luxury-flex genre.",
        "map": "NOT USABLE. Lifting a shape whose engine is a Ferrari onto a GTM post "
               "gets you the shape and none of the engine.",
    },
]

BY_ID = {p["id"]: p for p in PATTERNS}
USABLE = [p for p in PATTERNS if not p.get("unusable")]


def cite(pattern_id: str) -> str:
    p = BY_ID[pattern_id]
    return f"{pattern_id} ({p['views']}, {p['who']})"


if __name__ == "__main__":
    print(f"{len(USABLE)} usable patterns, {len(PATTERNS) - len(USABLE)} logged and refused\n")
    for p in PATTERNS:
        flag = "  [NOT USABLE]" if p.get("unusable") else ""
        print(f"{p['id']:20} {p['views']:>8}  {p['who']}{flag}")
        print(f"  \"{p['src'][:88]}\"")
