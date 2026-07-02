#!/usr/bin/env python3
# FIRST PASS, HUMAN FINISH - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/firstpass"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('The desk does the first pass.')],[co('Your taste does the rest.')]])
T2.CONTENT=[
 ('THE CHATBOX', [[wo('Most people run a team')],[co('like a chat box.')]], 'One prompt at a time, one person typing, nine roles unfilled.', [co('Wire it like an org chart.')], f"{M}/chatbox.png", 1.0),
 ('THE ROSTER', [[wo('Researcher, editor,')],[co('analyst, deck builder.')]], 'Ten roles, each an installed skill with a real job, not a prompt with a nickname.', [co('An org chart, not a toy.')], f"{M}/roster.png", 1.0),
 ('THE SPLIT', [[wo('It drafts.')],[co('You decide.')]], 'The first pass is volume work: reading, sorting, drafting. The finish is judgement.', [co('Machines pass, humans finish.')], f"{M}/split8.png", 1.0),
 ('THE MORNING', [[wo('Nine first passes')],[co('waiting at 07:00.')]], 'Briefs read, drafts ranked, deck skeletons built. Your day starts at the decision layer.', [co('You skipped the grind layer.')], f"{M}/morning.png", 1.0),
 ('THE CRAFT', [[wo('Your team stops producing')],[co('and starts directing.')]], 'Editors edit taste, not typos. Analysts read meaning, not spreadsheets.', [co('Everyone moves up one level.')], f"{M}/craft.png", 1.0),
 ('THE SKILL MAKER', [[wo('One skill on the roster')],[co('builds new skills.')]], 'Spot a repeated job, mint it into the org chart by Friday.', [co('The team grows itself.')], f"{M}/skillmaker.png", 1.0),
 ('THE LINE', [[wo('Nothing external ships')],[co('without a human finish.')]], 'First passes run free inside. The last touch is always yours.', [co('That line never moves.')], f"{M}/line8.png", 1.0),
 ('THE RESULT', [[wo('Same headcount.')],[co('Triple the throughput.')]], 'Not replacement: elevation. The work everyone hated does itself now.', [co('First pass, solved.')], f"{M}/result8.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1='Save the split',l2='and audit your week with it.',q='Where does your first pass go?')
MARK2="claude"
