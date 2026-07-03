#!/usr/bin/env python3
# 60 MINUTES TO AN OPERATOR - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/setup"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Give me one hour.')],[co('Get back a coworker.')]])
T2.CONTENT=[
 ('MIN 0-10', [[wo('Minute 10:')],[co('the stack clicks in.')]], 'Mail, CRM, calendar, payments. Ultron plugs into what you already run.', [co('No migration.')], f"{M}/connect.png", 1.0),
 ('MIN 10-20', [[wo('Minute 20:')],[co('it knows my business.')]], 'It interviews you once: ICP, offer, pricing, the no-list.', [co('The memory is born.')], f"{M}/init.png", 1.0),
 ('MIN 20-30', [[wo('Minute 30:')],[co('it sounds like me.')]], 'Paste your best posts. Every future draft sounds like you wrote it.', [co('No AI-speak, ever.')], f"{M}/voice.png", 1.0),
 ('MIN 30-40', [[wo('Minute 40:')],[co('the handbrake is set.')]], 'Decide what runs free and what waits for your tap. Default: external waits.', [co('Permissions first.')], f"{M}/permissions.png", 1.0),
 ('MIN 40-50', [[wo('Minute 50:')],[co('first job, done.')]], 'Source 20 accounts and brief them. Watch it finish work, not answer.', [co('The first win.')], f"{M}/firsttask.png", 1.0),
 ('MIN 50-60', [[wo('Minute 60:')],[co('the digest lands.')]], 'Overnight jobs, parked approvals, hot threads. Your new morning paper.', [co('You built a coworker.')], f"{M}/digest.png", 1.0),
 ('THE COMPOUND', [[wo('Week two:')],[co('smarter than week one.')]], 'Corrections become rules. Month two beats month one on its own.', [co('Setup pays forever.')], f"{M}/compound.png", 1.0),
 ('THE OPERATOR', [[wo('One hour once.')],[co('Leverage forever.')]], 'One founder, one memory, a company that runs behind a chat.', [co('Block the hour.')], f"{M}/operator.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save the checklist',l2='and block the hour.',q='Which minute are you stuck on?')
MARK2="claude"
