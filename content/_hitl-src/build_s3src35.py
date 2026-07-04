#!/usr/bin/env python3
# THE ATOMIZER - adaptare IG Scraped (one idea in, every channel out) in context Ultron.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src35"; LIB=T2.LIB
PREMIUM=1
TITLE="THE ATOMIZER"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('One idea in.')],[co('Every channel out.')]])
T2.CONTENT=[
 ('THE FAN-OUT', [[wo('One note in.')],[co('Seven outputs.')]], 'A post, a thread, a newsletter, an image and scripts, from a single idea.', [co('One in, many out.')], f"{M}/fanout.png", 1.0),
 ('THE BRIEF', [[wo('PULSE asks first,')],[co('then writes.')]], 'It turns your half-formed note into a clean brief, ready to write.', [co('Sharp, not vague.')], f"{M}/brief.png", 1.0),
 ('THE MASTER', [[wo('One master piece,')],[co('every claim sourced.')]], 'CORTEX pulls real web data, PULSE writes one hooked master article.', [co('Real, not made up.')], f"{M}/master.png", 1.0),
 ('THE ATOMIZE', [[wo('The master splits')],[co('into every format.')]], 'One article becomes a post, a thread, a newsletter, an image and a reel.', [co('Sized per channel.')], f"{M}/atomize.png", 1.0),
 ('THE VOICE', [[wo('Every format,')],[co('your voice.')]], 'A 40-word thread and a 1,200-word newsletter keep the same cadence.', [co('Multiplied, not diluted.')], f"{M}/voice.png", 1.0),
 ('THE SCHEDULE', [[wo('AMPLIFY slots')],[co('each one.')]], 'Every format lands on its best channel, day and time zone.', [co('Right place, right time.')], f"{M}/schedule.png", 1.0),
 ('THE GATE', [[wo('Nothing ships')],[co('without your tap.')]], 'Every draft parks at the gate. One tap sends it live.', [co('Still your call.')], f"{M}/gate.png", 1.0),
 ('THE ENGINE', [[wo('Write once.')],[co('Ship everywhere.')]], 'PULSE writes, AMPLIFY publishes, and it all runs from one login.', [co('One idea, everywhere.')], f"{M}/engine.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and turn',l2='one idea into ten.',q='What is the one idea you would fan out first?')
MARK2="claude"
