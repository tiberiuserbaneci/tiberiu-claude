#!/usr/bin/env python3
# FREE IS NOT A MOAT (Google Gemini Pro free 18mo reframe) - adaptare IG/TikTok in context Ultron
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
TITLE="FREE IS NOT A MOAT"
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2googlegeminipro"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Google made Gemini free.')],[co('It changed nothing for me.')]])
T2.CONTENT=[
 ('THE TRAP', [[wo('A free tool')],[co('is not a moat.')]], 'Free for everyone is an edge for no one. The deal expires. The system does not.', [co('Free is a floor.')], f"{M}/trap.png", 1.0),
 ('THE ROUTER', [[wo('Every model,')],[co('one router.')]], 'It reads each job and rents whichever model is cheapest for it, in cents.', [co('You never pick a model.')], f"{M}/router.png", 1.0),
 ('THE CURVE', [[wo('Free plateaus.')],[co('Systems compound.')]], 'The free window ticks down. Memory, agents and data keep stacking every day.', [co('Compounds while it ticks.')], f"{M}/compound.png", 1.0),
 ('THE EYES', [[wo('A free model waits.')],[co('Mine watches.')]], 'Funding, hiring, stack, intent. The market watched for you overnight.', [co('It reads, not waits.')], f"{M}/radar.png", 1.0),
 ('THE STACK', [[wo('The model is')],[co('the bottom layer.')]], 'Swap the model like a battery. Memory, agents and the gate are the company.', [co('Swap it, keep the system.')], f"{M}/stack.png", 1.0),
 ('THE PRICE', [[wo('Priced in cents.')],[co('Not a seat.')]], 'Pay per token. A thousand rows scored costs cents, not a subscription you forget.', [co('Cents, not seats.')], f"{M}/gauge.png", 1.0),
 ('THE FIELD', [[wo('Models come and go.')],[co('You compound.')]], 'A dozen free-model waves in two years. The operating system outlives them all.', [co('It outlives the wave.')], f"{M}/field.png", 1.0),
 ('THE MOAT', [[wo('The moat is')],[co('the whole system.')]], 'Seven agents, memory, the router and the gate. A free model has none of it.', [co('One core, one operator.')], f"{M}/hub.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the system?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this before',l2='the next free deal.',q='Which free tool are you mistaking for a moat?')
MARK2="claude"
