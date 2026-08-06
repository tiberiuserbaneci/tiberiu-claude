#!/usr/bin/env python3
"""Deck 12 PITCH, on the photographic ground.

Adapted from the operator's reference clip. The reference's shape is: I built something I was
proud of, then I looked at the thing standing in front of it, and one line fixed that thing.
Ultron's honest version keeps the shape and changes the object: the product is not the problem.
What you built took months; how you sell it took an afternoon, and it shows.

Collision: deck 02 builds the page from nothing in 24 hours. This one starts from a product
that already exists and is being let down by everything around it, which is the more common
founder situation and a different starting state.
"""
import pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import _cine as C

SL = []


def S(eyebrow, h, sub, scene, cap=None):
    SL.append(dict(eyebrow=eyebrow, h=h, sub=sub, scene=scene, cap=cap))


S("THE PART NOBODY POSTS", "YOU BUILT<br>SOMETHING<br><em>GOOD.</em>",
  "Then you read your own cold email. <b>And you knew.</b>",
  C.scene_screen("your last outbound", "WHAT YOU ACTUALLY SENT",
                 [dict(b="Hi {first_name}, hope this finds you well", t="TEMPLATE"),
                  dict(b="I wanted to reach out because", t="TEMPLATE", hot=True),
                  dict(b="We help companies like yours", t="TEMPLATE"),
                  dict(b="Would you be open to a quick chat?", t="TEMPLATE", hot=True)],
                 "THE PRODUCT TOOK MONTHS. THIS TOOK AN AFTERNOON."),
  ("THE MOMENT", "The build was never the weak part.")),

S("THE MATH", "MONTHS ON<br>THE PRODUCT.<br>AN <em>AFTERNOON</em><br>ON THE PITCH.",
  "And the pitch is the only part anyone ever sees first.",
  C.scene_versus(dict(u="WHAT YOU BUILT", b="MONTHS", i="tested, rewritten, argued over, shipped"),
                 dict(u="WHAT THEY SEE", b="1 LINE", i="a subject line you wrote between two calls")),
  ("THE ORDER", "They meet the sentence before they meet the software.")),

S("WHAT IS ACTUALLY BROKEN", "THREE THINGS,<br>AND NONE OF THEM<br>ARE THE <em>CODE.</em>",
  "Every one of them is a sentence somebody has to read.",
  C.scene_rows([dict(n="01", b="The first line", i="says what you do, not why now", dim=True),
                dict(n="02", b="The page they open", i="explains the product, not the problem", hot=True),
                dict(n="03", b="The follow up", i="the one you never send")],
               "ALL THREE ARE WRITING, NOT ENGINEERING"),
  ("THE PATTERN", "You outsourced none of it, and did none of it.")),

S("WHAT CHANGES IT", "ONE LINE.<br>NOT A <em>REWRITE.</em>",
  "You describe who it is for and what breaks without it. <b>Once.</b>",
  C.scene_chat([dict(t="who this is for, and what breaks for them without it"),
                dict(t="reading your product, your posts, your past deals", you=True),
                dict(t="a first line, a page, and the follow up, in your voice", you=True)],
               "WRITTEN FROM WHAT ALREADY EXISTS"),
  ("PLAIN ENGLISH", "One paragraph. Not a positioning workshop.")),

S("WHAT COMES BACK", "THE SAME<br>PRODUCT.<br>A DIFFERENT<br><em>FIRST LINE.</em>",
  "Nothing about what you built has changed.",
  C.scene_screen("your next outbound", "WHAT GOES OUT NOW",
                 [dict(b="One trigger, from something they posted", t="WRITTEN", hot=True),
                  dict(b="A page about their problem, not your features", t="LIVE"),
                  dict(b="The follow up, already queued", t="HELD", hot=True),
                  dict(b="Held for your yes", t="YOURS")],
                 "NOTHING SENDS WITHOUT YOU"),
  ("THE DIFFERENCE", "It reads like you wrote it on your best day.")),

S("WHAT ACTUALLY CHANGED", "YOU STOPPED<br>BEING THE<br>WEAKEST PART<br>OF YOUR OWN<br><em>PITCH.</em>",
  "The thing you were proud of finally arrives that way.",
  C.scene_quote("1", "paragraph is the whole brief. The product was always fine.",
                "THE BUILD WAS NEVER THE WEAK PART"),
  ("THE TRUTH", "Good products lose to better first lines every day.")),

S("THE ASK", "TAKE THE<br>ONE PARAGRAPH<br><em>PITCH.</em>",
  "What to write, and what it turns into.",
  C.scene_ask("PITCH", "and I will send you the exact paragraph.", "ALL ACCESS")),


def main():
    run = [re.search(r'data-ob="([a-z0-9]+)"', s["scene"]).group(1) for s in SL]
    dupes = {o for o in run if run.count(o) > 1}
    print(f"  run: {','.join(run)}")
    if dupes:
        print(f"  NOTE repeated forms: {', '.join(sorted(dupes))} "
              f"(cine has 6 forms for 7 slides, so one returns)")
    p = C.build("cine-12-pitch", "PITCH", SL)
    print(f"  {p.name}  {len(SL)} slides  {C.CANVAS_W}x{C.CANVAS_H}")


if __name__ == "__main__":
    main()
