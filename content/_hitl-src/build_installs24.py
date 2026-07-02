#!/usr/bin/env python3
# THE POWER USER SETUP - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/installs24"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your AI is stock.')],[co('Power users install.')]])
T2.CONTENT=[
 ('STOCK', [[wo('Out of the box')],[co('it only answers.')]], 'Stock settings are training wheels. Installed right, it operates.', [co('Stock is the floor.')], f"{M}/stock.png", 1.0),
 ('PLUGINS', [[wo('A whole team')],[co('in one install.')]], 'Each plugin is a desk: research, content, deals, code. Installed once.', [co('Desks, not features.')], f"{M}/plugins.png", 1.0),
 ('SKILLS', [[wo('One line runs')],[co('the whole play.')]], 'A slash command replaces a page of prompting. Repeatable, every time.', [co('Shortcuts with depth.')], f"{M}/skills.png", 1.0),
 ('CONNECTORS', [[wo('It acts inside')],[co('your real apps.')]], 'Mail, docs, CRM, payments. No copy-paste bridge, no tab zoo.', [co('Wired, not beside.')], f"{M}/connectors.png", 1.0),
 ('THE TRIO', [[wo('Install three tonight:')],[co('marketing, design, docs.')]], 'The starter trio that covers the loudest jobs first.', [co('Twenty minutes total.')], f"{M}/three.png", 1.0),
 ('ULTRON', [[wo('Or skip the setup.')],[co('It comes installed.')]], '71 skills, 7 agents, connectors wired. Day one behaves like day one hundred.', [co('Pre-built power user.')], f"{M}/preinstalled.png", 1.0),
 ('THE GATE', [[wo('The brake comes')],[co('installed too.')]], 'Everything external waits for your tap. Power without accidents.', [co('Default: gated.')], f"{M}/gate.png", 1.0),
 ('COMPOUND', [[wo('Set once.')],[co('Collect monthly.')]], 'Corrections become rules. The setup pays rent every month after.', [co('It only gets sharper.')], f"{M}/compound.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], f"{LIB}/cta3d-builder.png", 0.92)
T2.CLOSE=dict(l1='Save the setup',l2='and install tonight.',q='Which install goes first?')
MARK2="claude"
