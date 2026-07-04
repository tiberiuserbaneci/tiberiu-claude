#!/usr/bin/env python3
# THE ONE-LAPTOP COMPANY - adaptare IG "70 AI business ideas this weekend" in context Ultron
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
TITLE="THE ONE-LAPTOP COMPANY"
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s270aibusiness"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('One laptop.')],[co('One whole company.')]])
T2.CONTENT=[
 ('THE LIST', [[wo('Seventy weekend ideas.')],[co('You need one.')]], 'Not a list to pick from. One operator that runs the business you pick.', [co('One, not seventy.')], f"{M}/seventy.png", 1.0),
 ('THE COMPANY', [[wo('The whole company')],[co('runs on one screen.')]], 'Research, outreach, content, deals, delivery. Five departments, no hires.', [co('No team. No office.')], f"{M}/laptop.png", 1.0),
 ('THE WEEKEND', [[wo('Friday night to')],[co('a running company.')]], 'Set it up over a weekend. By Sunday it is already working the pipeline.', [co('48 hours, not 48 days.')], f"{M}/weekend.png", 1.0),
 ('THE ROSTER', [[wo('Seven agents')],[co('do the jobs.')]], 'CORTEX researches, SPECTER writes outreach, STRIKER closes, PULSE posts.', [co('Your whole team, named.')], f"{M}/roster.png", 1.0),
 ('THE COST', [[wo('A team is salaries.')],[co('This is cents.')]], 'The stack a founder would hire runs to thousands a month. Ultron runs per token.', [co('Cents per run.')], f"{M}/cents.png", 1.0),
 ('THE MONEY', [[wo('Real money,')],[co('not a side project.')]], 'First outreach Saturday, first reply Sunday, first deal the week after.', [co('Revenue, not a demo.')], f"{M}/revenue.png", 1.0),
 ('THE GATE', [[wo('It moves.')],[co('You approve.')]], 'Every send, every deal, every publish parks for your tap. Nothing goes rogue.', [co('Your hand on it.')], f"{M}/gate.png", 1.0),
 ('THE CORE', [[wo('It never forgets')],[co('your company.')]], 'ICP, pipeline, pricing, docs. One memory every agent draws from.', [co('One brain, always on.')], f"{M}/memory.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the weekend playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='launch this weekend.',q='What would you run from one laptop?')
MARK2="claude"
