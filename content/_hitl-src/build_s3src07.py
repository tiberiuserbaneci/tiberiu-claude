#!/usr/bin/env python3
# THE TRIAL RUNS OUT - adaptare IG Scraped (s3src07) in context Ultron (generat de adapt_build.py)
# Source: growth-hack carousel "use Claude Opus 4.8 free via a 30-day trial". Re-told as Ultron:
# a borrowed trial is a countdown; an operator is permanent - routed models, agents that run the
# work, cents per token, human-gated, no expiry.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src07"; LIB=T2.LIB
PREMIUM=1
TITLE="THE TRIAL RUNS OUT"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your free AI trial')],[co('runs out in 30 days.')]])
T2.CONTENT=[
 ('THE COUNTDOWN', [[wo('A free trial is')],[co('a 30-day timer.')]], 'You borrow frontier access, then day 31 locks you back out.', [co('Borrowed, not owned.')], f"{M}/expire.png", 1.0),
 ('THE MODELS', [[wo('You never pick')],[co('the model again.')]], 'Lite, Smart and Deep tiers. The router reads each job and picks.', [co('One login, every tier.')], f"{M}/models.png", 1.0),
 ('NO CEILING', [[wo('No message cap.')],[co('You pay per token.')]], 'Not throttled by a plan. Billed only for the tokens you spend.', [co('Cents, not a quota.')], f"{M}/nolimits.png", 1.0),
 ('24 / 7', [[wo('Agents that run')],[co('while you sleep.')]], 'Seven specialists ship finished work to your vault by morning.', [co('Work done, not chat.')], f"{M}/agents.png", 1.0),
 ('THE ROSTER', [[wo('Type plain English.')],[co('It picks the specialist.')]], 'Research, outbound, deals, content, code, publishing and legal.', [co('Seven, on call.')], f"{M}/roster.png", 1.0),
 ('THE BILL', [[wo('Their stack bills')],[co('by the month.')]], 'Cancel four subscriptions. Pay only for the runs you actually make.', [co('Ultron costs cents.')], f"{M}/cents.png", 1.0),
 ('HUMAN GATE', [[wo('Nothing sends')],[co('without your tap.')]], 'Every external move parks in a queue until you approve it.', [co('Augmented, not loose.')], f"{M}/gate.png", 1.0),
 ('NO EXPIRY', [[wo('One expires.')],[co('One compounds.')]], 'A 30-day borrow resets to zero. An operator keeps memory and models.', [co('It does not run out.')], f"{M}/horizon.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the setup?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this before',l2='your trial expires.',q='What runs your company when the trial ends?')
MARK2="claude"
