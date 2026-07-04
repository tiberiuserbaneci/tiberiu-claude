#!/usr/bin/env python3
# THE ONE-LAPTOP COMPANY - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/million"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your next competitor')],[co('has no employees.')]])
T2.CONTENT=[
 ('THE SHAPE', [[wo('Not a funded startup.')],[co('Not a team of 20.')]], 'A laptop, a subscription measured in cents, systems that do not sleep.', [co('New shape of company.')], f"{M}/notteam.png", 1.0),
 ('THE SPLIT', [[wo('The agents work.')],[co('The founder decides.')]], 'Research, outreach, content, builds: parallel, gated by one tap.', [co('Judgement is the job.')], f"{M}/agents.png", 1.0),
 ('THE CURVE', [[wo('Revenue compounds.')],[co('Headcount stays 1.')]], 'Up 32% this month; payroll unchanged since day zero.', [co('The lines diverge.')], f"{M}/revenue.png", 1.0),
 ('THE MOAT', [[wo('Speed beats size')],[co('every quarter now.')]], 'Idea to live offer in an afternoon. Feedback to fix in an hour.', [co('Size became drag.')], f"{M}/speed.png", 1.0),
 ('THE COSTS', [[wo('The meter runs cents.')],[co('The market pays full.')]], 'Costs flat while output multiplies. That spread is the business.', [co('Margin by design.')], f"{M}/costs.png", 1.0),
 ('THE CALENDAR', [[wo('Empty calendar.')],[co('Full pipeline.')]], 'No standups, no syncs. Digests at 07:00, decisions when you choose.', [co('Time became yours.')], f"{M}/calendar.png", 1.0),
 ('THE CONTROL', [[wo('Every send gated.')],[co('Every risk yours.')]], 'Autonomy scaled, control kept. That is the whole architecture.', [co('Power with a keel.')], f"{M}/gated.png", 1.0),
 ('THE BET', [[wo('Someone builds this')],[co('this year.')]], 'The only question left is whether it is you.', [co('Why not you.')], f"{M}/you.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this thesis,',l2='then start tonight.',q='Could you run it alone?')
MARK2="claude"
