#!/usr/bin/env python3
# THE SMMA THAT RUNS ON CENTS - adaptare IG Scraped (s3src51) in context Ultron
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src51"; LIB=T2.LIB
PREMIUM=1
TITLE="THE SMMA THAT RUNS ON CENTS"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Ten client retainers.')],[co('Run by cents, not a team.')]])
T2.CONTENT=[
 ('THE CEILING', [[wo('By hand you cap out')],[co('at four clients.')]], 'Every retainer wants weekly posts. You grind them by hand and growth stops.', [co('Content is the ceiling.')], f"{M}/ceiling.png", 1.0),
 ('THE ROSTER', [[wo('Ten client workspaces,')],[co('each shipping weekly.')]], 'Every client is a workspace with its own brand, memory and voice inside Ultron.', [co('One agency, many brands.')], f"{M}/roster.png", 1.0),
 ('THE INTAKE', [[wo('New client, profiled')],[co('in a single pass.')]], 'CORTEX reads their brand, past posts, offer and ICP into one saved profile.', [co('Onboard in minutes.')], f"{M}/intake.png", 1.0),
 ('THE PRODUCTION', [[wo('Posts written')],[co('in each brand voice.')]], 'PULSE drafts carousels and captions per client, matched to their real voice.', [co('No designer, no wait.')], f"{M}/production.png", 1.0),
 ('THE CALENDAR', [[wo('Scheduled across')],[co('every channel.')]], 'AMPLIFY queues each post per channel and time zone, a full week per client.', [co('Set once, ships itself.')], f"{M}/calendar.png", 1.0),
 ('THE REPORT', [[wo('The monthly report')],[co('writes itself.')]], 'Reach, saves and engagement per client, packaged and sent without you.', [co('Clients stay longer.')], f"{M}/report.png", 1.0),
 ('THE MARGIN', [[wo('You bill thousands,')],[co('it costs cents.')]], 'A five thousand dollar designer and a tool stack become cents per post.', [co('The margin is the moat.')], f"{M}/margin.png", 1.0),
 ('THE OPERATOR', [[wo('Ten clients ship')],[co('on your one tap.')]], 'Every post parks at the gate. You approve, Ultron publishes across the roster.', [co('You run it all, gated.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the agency build?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='run the agency on cents.',q='How many clients could you carry with none of the team?')
MARK2="claude"
