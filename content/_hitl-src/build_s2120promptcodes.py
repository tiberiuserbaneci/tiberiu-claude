#!/usr/bin/env python3
# THE COMMAND PALETTE - adaptare IG/TikTok in context Ultron (reframe: "120 prompt codes for Claude")
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2120promptcodes"; LIB=T2.LIB
PREMIUM=1
TITLE="THE COMMAND PALETTE"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You memorized 120 codes.')],[co('I type one slash.')]])
T2.CONTENT=[
 ('THE CHEAT SHEET', [[wo('A syllabus of codes.')],[co('You forgot it by Friday.')]], 'Prompt codes live on a cheat sheet you reopen every single time.', [co('Nothing sticks.')], f"{M}/codechaos.png", 1.0),
 ('THE SHIFT', [[wo('Stop memorizing prompts.')],[co('Install commands.')]], 'One named slash command does what a hundred codes never could.', [co('Slash, not syllabus.')], f"{M}/palette.png", 1.0),
 ('THE ROSTER', [[wo('Seven named agents.')],[co('Each owns one job.')]], 'CORTEX, SPECTER, STRIKER, PULSE, SENTINEL, AMPLIFY, COUNSEL.', [co('Call one by name.')], f"{M}/roster.png", 1.0),
 ('THE SYSTEM', [[wo('One command.')],[co('A whole system runs.')]], 'Slash outreach and three agents research, write and qualify in one pass.', [co('Systems, not prompts.')], f"{M}/oneflow.png", 1.0),
 ('INSTALLED', [[wo('Learn it once.')],[co('It never forgets.')]], 'Every command installs into your workspace and stays wired for good.', [co('Yours forever.')], f"{M}/install.png", 1.0),
 ('THE GATE', [[wo('It runs the whole system.')],[co('You still tap send.')]], 'Every external move parks at the HUMAN GATE for your approval.', [co('Augmented, not loose.')], f"{M}/gate.png", 1.0),
 ('THE PRICE', [[wo('A hundred codes.')],[co('A few cents a run.')]], 'Pay per token, so a full command run costs cents, not a seat license.', [co('Cents, not seats.')], f"{M}/cents.png", 1.0),
 ('THE PAYOFF', [[wo('Install today.')],[co('It ships every day after.')]], 'The command you set up once fires on demand, every day, forever.', [co('Set once, run daily.')], f"{M}/ship.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the command map?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='install the commands.',q='Which command would you install first?')
MARK2="claude"
