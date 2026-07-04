#!/usr/bin/env python3
# SYSTEMS NOT EMPLOYEES - adaptare IG "most businesses need better AI systems, not more employees"
# in context Ultron: stop hiring, start wiring - the 7-agent roster replaces headcount at cents.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2mostbusinessesdo"; LIB=T2.LIB
PREMIUM=1
TITLE="SYSTEMS NOT EMPLOYEES"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Stop hiring.')],[co('Start wiring.')]])
T2.CONTENT=[
 ('THE ROSTER', [[wo('Five job posts,')],[co('or one login.')]], 'Research, outbound, deals, content, code, publishing, legal. Seven roles, one seat.', [co('Seven agents, one seat.')], f"{M}/roles.png", 1.0),
 ('THE MATH', [[wo('A hire costs a salary.')],[co('An agent costs cents.')]], 'The stack a founder hires runs six figures a year. The same work runs on tokens.', [co('Cents, not salaries.')], f"{M}/payroll.png", 1.0),
 ('THE PIPELINE', [[wo('One job, wired')],[co('end to end.')]], 'Research hands to outbound, outbound to deals. No handoff meetings, no dropped context.', [co('Nothing lost between roles.')], f"{M}/pipeline.png", 1.0),
 ('THE WORK', [[wo('Briefs, emails, pages.')],[co('Done by morning.')]], 'Every role ships real output overnight while you are offline.', [co('Shipped while you slept.')], f"{M}/shipped.png", 1.0),
 ('THE EYES', [[wo('It saw the market')],[co('before I did.')]], 'Funding, hiring, stack, churn. One agent watches every night, not once a quarter.', [co('Overnight, every night.')], f"{M}/watch.png", 1.0),
 ('THE SCALE', [[wo('One founder,')],[co('a thousand tasks.')]], 'The roster runs in parallel. You review the ones that matter, you do not do the work.', [co('Parallel, not serial.')], f"{M}/scale.png", 1.0),
 ('THE CORE', [[wo('One memory')],[co('feeds them all.')]], 'ICP, pipeline, pricing, docs. Every agent reads and writes the same core.', [co('Nothing forgets you.')], f"{M}/hub.png", 1.0),
 ('THE GATE', [[wo('Nothing sends')],[co('without your tap.')]], 'Every external move parks at the human gate. Augmented, never unsupervised.', [co('Still your company.')], f"{M}/gate.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the roster?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='wire the roster.',q='Which role would you wire first?')
MARK2="claude"
