#!/usr/bin/env python3
# THREE PARTS, NO CODE - adaptare IG Scraped (s3src11) in context Ultron
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src11"; LIB=T2.LIB
PREMIUM=1
TITLE="THREE PARTS, NO CODE"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('No code, no engineer.')],[co('A real agent in 20 min.')]])
T2.CONTENT=[
 ('CHAT VS AGENT', [[wo('Your chatbot talks.')],[co('It never acts.')]], 'You ask, it answers, then it waits. The work is still sitting on your desk.', [co('Talking is not doing.')], f"{M}/chat.png", 1.0),
 ('THE FORMULA', [[wo('An agent is a chat')],[co('plus three parts.')]], 'Tools it calls itself, memory that persists, a loop that runs until done.', [co('Add all three.')], f"{M}/parts.png", 1.0),
 ('PART ONE', [[wo('It reaches for')],[co('its own tools.')]], 'Search, email, drafting, code, calendar. No copy-paste between tabs.', [co('It does not ask you.')], f"{M}/tools.png", 1.0),
 ('PART TWO', [[wo('It never forgets')],[co('what you told it.')]], 'ICP, pricing, your voice, written once and carried into every session.', [co('Explain it once.')], f"{M}/memory.png", 1.0),
 ('PART THREE', [[wo('It runs until')],[co('the job is done.')]], 'Plan, act, check, repeat. It stops when the work is finished, not you.', [co('You stop clicking.')], f"{M}/loop.png", 1.0),
 ('ZERO CODE', [[wo('You describe it')],[co('in plain English.')]], 'One paragraph of instruction is the whole build. No repo, no deploy.', [co('Not an engineer.')], f"{M}/nocode.png", 1.0),
 ('PICK THE JOB', [[wo('Same build.')],[co('Seven jobs.')]], 'Research, content, code, outbound, deals, legal. Switch on the one you need.', [co('One today, another tomorrow.')], f"{M}/pick.png", 1.0),
 ('BUILT AND GATED', [[wo('Live in twenty')],[co('minutes, gated.')]], 'Assembled and running, and every external move still waits for your tap.', [co('Still your call.')], f"{M}/live.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the no-code build?')],[co('comment BUILDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-builder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='build one this weekend.',q='Which agent would you switch on first?')
MARK2="claude"
