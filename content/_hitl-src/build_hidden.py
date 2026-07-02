#!/usr/bin/env python3
# THE HIDDEN SKILLS - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/hidden"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Prompting is level zero.')],[co('Installing is the game.')]])
T2.CONTENT=[
 ('THE MYTH', [[wo('Re-wording requests')],[co('is not a skill.')]], 'The top operators install capabilities. The rest re-word requests.', [co('Skills beat phrasing.')], f"{M}/myth.png", 1.0),
 ('DECKS', [[wo('The proposal built itself.')],[co('I added the price.')]], 'Client name in, structured deck out, in your tokens and your voice.', [co('No blank slides.')], f"{M}/decks.png", 1.0),
 ('SHEETS', [[wo('Numbers with receipts.')],[co('Every figure traces.')]], 'Live figures with sources attached, not screenshots of spreadsheets.', [co('Ask, do not assemble.')], f"{M}/sheets.png", 1.0),
 ('CONTRACTS', [[wo('The NDA came back')],[co('already redlined.')]], 'COUNSEL reads the NDA, flags the risk lines, drafts the redlines.', [co('Minutes, not lawyers-first.')], f"{M}/contracts.png", 1.0),
 ('VISUALS', [[wo('822 parts,')],[co('zero design queue.')]], '822 Crescendo components assemble into on-brand visuals and sites.', [co('No design queue.')], f"{M}/visuals.png", 1.0),
 ('CONNECTORS', [[wo('It acts inside my tools.')],[co('Not beside them.')]], 'Mail, CRM, calendar, payments. It acts in your tools, not beside them.', [co('No copy-paste bridge.')], f"{M}/connectors.png", 1.0),
 ('THE RESULT', [[wo('Answers are cheap.')],[co('Execution is the product.')]], 'Files created, work automated, tasks finished. That is the difference.', [co('Executor, not assistant.')], f"{M}/result.png", 1.0),
 ('THE GATE', [[wo('Executes at AI speed.')],[co('Sends at my speed.')]], 'Everything external parks first. You stay the only trigger.', [co('Power needs brakes.')], f"{M}/gate.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1='Save the list',l2='before you prompt again.',q='Which skill would save you the most hours?')
MARK2="claude"
