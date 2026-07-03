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
T2.COVER=dict(head=[[wo('You rented a mouth.')],[co('Your company needs hands.')]])
T2.CONTENT=[
 ('THE DIFFERENCE', [[wo('Talking is not working.')],[co('Ask your chatbot.')]], 'Most founders rent one mouth. The top operators wire every organ.', [co('Augment, not chat.')], f"{M}/difference.png", 1.0),
 ('THE BRAIN', [[wo('A brain that budgets')],[co('its own thinking.')]], 'It reads each job, hires the right agent, picks the model tier per turn.', [co('You never pick a model.')], f"{M}/router.png", 1.0),
 ('THE EYES', [[wo('It saw the funding round')],[co('before my VC did.')]], 'Funding, hiring, stack, intent. Signals you would never spot by hand.', [co('Overnight, every night.')], f"{M}/eyes.png", 1.0),
 ('THE VOICE', [[wo('It stole my writing style.')],[co('I approved.')]], 'Sampled from your real posts. Banned words enforced on every draft.', [co('Your voice, multiplied.')], f"{M}/voice.png", 1.0),
 ('THE HANDS', [[wo('Built, tested, shipped.')],[co('I was at dinner.')]], 'Pages, dashboards and fixes from plain English, tested before you see them.', [co('Built while you sleep.')], f"{M}/hands.png", 1.0),
 ('THE HEART', [[wo('Cut the memory')],[co('and the body dies.')]], 'ICP, pipeline, pricing, docs. Every agent draws from the same core.', [co('Nothing forgets you.')], f"{M}/heart.png", 1.0),
 ('THE GATE', [[wo('Strong body.')],[co('My reins.')]], 'Every external move parks for your tap. Augmented, not replaced.', [co('Still your company.')], f"{M}/gate.png", 1.0),
 ('THE OPERATOR', [[wo('Stop chatting with organs.')],[co('Assemble the body.')]], 'One chat wires brain, eyes, voice, hands and heart into one operator.', [co('The full body, one login.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='augment every part.',q='Which part of you needs the upgrade first?')
MARK2="claude"
