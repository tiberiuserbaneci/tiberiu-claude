#!/usr/bin/env python3
# THE 500K CONTENT DESK - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/contentdesk"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(200, 70, 35); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('My content team never sleeps')],[co('and never meets.')]])
T2.CONTENT=[
 ('SKILL 1', [[wo('Monday, 07:00.')],[co('The week plans itself.')]], 'One line in, 14 slots out, spread across channels at 10:00 local.', [co('Zero coordinators.')], f"{M}/cal.png", 1.0),
 ('SKILL 2', [[wo('Three hooks fight.')],[co('I crown one.')]], 'Three angles per post from your proven hook bank. You pick the winner.', [co('A/B/C, one tap.')], f"{M}/hooks.png", 1.0),
 ('SKILL 3', [[wo('It writes like me')],[co('on my best day.')]], 'Sampled from your real posts, banned words enforced, ranked before you read.', [co('No AI-speak.')], f"{M}/voice.png", 1.0),
 ('SKILL 4', [[wo('One brief.')],[co('Five channels, native.')]], 'LinkedIn long-form, caption, carousel, newsletter, script. Same brief.', [co('Native per channel.')], f"{M}/repurpose.png", 1.0),
 ('SKILL 5', [[wo('99.2% inboxed.')],[co('Unseen content is rent.')]], 'Warm domains, ramped sends, 99.2% placement. Content nobody reads is free.', [co('Delivery is the job.')], f"{M}/inbox.png", 1.0),
 ('THE DESK', [[wo('No standups.')],[co('The desk never meets.')]], 'The whole pipeline runs behind one chat with one memory of your brand.', [co('PULSE owns it.')], f"{M}/desk.png", 1.0),
 ('THE GATE', [[wo('My feed, my thumb.')],[co('Nothing posts alone.')]], 'Every draft parks first. You approve the batch in one read.', [co('Your feed, your call.')], f"{M}/gate.png", 1.0),
 ('THE MATH', [[wo('The desk bills in cents.')],[co('Not in Mondays.')]], 'Planner, writer, designer, distributor: one subscription, metered by use.', [co('Payroll: zero.')], f"{M}/math.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save the desk',l2='and steal the setup.',q='Which of the five would you run first?')
MARK2="claude"
