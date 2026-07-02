#!/usr/bin/env python3
# THE PLATFORM WAS NEVER IT - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/starthere"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('45 websites to make money.')],[co('You needed a system, not a list.')]])
T2.CONTENT=[
 ('THE LISTS', [[wo('Another 45 platforms.')],[co('Still no first dollar.')]], 'Freelance sites, store builders, writing platforms: the doors were never locked.', [co('Access was never the issue.')], f"{M}/lists9.png", 1.0),
 ('THE REAL GAP', [[wo('Platforms reward')],[co('systems, not signups.')]], 'The winners on every list show up daily, respond fast, and follow up. That is it.', [co('Boring, repeated, paid.')], f"{M}/gap9.png", 1.0),
 ('THE PROFILE', [[wo('Your profile is')],[co('an offer page.')]], 'The desk drafts it like one: outcome, proof, one clear next step.', [co('Most read like resumes.')], f"{M}/profile9.png", 1.0),
 ('THE RESPONSE', [[wo('First reply wins')],[co('on every platform.')]], 'Briefs read, responses drafted in minutes, parked for your tap.', [co('Speed is the algorithm.')], f"{M}/response9.png", 1.0),
 ('THE FOLLOW', [[wo('The money is in')],[co('reply number three.')]], 'Quiet clients get chased on triggers; delivered work gets reviewed and re-pitched.', [co('Nobody does this part.')], f"{M}/follow9.png", 1.0),
 ('THE PORTFOLIO', [[wo('Every delivery becomes')],[co('public proof.')]], 'The desk turns finished work into posts and case notes automatically.', [co('The flywheel starts here.')], f"{M}/portfolio9.png", 1.0),
 ('ONE PLATFORM', [[wo('Pick one door.')],[co('Run the system on it.')]], 'One platform, thirty days, the full loop. Then and only then, add the second.', [co('Depth beats directory.')], f"{M}/onedoor.png", 1.0),
 ('THE TRUTH9', [[wo('The list was free.')],[co('The discipline was not.')]], '45 websites, one differentiator: the operator behind the account.', [co('Be the operator.')], f"{M}/truth9.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], f"{LIB}/cta3d-founder.png", 0.92)
T2.CLOSE=dict(l1='Save this instead',l2='of another platform list.',q='Which platform are you blaming?')
MARK2="strip"
