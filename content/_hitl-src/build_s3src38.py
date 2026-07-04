#!/usr/bin/env python3
# THE TOOL HALF-LIFE - adaptare IG Scraped (s3src38) in context Ultron. Angle: learning treadmill /
# tool obsolescence - every tool you memorize dies in months; skill compounds only in a standing operator.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src38"; LIB=T2.LIB
PREMIUM=1
TITLE="THE TOOL HALF-LIFE"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You keep learning tools.')],[co('They keep dying on you.')]])
T2.CONTENT=[
 ('THE TREADMILL', [[wo('The tool you master in March')],[co('is obsolete by September.')]], 'The half-life of an AI tool is now months, not years. You learn, forget, repeat.', [co('Not you. The clock.')], f"{M}/treadmill.png", 1.0),
 ('THE HALF-LIFE', [[wo('Every tool')],[co('has a shelf life.')]], 'Prompt hacks, wrappers, the framework of the week. All decay on a timer.', [co('Half your bookmarks are dead.')], f"{M}/shelflife.png", 1.0),
 ('THE GRAVEYARD', [[wo('Count the tools')],[co('you already forgot.')]], 'You did not fall behind. The ground moved under everything you memorized.', [co('48 dead, 6 alive.')], f"{M}/graveyard.png", 1.0),
 ('THE LEAK', [[wo('Your head is')],[co('a leaky bucket.')]], 'Knowledge you hold in memory drains between projects. It never compounds in you.', [co('Retention loses the race.')], f"{M}/leak.png", 1.0),
 ('THE OPERATOR', [[wo('Put the skill in')],[co('a standing operator.')]], 'The workflow lives in the system, not your head. Seven agents, always on.', [co('It does not forget.')], f"{M}/standing.png", 1.0),
 ('THE HOT-SWAP', [[wo('Tools swap.')],[co('The system stays.')]], 'The router picks the best model per job and swaps it underneath. You relearn nothing.', [co('New tool, same workflow.')], f"{M}/hotswap.png", 1.0),
 ('THE COMPOUND', [[wo('Sitting in a system,')],[co('skill compounds.')]], 'Every brief you approve feeds the memory. The next one starts sharper, never from zero.', [co('It climbs, never resets.')], f"{M}/compound.png", 1.0),
 ('LEARN ONCE', [[wo('Stop relearning')],[co('every quarter.')]], 'Own one operator that learns once and upgrades itself. The tools are its problem.', [co('Learn once. It updates.')], f"{M}/learnonce.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the operator playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Stop collecting tools.',l2='Install one operator.',q='What did you learn this year that is already dead?')
MARK2="claude"
