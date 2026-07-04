#!/usr/bin/env python3
# THE AGENT THAT CALLS - adaptare IG Scraped s3src36 in context Ultron (voice sales agent).
# Angle: it researches every lead, then places a REAL CALL, qualifies live, books the meeting.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src36"; LIB=T2.LIB
PREMIUM=1
TITLE="THE AGENT THAT CALLS"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('It researched the lead,')],[co('then called them.')]])
T2.CONTENT=[
 ('THE CALL', [[wo('It picked up the phone.')],[co('You were asleep.')]], 'Not another email in a dead inbox. A real voice, dialing a real number.', [co('The call, not the send.')], f"{M}/ring.png", 1.0),
 ('THE BRIEF', [[wo('It knew them')],[co('before it dialed.')]], 'Funding, role, stack, the hook. One page pulled from the live web in seconds.', [co('Research, then ring.')], f"{M}/dossier.png", 1.0),
 ('THE SCRIPT', [[wo('A branch for')],[co('every answer.')]], 'Objections mapped in advance. It never goes silent or freezes on the line.', [co('It handles the no.')], f"{M}/branch.png", 1.0),
 ('THE SCORE', [[wo('It qualified them')],[co('while it talked.')]], 'Budget, authority, need, timing scored live during the call, not after.', [co('Qualified on the call.')], f"{M}/gauge.png", 1.0),
 ('THE BOOKING', [[wo('It booked the meeting')],[co('before it hung up.')]], 'Reads your live availability and drops the invite onto your week itself.', [co('Straight to your week.')], f"{M}/calendar.png", 1.0),
 ('THE MEMORY', [[wo('Every word,')],[co('remembered.')]], 'Transcript, summary and next step logged. The next call opens where this closed.', [co('Nothing gets lost.')], f"{M}/memory.png", 1.0),
 ('THE VOLUME', [[wo('240 dials.')],[co('12 booked.')]], 'It worked the whole list overnight. You woke up to a full calendar.', [co('One night, one list.')], f"{M}/funnel.png", 1.0),
 ('THE GATE', [[wo('It calls.')],[co('You approve.')]], 'Every number it dials is on a list you signed off. Augmented, never rogue.', [co('Still your company.')], f"{M}/gate.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the call playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and let it',l2='call your list tonight.',q='What would 12 booked meetings by morning change?')
MARK2="claude"
