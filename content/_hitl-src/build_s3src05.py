#!/usr/bin/env python3
# OUTCOMES, NOT INSTRUCTIONS - adaptare IG s3src05 in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src05"; LIB=T2.LIB
PREMIUM=1
TITLE="OUTCOMES, NOT INSTRUCTIONS"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You still tell Claude every step.')],[co('Just give it the outcome.')]])
T2.CONTENT=[
 ('THE SHIFT', [[wo('A chatbot answers.')],[co('An operator acts.')]], 'You are still typing steps into a box. The job never actually gets finished.', [co('Talk is not work.')], f"{M}/shift.png", 1.0),
 ('THE BRIEF', [[wo('Type the outcome,')],[co('not the steps.')]], 'Book 20 demos. Ship the page. One line of intent, never a checklist.', [co('Intent in, work out.')], f"{M}/brief.png", 1.0),
 ('THE CREW', [[wo('It hires its own')],[co('crew for you.')]], 'The router reads the brief and assigns the agent that owns the job.', [co('You never pick.')], f"{M}/crew.png", 1.0),
 ('THE LOOP', [[wo('It fixes its')],[co('own mistakes.')]], 'Runs the work, catches its own error, retries, and keeps iterating for hours.', [co('It never stalls.')], f"{M}/loop.png", 1.0),
 ('THE MEMORY', [[wo('It knows your')],[co('whole business.')]], 'ICP, pipeline, pricing, docs. One memory every agent reads before it moves.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('THE GATE', [[wo('Nothing sends')],[co('without your tap.')]], 'It does the work. Every outbound move parks at the gate for your approval.', [co('Still your call.')], f"{M}/gate.png", 1.0),
 ('THE COST', [[wo('They bill seats.')],[co('You pay cents.')]], 'No per-seat licences you pay while idle. Every finished job costs cents.', [co('Cents, not dollars.')], f"{M}/cost.png", 1.0),
 ('THE OPERATOR', [[wo('One login runs')],[co('the whole crew.')]], 'Brief it once. Brain, crew, memory and gate report back in one place.', [co('The full operator.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the delegation playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and stop', l2='typing instructions.', q='What outcome would you hand over first?')
MARK2="claude"
