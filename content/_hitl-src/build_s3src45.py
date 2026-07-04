#!/usr/bin/env python3
# THE WALL AT LEVEL THREE - adaptare IG Scraped "7 Levels" in context Ultron. Built around the ONE wall:
# level 3 = Tools = the jump from answering to acting, where most people quit (not a full ladder recount).
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src45"; LIB=T2.LIB
PREMIUM=1
TITLE="THE WALL AT LEVEL THREE"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Most quit at level 3.')],[co('That is where it acts.')]])
T2.CONTENT=[
 ('THE WALL', [[wo('Level 3 is not a step.')],[co('It is a cliff.')]], 'One and two just talk. Three is where the agent starts to act, and the crowd stops climbing.', [co('This is the wall.')], f"{M}/wall.png", 1.0),
 ('THE JUMP', [[wo('Below three it answers.')],[co('At three it does.')]], 'The whole ladder pivots on one move: from typing questions to taking real actions in your stack.', [co('Talk becomes act.')], f"{M}/jump.png", 1.0),
 ('THE FREEZE', [[wo('You left every action')],[co('switched off.')]], 'Send, edit, book, ship. Real power sits behind toggles most founders are too scared to flip on.', [co('Fear keeps it a chat.')], f"{M}/freeze.png", 1.0),
 ('THE TOOLS', [[wo('A tool is a wire')],[co('into a real system.')]], 'SPECTER to the inbox, SENTINEL to the repo, AMPLIFY to the calendar. Not a chat box, a hand.', [co('Wired, not talking.')], f"{M}/tools.png", 1.0),
 ('THE GATE', [[wo('It crosses safely')],[co('because it asks first.')]], 'Every external move parks for your tap. HUMAN GATE is what makes tools safe to switch on.', [co('Nothing sends unseen.')], f"{M}/gate.png", 1.0),
 ('THE PROOF', [[wo('It stopped answering.')],[co('It started shipping.')]], 'Twelve emails sent, three pull requests merged, eight meetings booked. Real actions, not more advice.', [co('And it costs cents.')], f"{M}/proof.png", 1.0),
 ('PAST THE WALL', [[wo('Clear three and')],[co('four to seven open.')]], 'MCP, skills, subagents, agent teams. The top rungs only unlock once the agent can act.', [co('The pros climb to 7.')], f"{M}/unlock.png", 1.0),
 ('THE OPERATOR', [[wo('Ultron starts you')],[co('on the far side.')]], 'Tools, the router and the gate wired from day one. You begin where most people quit.', [co('Past the wall by default.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the climb?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this before',l2='you hit the wall.',q='Which rung are you stuck on?')
MARK2="claude"
