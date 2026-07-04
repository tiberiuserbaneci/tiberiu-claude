#!/usr/bin/env python3
# CREATE ONCE, SELL FOREVER - adaptare IG/TikTok in context Ultron (generat de adapt_build.py)
# Sursa Catalin: "50 Digital Product Ideas to sell". Reframe: nu ai nevoie de 50 de idei, ai
# nevoie de UN sistem care le livreaza. Ultron transforma o propozitie in produs digital, pe cents.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s250digitalproduct"; LIB=T2.LIB
PREMIUM=1
TITLE="CREATE ONCE, SELL FOREVER"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('50 product ideas.')],[co('One system ships them.')]])
T2.CONTENT=[
 ('THE TRAP', [[wo('A list of 50 ideas')],[co('ships zero products.')]], 'Every list adds ideas. None of them adds a product. The list is the procrastination.', [co('Pick one. Ship it.')], f"{M}/myth.png", 1.0),
 ('ONE SENTENCE', [[wo('Type it in plain English.')],[co('Get a product back.')]], 'One sentence in. Ultron returns the offer page, the PDF and the delivery email.', [co('No code, no designer.')], f"{M}/sentence.png", 1.0),
 ('THE OFFER PAGE', [[wo('A page that sells')],[co('while you sleep.')]], 'Hosted offer page, priced and live. A 49 dollar checkout, no Stripe wrestling.', [co('Live in minutes.')], f"{M}/offer.png", 1.0),
 ('PULSE + AMPLIFY', [[wo('Written, formatted,')],[co('scheduled, gated.')]], 'PULSE writes the launch, AMPLIFY schedules it, HUMAN GATE holds the send for your tap.', [co('You approve, it ships.')], f"{M}/pipeline.png", 1.0),
 ('THE HANDOFF', [[wo('Someone buys at 2am.')],[co('The file is already sent.')]], 'Payment clears, the delivery email fires, the PDF lands. You were asleep.', [co('Fulfilled overnight.')], f"{M}/delivery.png", 1.0),
 ('THE COMPOUND', [[wo('Create once.')],[co('Sell forever.')]], 'One product, sold on repeat. A 49 dollar sale became 1,240 a month while I did nothing.', [co('Recurring, hands-off.')], f"{M}/growth.png", 1.0),
 ('THE MATH', [[wo('You charge 49 dollars.')],[co('It runs for cents.')]], 'The whole build and every delivery cost pennies in tokens. The margin is almost the price.', [co('Cents in, dollars out.')], f"{M}/cents.png", 1.0),
 ('THE SYSTEM', [[wo('Stop collecting ideas.')],[co('Ship one system.')]], 'One system turns any idea into a live product. Memory keeps every past launch on file.', [co('One system, many products.')], f"{M}/system.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the build?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='ship your first product.',q='What would you sell if shipping took one sentence?')
MARK2="claude"
