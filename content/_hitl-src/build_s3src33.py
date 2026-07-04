#!/usr/bin/env python3
# ENGINEER THE AGENT NOT THE PROMPT - adaptare IG Scraped s3src33 in context Ultron
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src33"; LIB=T2.LIB
PREMIUM=1
TITLE="ENGINEER THE AGENT NOT THE PROMPT"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Prompting is dead.')],[co('Here is what replaced it.')]])
T2.CONTENT=[
 ('THE SHIFT', [[wo('You stopped writing prompts.')],[co('The config writes them.')]], 'Tourists re-type the same prompt. Operators set it once and never again.', [co('Set it once.')], f"{M}/deadloop.png", 1.0),
 ('SKILL 01', [[wo('Context engineering')],[co('is the new backbone.')]], 'Your ULTRON.md holds the rules, the voice and the docs. Every agent reads it.', [co('One file runs it all.')], f"{M}/context.png", 1.0),
 ('SKILL 02', [[wo('Package a workflow once.')],[co('Reuse it on every agent.')]], 'Wrap any repeatable job into a skill. Every agent can call it on demand.', [co('Build once, run always.')], f"{M}/skills.png", 1.0),
 ('SKILL 03', [[wo('One plug for')],[co('every tool you own.')]], 'MCP connects your agent to your whole stack. 10,000 servers and counting.', [co('Wire in anything.')], f"{M}/mcp.png", 1.0),
 ('SKILL 04', [[wo('Bundle your whole setup.')],[co('Ship it in one command.')]], 'Plugins and markets let you install a full operator, not glue tabs together.', [co('Install, do not assemble.')], f"{M}/market.png", 1.0),
 ('SKILL 05', [[wo('The agent polices')],[co('its own quality.')]], 'Hooks and slash commands gate every step, so you stop babysitting the output.', [co('It checks itself.')], f"{M}/gate.png", 1.0),
 ('SKILL 06', [[wo('Stop running one agent.')],[co('Run a whole fleet.')]], 'Subagents split the brief across seven specialists working in parallel.', [co('Seven, not one.')], f"{M}/teams.png", 1.0),
 ('SKILL 07', [[wo('It writes its own')],[co('workflow to scale.')]], 'Dynamic workflows spawn hundreds of runs from one plain-English brief.', [co('Hundreds at once.')], f"{M}/flows.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the operator stack?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='engineer the agent.',q='Which skill are you still missing?')
MARK2="claude"
