#!/usr/bin/env python3
# PROMPTS ARE DEAD, LOOPS RUN - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/loops"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Stop writing prompts.')],[co('Start setting exits.')]])
T2.CONTENT=[
 ('THE OLD WAY', [[wo('You are a human cron job.')],[co('Admit it.')]], 'If you type prompt after prompt, you work backwards, one output at a time.', [co('You are the cron job.')], f"{M}/oldway.png", 1.0),
 ('THE LOOP', [[wo('212 cycles ran.')],[co('I typed 3 sentences.')]], 'An Ultron flow has a goal, a checker and an exit. It cycles until done.', [co('24/7, no typing.')], f"{M}/loop.png", 1.0),
 ('STEP 1', [[wo('One sentence replaced')],[co('my follow-up job.')]], 'Follow up every lead that goes quiet for 3 days. One sentence, one flow.', [co('That is the whole setup.')], f"{M}/define.png", 1.0),
 ('STEP 2', [[wo('9:00 fires without me.')],[co('Every single day.')]], 'Daily 09:00, on every reply, on usage drop. Triggers replace your memory.', [co('No reminders app.')], f"{M}/trigger.png", 1.0),
 ('STEP 3', [[wo('It grades its own work.')],[co('Before I ever see it.')]], 'Every cycle checks the result before it reports. Failures retry, not repeat.', [co('The checker is built in.')], f"{M}/verify.png", 1.0),
 ('THE TRAP', [[wo('Loops without exits')],[co('eat budgets alive.')]], 'A loop without an exit spends while you sleep. Ultron caps every flow.', [co('Guardrails by default.')], f"{M}/trap.png", 1.0),
 ('THE GATE', [[wo('Full speed inside.')],[co('Handbrake on the door.')]], 'Anything external still parks on HOLD for your tap. Speed with brakes.', [co('You stay the exit.')], f"{M}/gate.png", 1.0),
 ('THE SCALE', [[wo('My hours stopped scaling.')],[co('My systems did not.')]], 'Nine flows ran 212 cycles last week. You typed three sentences.', [co('Scale past your hours.')], f"{M}/scale.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], f"{LIB}/cta3d-builder.png", 0.92)
T2.CLOSE=dict(l1='Save this before',l2='your next prompt.',q='Which task would you loop first?')
MARK2="claude"
