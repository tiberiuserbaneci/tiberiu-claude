#!/usr/bin/env python3
# OUTPUT HAS NO CEILING - IG Scraped s3src55 ("If you love [terminal] + [money]: people are making
# real money with Claude Code, $250K+ from selling automations as templates") re-told as Ultron.
# The reframe: most people point AI at saving time. Saved hours just hand back a slow human who still
# does one task at a time. Operators point the same AI at volume they could never run alone - one
# brief fanned into sixty, seven agents in parallel, 945 accounts overnight, 10x output billed in cents.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src55"; LIB=T2.LIB
PREMIUM=1
TITLE="OUTPUT HAS NO CEILING"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Most people save time.')],[co('Operators multiply output.')]])
T2.CONTENT=[
 ('THE FLAT LINE', [[wo('Saved hours')],[co('cap at the hours.')]], 'Two hours back is two hours. Output is the curve with no ceiling.', [co('Linear is the trap.')], f"{M}/curve.png", 1.0),
 ('THE SLOW HUMAN', [[wo('Time back just hands you')],[co('one slow human.')]], 'You skipped the commute and still do one task at a time.', [co('One lane, all day.')], f"{M}/serial.png", 1.0),
 ('THE MULTIPLIER', [[wo('Run the one prompt')],[co('sixty times over.')]], 'One brief fans out into sixty finished drafts, not a single one.', [co('One in, many out.')], f"{M}/fanout.png", 1.0),
 ('THE PARALLEL DESK', [[wo('Seven desks')],[co('fire at once.')]], 'Research, outbound, deals, content, code, publishing and legal, together.', [co('Not one at a time.')], f"{M}/parallel.png", 1.0),
 ('THE VOLUME', [[wo('Work nine hundred,')],[co('not fifteen.')]], 'Fifteen accounts by hand, or the whole field worked overnight.', [co('Reach you cannot.')], f"{M}/field.png", 1.0),
 ('THE BILL', [[wo('Tenfold output,')],[co('billed in cents.')]], 'The extra volume costs tokens, not a second salary on payroll.', [co('Cents, not a hire.')], f"{M}/cents.png", 1.0),
 ('THE FLOOR', [[wo('Ten times')],[co('is the floor.')]], 'What one operator ships in a day used to take a team a quarter.', [co('A team of one.')], f"{M}/gauge.png", 1.0),
 ('THE TAP', [[wo('The flood still parks')],[co('for your tap.')]], 'It can send at volume, but nothing external ships until you approve.', [co('Still your call.')], f"{M}/gate.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the volume play?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this before you',l2='cheer an hour saved.',q='What would you ship at ten times the volume?')
MARK2="claude"
