#!/usr/bin/env python3
# FIVE ENGINEERS, ONE TERMINAL - adaptare IG Scraped s3src31 in context Ultron (roles angle:
# SENTINEL as a whole engineering ORG staffed by one terminal command).
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src31"; LIB=T2.LIB
PREMIUM=1
TITLE="FIVE ENGINEERS, ONE TERMINAL"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You hired one coder.')],[co('You needed a team.')]])
T2.CONTENT=[
 ('THE TEAM', [[wo('One line staffs')],[co('a whole dev team.')]], 'Architect, builder, tester, reviewer, docs. All from one terminal.', [co('Type once. Team reports.')], f"{M}/org.png", 1.0),
 ('THE ARCHITECT', [[wo('It plans first,')],[co('then it builds.')]], 'Brainstorm, plan, then write. The fix for rushed AI slop.', [co('No more blind coding.')], f"{M}/architect.png", 1.0),
 ('THE BUILDER', [[wo('It ships a screen,')],[co('not a snippet.')]], 'Plain English in, a working page out. You see the product, not code.', [co('Built end to end.')], f"{M}/builder.png", 1.0),
 ('THE TESTER', [[wo('It tests what')],[co('it just wrote.')]], '40 checks run on every change. It caught the one that would break.', [co('Green before you look.')], f"{M}/tester.png", 1.0),
 ('THE REVIEWER', [[wo('A second set of eyes')],[co('on every diff.')]], 'It reviews its own work, flags the blocker, fixes it before merge.', [co('Caught in review.')], f"{M}/reviewer.png", 1.0),
 ('THE WRITER', [[wo('It writes the docs')],[co('you always skip.')]], 'Every change logged, so future you is never lost in the code.', [co('Documented on merge.')], f"{M}/docs.png", 1.0),
 ('THE SHIP', [[wo('The whole team,')],[co('one pull request.')]], 'Plan, build, test, review, docs. It all lands as one clean PR.', [co('You just approve.')], f"{M}/ship.png", 1.0),
 ('THE OPERATOR', [[wo('Five roles.')],[co('One terminal.')]], 'You run the engineering team from one line, and you still hold the merge.', [co('Your hand on ship.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the setup?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and staff', l2='your whole team.', q='Which role would you hire first?')
MARK2="claude"
