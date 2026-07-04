#!/usr/bin/env python3
# THE FIVE YOU SKIP - adaptare IG s3src56 (5 Claude Code features nobody uses) in context Ultron.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src56"; LIB=T2.LIB
PREMIUM=1
TITLE="THE FIVE YOU SKIP"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Five Claude Code features')],[co('you never turned on.')]])
T2.CONTENT=[
 ('SKILLS', [[wo('Write the recipe once.')],[co('It runs on cue.')]], 'A named playbook loads the instant its trigger shows up. Stop pasting the same brief.', [co('Your plays, on tap.')], f"{M}/skills.png", 1.0),
 ('SUBAGENTS', [[wo('Hand off a scoped job.')],[co('It runs in parallel.')]], 'A fresh agent takes one task in its own context and reports back. Your thread stays clean.', [co('Three minds at once.')], f"{M}/subagents.png", 1.0),
 ('HOOKS', [[wo('It stops itself')],[co('before it sends.')]], 'A hook fires the approval gate automatically. Nothing external moves without your tap.', [co('Guardrails, built in.')], f"{M}/hooks.png", 1.0),
 ('SLASH COMMANDS', [[wo('Call an operator')],[co('by name.')]], 'Type one command and the right agent is already working. No menus, no setup.', [co('One keystroke each.')], f"{M}/commands.png", 1.0),
 ('CONNECTORS', [[wo('Plug in')],[co('your whole stack.')]], 'Inbox, deals, docs and calendar wired into one core. It works your real tools.', [co('Reads your real data.')], f"{M}/connect.png", 1.0),
 ('MODEL TIER', [[wo('The cheap model,')],[co('unless it cannot.')]], 'Each job is read and routed to the smallest tier that can do it. You pay cents.', [co('Cents, not dollars.')], f"{M}/router.png", 1.0),
 ('MEMORY', [[wo('It never forgets')],[co('your company.')]], 'ICP, pricing, pipeline and docs live in one vault every agent reads. Set it once.', [co('Nothing resets.')], f"{M}/memory.png", 1.0),
 ('THE STACK', [[wo('Five switches on')],[co('is an operator.')]], 'Wire all five and you stop chatting with a tool. You are running a company.', [co('One login, full stack.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the full setup?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='flip all five on.',q='Which one have you never used?')
MARK2="claude"
