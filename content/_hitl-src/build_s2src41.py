#!/usr/bin/env python3
# ONE COMMAND, SEVEN HIRES - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
TITLE="ONE COMMAND, SEVEN HIRES"
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src41"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('I gave one command.')],[co('Seven agents ran it.')]])
T2.CONTENT=[
 ('THE COMMAND', [[wo('You type an order,')],[co('not a prompt.')]], 'Plain English in. The right agent picks it up and runs, with zero setup.', [co('Command, do not chat.')], f"{M}/command.png", 1.0),
 ('THE ROSTER', [[wo('Seven named hires,')],[co('one login.')]], 'CORTEX, SPECTER, STRIKER, PULSE, SENTINEL, AMPLIFY, COUNSEL. Each owns one job.', [co('A team, not a chatbot.')], f"{M}/roster.png", 1.0),
 ('THE ROUTER', [[wo('It hands the job')],[co('to the right one.')]], 'The router reads each order, assigns the owner, and picks the model tier.', [co('You never pick a model.')], f"{M}/dispatch.png", 1.0),
 ('THE BILL', [[wo('The agency quoted')],[co('four figures.')]], 'Retainers, seats and six point tools. Same work, priced in cents per run here.', [co('Ours runs in cents.')], f"{M}/bill.png", 1.0),
 ('CORTEX', [[wo('One name in,')],[co('a ranked brief out.')]], 'Person, company and market profiled into one brief, ranked before you read it.', [co('Research, done for you.')], f"{M}/dossier.png", 1.0),
 ('THE GATE', [[wo('Nothing sends')],[co('without your tap.')]], 'Every external move parks in a queue. You approve, hold or edit, then it fires.', [co('Still your company.')], f"{M}/gate.png", 1.0),
 ('THE MEMORY', [[wo('Every hire reads')],[co('the same memory.')]], 'ICP, pipeline, pricing and docs live in one core. Nobody asks you twice.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('THE HANDOFF', [[wo('They pass work')],[co('to each other.')]], 'CORTEX briefs SPECTER, SPECTER feeds STRIKER. One order, a finished chain.', [co('One order, one chain.')], f"{M}/handoff.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the roster?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='command your team.',q='Which hire would you run first?')
MARK2="claude"
