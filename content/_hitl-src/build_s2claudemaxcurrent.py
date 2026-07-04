#!/usr/bin/env python3
# PLAN VS SYSTEM (Claude Max 6-mo deal reframe) - adaptare IG/TikTok in context Ultron
# Reframe: a bigger plan gives you more chat; a system gives you output. Ultron = pay-per-token
# cents, no seat/no cap, agents + memory + the gate. (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2claudemaxcurrent"; LIB=T2.LIB
PREMIUM=1
TITLE="PLAN VS SYSTEM"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('More usage limits.')],[co('Still just a chat box.')]])
T2.CONTENT=[
 ('THE SPLIT', [[wo('A plan gives you chat.')],[co('A system gives output.')]], 'A bigger plan is more messages in one box. A system turns each one into shipped work.', [co('Chat is not output.')], f"{M}/plan.png", 1.0),
 ('PAY PER TOKEN', [[wo('No seat. No cap.')],[co('Only the runs you use.')]], 'No monthly seat, no usage ceiling. You pay cents per run, for the runs that actually fired.', [co('Cents, not a subscription.')], f"{M}/meter.png", 1.0),
 ('THE OUTPUT', [[wo('It does not answer.')],[co('It ships.')]], 'Emails sent, briefs written, deals scored, code merged. A stack of done work while you were out.', [co('Results, not replies.')], f"{M}/output.png", 1.0),
 ('THE ROSTER', [[wo('One chat.')],[co('Seven agents behind it.')]], 'Research, outbound, deals, content, code, publishing, legal. Each a named agent owning its job.', [co('A roster, not a bot.')], f"{M}/graph.png", 1.0),
 ('THE EYES', [[wo('It saw the round')],[co('before I did.')]], 'Funding, hiring, stack, intent. It watches the web overnight and hands you the signal first.', [co('Overnight, every night.')], f"{M}/radar.png", 1.0),
 ('NO CEILING', [[wo('A plan runs out.')],[co('A system scales.')]], 'A seat caps your month. Pay-per-token scales run by run, from ten to ten thousand, same cents.', [co('Scale, never a wall.')], f"{M}/gauge.png", 1.0),
 ('THE RUNS', [[wo('Ten thousand runs.')],[co('Cents each.')]], 'Every dot is one run that happened. You pay for the ones that fired, nothing for the rest.', [co('You pay for work done.')], f"{M}/field.png", 1.0),
 ('ONE SYSTEM', [[wo('Memory. Agents.')],[co('The gate. One core.')]], 'One memory feeds every agent, and every external move waits for your tap at the gate.', [co('A system, not a seat.')], f"{M}/hub.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the system?')],[co('comment FOUNDER.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-founder.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='stop paying for a bigger chat.',q='A bigger plan, or a system that ships?')
MARK2="claude"
