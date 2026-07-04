#!/usr/bin/env python3
# THE MODEL OF THE WEEK - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/modelwars"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('A new model drops weekly.')],[co('Your system should not care.')]])
T2.CONTENT=[
 ('THE CYCLE', [[wo('Every Tuesday,')],[co('a new king is crowned.')]], 'A benchmark, a hype thread, a migration guide. By Friday there is another one.', [co('You cannot build on a carousel.')], f"{M}/cycle.png", 1.0),
 ('THE SWITCHERS', [[wo('They moved stacks')],[co('four times this year.')]], 'Each move: new quirks, new prompts, new bugs. Their pipeline never noticed a difference.', [co('Motion, not progress.')], f"{M}/switchers.png", 1.0),
 ('THE TRUTH', [[wo('Models converged.')],[co('Systems did not.')]], 'The top models are within points of each other. The gap is everything wrapped around them.', [co('The wrapper is the moat.')], f"{M}/truth.png", 1.0),
 ('THE ROUTER', [[wo('One goal in,')],[co('the right tier picked.')]], 'Lite for lookups, Smart for the daily work, Deep for judgement. Chosen per turn, not per hype.', [co('You never pick a model again.')], f"{M}/router.png", 1.0),
 ('THE ASSETS', [[wo('Memory, skills, gate:')],[co('none of them expire.')]], 'Your ICP, your voice, your rules survive every model release untouched.', [co('Launches cannot erase them.')], f"{M}/assets.png", 1.0),
 ('THE UPGRADE', [[wo('New model lands,')],[co('your desk just improves.')]], 'The router adopts it under the hood. Same commands, same memory, better engine.', [co('Zero migration, ever.')], f"{M}/upgrade.png", 1.0),
 ('THE COST', [[wo('Chasing models is')],[co('a part-time job.')]], 'Reinstalling, re-prompting, re-learning: hours that never touch revenue.', [co('Hype is expensive.')], f"{M}/cost.png", 1.0),
 ('THE POSITION', [[wo('Own the layer')],[co('above the models.')]], 'Let them fight. Whoever wins, your system gets stronger the same afternoon.', [co('That is the only safe seat.')], f"{M}/position.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this before',l2='the next launch thread.',q='Which model panic did you buy?')
MARK2="claude"
