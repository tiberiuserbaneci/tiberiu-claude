#!/usr/bin/env python3
# DAY ONE: THE FIVE PLAYS - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/dayone"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Day one with Claude:')],[co('run these five plays.')]])
T2.CONTENT=[
 ('PLAY 1', [[wo('Teach it your business')],[co('before you ask anything.')]], '/init: one interview, ICP, offer, pricing, no-list. Ten minutes that change every answer after.', [co('Context beats clever prompts.')], f"{M}/teach.png", 1.0),
 ('PLAY 2', [[wo('Make it read')],[co('before it speaks.')]], 'First research run: twenty accounts profiled and scored against YOUR customer, not averages.', [co('Warm beats generic.')], f"{M}/read.png", 1.0),
 ('PLAY 3', [[wo('Feed it your voice,')],[co('not your instructions.')]], 'Paste your five best posts. Every draft after sounds like you on a good day.', [co('Voice is set once.')], f"{M}/voice.png", 1.0),
 ('PLAY 4', [[wo('Put one chore')],[co('on a trigger.')]], 'Follow up every quiet lead: typed once, runs daily, exits set, sends parked.', [co('Your first employee-shaped flow.')], f"{M}/chore.png", 1.0),
 ('PLAY 5', [[wo('End the day')],[co('with a digest.')]], 'Everything it did, everything it wants approved, tomorrow queued: one page at 07:00.', [co('You read, tap, done.')], f"{M}/digest.png", 1.0),
 ('THE HOUR', [[wo('Five plays,')],[co('sixty minutes total.')]], 'Not a course, not a certification. One hour of setup on the Ultron desk.', [co('Beginner is a choice.')], f"{M}/hour.png", 1.0),
 ('THE TRAP', [[wo('Skipping play one')],[co('breaks the other four.')]], 'Generic context makes generic outputs. Every disappointment traces back here.', [co('Do not skip the interview.')], f"{M}/trap.png", 1.0),
 ('THE CURVE', [[wo('Day one is the floor.')],[co('It only compounds.')]], 'Corrections become rules, rules become skills, the desk gets sharper weekly.', [co('Start the clock.')], f"{M}/curve.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], f"{LIB}/cta3d-builder.png", 0.92)
T2.CLOSE=dict(l1='Save the five plays',l2='for your first hour.',q='Which play do you run first?')
MARK2="claude"
