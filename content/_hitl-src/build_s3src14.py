#!/usr/bin/env python3
# YOU ARE THE INTEGRATION LAYER - adaptare IG Scraped (s3src14) in context Ultron
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src14"; LIB=T2.LIB
PREMIUM=1
TITLE="YOU ARE THE INTEGRATION LAYER"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You are the')],[co('integration layer.')]])
T2.CONTENT=[
 ('THE PROBLEM', [[wo('Six tools.')],[co('Zero of them talk.')]], 'Apollo, a CRM, a sheet, a calendar, an inbox. You are the cable between every one.', [co('You are the glue.')], f"{M}/broken.png", 1.0),
 ('THE FIX', [[wo('Plug them in once.')],[co('No API keys.')]], 'Connect Apollo and Gmail as native connectors. OAuth, not glue code. One project holds them.', [co('Two clicks, wired.')], f"{M}/socket.png", 1.0),
 ('THE PIPELINE', [[wo('One project runs')],[co('the whole line.')]], 'Research, write, send, reply, book. Each stage handed to the agent that owns it.', [co('It runs itself.')], f"{M}/flow.png", 1.0),
 ('THE FUNNEL', [[wo('1,248 leads in.')],[co('16 deals out.')]], 'Contacted, replied, booked, won. Every stage measured, the line reports its own math.', [co('47 meetings booked.')], f"{M}/funnel.png", 1.0),
 ('THE SCALE', [[wo('It worked 1,248 leads.')],[co('You slept.')]], 'One week of outbound. 3,842 emails sent, 342 replies, 47 meetings, all logged.', [co('47 booked, hands off.')], f"{M}/field.png", 1.0),
 ('THE RATE', [[wo('342 replies')],[co('from 3,842 sends.')]], 'An 8.9 percent reply rate, held steady while it ran unattended for seven days.', [co('Steady, not lucky.')], f"{M}/gauge.png", 1.0),
 ('THE GATE', [[wo('Nothing sends')],[co('without your tap.')]], 'Every draft parks at the gate. You approve the batch, then it goes. Augmented, never loose.', [co('Your name, your call.')], f"{M}/gate.png", 1.0),
 ('THE CHOICE', [[wo('Seven tabs,')],[co('or one operator.')]], 'Keep being the integration layer, or install the operator that is the integration layer for you.', [co('Stop being the wire.')], f"{M}/split.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the full build?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and stop',l2='being the wire.',q='Which tool are you still gluing by hand?')
MARK2="claude"
