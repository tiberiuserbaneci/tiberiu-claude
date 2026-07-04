#!/usr/bin/env python3
# S2SRC47 - adaptare IG scraped ("200 Powerful Claude Prompts") reincadrata in Ultron founder-GTM.
# Sursa = o biblioteca de 200 de prompturi copy-paste (Category 1 Coding & Debugging, [PASTE CODE]).
# Reframe: un prompt e o linie stateless; Ultron e stratul de deasupra - 7 agenti care ruteaza,
# tin memoria afacerii, gateaza trimiterile si compun. Prompturile nu retin nimic.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2src47"; LIB=T2.LIB
PREMIUM=1
TITLE="PROMPTS DON'T REMEMBER"
T2.TITLE=TITLE
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You saved 200 prompts.')],[co('You still start from zero.')]])
T2.CONTENT=[
 ('STATELESS', [[wo('Every prompt')],[co('starts blank.')]], 'A saved prompt keeps the words and forgets the business. You paste your context back in, every single time.', [co('Zero memory.')], f"{M}/paste.png", 1.0),
 ('MODEL ROUTER', [[wo('A prompt cannot')],[co('pick its own model.')]], 'The router reads each job and hires the cheapest tier that can do it. Lite for lookups, Deep for judgement.', [co('Cents per job.')], f"{M}/router.png", 1.0),
 ('SEVEN AGENTS', [[wo('A sentence does a task.')],[co('An agent owns the job.')]], 'Seven named agents run research, outbound, deals, content, code, publishing and legal end to end.', [co('Staff, not snippets.')], f"{M}/agents.png", 1.0),
 ('SHARED MEMORY', [[wo('It knows your ICP')],[co('before you type.')]], 'ICP, pipeline, pricing and docs live in one core every agent reads. Nothing ever re-briefs you.', [co('Nothing forgets you.')], f"{M}/memory.png", 1.0),
 ('HUMAN GATE', [[wo('It drafts everything.')],[co('It sends nothing.')]], 'Every external move parks in a queue for your tap. The speed of an agent, the control of a founder.', [co('Still your call.')], f"{M}/gate.png", 1.0),
 ('THE MATH', [[wo('The old stack billed')],[co('by the seat.')]], 'A shelf of point tools runs over a thousand a month. Ultron bills only the tokens a job actually burns.', [co('You pay cents.')], f"{M}/cost.png", 1.0),
 ('ONE PIPELINE', [[wo('Four folders of prompts.')],[co('Or one pipeline.')]], 'Research to outbound to deals to content to code to publish to legal, each handoff wired automatically.', [co('Nothing copy-pasted.')], f"{M}/coverage.png", 1.0),
 ('ONE LOGIN', [[wo('Close the prompt folder.')],[co('Open the operator.')]], 'Two hundred snippets collapse into one system that routes, remembers and gates, from a single chat.', [co('One login, whole team.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the build map?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='stop pasting prompts.',q='Which job are you still copy-pasting by hand?')
MARK2="claude"
