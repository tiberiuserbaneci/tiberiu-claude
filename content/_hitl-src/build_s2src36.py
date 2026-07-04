#!/usr/bin/env python3
# THE COLD-START ROADMAP - adaptare IG/TikTok in context Ultron (consumat de adapt_build.py).
# Reframe al sursei "Complete Roadmap to Launch a Product with Claude" (roadmap numerotat pas cu pas)
# intr-un roadmap founder de pipeline: 8 pasi, fiecare un agent/outcome Ultron. Pret in centi.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src36"; LIB=T2.LIB
PREMIUM=1
TITLE="THE COLD-START ROADMAP"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('The 8-step roadmap')],[co('to booked pipeline.')]])
T2.CONTENT=[
 ('STEP 01 · RESEARCH', [[wo('Skip the list-building.')],[co('CORTEX ranks who to hit.')]], 'It profiles your market and hands back a ranked target list, best-fit first.', [co('50 accounts, scored.')], f"{M}/targets.png", 1.0),
 ('STEP 02 · WATCH', [[wo('Catch the trigger')],[co('the day it fires.')]], 'Funding, hiring, stack switches, intent. The buying window opens and you already know.', [co('Timed, not cold.')], f"{M}/signals.png", 1.0),
 ('STEP 03 · WRITE', [[wo('It writes the sequence')],[co('in your voice.')]], 'SPECTER drafts the cold email and every follow-up, sampled from your real posts.', [co('No template smell.')], f"{M}/write.png", 1.0),
 ('STEP 04 · ROUTE', [[wo('The cheapest brain')],[co('that can do the job.')]], 'The router reads each turn and picks the tier. Most work runs at a fraction of a cent.', [co('Cents, not retainers.')], f"{M}/route.png", 1.0),
 ('STEP 05 · QUALIFY', [[wo('A reply lands.')],[co('STRIKER qualifies it.')]], 'Budget, authority, need, timing scored on the spot, objections handled before you read it.', [co('Only real ones reach you.')], f"{M}/qualify.png", 1.0),
 ('STEP 06 · GATE', [[wo('Nothing sends')],[co('without your tap.')]], 'Every external move parks at the human gate. Augmented outbound, never unsupervised.', [co('Still your name on it.')], f"{M}/gate.png", 1.0),
 ('STEP 07 · MEMORY', [[wo('Every agent knows')],[co('your whole company.')]], 'ICP, pipeline, pricing, docs live in one core. Nothing you say twice, nothing forgotten.', [co('One memory, seven agents.')], f"{M}/memory.png", 1.0),
 ('STEP 08 · BOOKED', [[wo('The week fills up')],[co('while you build.')]], 'Meetings land on your calendar. The whole run costs cents, not an SDR salary.', [co('Zero to pipeline.')], f"{M}/booked.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the full roadmap?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and run',l2='the whole roadmap.',q='Which step is your pipeline stuck on?')
MARK2="claude"
