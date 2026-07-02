#!/usr/bin/env python3
# THE BOARD OF ADVISORS - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/advisors"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('I built a board')],[co('that knows my numbers.')]])
T2.CONTENT=[
 ('THE PROBLEM', [[wo('Advice is cheap.')],[co('Context is not.')]], 'Generic advice ignores your deals, your clients, your cash. That is why it fails.', [co('Context is the moat.')], f"{M}/context.png", 1.0),
 ('THE BOARD', [[wo('Three advisors,')],[co('three lenses.')]], 'The pricer, the editor, the strategist. Each one a skill, each one on call.', [co('Zero retainers.')], f"{M}/three.png", 1.0),
 ('THE UNLOCK', [[wo('They read')],[co('your books.')]], 'Wired into the same memory: deals, clients, numbers. They advise on your data.', [co('Your numbers, not averages.')], f"{M}/books.png", 1.0),
 ('THE PRICER', [[wo('It ran the numbers')],[co('and said: raise.')]], 'Unit economics on a real proposal. The floor was too low and it proved why.', [co('Math, not vibes.')], f"{M}/pricer.png", 1.0),
 ('THE EDITOR', [[wo('It read the draft')],[co('and said: cut half.')]], 'Overwritten proposals bury the offer. It stripped it to the spine.', [co('Less closed more.')], f"{M}/editor.png", 1.0),
 ('THE STRATEGIST', [[wo('It asked one question:')],[co('does this open doors?')]], 'Not is the deal good. Is the deal a doorway. Better filter, better clients.', [co('Doors, not dollars.')], f"{M}/strategist.png", 1.0),
 ('THE CLOSE', [[wo('The deal signed')],[co('clean.')]], 'Repriced, rewritten, requalified. One of the cleanest signatures this year.', [co('Three lenses, one win.')], f"{M}/closed.png", 1.0),
 ('THE SEAT', [[wo('Your board sits')],[co('in one chat.')]], 'On call at 2am, briefed on everything you sell, costing cents.', [co('Seat them tonight.')], f"{M}/board.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], f"{LIB}/cta3d-founder.png", 0.92)
T2.CLOSE=dict(l1='Save this and',l2='seat your board.',q='Which advisor do you need first?')
MARK2="claude"
