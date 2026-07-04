#!/usr/bin/env python3
# NEVER RENT ONE BRAIN - adaptare IG Scraped s3src25 in context Ultron (vendor lock-in / multi-model)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src25"; LIB=T2.LIB
PREMIUM=1
TITLE="NEVER RENT ONE BRAIN"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('18 free months.')],[co('One vendor forever.')]])
T2.CONTENT=[
 ('THE CAGE', [[wo('Free rents you')],[co('one brain.')]], 'One vendor gives you a single model and walls off every other frontier brain.', [co('One ceiling, no exit.')], f"{M}/cage.png", 1.0),
 ('THE TAX', [[wo('One tier bills')],[co('every job the same.')]], 'A single plan charges flagship rates for a two-word lookup and a deep analysis alike.', [co('You overpay the small jobs.')], f"{M}/tax.png", 1.0),
 ('THE ROUTER', [[wo('It shops every')],[co('model for you.')]], 'Each job gets read, then sent to the cheapest tier across providers that can do it.', [co('You never pick a model.')], f"{M}/router.png", 1.0),
 ('THE BENCH', [[wo('Every frontier model')],[co('on one account.')]], 'Lite, Smart and Deep across providers, all on tap. None of them your landlord.', [co('Swap any time.')], f"{M}/bench.png", 1.0),
 ('THE PRICE', [[wo('Prepay a leash,')],[co('or pay in cents.')]], 'A locked yearly plan, or pay-per-token where you only spend on the work you run.', [co('Cents, not a contract.')], f"{M}/cents.png", 1.0),
 ('THE MEMORY', [[wo('Your context is')],[co('not their hostage.')]], 'ICP, pipeline and docs live in one core you own. Change the model, keep the memory.', [co('Portable, always yours.')], f"{M}/memory.png", 1.0),
 ('THE SWAP', [[wo('Best model this month,')],[co('not last year.')]], 'Providers hot-swap under one socket. No contract, no expiry, no migration.', [co('No lock-in, ever.')], f"{M}/swap.png", 1.0),
 ('THE OPERATOR', [[wo('Own the router,')],[co('not the rental.')]], 'One login wires every model, cents per job and your own memory into one operator.', [co('All models, one system.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the model map?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='stop renting one brain.',q='Which model would you pick if you were not locked in?')
MARK2="claude"
