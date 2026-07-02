#!/usr/bin/env python3
# STUCK AT LEVEL ONE - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/unstuck"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You use 12% of Claude.')],[co('Here is the other 88.')]])
T2.CONTENT=[
 ('LEVEL 1', [[wo('Ask. Copy. Close.')],[co('The hamster wheel.')]], 'Ask, copy, close the tab. A smarter search bar, nothing more.', [co('The floor, not the ceiling.')], f"{M}/floor.png", 1.0),
 ('LEVEL 2', [[wo('Level 2: it remembers')],[co('what you hate.')]], 'Your ICP, voice and pricing persist. No more introductions every morning.', [co('It remembers you now.')], f"{M}/memory.png", 1.0),
 ('LEVEL 3', [[wo('Level 3: it works')],[co('while you watch.')]], 'Agents source, brief and draft while you do the one thing only you can do.', [co('Work, not answers.')], f"{M}/jobs.png", 1.0),
 ('LEVEL 4', [[wo('Level 4: it ships')],[co('while you sell.')]], 'Pages and fixes from plain English, tested before you ever see them.', [co('Your eng team in a chat.')], f"{M}/ship.png", 1.0),
 ('LEVEL 5', [[wo('Level 5: it runs')],[co('while you sleep.')]], 'Triggers replace typing. The digest waits for you at 07:00.', [co('The machine works nights.')], f"{M}/routines.png", 1.0),
 ('THE GAP', [[wo('Nobody told you')],[co('level 3 exists.')]], 'Most founders never hear that the next level exists. Now you have.', [co('Five levels, one chat.')], f"{M}/gap.png", 1.0),
 ('THE GATE', [[wo('Climb fast.')],[co('Keep the handbrake.')]], 'Autonomy grows, control does not shrink. External moves park for you.', [co('Climb without crashing.')], f"{M}/gate.png", 1.0),
 ('THE CEILING', [[wo('The ceiling is quiet.')],[co('Just running.')]], 'One founder, one subscription, a company that moves overnight.', [co('See you up there.')], f"{M}/ceiling.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], f"{LIB}/cta3d-builder.png", 0.92)
T2.CLOSE=dict(l1='Save the map',l2='and climb one level.',q='Which level are you honestly at?')
MARK2="claude"
