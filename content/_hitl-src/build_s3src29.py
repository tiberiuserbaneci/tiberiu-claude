#!/usr/bin/env python3
# THE STARTER LOADOUT - adaptare IG Scraped s3src29 in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src29"; LIB=T2.LIB
PREMIUM=1
TITLE="THE STARTER LOADOUT"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('The 24 things')],[co('you install first.')]])
T2.CONTENT=[
 ('THE LOADOUT', [[wo('24 installs.')],[co('Three layers.')]], 'Eight skills, eight plug-ins, eight servers. The exact day-one kit.', [co('Save now, install later.')], f"{M}/loadout.png", 1.0),
 ('THE THREE LAYERS', [[wo('Skill, plug-in,')],[co('or server?')]], 'A recipe, a crew, a cable. Each layer adds a different thing.', [co('Know what you add.')], f"{M}/layers.png", 1.0),
 ('LAYER ONE. SKILLS', [[wo('One word runs')],[co('the whole recipe.')]], 'A skill is a shortcut. One command runs a workflow you would retype.', [co('Eight recipes, day one.')], f"{M}/skills.png", 1.0),
 ('LAYER TWO. PLUG-INS', [[wo('One install,')],[co('a whole crew.')]], 'A plug-in drops a bundle at once. gstack alone is 20+ tools.', [co('Install the team.')], f"{M}/plugins.png", 1.0),
 ('LAYER THREE. MCP', [[wo('Wired into')],[co('your real tools.')]], 'MCP servers connect Ultron to Notion, Slack, GitHub and Stripe, live.', [co('It acts where you work.')], f"{M}/connectors.png", 1.0),
 ('THE INSTALL', [[wo('The whole kit')],[co('in one pass.')]], 'One loadout file. One install. Twenty-four things land together.', [co('24 of 24, done.')], f"{M}/install.png", 1.0),
 ('THE UNLOCK', [[wo('Recipes, crews,')],[co('cables compound.')]], 'Alone each is a tool. Together they are one operator that ships.', [co('The layers stack.')], f"{M}/unlock.png", 1.0),
 ('SAVE THE KIT', [[wo('The exact')],[co('day-one sheet.')]], 'Screenshot this. Install these twenty-four first and ignore the rest.', [co('Your starter loadout.')], f"{M}/ledger.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the full kit?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='equip your operator.',q='Which layer are you missing right now?')
MARK2="claude"
