#!/usr/bin/env python3
# THE NEW LEVERAGE - adaptare Naval ("there are only 4 ways to get rich: labor, capital, code, media")
# in context Ultron: the new leverage is agents. One operator gets code + media + labor leverage
# without a team - permissionless, run by one person, at cents. The operator IS the leverage.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s2navalravikantsai"; LIB=T2.LIB
PREMIUM=1
TITLE="THE NEW LEVERAGE"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Four kinds of leverage.')],[co('Agents are the fifth.')]])
T2.CONTENT=[
 ('THE FOUR', [[wo('Labor, capital,')],[co('code and media.')]], 'The classic four each needed a team, a check, or an audience a solo founder did not have.', [co('Every one gatekept.')], f"{M}/fourways.png", 1.0),
 ('THE FIFTH', [[wo('One prompt in.')],[co('Real leverage out.')]], 'One operator routes work to a roster of agents. Code, media and labor leverage, no headcount to hire.', [co('Permissionless leverage.')], f"{M}/agents.png", 1.0),
 ('THE MATH', [[wo('One person.')],[co("A whole team's output.")]], 'The operator is the leverage now. One login produces the work a nine-person team used to grind out.', [co('9x, one seat.')], f"{M}/multiplier.png", 1.0),
 ('THE STACK', [[wo('Code, media, labor.')],[co('Stacked under you.')]], 'Sentinel ships the code, Pulse makes the media, Specter runs the outreach. No team to manage.', [co('No headcount.')], f"{M}/stack.png", 1.0),
 ('THE EDGE', [[wo('It saw the opening')],[co('before the market.')]], 'Cortex watches funding, hiring and intent so a one-person company moves before the crowd does.', [co('First to move.')], f"{M}/market.png", 1.0),
 ('THE VOLUME', [[wo('240 touches.')],[co('One afternoon, solo.')]], 'Outreach, follow-ups and posts at a volume a solo founder could never hit by hand. Cents each.', [co('Cents per run.')], f"{M}/output.png", 1.0),
 ('THE ROSTER', [[wo('Seven agents.')],[co('One shared memory.')]], 'Cortex, Specter, Striker, Pulse, Sentinel, Amplify and Counsel all draw from one core, and every send waits for your tap.', [co('Memory plus the gate.')], f"{M}/roster.png", 1.0),
 ('THE COST', [[wo('A team cost thousands.')],[co('This runs on cents.')]], 'The leverage that used to need payroll now runs per token on a card. You pay for the work, not the seats.', [co('Cents, not salaries.')], f"{M}/shift.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='build the leverage.',q='Which leverage would you wire first?')
MARK2="claude"
