#!/usr/bin/env python3
# THE 3-HOUR COURSE, INSTALLED - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/syllabus"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('I read the 3-hour syllabus.')],[co('My desk ships it preinstalled.')]])
T2.CONTENT=[
 ('MODULE 1', [[wo('Memory files and')],[co('system prompts.')]], 'The course teaches you to write them. The desk interviews you once and writes its own.', [co('Module one: automated.')], f"{M}/mod1.png", 1.0),
 ('MODULE 2', [[wo('Agent teams and')],[co('parallel harnesses.')]], 'Three hours on orchestration; here the seven agents already compose and hand off.', [co('Module two: wired.')], f"{M}/mod2.png", 1.0),
 ('MODULE 3', [[wo('Skills and subagents,')],[co('the leverage layer.')]], 'The syllabus explains the concept. The desk ships 71 working ones.', [co('Module three: stocked.')], f"{M}/mod3.png", 1.0),
 ('MODULE 4', [[wo('Browser automation')],[co('and computer use.')]], 'The lecture shows demos. The desk books, fills, checks and files, gated.', [co('Module four: hands, live.')], f"{M}/mod4.png", 1.0),
 ('MODULE 5', [[wo('Security, permissions')],[co('and org hygiene.')]], 'The course warns you. The desk defaults to the gate: nothing external without a tap.', [co('Module five: the keel.')], f"{M}/mod5.png", 1.0),
 ('THE GAP10', [[wo('Courses teach configuration.')],[co('Founders need outcomes.')]], 'Every hour configuring is an hour not selling. The config IS the product here.', [co('Buy outcomes, not setup.')], f"{M}/gap10.png", 1.0),
 ('THE HOUR10', [[wo('The 3 hours became')],[co('one onboarding.')]], 'Connect, interview, first run: the whole syllabus, lived by lunch.', [co('Watch it work instead.')], f"{M}/hour10.png", 1.0),
 ('THE POINT10', [[wo('Knowledge was never')],[co('the moat.')]], 'The people shipping are not the ones studying. Install, run, correct, repeat.', [co('Operators outlearn students.')], f"{M}/point10.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1='Save the checklist',l2='and skip the course.',q='Which module are you still doing by hand?')
MARK2="claude"
