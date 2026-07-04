#!/usr/bin/env python3
# THE BUILD-IT-YOURSELF TRAP - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/diytrap"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('I built an agent from scratch.')],[co('Installing took 10 minutes.')]])
T2.CONTENT=[
 ('THE TUTORIAL', [[wo('Ten slides in,')],[co('you are an engineer.')]], 'Frameworks, graphs, state machines, control flow. The tutorial forgot you run a company.', [co('You wanted leverage, not a job.')], f"{M}/recipe.png", 1.0),
 ('THE WIRING', [[wo('Plan, act, observe.')],[co('You wire every arrow.')]], 'The loop the tutorials teach is real. Wiring it yourself is three weekends.', [co('The diagram is the easy part.')], f"{M}/wiring.png", 1.0),
 ('THE REALITY', [[wo('It breaks the week')],[co('you stop watching.')]], 'Edge cases, silent failures, no gate on sends. DIY agents fail in private.', [co('Nobody audits your graph.')], f"{M}/breaks.png", 1.0),
 ('THE BILL', [[wo('The hours went in.')],[co('The leads did not come out.')]], 'Every weekend on plumbing is a weekend not selling. That is the real invoice.', [co('Opportunity cost compounds.')], f"{M}/bill.png", 1.0),
 ('THE INSTALL', [[wo('Seven agents,')],[co('already wired.')]], 'CORTEX, SPECTER, STRIKER and the rest: built, tested, composing with each other.', [co('Ten minutes to first run.')], f"{M}/install.png", 1.0),
 ('THE DIFFERENCE', [[wo('Their loop is a demo.')],[co('This one is audited.')]], 'Every cycle checks its own work, every external send parks for your tap.', [co('Power with a keel.')], f"{M}/audited.png", 1.0),
 ('THE FIRST RUN', [[wo('One sentence in.')],[co('Twenty briefs out.')]], 'Source my next twenty accounts: typed at 09:14, briefed by 09:23.', [co('That was minute ten.')], f"{M}/firstrun.png", 1.0),
 ('THE VERDICT', [[wo('Build your product.')],[co('Not your plumbing.')]], 'The company wins on offers and distribution, not on hand-wired graphs.', [co('Leverage, not homework.')], f"{M}/verdict.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save the comparison',l2='before you open the tutorial.',q='Would you build or install?')
MARK2="claude"
