#!/usr/bin/env python3
# IT FILES A REPORT - adaptare IG Scraped (s3src43 "Not a chatbot, a worker") in context Ultron.
# Narrow angle: proof-of-work. An agent is a WORKER because it clocks in, does a shift and LEAVES A
# DELIVERABLE you can open (a timestamped daily briefing) - it reports output, not chat.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
TITLE="IT FILES A REPORT"
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src43"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You do not chat a worker.')],[co('You read its report.')]])
T2.CONTENT=[
 ('THE PROOF', [[wo('A chatbot waits.')],[co('A worker files.')]], 'You wake to a finished briefing on your desk, not a blinking cursor.', [co('Read it, do not prompt it.')], f"{M}/proof.png", 1.0),
 ('THE ROLE', [[wo('It has a job title,')],[co('not a chat window.')]], 'Content operator, reports to you, on shift while you sleep.', [co('An employee, not a tab.')], f"{M}/badge.png", 1.0),
 ('THE SHIFT', [[wo('It clocks in')],[co('before you wake.')]], 'Runs on a 06:00 schedule, not on the second you happen to type.', [co('A shift, not a session.')], f"{M}/clockin.png", 1.0),
 ('THE TOOLS', [[wo('It reaches for')],[co('its own tools.')]], 'Web, inbox, calendar, docs, CRM, called on its own, unprompted.', [co('You paste nothing.')], f"{M}/tools.png", 1.0),
 ('THE MEMORY', [[wo('It remembers')],[co('every shift.')]], 'Yesterday feeds today. ICP, pipeline and pricing never reset.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('THE LOOP', [[wo('It runs')],[co('until it is done.')]], 'Plan, act, check, repeat. A chat stops dead at one reply.', [co('Done, not answered.')], f"{M}/loop.png", 1.0),
 ('THE DELIVERABLE', [[wo('Open the briefing.')],[co('The work is finished.')]], 'Research, a draft, your tasks and calendar, one page you can open.', [co('Output, not answers.')], f"{M}/briefing.png", 1.0),
 ('THE ROSTER', [[wo('Five roles.')],[co('One hire each.')]], 'Research, outbound, deals, content, code, a named worker per job.', [co('Cents per shift.')], f"{M}/roster.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the hire playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and stop',l2='chatting. Start hiring.',q='What would you file first if it worked the night shift?')
MARK2="claude"
