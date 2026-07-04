#!/usr/bin/env python3
# THE FIFTEEN-HOUR AUDIT - adaptare IG Scraped (s3src54) in context Ultron. Angle: a per-task time
# map. The recurring founder tasks that eat 16 hrs a week, each handed to a named Ultron agent,
# itemized and given back. Hero = the weekly time-audit breakdown. (structura din build_aibody.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src54"; LIB=T2.LIB
PREMIUM=1
TITLE="THE FIFTEEN-HOUR AUDIT"
T2.TITLE=TITLE
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You lose 15 hours a week.')],[co('Here is where they go.')]])
T2.CONTENT=[
 ('THE AUDIT', [[wo('Sixteen hours, hiding')],[co('in your calendar.')]], 'Not one big task. Seven recurring ones, each eating hours you never bill.', [co('Itemized, not vague.')], f"{M}/audit.png", 1.0),
 ('CORTEX', [[wo('Monday prospecting,')],[co('done before coffee.')]], 'Four hours of tabs and note-taking, returned as one ranked account brief.', [co('4 hours back.')], f"{M}/cortex.png", 1.0),
 ('SPECTER', [[wo('The follow-ups')],[co('run themselves.')]], 'Four-step sequences written and timed for every prospect, no more chasing.', [co('3 hours back.')], f"{M}/specter.png", 1.0),
 ('PULSE', [[wo('One idea reaches')],[co('four feeds.')]], 'A single operator note reshaped in your voice for every channel you post to.', [co('3 hours back.')], f"{M}/pulse.png", 1.0),
 ('STRIKER', [[wo('Discovery prep,')],[co('already handled.')]], 'Questions, objections and the priced proposal drafted before every call.', [co('2 hours back.')], f"{M}/striker.png", 1.0),
 ('SENTINEL', [[wo('Fixes shipped')],[co('from a sentence.')]], 'Dashboards, fixes and automations described in plain English, tested first.', [co('2 hours back.')], f"{M}/sentinel.png", 1.0),
 ('THE LAST TWO', [[wo('The quiet hours')],[co('nobody sees.')]], 'Formatting, scheduling and contract review, off your plate every week.', [co('2 hours back.')], f"{M}/routine.png", 1.0),
 ('GIVEN BACK', [[wo('The hours do not')],[co('vanish. They move.')]], 'Sixteen hours redirected to selling, building and the work only you can do.', [co('Your week, returned.')], f"{M}/giveback.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the time map?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='audit your own week.',q='Which of the sixteen hours would you take back first?')
MARK2="claude"
