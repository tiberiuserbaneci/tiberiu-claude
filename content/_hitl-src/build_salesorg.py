#!/usr/bin/env python3
# A SALES ORG, NOT A BOT - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/salesorg"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your sales bot failed')],[co('because nobody was in charge.')]])
T2.CONTENT=[
 ('THE TRAP', [[wo('One agent doing all')],[co('does nothing well.')]], 'The mega-automation collapses under its own hundred branches.', [co('Complexity is not power.')], f"{M}/everything.png", 1.0),
 ('THE FIX', [[wo('Real teams')],[co('have structure.')]], 'Chief, desks, specialists. Sales worked this way for a century for a reason.', [co('Copy what works.')], f"{M}/structure.png", 1.0),
 ('DESK 1', [[wo('Research:')],[co('prospect intel.')]], 'CORTEX profiles, scores and briefs before anyone writes a word.', [co('Intel first.')], f"{M}/research.png", 1.0),
 ('DESK 2', [[wo('Outreach:')],[co('gated sends.')]], 'SPECTER drafts per channel; every send parks for your tap.', [co('Volume with brakes.')], f"{M}/outreach.png", 1.0),
 ('DESK 3', [[wo('Enablement:')],[co('paperwork, done.')]], 'Proposals, scheduling, follow-ups: the work nobody loves, on time.', [co('No dropped balls.')], f"{M}/enable.png", 1.0),
 ('DESK 4', [[wo('RevOps:')],[co('the pipe stays true.')]], 'Stages move on replies, data stays clean, digests land daily.', [co('Truth in the CRM.')], f"{M}/revops.png", 1.0),
 ('THE RULE', [[wo('One job per agent,')],[co('done extremely well.')]], 'That is a workforce, not a chatbot with a hundred to-dos.', [co('Specialists win.')], f"{M}/onejob.png", 1.0),
 ('THE CHIEF', [[wo('You sit on top.')],[co('One tap a day.')]], 'The org runs; you approve. Hierarchy with a human at the head.', [co('Chief, not operator.')], f"{M}/chief.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1='Save the org chart',l2='before you build a bot.',q='Which desk do you need first?')
MARK2="claude"
