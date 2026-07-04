#!/usr/bin/env python3
# THE SIX-DOLLAR MARKET - adaptare IG Scraped (Sequoia $1 software vs $6 services thesis) in
# context Ultron: software is a small slice, services (human labor) is the giant market, Ultron
# automates the services layer in cents. (structura din build_aibody.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src44"; LIB=T2.LIB
PREMIUM=1
TITLE="THE SIX-DOLLAR MARKET"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Software was the $1.')],[co('Services are the $6.')]])
T2.CONTENT=[
 ('THE SPLIT', [[wo('For every dollar on software,')],[co('six go to services.')]], 'SaaS captured the small slice. The services spend was six times bigger.', [co('Six to one.')], f"{M}/split.png", 1.0),
 ('THE MARKET', [[wo('Software is a $650B')],[co('corner of the map.')]], 'Services are a multi-trillion market. The next era captures the service dollar.', [co('The rest is open.')], f"{M}/treemap.png", 1.0),
 ('THE BUDGET', [[wo('One software line.')],[co('Six services lines.')]], 'Research, outbound, deals, content, code, legal. Every line is human labor.', [co('Where the money sits.')], f"{M}/ledger.png", 1.0),
 ('THE SHIFT', [[wo('Nobody buys the tool.')],[co('They buy the finished work.')]], 'Not a legal app, the reviewed contract. Not a mail tool, the booked meeting.', [co('Sell the outcome.')], f"{M}/outcomes.png", 1.0),
 ('THE ROSTER', [[wo('Six services,')],[co('one operator runs them.')]], 'CORTEX research, SPECTER outbound, STRIKER deals, PULSE content, SENTINEL code, COUNSEL legal.', [co('The work, not the app.')], f"{M}/roster.png", 1.0),
 ('THE PRICE', [[wo('The six dollars in labor,')],[co('delivered for cents.')]], 'A human services line bills by the hour. Ultron bills by the token.', [co('Cents, not retainers.')], f"{M}/cents.png", 1.0),
 ('THE DELIVERY', [[wo('Request in, finished')],[co('work back out.')]], 'Sourced, drafted, reviewed, gated. The service runs end to end, not a blank tool.', [co('Done, not assisted.')], f"{M}/pipeline.png", 1.0),
 ('THE WEDGE', [[wo('The services spend')],[co('flows to one operator.')]], 'Automate the six-dollar layer. That is where the next company gets built.', [co('Own the six.')], f"{M}/wedge.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the services map?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='automate the six.',q='Which services line eats your week?')
MARK2="claude"
