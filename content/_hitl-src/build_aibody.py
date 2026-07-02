#!/usr/bin/env python3
# THE COMPLETE AI BODY - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/aibody"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Chatbot founders type.')],[co('Operators are augmented.')]])
T2.CONTENT=[
 ('THE DIFFERENCE', [[wo('A chatbot answers.')],[co('A body works.')]], 'Most founders rent one mouth. The top operators wire every organ.', [co('Augment, not chat.')], f"{M}/difference.png", 1.0),
 ('THE BRAIN', [[wo('The router thinks')],[co('before it spends.')]], 'It reads each job, hires the right agent, picks the model tier per turn.', [co('You never pick a model.')], f"{M}/router.png", 1.0),
 ('THE EYES', [[wo('CORTEX reads')],[co('1,284 companies.')]], 'Funding, hiring, stack, intent. Signals you would never spot by hand.', [co('Overnight, every night.')], f"{M}/eyes.png", 1.0),
 ('THE VOICE', [[wo('PULSE writes')],[co('like you.')]], 'Sampled from your real posts. Banned words enforced on every draft.', [co('Your voice, multiplied.')], f"{M}/voice.png", 1.0),
 ('THE HANDS', [[wo('SENTINEL ships')],[co('real product.')]], 'Pages, dashboards and fixes from plain English, tested before you see them.', [co('Built while you sleep.')], f"{M}/hands.png", 1.0),
 ('THE HEART', [[wo('One memory keeps')],[co('it all alive.')]], 'ICP, pipeline, pricing, docs. Every agent draws from the same core.', [co('Nothing forgets you.')], f"{M}/heart.png", 1.0),
 ('THE GATE', [[wo('The body is strong.')],[co('You hold the reins.')]], 'Every external move parks for your tap. Augmented, not replaced.', [co('Still your company.')], f"{M}/gate.png", 1.0),
 ('THE OPERATOR', [[wo('Stop typing.')],[co('Start operating.')]], 'One chat wires brain, eyes, voice, hands and heart into one operator.', [co('The full body, one login.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], f"{LIB}/cta3d-founder.png", 0.92)
T2.CLOSE=dict(l1='Save this and',l2='augment every part.',q='Which part of you needs the upgrade first?')
MARK2="orb"
