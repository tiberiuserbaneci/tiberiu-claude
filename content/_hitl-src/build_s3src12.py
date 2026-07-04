#!/usr/bin/env python3
# THE LAST RUNG IS A TEAM - adaptare IG Scraped "7 Levels of Claude Code" in context Ultron.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src12"; LIB=T2.LIB
PREMIUM=1
TITLE="THE LAST RUNG IS A TEAM"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You type one prompt.')],[co('The ceiling is a team.')]])
T2.CONTENT=[
 ('THE CLIMB', [[wo('Seven rungs.')],[co('Most stop at three.')]], 'Prompt, context, tools, MCP, skills, subagents, a team. The climb has a top.', [co('The top runs itself.')], f"{M}/ladder.png", 1.0),
 ('LEVEL 1', [[wo('You type. It answers.')],[co('One question at a time.')]], 'Where everyone meets Claude, and where most quietly get stuck.', [co('Powerful. Still solo.')], f"{M}/prompt.png", 1.0),
 ('LEVEL 2', [[wo('Hand it a CLAUDE.md.')],[co('Now it knows your world.')]], 'Your code, your docs, your rules. It works off your real project, not a guess.', [co('Context beats cleverness.')], f"{M}/context.png", 1.0),
 ('LEVEL 3', [[wo('Tools are the wall.')],[co('Most climbers stop here.')]], 'Read, edit, run, search. Real actions, but still one worker doing one thing.', [co('The wall is not the top.')], f"{M}/toolwall.png", 1.0),
 ('LEVEL 4', [[wo('MCP plugs it')],[co('into your stack.')]], 'Your CRM, database, inbox and calendar become tools it can actually use.', [co('It touches real systems.')], f"{M}/mcp.png", 1.0),
 ('LEVEL 5', [[wo('Skills it can reuse.')],[co('Not prompts it forgets.')]], 'Package a workflow once. It runs the same audit, the same score, every time.', [co('Repeatable, not one-off.')], f"{M}/skills.png", 1.0),
 ('LEVEL 6', [[wo('One task, split')],[co('across many workers.')]], 'Subagents run in parallel, each on a slice, then fold the work back into one.', [co('Wide, not just deep.')], f"{M}/subagents.png", 1.0),
 ('LEVEL 7', [[wo('The last rung')],[co('is a team.')]], 'Seven named agents, a router that picks each one, your tap on every send.', [co('That team is Ultron.')], f"{M}/team.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the whole climb?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='climb past the wall.',q='Which rung are you stuck on?')
MARK2="claude"
