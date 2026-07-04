#!/usr/bin/env python3
# THE WRONG PLUGIN AISLE - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/wrongaisle"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You installed developer toys.')],[co('Your pipeline noticed nothing.')]])
T2.CONTENT=[
 ('THE AISLE', [[wo('The plugin lists are')],[co('written for engineers.')]], 'Repo mappers, knowledge graphs, code navigators. Impressive, and irrelevant to your quarter.', [co('Wrong aisle for a founder.')], f"{M}/aisle.png", 1.0),
 ('THE TELL', [[wo('Cool demo,')],[co('zero revenue path.')]], 'If you cannot name the deal it moves or the hour it saves, it is a toy.', [co('Name it or skip it.')], f"{M}/tell.png", 1.0),
 ('THE FLIP', [[wo('Founder plugins')],[co('are desks, not tools.')]], 'Research, outbound, deals, content, legal: each install owns an outcome.', [co('Outcomes, not extensions.')], f"{M}/flip.png", 1.0),
 ('DESK CHECK', [[wo('Every plugin answers')],[co('one question:')]], 'What lands in the pipeline because this exists? CORTEX: briefs. SPECTER: replies. STRIKER: closes.', [co('One job, named.')], f"{M}/deskcheck.png", 1.0),
 ('THE STACK', [[wo('Five desks cover')],[co('a founder company.')]], 'Intel, outreach, deals, content, paperwork. The sixth is you, on the gate.', [co('That is the whole aisle.')], f"{M}/stackp.png", 1.0),
 ('THE TEST RUN', [[wo('Install, then demand')],[co('a receipt in 48 hours.')]], 'Twenty briefs, ten drafts, one proposal out. No receipt, uninstall.', [co('Plugins earn their slot.')], f"{M}/testrun.png", 1.0),
 ('THE TRAP', [[wo('Ten dev plugins deep,')],[co('still drafting alone.')]], 'The graph mapper cannot write your follow-up. The desk can.', [co('Tools do not sell.')], f"{M}/trapb.png", 1.0),
 ('THE RULE', [[wo('Shop by outcome,')],[co('never by demo.')]], 'If the plugin page shows code, you are in the wrong aisle. If it shows pipeline, install.', [co('Buy desks. Skip toys.')], f"{M}/rule7.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this before',l2='your next install spree.',q='Which aisle are you shopping in?')
MARK2="claude"
