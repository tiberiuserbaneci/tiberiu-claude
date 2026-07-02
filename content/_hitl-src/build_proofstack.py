#!/usr/bin/env python3
# BUILDS THAT PAY RENT - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/proofstack"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Stop building portfolio pieces.')],[co('Build things that invoice.')]])
T2.CONTENT=[
 ('THE TRAP', [[wo('Demo projects impress.')],[co('They do not deposit.')]], 'Tutorial agents and portfolio repos collect stars, not revenue.', [co('Recruiters are not your market.')], f"{M}/trapd.png", 1.0),
 ('BUILD 1', [[wo('The lead machine:')],[co('live in a weekend.')]], 'Sources your ICP nightly, briefs every account, parks the openers for your tap.', [co('Pipeline while you sleep.')], f"{M}/build1.png", 1.0),
 ('BUILD 2', [[wo('The follow-up loop:')],[co('zero dropped threads.')]], 'Fires on silence, drafts on replies, logs everything to the pipe.', [co('Deals stop leaking.')], f"{M}/build2.png", 1.0),
 ('BUILD 3', [[wo('The content desk:')],[co('proof in public, daily.')]], 'Fourteen posts a week from one line, in your voice, gated.', [co('Distribution, automated.')], f"{M}/build3.png", 1.0),
 ('THE STACK', [[wo('Three builds,')],[co('one memory, one gate.')]], 'Each feeds the others: content warms leads, leads feed loops, loops close.', [co('A system, not a portfolio.')], f"{M}/stack8.png", 1.0),
 ('THE RECEIPTS', [[wo('Every build reports')],[co('in money terms.')]], 'Briefs became calls, threads became invoices, posts became inbound.', [co('Stars do not compound. This does.')], f"{M}/receipts8.png", 1.0),
 ('THE TIME', [[wo('Each build is')],[co('an evening, not a semester.')]], 'Described in plain English, assembled by the desk, tested on your real pipeline.', [co('Ship all three this week.')], f"{M}/time8.png", 1.0),
 ('THE FILTER', [[wo('Would a client pay')],[co('for this build?')]], 'If not, it is a hobby. Hobbies are fine. Just label them honestly.', [co('Invoice or hobby. Choose.')], f"{M}/filter8.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], f"{LIB}/cta3d-builder.png", 0.92)
T2.CLOSE=dict(l1='Save the three builds',l2='and ship the first one.',q='Which build pays your rent first?')
MARK2="claude"
