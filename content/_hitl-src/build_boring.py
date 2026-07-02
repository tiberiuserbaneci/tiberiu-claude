#!/usr/bin/env python3
# BORING BEATS CLEVER - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/boring"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Clever got 800 views.')],[co('Boring got 47,000.')]])
T2.CONTENT=[
 ('THE WINDOW', [[wo('You get 1.7 seconds.')],[co('Nobody is reading.')]], 'They are scrolling. The brain picks safe and predictable over smart and subtle, every time.', [co('Confusion kills reach.')], f"{M}/window.png", 1.0),
 ('THE PROOF', [[wo('Same idea, two posts,')],[co('one week apart.')]], 'The clever version optimised asymmetric distribution. The boring one said: post daily for 30 days.', [co('800 versus 47,000.')], f"{M}/proof.png", 1.0),
 ('THE RULES', [[wo('One idea per post.')],[co('Payoff in two seconds.')]], 'Words a 12-year-old gets, a format the feed already knows. That is the whole religion.', [co('Boring is a discipline.')], f"{M}/rules.png", 1.0),
 ('THE EGO', [[wo('Clever is for you.')],[co('Boring is for them.')]], 'Sounding smart is a founder vanity metric. Being understood is a growth metric.', [co('Kill the vanity.')], f"{M}/ego.png", 1.0),
 ('THE TEST', [[wo('Four boxes')],[co('before every post.')]], 'Point lands in 2 seconds? One idea only? Your dad gets it? Format familiar?', [co('Fail one, rewrite.')], f"{M}/fourtest.png", 1.0),
 ('THE SKILL', [[wo('My desk runs the test')],[co('before I ever see a draft.')]], 'PULSE drafts to the boring rules: one idea, plain words, visible payoff. Ranked before review.', [co('Discipline, automated.')], f"{M}/skill.png", 1.0),
 ('THE CLIENT', [[wo('One trader switched.')],[co('2K to 30K in 25 days.')]], 'Same expertise, same niche. One trade idea per post instead of technical essays.', [co('Boring delivery, expert core.')], f"{M}/client.png", 1.0),
 ('THE REFRAME', [[wo('Boring does not mean')],[co('low value.')]], 'It means legible at scroll speed. The smartest content looks the simplest.', [co('Simple is the flex.')], f"{M}/reframe.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1='Save the 4-second test',l2='and run it on your next post.',q='Are you writing for the scroll?')
MARK2="claude"
