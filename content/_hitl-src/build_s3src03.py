#!/usr/bin/env python3
# YOU ARE THE BILL - adaptare IG Scraped "67 best open-source AI repos" in context Ultron.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src03"; LIB=T2.LIB
PREMIUM=1
TITLE="YOU ARE THE BILL"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('No api. No bill.')],[co('You are the bill.')]])
T2.CONTENT=[
 ('THE LIST', [[wo('Sixty-seven repos')],[co('to clone this month.')]], 'Four layers of open-source tools, and cloning is the only free part.', [co('Free to download.')], f"{M}/shoppinglist.png", 1.0),
 ('VANITY METRIC', [[wo('98K stars.')],[co('Zero of them run.')]], 'A star is a bookmark. It will not host the model or answer your pager.', [co('Stars are not deploys.')], f"{M}/startrap.png", 1.0),
 ('THE GLUE', [[wo('Cloning is the easy part.')],[co('Now wire them.')]], 'Seven repos, six integrations, all of it yours to write and maintain.', [co('You are the integrator.')], f"{M}/theglue.png", 1.0),
 ('DEPENDENCY ROT', [[wo('Monday it breaks')],[co('again.')]], 'Every repo ships on its own clock. You are the on-call for all of them.', [co('The version treadmill.')], f"{M}/rot.png", 1.0),
 ('TRUE COST', [[wo('No bill?')],[co('Read the invoice.')]], 'The repo is free. The GPUs, the ops and your nights are the price.', [co('Cents, not a cluster.')], f"{M}/truecost.png", 1.0),
 ('THE OPERATOR', [[wo('The whole stack,')],[co('pre-wired.')]], 'Seven agents on Claude, assembled on login one, with nothing to host.', [co('No repos to clone.')], f"{M}/operator.png", 1.0),
 ('MODEL ROUTER', [[wo('No model to choose.')],[co('It picks the tier.')]], 'You never pick ollama vs vllm vs a model. The router picks the cheapest that works.', [co('Priced in cents.')], f"{M}/modelshelf.png", 1.0),
 ('HUMAN GATE', [[wo('You approve.')],[co('It ships.')]], 'No cloning, no hosting, no pager. One login and cents per run.', [co('Still your company.')], f"{M}/gate.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the build map?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this before',l2='you clone repo one.',q='What are you still self-hosting that a login could replace?')
MARK2="claude"
