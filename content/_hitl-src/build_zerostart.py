#!/usr/bin/env python3
# STARTING FROM ZERO, 2026 - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/zerostart"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Do not learn to code.')],[co('Build the business instead.')]])
T2.CONTENT=[
 ('THE SHIFT', [[wo('The barrier moved.')],[co('It is not technical.')]], 'Niche, distribution, consistency: the only three problems left.', [co('Everything else is solved.')], f"{M}/barrier.png", 1.0),
 ('THE BUILD', [[wo('The build is')],[co('a sentence now.')]], 'Describe the offer; Crescendo assembles the page from 822 parts.', [co('Live the same day.')], f"{M}/build.png", 1.0),
 ('THE ENGINE', [[wo('The workflow runs')],[co('without you.')]], 'Flows on triggers handle follow-up, delivery and reporting.', [co('Set exits, not alarms.')], f"{M}/workflow.png", 1.0),
 ('THE NICHE', [[wo('Pick a problem')],[co('people already pay for.')]], 'Boring niches, real invoices. The unglamorous print money.', [co('Boring is beautiful.')], f"{M}/problem.png", 1.0),
 ('THE HABIT', [[wo('Show up daily.')],[co('The desk makes it cheap.')]], '14 posts planned from one line; your only job is to be real.', [co('Consistency, automated.')], f"{M}/daily.png", 1.0),
 ('THE ODDS', [[wo('Most solo founders')],[co('hit profit in year one.')]], "Because the cost base is cents and the output is a team's.", [co('The math flipped.')], f"{M}/profit.png", 1.0),
 ('THE FIRST TEN', [[wo('Ten customers,')],[co('ten handshakes.')]], 'The machine sources and drafts; you close like a human.', [co('Humans buy from humans.')], f"{M}/ten.png", 1.0),
 ('THE DEED', [[wo('Zero code. One gate.')],[co('All yours.')]], 'Build, run, approve. The stack finally fits one person.', [co('Ownership, complete.')], f"{M}/yours.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], f"{LIB}/cta3d-builder.png", 0.92)
T2.CLOSE=dict(l1='Save the zero plan',l2='and pick the niche.',q='What would you start with?')
MARK2="claude"
