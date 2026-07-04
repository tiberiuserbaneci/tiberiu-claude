#!/usr/bin/env python3
# I CHECKED THE LISTS - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/verified"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('I installed all 50 viral skills.')],[co('A third are fake.')]])
T2.CONTENT=[
 ('THE FLOOD', [[wo('Fifty skills per list.')],[co('Zero receipts.')]], 'The same recycled lists, reposted daily. Nobody installs them, nobody verifies them.', [co('So I did.')], f"{M}/flood.png", 1.0),
 ('THE TEST', [[wo('I installed')],[co('every single one.')]], 'One week, every skill run on real work: briefs, drafts, builds, audits.', [co('Real work, not demos.')], f"{M}/test.png", 1.0),
 ('THE FAKES', [[wo('A third were')],[co('made up.')]], 'Dead links, renamed duplicates, skills that answer instead of execute.', [co('Cut without mercy.')], f"{M}/fakes.png", 1.0),
 ('THE KEEPERS', [[wo('What survived')],[co('earns its slot.')]], 'Writing, research, design, build: the shortlist that finishes work.', [co('Grouped by job.')], f"{M}/keepers.png", 1.0),
 ('THE ORDER', [[wo('Start with the two')],[co('built by Anthropic.')]], 'First-party skills first, then the verified community layer on top.', [co('The safe install order.')], f"{M}/safest.png", 1.0),
 ('ULTRON', [[wo('Ultron ships them')],[co('pre-verified.')]], 'The techniques library is curated and tested before it reaches your desk.', [co('No gambling on links.')], f"{M}/curated.png", 1.0),
 ('THE RULE', [[wo('If it cannot execute,')],[co('it does not count.')]], 'A skill that returns advice is a bookmark. Keep the ones that finish work.', [co('Execution or nothing.')], f"{M}/rule.png", 1.0),
 ('THE DESK', [[wo('My desk runs')],[co('on survivors.')]], 'Twelve skills, each tested on my own pipeline, running daily.', [co('Quality beats quantity.')], f"{M}/desk.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save the shortlist,',l2='skip the flood.',q='Which list burned you last?')
MARK2="claude"
