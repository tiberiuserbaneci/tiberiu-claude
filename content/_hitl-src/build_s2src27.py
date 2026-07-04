#!/usr/bin/env python3
# THE OPERATOR STACK - adaptare IG Scraped (TOP 5 Claude Code Plugins) in context Ultron (via adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
TITLE="THE OPERATOR STACK"
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src27"; LIB=T2.LIB
PREMIUM=1
T2.TITLE=TITLE
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You rented a chatbot.')],[co('Founders install an operator.')]])
T2.CONTENT=[
 ('THE ROUTER', [[wo('It picks the model,')],[co('so you never do.')]], 'Reads each job, hires the right agent, sets the tier per turn. You just talk.', [co('Cents, not a subscription.')], f"{M}/router.png", 1.0),
 ('THE RESEARCH', [[wo('The whole web,')],[co('one ranked brief.')]], 'People, companies and markets profiled and scored before your first call.', [co('CORTEX, in minutes.')], f"{M}/research.png", 1.0),
 ('THE SIGNALS', [[wo('It saw the round')],[co('before my VC did.')]], 'Funding, hiring, stack, intent. Watched overnight, digested by 07:00.', [co('Every night, for you.')], f"{M}/signals.png", 1.0),
 ('THE VOICE', [[wo('It stole my writing.')],[co('I approved.')]], 'Sampled from your real posts. Banned words enforced on every draft.', [co('Your voice, multiplied.')], f"{M}/voice.png", 1.0),
 ('THE HANDS', [[wo('Built, tested, shipped.')],[co('I was at dinner.')]], 'Pages, dashboards and fixes from plain English, tested before you see them.', [co('Shipped while you sleep.')], f"{M}/hands.png", 1.0),
 ('THE MEMORY', [[wo('Cut the memory')],[co('and the stack dies.')]], 'ICP, pipeline, pricing, docs. Every agent draws from one shared core.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('THE GATE', [[wo('Full power.')],[co('Your tap.')]], 'Every external move parks for approval. Augmented, never unsupervised.', [co('Still your company.')], f"{M}/gate.png", 1.0),
 ('THE PRICE', [[wo('A full sales team')],[co('for cents a task.')]], 'Pay per token, not per seat. The stack you replace bills thousands a month.', [co('Cents in, pipeline out.')], f"{M}/price.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the full stack?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='install the operator.',q='Which upgrade would change your month first?')
MARK2="claude"
