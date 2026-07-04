#!/usr/bin/env python3
# MONETIZE WHAT EXISTS - adaptare IG/TikTok in context Ultron (model build_aibody.py).
# Reframe: you already own the inputs (expertise, contacts, offer). Ultron turns what you
# already have into revenue - one system, not a new idea.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2mostpeoplethink"; LIB=T2.LIB
PREMIUM=1
TITLE="MONETIZE WHAT EXISTS"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You do not need')],[co('a new idea.')]])
T2.CONTENT=[
 ('WHAT YOU HAVE', [[wo('You already own')],[co('the raw material.')]], 'Your expertise, your contacts, your offer. The inputs are already yours.', [co('Nothing new to invent.')], f"{M}/assets.png", 1.0),
 ('THE PATH', [[wo('Asset to first')],[co('dollar, in days.')]], 'One asset in, one agent on it, first revenue out. No new product to build.', [co('Cents to run it.')], f"{M}/path.png", 1.0),
 ('THE CONTACTS', [[wo('Your dead list')],[co('is a live pipeline.')]], 'CORTEX reads the network you already have and ranks who to reach first.', [co('Warm, not cold.')], f"{M}/graph.png", 1.0),
 ('THE OFFER', [[wo('One offer, sent')],[co('while you sleep.')]], 'SPECTER writes it in your voice and works the follow-ups you never send.', [co('Replies stack up.')], f"{M}/stack.png", 1.0),
 ('THE COST', [[wo('It runs on cents,')],[co('not on salaries.')]], 'Pay per token. A full outbound week costs less than one coffee.', [co('The margin stays yours.')], f"{M}/gauge.png", 1.0),
 ('THE SIGNAL', [[wo('900 contacts.')],[co('Seven warm today.')]], 'It watches the list you forgot and flags the few worth a message now.', [co('Timing, done for you.')], f"{M}/field.png", 1.0),
 ('THE SYSTEM', [[wo('One system,')],[co('not a new idea.')]], 'Research, outbound, deals and content, wired around what you already own.', [co('Seven agents, one login.')], f"{M}/hub.png", 1.0),
 ('THE FLIP', [[wo('Stop hunting ideas.')],[co('Monetize what exists.')]], 'The revenue was never in a new idea. It was in the assets you already had.', [co('Start this week.')], f"{M}/flip.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the system?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='monetize what you own.',q='Which asset would you turn on first?')
MARK2="claude"
