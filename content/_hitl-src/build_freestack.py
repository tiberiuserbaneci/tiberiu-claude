#!/usr/bin/env python3
# THE PRICE OF FULL PRICE - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/freestack"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You pay full price')],[co('for tools that exist free.')]])
T2.CONTENT=[
 ('THE TERMINAL', [[wo('One desk pays yearly')],[co('what a clone gives free.')]], 'The Bloomberg-style terminal has an open twin at zero. Same charts, same data feeds.', [co('The gap is knowledge.')], f"{M}/terminal.png", 1.0),
 ('THE AUDIT', [[wo('Agencies bill monthly')],[co('for a script that runs daily.')]], 'Ad audits, inbox triage, model routers: open versions exist for all of them.', [co('You fund their margin.')], f"{M}/agencyfee.png", 1.0),
 ('THE CATCH', [[wo('Free tools are free')],[co('like a puppy is free.')]], 'Setup, updates, breakage, no gate, no memory. Assembly is the hidden invoice.', [co('Someone pays in weekends.')], f"{M}/catch.png", 1.0),
 ('THE GLUE', [[wo('Ten free tools')],[co('is eleven new jobs.')]], 'Each one alone, logged out, forgetting you. The glue between them is the product.', [co('Nobody ships the glue.')], f"{M}/glue.png", 1.0),
 ('THE LAYER', [[wo('One operator layer')],[co('over the whole stack.')]], 'Ultron wires mail, docs, CRM and payments into one desk with one memory.', [co('Assembled, not collected.')], f"{M}/layer.png", 1.0),
 ('THE METER', [[wo('The meter runs cents.')],[co('The retainers ran monthly.')]], 'Pay per run, not per seat, not per logo. High bills only live in the old stack.', [co('Cents, by design.')], f"{M}/meter.png", 1.0),
 ('THE KEEP', [[wo('Keep the free gems.')],[co('Wire them, gated.')]], 'Open tools plug into the desk; every external action still parks for your tap.', [co('Best of both, one gate.')], f"{M}/keep.png", 1.0),
 ('THE MATH', [[wo('Knowledge is the discount.')],[co('Assembly is the price.')]], 'Know the free twin, pay only for the layer that runs it while you sleep.', [co('That spread is yours.')], f"{M}/math.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this before',l2='your next renewal.',q='Which bill would you kill first?')
MARK2="strip"
