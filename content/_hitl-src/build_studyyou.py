#!/usr/bin/env python3
# IT STUDIED MY BEST POSTS - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/studyyou"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('It studied my 50 best posts.')],[co('Then it wrote the 51st.')]])
T2.CONTENT=[
 ('THE ARCHIVE', [[wo('Your best posts are')],[co('training data you own.')]], 'Fifty posts that already worked, sitting unused in your profile.', [co('The goldmine is behind you.')], f"{M}/archive.png", 1.0),
 ('THE EXTRACT', [[wo('Pull them all.')],[co('Every winner, dated.')]], 'The desk collects your top posts with their numbers attached.', [co('Receipts, not memories.')], f"{M}/extract.png", 1.0),
 ('THE AUTOPSY', [[wo('What actually worked')],[co('was not what I thought.')]], 'Short openers, one number per post, questions that end. The data disagreed with my taste.', [co('Patterns beat opinions.')], f"{M}/autopsy.png", 1.0),
 ('THE DISTILL', [[wo('The findings became')],[co('a reusable skill.')]], 'Not notes, not a doc: an installed play the desk runs on every future draft.', [co('Insight, made executable.')], f"{M}/distill.png", 1.0),
 ('THE 51ST', [[wo('The next post came out')],[co('sounding like my best day.')]], 'Drafted against my own winning patterns, ranked before I saw it.', [co('Me, on repeat.')], f"{M}/fifty1.png", 1.0),
 ('THE REFRESH', [[wo('Every month,')],[co('the study reruns.')]], 'New winners join the corpus; the skill updates itself with fresh patterns.', [co('The bar keeps moving up.')], f"{M}/refresh.png", 1.0),
 ('THE MOAT', [[wo('Nobody can copy')],[co('your archive.')]], 'Generic AI writes averages. This writes from evidence only you own.', [co('Your history is the moat.')], f"{M}/moat8.png", 1.0),
 ('THE ORDER', [[wo('Study first.')],[co('Generate second.')]], 'Most people ask AI to write. Operators make it learn, then write.', [co('Reverse the order.')], f"{M}/order8.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1='Save the self-study loop',l2='and feed it your archive.',q='Which post should it study first?')
MARK2="claude"
