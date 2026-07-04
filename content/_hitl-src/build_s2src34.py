#!/usr/bin/env python3
# THE DORMANT ROSTER - adaptare IG Scraped ("20 Claude features most people are paying for and not
# using") in context Ultron. Fresh angle: you already pay cents for the full roster - seven agents,
# the router, the gate, the memory - and run it like a single chatbot. Each panel = one dormant seat.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
TITLE="THE DORMANT ROSTER"
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src34"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You pay for seven agents.')],[co('You talk to one.')]])
T2.CONTENT=[
 ('THE ROUTER', [[wo('You pick the model by hand.')],[co('It picks for you.')]], 'The router reads each job, hires the right agent and sets the tier per turn.', [co('Cents per run, not dollars.')], f"{M}/router.png", 1.0),
 ('CORTEX', [[wo('You are paying for research')],[co('that never ran.')]], 'CORTEX profiles people, companies and markets into one ranked brief.', [co('Overnight, for cents.')], f"{M}/cortex.png", 1.0),
 ('SPECTER', [[wo('The outbound seat')],[co('sits empty.')]], 'SPECTER writes the opener, the follow-ups and the whole multi-step chase.', [co('Sequences that run themselves.')], f"{M}/specter.png", 1.0),
 ('STRIKER', [[wo('Every deal is guessing')],[co('its next move.')]], 'STRIKER qualifies, handles objections and builds the close plan per deal.', [co('Pipeline that thinks.')], f"{M}/striker.png", 1.0),
 ('THE MEMORY', [[wo('You retype your context')],[co('into every chat.')]], 'One memory holds ICP, pipeline, pricing and docs. Every agent reads it.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('PULSE', [[wo('It already learned your voice.')],[co('You never used it.')]], 'PULSE samples your real posts and drafts in your voice, banned words enforced.', [co('Your voice, multiplied.')], f"{M}/pulse.png", 1.0),
 ('HUMAN GATE', [[wo('Full power.')],[co('Your tap.')]], 'Every external move parks for your approval before it ever sends.', [co('Augmented, never loose.')], f"{M}/gate.png", 1.0),
 ('THE OPERATOR', [[wo('Stop running one seat.')],[co('Fill the roster.')]], 'One chat wakes all seven agents, the router and the gate into one operator.', [co('The whole roster, one login.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the wake-up list?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='fill every seat.',q='Which seat have you left empty?')
MARK2="claude"
