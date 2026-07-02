#!/usr/bin/env python3
# FIVE CLAUDES, ONE FOUNDER - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/fivetools"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You are using one Claude.')],[co('There are five.')]])
T2.CONTENT=[
 ('DOOR 1', [[wo('Chat:')],[co('the fast answer.')]], 'Quick questions, summaries, first drafts. Where everyone starts and most people stop.', [co('The lobby, not the building.')], f"{M}/door1.png", 1.0),
 ('DOOR 2', [[wo('Projects:')],[co('the memory.')]], 'Recurring workstreams with context that survives: reporting, client work, board prep.', [co('Stop re-explaining yourself.')], f"{M}/door2.png", 1.0),
 ('DOOR 3', [[wo('Cowork:')],[co('the hands on files.')]], 'Reads your folders, works your spreadsheets, drafts your reports where they live.', [co('Real files, real work.')], f"{M}/door3.png", 1.0),
 ('DOOR 4', [[wo('Skills:')],[co('the repeatable plays.')]], 'Your workflows installed as commands: same play, every run, no re-prompting.', [co('Where leverage lives.')], f"{M}/door4.png", 1.0),
 ('DOOR 5', [[wo('Code:')],[co('the builder.')]], 'Pages, dashboards, tools from plain English, tested and shipped.', [co('For outcomes, not engineers.')], f"{M}/door5.png", 1.0),
 ('THE MISTAKE', [[wo('Using door one')],[co('for door four jobs.')]], 'Re-typing a workflow into Chat weekly is a Skills job done badly.', [co('Match the door to the job.')], f"{M}/mistake9.png", 1.0),
 ('THE DESK9', [[wo('Ultron wires all five')],[co('behind one composer.')]], 'Type the goal; the router opens the right door and carries your memory through it.', [co('No door knowledge required.')], f"{M}/desk9.png", 1.0),
 ('THE UNLOCK', [[wo('Non-technical was never')],[co('the barrier.')]], 'Knowing which door exists is 80% of mastering the machine.', [co('Open door two tonight.')], f"{M}/unlock9.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], f"{LIB}/cta3d-builder.png", 0.92)
T2.CLOSE=dict(l1='Save the map',l2='and open the right door.',q='Which Claude have you never opened?')
MARK2="claude"
