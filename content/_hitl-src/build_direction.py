#!/usr/bin/env python3
# DIRECTION BEATS PROMPTS - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/direction"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Your AI is not weak.')],[co('It is undirected.')]])
T2.CONTENT=[
 ('THE MISTAKE', [[wo('Everyone prompts.')],[co('Few direct.')]], 'The biggest error is asking without direction: no audience, no tone, no goal attached.', [co('Direction is the skill.')], f"{M}/mist10.png", 1.0),
 ('DIRECTION 1', [[wo('Give it the reader,')],[co('not the topic.')]], 'Founders scanning at 1.7 seconds is a brief. Write about AI is a shrug.', [co('Audience first.')], f"{M}/dir1.png", 1.0),
 ('DIRECTION 2', [[wo('Feed it your tone')],[co('from real samples.')]], 'Five best posts in, voice locked, every draft yours.', [co('Tone is data, not adjectives.')], f"{M}/dir2.png", 1.0),
 ('DIRECTION 3', [[wo('Demand hooks')],[co('in three shapes.')]], 'Confession, number, enemy: pick the winner instead of accepting the first.', [co('Options beat outputs.')], f"{M}/dir3.png", 1.0),
 ('DIRECTION 4', [[wo('One idea in,')],[co('five formats out.')]], 'Post, carousel, reel script, caption, newsletter: the multiplication is free.', [co('Never one-and-done.')], f"{M}/dir4.png", 1.0),
 ('DIRECTION 5', [[wo('Set the bar')],[co('before the draft.')]], 'Your scoring rules go in the instructions, so ranking happens before you look.', [co('The desk grades itself.')], f"{M}/dir5.png", 1.0),
 ('THE BURNOUT', [[wo('Consistency is a system,')],[co('not a mood.')]], 'Planned slots, drafted queues, gated sends: showing up became automatic.', [co('The desk holds the streak.')], f"{M}/burnout.png", 1.0),
 ('THE SHIFT9', [[wo('Stop prompting harder.')],[co('Start directing better.')]], 'Same model, same cost: direction is the whole difference.', [co('Direct, then delegate.')], f"{M}/shift9.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], f"{LIB}/cta3d-operator.png", 0.92)
T2.CLOSE=dict(l1='Save the seven directions',l2='and re-run your last ask.',q='Which direction were you missing?')
MARK2="claude"
