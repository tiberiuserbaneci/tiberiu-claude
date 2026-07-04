#!/usr/bin/env python3
# AGENTS THAT LEARN - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/selflearn"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Most agents forget everything.')],[co('Mine files the lesson.')]])
T2.CONTENT=[
 ('THE AMNESIA', [[wo('Same mistakes.')],[co('Every single run.')]], 'A task finishes, the context dies, tomorrow starts from zero. That is most agents today.', [co('Groundhog day, automated.')], f"{M}/amnesia7.png", 1.0),
 ('THE TAX', [[wo('You correct the same error')],[co('for the fortieth time.')]], 'Every repeated correction is payroll you pay in attention.', [co('Forgetting is expensive.')], f"{M}/tax.png", 1.0),
 ('THE LOOP', [[wo('Evaluate. Reflect.')],[co('Store. Apply.')]], 'The self-improving loop: the agent grades its output, writes the lesson, uses it next run.', [co('Sharper every cycle.')], f"{M}/looplearn.png", 1.0),
 ('THE FILE', [[wo('Corrections become rules.')],[co('Rules become skills.')]], 'Say no discounts once: blocked forever. Fix a draft once: the fix generalizes.', [co('Your feedback compounds.')], f"{M}/file7.png", 1.0),
 ('THE CURVE', [[wo('Run one is average.')],[co('Run one hundred is yours.')]], 'The same flow, months later, writes like you, prices like you, filters like you.', [co('Time turns it native.')], f"{M}/curve7.png", 1.0),
 ('THE PROOF', [[wo('My no-list has 34 rules.')],[co('I wrote none of them twice.')]], 'Each one came from a single correction that never needed repeating.', [co('Said once, kept forever.')], f"{M}/proof7.png", 1.0),
 ('THE GATE', [[wo('It learns alone.')],[co('It still sends with you.')]], 'Self-improvement stays internal; every external move parks for your tap.', [co('Smarter, not looser.')], f"{M}/gate7.png", 1.0),
 ('THE QUESTION', [[wo('If it cannot remember you,')],[co('why are you training it daily?')]], 'Demand memory before you demand intelligence.', [co('Memory first. Always.')], f"{M}/question7.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save the learning loop',l2='and stop repeating yourself.',q='What has yours learned this month?')
MARK2="claude"
