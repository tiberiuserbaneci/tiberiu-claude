#!/usr/bin/env python3
# THE DAY-ONE SKILL STACK - adaptare IG "beginner Claude skills" in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2everybeginnersho"; LIB=T2.LIB
PREMIUM=1
TITLE="THE DAY-ONE STACK"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('The first skills a')],[co('founder installs.')]])
T2.CONTENT=[
 ('THE STACK', [[wo('Install the stack,')],[co('not toy prompts.')]], 'Five skills that finish real work, live the day you sign in.', [co('Skills, not prompts.')], f"{M}/shelf.png", 1.0),
 ('THE BRIEF', [[wo('40 tabs collapse')],[co('into one brief.')]], 'CORTEX scores your accounts on your ICP and hands back one ranked page.', [co('Read the one page.')], f"{M}/brief.png", 1.0),
 ('THE OUTREACH', [[wo('One ICP becomes')],[co('a full sequence.')]], 'Name one prospect. SPECTER writes and paces the whole thread for cents.', [co('Cents a send.')], f"{M}/outreach.png", 1.0),
 ('THE CONTENT', [[wo('One topic, the')],[co('whole content kit.')]], 'PULSE turns one line into post, carousel, hook, ALT, comment and DM.', [co('Six assets, your voice.')], f"{M}/carousel.png", 1.0),
 ('THE AUDIT', [[wo('Nine seats, or')],[co('a few cents.')]], 'List what you pay monthly. The audit prices the same work in cents.', [co('Cents, not seats.')], f"{M}/audit.png", 1.0),
 ('THE RADAR', [[wo('It saw the round')],[co('before my VC did.')]], 'Funding, hiring, stack, intent. This morning web, watched for you.', [co('Overnight, every night.')], f"{M}/signals.png", 1.0),
 ('THE GATE', [[wo('Nothing sends')],[co('without your tap.')]], 'It drafts all 240 and stops. Human gate on every external move.', [co('Still your company.')], f"{M}/gate.png", 1.0),
 ('THE WEEK', [[wo('Day one you install.')],[co('This week you ship.')]], 'Not another course to finish. Install day one, ship a real asset by Friday.', [co('Start here, ship this week.')], f"{M}/week1.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the day-one setup?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='install the stack today.',q='Which skill do you install first?')
MARK2="claude"
