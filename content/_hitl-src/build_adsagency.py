#!/usr/bin/env python3
# THE AD DESK, IN-HOUSE - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/adsagency"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('I fired my ad agency.')],[co('A chat window replaced it.')]])
T2.CONTENT=[
 ('THE RETAINER', [[wo('It bought slides')],[co('and delays.')]], 'Research, copy, audits: billed monthly, delivered quarterly.', [co('That bill ends here.')], f"{M}/retainer.png", 1.0),
 ('MONDAY', [[wo('Rival ads,')],[co('diffed weekly.')]], 'Every new creative your competitors launched, in one report.', [co('You see their moves.')], f"{M}/spy.png", 1.0),
 ('THE GAP', [[wo('The empty angle')],[co('is found for you.')]], 'Hooks ranked by frequency; the angles nobody covers become yours.', [co('Attack the gap.')], f"{M}/gap.png", 1.0),
 ('THE DRAFTS', [[wo('Twenty variations')],[co('from one description.')]], 'Short, medium, long: in your voice, against your brand rules.', [co('A week of copy, instantly.')], f"{M}/variations.png", 1.0),
 ('THE AUDIT', [[wo('186 checks')],[co('before budget moves.')]], 'Fatigue, overlap, anomalies: a health score with a fix list attached.', [co('Audit, then spend.')], f"{M}/audit.png", 1.0),
 ('THE SCORE', [[wo('Any ad, scored')],[co('before it spends.')]], 'Six dimensions; weak hooks get rewritten, not launched.', [co('No gut launches.')], f"{M}/score.png", 1.0),
 ('THE CHAIN', [[wo('The retainer month,')],[co('in one morning.')]], 'Spy, gap, draft, audit, score: chained, under an hour.', [co('Monday ritual.')], f"{M}/chain.png", 1.0),
 ('THE SIGNATURE', [[wo('Every launch')],[co('signs with your tap.')]], 'Nothing spends without you. In-house means in your hands.', [co('Your call, always.')], f"{M}/sign.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save the ad desk,',l2='cancel the retainer.',q='Which check would save you most?')
MARK2="claude"
