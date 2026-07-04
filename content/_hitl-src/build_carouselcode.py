#!/usr/bin/env python3
# THE CAROUSEL CODE - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/carouselcode"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Eight months of carousels.')],[co('The patterns finally cracked.')]])
T2.CONTENT=[
 ('THE MYTH', [[wo('It was never')],[co('the pretty template.')]], 'Eight months of posting proved it: sophistication and polish did not move a single metric.', [co('Patterns move metrics.')], f"{M}/myth7.png", 1.0),
 ('PATTERN 1', [[wo('The cover sells')],[co('the swipe, nothing else.')]], 'One promise, one visual, zero cleverness. Its only job is the next slide.', [co('Covers are doormen.')], f"{M}/pat1.png", 1.0),
 ('PATTERN 2', [[wo('One beat per page.')],[co('Cut everything else.')]], 'Two ideas on a slide is one idea too many. The swipe rhythm is the retention.', [co('Rhythm beats density.')], f"{M}/pat2.png", 1.0),
 ('PATTERN 3', [[wo('Slide two decides')],[co('if they finish.')]], 'The swipe-off page carries the tension: open a loop the last page closes.', [co('Hook them twice.')], f"{M}/pat3.png", 1.0),
 ('PATTERN 4', [[wo('The save happens')],[co('on the reference page.')]], 'One page they will need again: the list, the test, the map. Saves are the algorithm.', [co('Build the save page in.')], f"{M}/pat4.png", 1.0),
 ('THE GRADE', [[wo('I review posts')],[co('against the code now.')]], 'Cover promise, beat rhythm, loop tension, save page, one CTA. Five boxes, thirty seconds.', [co('Growth became a checklist.')], f"{M}/grade7.png", 1.0),
 ('THE DESK', [[wo('PULSE builds to the code')],[co('by default.')]], 'Every deck it drafts carries the five patterns before I ever see it.', [co('The code, automated.')], f"{M}/desk7.png", 1.0),
 ('THE PAYOFF', [[wo('Growth stopped being luck')],[co('and became a consequence.')]], 'Same niche, same effort, patterned delivery. The metrics followed.', [co('Consequence, not lottery.')], f"{M}/payoff7.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save the code',l2='and grade your last post.',q='Which pattern were you missing?')
MARK2="claude"
