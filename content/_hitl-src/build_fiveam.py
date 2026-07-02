#!/usr/bin/env python3
# THE 5AM SHIFT - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/fiveam"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('My team clocks in at 5am.')],[co('I meet them at seven.')]])
T2.CONTENT=[
 ('05:00', [[wo('The shift starts.')],[co('Nobody set an alarm.')]], 'Research, triage and drafting wake on schedule, not on willpower.', [co('Scheduled beats motivated.')], f"{M}/clockin.png", 1.0),
 ('05:10', [[wo('Trends read.')],[co('Signals scored.')]], 'Overnight movers in your niche, ranked against your ICP before sunrise.', [co('The market got read first.')], f"{M}/trends.png", 1.0),
 ('05:30', [[wo('Content drafted')],[co('against the calendar.')]], "Today's slots filled in your voice, ranked by your bar, parked for your tap.", [co('The feed is prepped.')], f"{M}/drafted.png", 1.0),
 ('06:00', [[wo('Workflows built')],[co("from yesterday's friction.")]], 'The repeated job you cursed at 16:00 became a flow by 06:00.', [co('The desk self-extends.')], f"{M}/builtflow.png", 1.0),
 ('06:45', [[wo('The digest compiles.')],[co('One page, everything.')]], 'Done, parked, waiting, suggested: your whole company on one screen.', [co('Reading time: 4 minutes.')], f"{M}/digest10.png", 1.0),
 ('07:00', [[wo('You walk in.')],[co('The work is staged.')]], 'Approvals, two calls, one judgement decision: the day is already moving.', [co('You start at the top.')], f"{M}/walkin.png", 1.0),
 ('THE COST10', [[wo('The night shift')],[co('bills in cents.')]], 'No overtime, no burnout, no Monday mood.', [co('Payroll stayed flat.')], f"{M}/cost10.png", 1.0),
 ('THE FLIP10', [[wo('Stop starting your day.')],[co('Start joining it.')]], 'The 5am team exists. Yours is just not hired yet.', [co('Hire it tonight.')], f"{M}/flip10.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1='Save the 5am setup',l2='and hire the night shift.',q='What should run before you wake?')
MARK2="claude"
