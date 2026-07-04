#!/usr/bin/env python3
# RESELL THE VOICE AGENT - adaptare IG Scraped (s3src47) in context Ultron.
# Angle: the BUSINESS of reselling voice-AI agents to local shops (Ultron builds+runs them in cents).
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src47"; LIB=T2.LIB
PREMIUM=1
TITLE="RESELL THE VOICE AGENT"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Local shops book by phone.')],[co('Resell them a voice agent.')]])
T2.CONTENT=[
 ('THE GAP', [[wo('Every missed call')],[co('is a booking gone.')]], 'Local shops still book by phone, and half the calls ring out to voicemail.', [co('That gap is your market.')], f"{M}/gap.png", 1.0),
 ('THE PROSPECTS', [[wo('Find the shops still')],[co('stuck on the phone.')]], 'Google Maps is full of clinics, salons and garages drowning in calls.', [co('Thirty in your city.')], f"{M}/market.png", 1.0),
 ('THE BUILD', [[wo('One brief in.')],[co('A voice agent out.')]], 'Paste their services into Ultron. It builds the agent that answers and books.', [co('You write zero code.')], f"{M}/build.png", 1.0),
 ('THE MARGIN', [[wo('It runs for cents.')],[co('You bill by the month.')]], 'Ultron answers each call for a few cents. The client pays you a flat retainer.', [co('The margin is yours.')], f"{M}/margin.png", 1.0),
 ('THE OFFER', [[wo('Setup fee, then')],[co('a monthly retainer.')]], 'Charge to launch it, then bill every month it keeps answering their phone.', [co('Priced like a service.')], f"{M}/offer.png", 1.0),
 ('ALWAYS ON', [[wo('It answers every call,')],[co('day and night.')]], 'No lunch break, no voicemail, no missed booking. It picks up on ring one.', [co('Zero calls dropped.')], f"{M}/alwayson.png", 1.0),
 ('THE STACK', [[wo('Each client is')],[co('a recurring line.')]], 'Stack a handful of local shops and the monthly retainers add up fast.', [co('Recurring, not one-off.')], f"{M}/mrr.png", 1.0),
 ('THE PORTFOLIO', [[wo('Ten clients,')],[co('one dashboard.')]], 'Ultron runs every agent. You watch the pipeline and collect the retainers.', [co('One operator, many shops.')], f"{M}/portfolio.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the reseller playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='resell the phone.',q='Which local shop would you pitch first?')
MARK2="claude"
