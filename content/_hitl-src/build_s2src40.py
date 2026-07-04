#!/usr/bin/env python3
# THE OVERNIGHT PIPELINE - adaptare IG in context Ultron (source: a "zero to agentic coder" resource
# guide, reframed as a founder OUTCOME/timeline: 18:00 lights out -> 09:00 full pipeline).
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src40"; LIB=T2.LIB
PREMIUM=1
TITLE="THE OVERNIGHT PIPELINE"
T2.TITLE=TITLE
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You went to bed empty.')],[co('You woke up booked.')]])
T2.CONTENT=[
 ('18:00 LIGHTS OUT', [[wo('You logged off at six.')],[co('It clocked in.')]], 'One line of plain English, then the operator worked the whole night shift.', [co('While you slept.')], f"{M}/lightsout.png", 1.0),
 ('THE RESEARCH', [[wo('847 accounts read.')],[co('40 worth your time.')]], 'CORTEX scanned the web overnight and ranked every account by fit.', [co('A shortlist by dawn.')], f"{M}/research.png", 1.0),
 ('THE ROUTER', [[wo('A full night of thinking')],[co('cost sixty cents.')]], 'The ROUTER picks the cheapest model tier that can do each job, per turn.', [co('Cents, not a salary.')], f"{M}/router.png", 1.0),
 ('THE OUTBOUND', [[wo('A 3-touch sequence,')],[co('written by midnight.')]], 'SPECTER drafted and queued a full sequence for all 40 prospects.', [co('Twelve cents total.')], f"{M}/outbound.png", 1.0),
 ('THE VOICE', [[wo('The drafts sound')],[co('like you wrote them.')]], 'Sampled from your real posts, your cadence, your banned words.', [co('Your voice, at scale.')], f"{M}/voice.png", 1.0),
 ('THE MEMORY', [[wo('It remembered')],[co('every no.')]], 'ICP, pipeline, pricing, past replies - every agent draws from one core.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('THE GATE', [[wo('Nothing sent.')],[co('All parked for you.')]], 'Forty emails ready, zero delivered until you tap approve at nine.', [co('Still your call.')], f"{M}/gate.png", 1.0),
 ('09:00 FULL PIPELINE', [[wo('You woke up')],[co('to a full pipeline.')]], 'One tap at nine ships the whole night. Thirty calls on the board.', [co('Zero to pipeline.')], f"{M}/morning.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the night-shift playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='wake up to pipeline.',q='What would you ship on the night shift?')
MARK2="claude"
