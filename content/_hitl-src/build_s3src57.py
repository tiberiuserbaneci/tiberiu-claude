#!/usr/bin/env python3
# THE MISSING FIFTH - adaptare IG Scraped (s3src57) in context Ultron. Angle: Claude Code got you
# 80 percent; the last fifth (memory, roster, router, gate) turns a raw model into an operator.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src57"; LIB=T2.LIB
PREMIUM=1
TITLE="THE MISSING FIFTH"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Claude Code got you 80 percent.')],[co('The last fifth is the operator.')]])
T2.CONTENT=[
 ('THE GAP', [[wo('You already did')],[co('the hard 80 percent.')]], 'Building with Claude Code is the hard part, and it is done. One fifth is left.', [co('The operator layer.')], f"{M}/gap.png", 1.0),
 ('THE RAW MODEL', [[wo('Raw power,')],[co('nothing wired to it.')]], 'A terminal is pure capability with no memory, no team, no router, no brake.', [co('One worker, four empty ports.')], f"{M}/haveit.png", 1.0),
 ('THE VAULT', [[wo('Every new chat')],[co('forgets your company.')]], 'The vault holds ICP, pipeline, pricing and docs so nothing starts from zero.', [co('It never forgets you.')], f"{M}/memory.png", 1.0),
 ('THE ROSTER', [[wo('One worker becomes')],[co('a named team of seven.')]], 'Research, outbound, deals, content, code, publishing and legal, each callable by name.', [co('Six specialists join.')], f"{M}/roster.png", 1.0),
 ('THE ROUTER', [[wo('It hires the agent')],[co('and prices the model.')]], 'Reads each job, picks the specialist and the cheapest tier that can actually do it.', [co('Cents, not dollars.')], f"{M}/router.png", 1.0),
 ('THE GATE', [[wo('Nothing sends')],[co('without your tap.')]], 'Every external move parks at a human gate. Powerful, never unsupervised.', [co('Still your company.')], f"{M}/gate.png", 1.0),
 ('RAW VS OPERATOR', [[wo('One layer of power')],[co('versus five that ship.')]], 'The raw model is layer one. Memory, roster, router and gate stack on top.', [co('Four layers you were missing.')], f"{M}/compare.png", 1.0),
 ('THE OPERATOR', [[wo('Stop running')],[co('a bare model.')]], 'Snap memory, roster, router and gate onto Claude Code and you have an operator.', [co('The full system, one login.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the last-fifth playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='wire the final fifth.',q='Which fifth are you still missing?')
MARK2="claude"
