#!/usr/bin/env python3
# DELETE THE PROMPT LIBRARY - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/no120"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Delete your prompt library.')],[co('Install 12 skills instead.')]])
T2.CONTENT=[
 ('THE HOARD', [[wo('120 saved prompts.')],[co('You reopened four.')]], 'The cheat sheet felt like leverage. It is a filing cabinet you never visit.', [co('Saving is not a system.')], f"{M}/hoard.png", 1.0),
 ('THE ROT', [[wo('Prompts rot')],[co('the week models change.')]], 'Copy-paste magic words decay. Skills get maintained, versioned, corrected.', [co('One survives updates.')], f"{M}/rot.png", 1.0),
 ('THE RETYPE', [[wo('Every use costs')],[co('a fresh re-wording.')]], 'Paste, tweak, hope. The 120 need YOU every single time they run.', [co('That is the tell.')], f"{M}/retype.png", 1.0),
 ('THE TWELVE', [[wo('Twelve installed skills')],[co('cover the 120.')]], 'Brief, draft, audit, price, follow up, report: one command each, same play every run.', [co('Compression is power.')], f"{M}/twelve.png", 1.0),
 ('ONE LINE', [[wo('The whole prompt')],[co('became /audit my funnel.')]], 'A page of instructions lives inside the skill now. You type five words.', [co('The page is installed.')], f"{M}/oneline.png", 1.0),
 ('THE RUNS', [[wo('Skills run without you.')],[co('Prompts wait for you.')]], 'On triggers, on schedules, overnight: a skill fires itself. A prompt never will.', [co('That gap is everything.')], f"{M}/runs.png", 1.0),
 ('THE GATE', [[wo('Autonomous inside.')],[co('Your tap outside.')]], 'Skills execute and compose, and every external send still parks for you.', [co('Speed with a keel.')], f"{M}/gate.png", 1.0),
 ('THE PURGE', [[wo('I deleted mine')],[co('in one afternoon.')]], 'Kept zero prompts, minted twelve skills. The notebook is empty and the desk is full.', [co('Empty yours tonight.')], f"{M}/purge.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='empty the notebook.',q='How many saved prompts do you own?')
MARK2="claude"
