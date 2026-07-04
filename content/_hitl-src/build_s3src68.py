#!/usr/bin/env python3
# SAME CLAUDE, SHAPED TO YOU - adaptare IG Scraped (s3src68) in context Ultron. Angle: the identical
# brilliant model gives everyone the same generic output until you shape it with context / voice /
# rules. Ultron is that shaping layer. (build structure copied from build_aibody.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src68"; LIB=T2.LIB
PREMIUM=1
TITLE="SAME CLAUDE, SHAPED TO YOU"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Same Claude as everyone.')],[co('Not the same output.')]])
T2.CONTENT=[
 ('THE DEFAULT', [[wo('Brilliant out of the box.')],[co('And completely generic.')]], 'Out of the box it hands everyone the same clean, safe, forgettable answer.', [co('Generic by default.')], f"{M}/clones.png", 1.0),
 ('DEFAULT VS YOURS', [[wo('It can read like a memo,')],[co('or read like you.')]], 'The exact same model. One output sounds like anyone. One sounds like your desk.', [co('You pick which.')], f"{M}/split.png", 1.0),
 ('YOUR CONTEXT', [[wo('It loads your business')],[co('before it starts.')]], 'What you sell, your pricing, your rules, your docs, read every single session.', [co('Never starts from zero.')], f"{M}/memory.png", 1.0),
 ('YOUR VOICE', [[wo('Sampled from your posts.')],[co('Mirrored in every draft.')]], 'Sentence length, how blunt you are, the words you reach for and the ones you ban.', [co('Sounds like your desk.')], f"{M}/voice.png", 1.0),
 ('YOUR RULES', [[wo('The words you ban')],[co('never reach the page.')]], 'Hard rules enforced on every output. No hype, no corporate, no emoji if you say so.', [co('Your guardrails hold.')], f"{M}/rules.png", 1.0),
 ('YOUR TEAM', [[wo('Seven agents inherit')],[co('the same context.')]], 'Research, outbound, deals, content, code, publishing, legal, all shaped by you.', [co('One brief, everywhere.')], f"{M}/team.png", 1.0),
 ('YOUR CALL', [[wo('Nothing ships')],[co('without your tap.')]], 'Every shaped output parks at the gate. You approve, then and only then it goes.', [co('Still your name on it.')], f"{M}/gate.png", 1.0),
 ('THE SHIFT', [[wo('Generic in.')],[co('Your operator out.')]], 'Context, voice and rules stack into one system that works like a teammate who knows you.', [co('Shaped, not rented.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the shaping prompts?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='stop shipping generic.',q='What would yours sound like, shaped to you?')
MARK2="claude"
