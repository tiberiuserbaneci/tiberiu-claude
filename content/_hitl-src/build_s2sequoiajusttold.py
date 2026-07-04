#!/usr/bin/env python3
# THE WRONG DOLLAR / THE LAYER - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
# Sequoia thesis reframe: valoarea nu e in tokenii modelului, ci in stratul din jur (memory,
# agents, router, gate). Ultron = stratul asta, la centi. "Sequoia" doar ca teza, nu ca endorsement.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2sequoiajusttold"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Sequoia says stop chasing')],[co('the model dollar.')]])
T2.CONTENT=[
 ('THE THESIS', [[wo('For every $1 on models')],[co('you spend more on the layer.')]], 'Sequoia told founders the value moved up the stack. The tokens are the cheap part.', [co('The layer is the moat.')], f"{M}/valuestack.png", 1.0),
 ('THE SPEND', [[wo('Where the money')],[co('actually goes.')]], 'Raw model calls are cents. Memory, routing, agents and the gate are the rest.', [co('Own the layer, not the tokens.')], f"{M}/spend.png", 1.0),
 ('THE ORCHESTRATION', [[wo('One job in.')],[co('The right agents out.')]], 'The router reads each job and wires the agents that finish it, cents per turn.', [co('Wiring beats prompting.')], f"{M}/graph.png", 1.0),
 ('THE MEMORY', [[wo('Cut the memory')],[co('and the layer dies.')]], 'ICP, pipeline, pricing and docs. Every agent draws from one shared core.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('THE GATE', [[wo('Full power.')],[co('Your reins.')]], 'Every external move parks for your tap. The layer is held, never loose.', [co('Still your company.')], f"{M}/gate.png", 1.0),
 ('THE SIGNALS', [[wo('It saw the round')],[co('before my VC did.')]], 'Funding, hiring, stack, intent. The layer watches the web while you sleep.', [co('Overnight, every night.')], f"{M}/radar.png", 1.0),
 ('THE OUTPUT', [[wo('Ranked accounts.')],[co('Not raw tokens.')]], 'The layer turns model calls into scored, sourced, ready-to-act briefs.', [co('Results, not prompts.')], f"{M}/iso.png", 1.0),
 ('THE SYSTEM', [[wo('Stop renting tokens.')],[co('Own the operating layer.')]], 'The router, the agents, the memory and the gate. One system, at cents.', [co('The layer, one login.')], f"{M}/hub.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the layer map?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='own the layer.',q='What are you still paying raw tokens for?')
MARK2="claude"
