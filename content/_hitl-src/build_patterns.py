#!/usr/bin/env python3
# HOW REAL AGENTS ARE BUILT - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/patterns"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your agent is fine.')],[co('Your architecture is not.')]])
T2.CONTENT=[
 ('PATTERN 1', [[wo('Think, act, look.')],[co('Then think again.')]], 'Real agents think before every tool call and check what came back.', [co('No blind execution.')], f"{M}/react.png", 1.0),
 ('PATTERN 2', [[wo('It does not describe fixes.')],[co('It merges them.')]], 'SENTINEL does not describe the fix. It writes it, tests it, ships it.', [co('Output you can merge.')], f"{M}/codeact.png", 1.0),
 ('PATTERN 3', [[wo('Plan with the big brain.')],[co('Run with the cheap one.')]], 'Deep judgement plans once, the light tier runs each step. Cents, not seats.', [co('The router does this.')], f"{M}/plan.png", 1.0),
 ('PATTERN 4', [[wo('v1 never reaches you.')],[co('v3 does.')]], 'Outputs are ranked against your bar before you ever see them.', [co('Quality is a loop.')], f"{M}/reflect.png", 1.0),
 ('PATTERN 5', [[wo('Seven specialists')],[co('beat one giant.')]], 'Research, outbound, deals, content: one job each, done extremely well.', [co('Seven agents, handoffs.')], f"{M}/multi.png", 1.0),
 ('THE STACK', [[wo('Real systems')],[co('stack all five.')]], 'Ultron composes all five per job. You just type the goal.', [co('Composed, not chosen.')], f"{M}/stack.png", 1.0),
 ('PATTERN 6', [[wo('Pattern six:')],[co('a human on the trigger.')]], 'The most reliable design keeps one human on the only external trigger.', [co('You are the exit.')], f"{M}/gate.png", 1.0),
 ('THE OPERATOR', [[wo('Same models.')],[co('Different companies.')]], 'The same models, structured right, become a workforce.', [co('Architecture wins.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment BUILDER.')]], f"{LIB}/cta3d-builder.png", 0.92)
T2.CLOSE=dict(l1='Save the patterns',l2='and check your stack.',q='Which pattern is your setup missing?')
MARK2="claude"
