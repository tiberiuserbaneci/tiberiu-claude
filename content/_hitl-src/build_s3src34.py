#!/usr/bin/env python3
# FOUR PARTS, ONE AGENT - adaptare IG Scraped s3src34 in context Ultron (four-primitive build)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src34"; LIB=T2.LIB
PREMIUM=1
TITLE="FOUR PARTS, ONE AGENT"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Files, commands,')],[co('memory, tools.')]])
T2.CONTENT=[
 ('THE ANATOMY', [[wo('You are chatting')],[co('with one part.')]], 'A chatbot answers. An agent wires files, commands, memory and tools.', [co('Four parts, one agent.')], f"{M}/anatomy.png", 1.0),
 ('THE FILES', [[wo('It reads your whole')],[co('project, no uploads.')]], 'Your file system is the workspace. 50 docs read into one brief.', [co('Context, not attachments.')], f"{M}/files.png", 1.0),
 ('THE COMMANDS', [[wo('One slash, the')],[co('right specialist.')]], 'Seven callable agents. Name the job and skip the busywork.', [co('Skills on command.')], f"{M}/commands.png", 1.0),
 ('THE MEMORY', [[wo('It remembers')],[co('across sessions.')]], 'ICP, pricing, pipeline, docs carried forward. A prompt starts blank.', [co('The vault never forgets.')], f"{M}/memory.png", 1.0),
 ('THE TOOLS', [[wo('It does not answer.')],[co('It acts.')]], 'Cold emails, pull requests, proposals, contracts. Done, not described.', [co('Real moves, real tools.')], f"{M}/tools.png", 1.0),
 ('THE STACK', [[wo('Four layers, not')],[co('a chat box.')]], 'Files, commands, memory and tools stacked into one operator.', [co('Stack, not chat.')], f"{M}/stack.png", 1.0),
 ('THE GATE', [[wo('Nothing fires')],[co('without your tap.')]], 'Every external action queues at the gate. You approve, it ships.', [co('Augmented, never loose.')], f"{M}/gate.png", 1.0),
 ('THE OPERATOR', [[wo('Stop chatting.')],[co('Assemble the agent.')]], 'Files, commands, memory and tools wired into one agent you run.', [co('One agent, cents per task.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the build?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='build the four parts.',q='Which part is your agent still missing?')
MARK2="claude"
