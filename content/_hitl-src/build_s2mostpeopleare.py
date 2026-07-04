#!/usr/bin/env python3
# QUESTIONS VS SYSTEMS - adaptare Catalin ("Most people are still asking AI questions. The ones
# winning in 2026 are building systems.") in context Ultron: stop asking, start operating.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2mostpeopleare"; LIB=T2.LIB
PREMIUM=1
TITLE="STOP ASKING, START OPERATING"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You keep asking AI.')],[co('Winners build systems.')]])
T2.CONTENT=[
 ('THE SPLIT', [[wo('You ask questions.')],[co('Operators wire systems.')]], 'A prompt gives one answer. A system runs the whole job without you in the loop.', [co('Stop asking. Start operating.')], f"{M}/split.png", 1.0),
 ('THE LOOP', [[wo('It runs while')],[co('you sleep.')]], 'The loop triggers, works, checks and repeats. Nobody sits there retyping a prompt.', [co('Set once, runs nightly.')], f"{M}/loop.png", 1.0),
 ('THE ROSTER', [[wo('One chat is one worker.')],[co('This is a whole team.')]], 'Seven named agents for research, outbound, deals, content, code and legal work.', [co('A roster, not a chatbot.')], f"{M}/roster.png", 1.0),
 ('THE WATCH', [[wo('It watched all night.')],[co('You asked once.')]], 'Funding, hiring, stack and intent, tracked on triggers while you were logged off.', [co('Watched, not queried.')], f"{M}/radar.png", 1.0),
 ('THE OUTPUT', [[wo('You wake to results.')],[co('Not a blank prompt.')]], 'Briefs, drafts and fixes stacked and ready, all done overnight while you slept.', [co('Output, not a cursor.')], f"{M}/stack.png", 1.0),
 ('THE SCALE', [[wo('One question, one answer.')],[co('One system, thousands.')]], 'A prompt scales to how fast you type. A system scales across every account at once.', [co('Cents per thousand runs.')], f"{M}/field.png", 1.0),
 ('THE GATE', [[wo('It runs without you.')],[co('It sends with you.')]], 'Every external move parks for your tap. Full power, still held on your reins.', [co('Autonomy, still gated.')], f"{M}/gate.png", 1.0),
 ('THE OPERATOR', [[wo('Stop asking AI.')],[co('Start running one.')]], 'Research, outbound, content and code composed into one system you operate by login.', [co('The system, one login.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='stop asking AI.',q='What could run tonight without you?')
MARK2="claude"
