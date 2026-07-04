#!/usr/bin/env python3
# ONE LOOP, HOUR BY HOUR - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/anatomy"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('A prompt is one guess.')],[co('A loop finishes the job.')]])
T2.CONTENT=[
 ('09:00', [[wo('The trigger fires.')],[co('Nobody typed anything.')]], 'Three leads went quiet for three days. The follow-up loop wakes itself up.', [co('Set once, weeks ago.')], f"{M}/trigger.png", 1.0),
 ('09:01', [[wo('It reads the thread')],[co('before it writes a word.')]], 'Last reply, the objection, your pricing rules: loaded from memory, not pasted.', [co('Context first, always.')], f"{M}/reads.png", 1.0),
 ('09:03', [[wo('Draft one.')],[co('It grades itself: 71.')]], 'Too long, weak trigger line. The loop does not ask you. It redoes.', [co('Your bar, applied.')], f"{M}/draft1.png", 1.0),
 ('09:06', [[wo('Draft three scores 90.')],[co('Now it stops.')]], 'Exit condition met. Not tired, not lazy, not hopeful. Verified.', [co('Loops end on proof.')], f"{M}/draft3.png", 1.0),
 ('09:07', [[wo('Three sends,')],[co('parked at the gate.')]], 'The loop is autonomous inside. Outside, it waits for one tap from you.', [co('Nothing leaves alone.')], f"{M}/parked.png", 1.0),
 ('09:40', [[wo('You tap twice,')],[co('kill one.')]], 'Ten seconds of judgement on top of forty minutes of machine work.', [co('That is the whole job now.')], f"{M}/tap.png", 1.0),
 ('14:20', [[wo('A reply lands.')],[co('The loop already logged it.')]], 'Pipeline moved, next follow-up scheduled, digest updated for 07:00.', [co('It closes its own circle.')], f"{M}/reply.png", 1.0),
 ('THE POINT', [[wo('One guess versus')],[co('a finished job.')]], 'A prompt gives you words. A loop gives you outcomes with receipts.', [co('Put one thing on repeat.')], f"{M}/point.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save the anatomy',l2='and set your first loop.',q='What would you put on repeat?')
MARK2="claude"
