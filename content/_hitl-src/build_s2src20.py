#!/usr/bin/env python3
# S2SRC20 - "the $2400 content team" reframed to Ultron (adaptare IG Scraped, generat de adapt_build.py)
import importlib.util
TITLE="THE CONTENT TEAM"
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src20"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You wired a $2400 content team.')],[co('I typed one sentence.')]])
T2.CONTENT=[
 ('THE OLD STACK', [[wo('Nine tools, taped together.')],[co('$2400 a month to glue it.')]], 'A content team built by hand is brittle wiring, API keys and a monthly bill that never stops.', [co('One node dies, it all dies.')], f"{M}/stack.png", 1.0),
 ('THE TEAM', [[wo('Seven agents, one login.')],[co('No glue, no keys.')]], 'CORTEX, PULSE and AMPLIFY already know each other. No workflow to wire, nothing to maintain.', [co('The team ships with the tool.')], f"{M}/team.png", 1.0),
 ('THE BRAIN', [[wo('It budgets its own')],[co('thinking, per turn.')]], 'The router reads each job and hires the cheapest tier that can do it. You never pick a model.', [co('Cents, not a subscription.')], f"{M}/router.png", 1.0),
 ('THE BRIEF', [[wo('One idea in. A clean')],[co('brief back, minutes later.')]], 'It asks the sharp questions, then folds your answers into one brief ready to be written.', [co('No blank page, ever.')], f"{M}/brief.png", 1.0),
 ('THE RESEARCH', [[wo('It reads this morning')],[co('web, not last year.')]], 'Live sources, real numbers, every claim carrying its own dated receipt before a word is drafted.', [co('Sourced or it does not ship.')], f"{M}/research.png", 1.0),
 ('THE VOICE', [[wo('It writes like you.')],[co('I approved the draft.')]], 'Sampled from your real posts, banned words enforced, so the master piece sounds like you wrote it.', [co('Your voice, multiplied.')], f"{M}/voice.png", 1.0),
 ('THE CHANNELS', [[wo('One master piece,')],[co('every channel native.')]], 'The same idea reshaped for LinkedIn, a thread, a short and a newsletter, formatted for each.', [co('Written once, cut many ways.')], f"{M}/channels.png", 1.0),
 ('THE GATE', [[wo('Nothing posts')],[co('without your tap.')]], 'The whole team drafts and schedules, then parks every send for one human approval. Still yours.', [co('A team you still run.')], f"{M}/gate.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the setup?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and stop',l2='paying to glue a team.',q='What would you ship if the team was already wired?')
MARK2="claude"
