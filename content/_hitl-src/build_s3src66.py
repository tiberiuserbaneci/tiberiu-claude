#!/usr/bin/env python3
# BLANK PAGE TO LIVE CAMPAIGN - adaptare IG Scraped s3src66 in context Ultron (blank ads manager ->
# live campaign generation: creatives + audiences + budget). Angle: the paralysis of the empty
# ads manager, not the "agency replacement" angle already built (adsagency / agency).
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src66"; LIB=T2.LIB
PREMIUM=1
TITLE="BLANK PAGE TO LIVE CAMPAIGN"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('A blank ads manager')],[co('is where budgets die.')]])
T2.CONTENT=[
 ('THE BLANK PAGE', [[wo('You open Ads Manager.')],[co('Then you just stare.')]], 'Day three, the campaign is still a blinking cursor and an empty budget field.', [co('Zero live, zero spend.')], f"{M}/blank.png", 1.0),
 ('THE BRIEF', [[wo('Give it three lines.')],[co('Offer, audience, pain.')]], 'Claude reads your brief the way a strategist would, then goes to work.', [co('That is the whole input.')], f"{M}/brief.png", 1.0),
 ('TWELVE OUT', [[wo('Twelve ad variants.')],[co('One afternoon.')]], 'Four angles by three hooks. Headline, primary text and CTA on every card.', [co('Not three, in two weeks.')], f"{M}/fanout.png", 1.0),
 ('THE AUDIENCE', [[wo('It builds the targeting')],[co('with the creative.')]], 'Each variant lands with the audience it was written for, not a guess you set later.', [co('Matched, not generic.')], f"{M}/audience.png", 1.0),
 ('YOUR VOICE', [[wo('It writes your offer')],[co('in your voice.')]], 'Sampled from your real copy. Banned words and agency fluff stripped on every draft.', [co('Sounds like you.')], f"{M}/voice.png", 1.0),
 ('THE SPEND', [[wo('Agencies bill 5K a month.')],[co('This runs on cents.')]], 'Pay per token. Twelve variants drafted and paced for the price of a coffee.', [co('Cents, not retainers.')], f"{M}/spend.png", 1.0),
 ('THE WINNER', [[wo('Twelve angles in.')],[co('One winner out.')]], 'Spread the bet, kill the flat lines fast, pour budget into the one that moves.', [co('Find it in days.')], f"{M}/winner.png", 1.0),
 ('GO LIVE', [[wo('Blank to live')],[co('before lunch.')]], 'Creatives, audiences and budget assembled into one campaign that waits for your tap.', [co('You approve. It ships.')], f"{M}/live.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the ad brief?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='never stare again.',q='What would you launch if the blank page was gone?')
MARK2="claude"
