#!/usr/bin/env python3
# THE HIRING FREEZE - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/neverhire"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('I froze five job openings.')],[co('The desk absorbed them.')]])
T2.CONTENT=[
 ('ROLE 1', [[wo('Lead generation:')],[co('frozen.')]], 'Sourcing, scoring, briefing: CORTEX runs it overnight on your ICP, every day.', [co('The intern became a flow.')], f"{M}/leadgen.png", 1.0),
 ('ROLE 2', [[wo('Support triage:')],[co('frozen.')]], 'Inbox read, sorted, drafted. The rare hard case escalates to you with context attached.', [co('First reply in seconds.')], f"{M}/support.png", 1.0),
 ('ROLE 3', [[wo('Content ops:')],[co('frozen.')]], 'Fourteen slots planned from one line, drafts in your voice, queued at 10:00 local.', [co('The desk never misses Monday.')], f"{M}/content.png", 1.0),
 ('ROLE 4', [[wo('Sales follow-ups:')],[co('frozen.')]], 'Every quiet thread chased on a trigger, every send parked for your tap.', [co('Nothing slips, nothing sent alone.')], f"{M}/followups.png", 1.0),
 ('ROLE 5', [[wo('Review collection:')],[co('frozen.')]], 'Asked at the right moment, chased politely, logged where you see it.', [co('The quiet growth lever.')], f"{M}/reviews.png", 1.0),
 ('THE MATH', [[wo('Five salaries stayed')],[co('in the company.')]], 'The fastest growing companies are not working more. They run systems that work around the clock.', [co('Systems, not headcount.')], f"{M}/math.png", 1.0),
 ('THE LINE', [[wo('Freeze the repetitive.')],[co('Hire the judgement.')]], 'People for taste, relationships and calls. Flows for everything that repeats.', [co('That is the split.')], f"{M}/line.png", 1.0),
 ('THE TEST', [[wo('Would a checklist')],[co('do this job?')]], 'If yes, it is a flow, not a hire. Run the test before every job posting.', [co('Post fewer jobs, ship more.')], f"{M}/test.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save the freeze list',l2='before your next posting.',q='Which role would you freeze first?')
MARK2="claude"
