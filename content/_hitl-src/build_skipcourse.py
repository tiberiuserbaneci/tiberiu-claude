#!/usr/bin/env python3
# SKIP THE COURSE - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/skipcourse"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Mastery is not a course.')],[co('It is a hundred gated runs.')]])
T2.CONTENT=[
 ('THE PATH', [[wo('Prompting course, automation')],[co('course, coding course.')]], 'The mastery ladder the feed sells you is three curriculums deep.', [co('You run a company, not a degree.')], f"{M}/path9.png", 1.0),
 ('THE FLIP9', [[wo('Learn on your pipeline,')],[co('not on toy examples.')]], 'Every lesson that matters comes from a real run on real work.', [co('Tuition: cents.')], f"{M}/flip9.png", 1.0),
 ('RUN 1', [[wo('Ship one research job')],[co('end to end.')]], 'Twenty accounts briefed teaches more than any prompt anatomy lecture.', [co('Lesson one: context.')], f"{M}/run1.png", 1.0),
 ('RUN 10', [[wo('Correct it ten times.')],[co('Watch the rules stick.')]], 'By run ten your no-list exists and the drafts stop disappointing.', [co('Lesson two: memory.')], f"{M}/run10.png", 1.0),
 ('RUN 50', [[wo('Wire the triggers.')],[co('Stop initiating.')]], 'The jobs fire themselves; you approve. This is the automation course, lived.', [co('Lesson three: exits.')], f"{M}/run50.png", 1.0),
 ('RUN 100', [[wo('Mint your workflow')],[co('as a skill.')]], 'The coding course you skipped becomes one command you own.', [co('Lesson four: leverage.')], f"{M}/run100.png", 1.0),
 ('THE GATE9', [[wo('Every run is safe')],[co('to learn on.')]], 'Nothing external ships without your tap, so mistakes stay internal.', [co('The classroom has a keel.')], f"{M}/gate9.png", 1.0),
 ('THE DIPLOMA', [[wo('A hundred runs in,')],[co('the desk works like you.')]], 'No certificate. Just a pipeline that moves and a system that remembers.', [co('That is mastery.')], f"{M}/diploma.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save the operator path',l2='and run job one today.',q='What would your first real run be?')
MARK2="claude"
