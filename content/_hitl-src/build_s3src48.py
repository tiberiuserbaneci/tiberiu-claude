#!/usr/bin/env python3
# NINE DAYS TO THREE PAYING - adaptare IG Scraped s3src48 in context Ultron. Narrowed angle:
# the idea -> first-paying-customer VALIDATION loop (validate demand -> build MVP -> land the
# first 3 paying customers), the exact sequence, speed to first revenue.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src48"; LIB=T2.LIB
PREMIUM=1
TITLE="NINE DAYS TO THREE PAYING"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Idea to three paying')],[co('customers in nine days.')]])
T2.CONTENT=[
 ('THE SPEED', [[wo('Six months to build.')],[co('Nine days to paid.')]], 'Most founders build for a season before revenue. The loop gets you paid in days.', [co('Days, not months.')], f"{M}/speed.png", 1.0),
 ('STEP 1 · VALIDATE', [[wo('Sold it first,')],[co('built it second.')]], 'CORTEX finds who is in pain, SPECTER asks. Sixty talks, three pre-paid before code.', [co('No buyers, no build.')], f"{M}/validate.png", 1.0),
 ('STEP 2 · OFFER', [[wo('A paid promise,')],[co('not a free demo.')]], 'One outcome, one price, a pre-pay link. STRIKER shapes the offer that closes.', [co('Sell the outcome.')], f"{M}/offer.png", 1.0),
 ('STEP 3 · BUILD', [[wo('The smallest thing')],[co('that delivers.')]], 'SENTINEL ships only what the three buyers asked for, live on your domain in two days.', [co('MVP, nothing extra.')], f"{M}/build.png", 1.0),
 ('STEP 4 · REACH', [[wo('Straight to the')],[co('warm twenty-two.')]], 'No cold list. SPECTER reaches the people who already said they feel the pain.', [co('Warm, not cold.')], f"{M}/reach.png", 1.0),
 ('STEP 5 · CLOSE', [[wo('Three cards')],[co('charged.')]], 'STRIKER handles the objections and sends the link. The first three customers pay.', [co('First revenue, live.')], f"{M}/close.png", 1.0),
 ('THE SYSTEM', [[wo('One chat runs')],[co('the whole loop.')]], 'The ROUTER hires CORTEX, SPECTER, SENTINEL and STRIKER, picks the model per step.', [co('One operator.')], f"{M}/orchestrate.png", 1.0),
 ('DAY NINE', [[wo('A sentence in.')],[co('Three paying out.')]], 'Idea to first revenue in one system, in days, at cents per step.', [co('Speed to paid.')], f"{M}/revenue.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the exact loop?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and ship', l2='to paid in days.', q='What would you charge for on day nine?')
MARK2="claude"
