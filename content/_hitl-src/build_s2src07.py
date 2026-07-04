#!/usr/bin/env python3
# BORING WINS - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
TITLE="BORING WINS"
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src07"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You need to run')],[co('boring AI.')]])
T2.CONTENT=[
 ('BORING WINS', [[wo('Clever spikes.')],[co('Boring compounds.')]], 'One viral hack, then silence. A boring system shows up every single day.', [co('Compounds while you sleep.')], f"{M}/compound.png", 1.0),
 ('THE BUYER RULE', [[wo('Predictable feels safe.')],[co('Safe gets signed.')]], 'The brain trusts what it can predict. Clever gets a scroll, boring gets the reply.', [co('Safe closes deals.')], f"{M}/brainrule.png", 1.0),
 ('THE BRAIN', [[wo('It picks the same')],[co('right tier every time.')]], 'The router reads each job and hires the cheapest agent that can actually do it.', [co('You never pick a model.')], f"{M}/router.png", 1.0),
 ('THE PRICE', [[wo('Boring costs cents.')],[co('Clever costs a salary.')]], 'Pay per token, per job. The expensive stack you were about to buy, replaced.', [co('Cents, not subscriptions.')], f"{M}/cents.png", 1.0),
 ('NOT A PROMPT', [[wo('A prompt is a trick.')],[co('A system is a body.')]], 'Memory, agents, router, gate. It runs the whole workflow, not one clever message.', [co('Stop retyping prompts.')], f"{M}/system.png", 1.0),
 ('THE MEMORY', [[wo('It never forgets')],[co('what you said once.')]], 'ICP, pipeline, pricing, docs. Every agent draws from the same core.', [co('Reliable because it remembers.')], f"{M}/memory.png", 1.0),
 ('THE GATE', [[wo('Nothing sends')],[co('until you tap.')]], 'Every external move parks for your approval. Powerful, never unsupervised.', [co('Predictable by design.')], f"{M}/gate.png", 1.0),
 ('THE ROSTER', [[wo('One clever bot?')],[co('Seven boring pros.')]], 'Research, outbound, deals, content, code, publishing, legal. Each owns one job.', [co('Seven agents, one login.')], f"{M}/roster.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='run boring on purpose.',q='What are you still doing by hand?')
MARK2="claude"
