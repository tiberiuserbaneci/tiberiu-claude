#!/usr/bin/env python3
# LOW EFFORT, DONE RIGHT - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/loweffort"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('Low effort content works.')],[co('Just not the guru way.')]])
T2.CONTENT=[
 ('THE PITCH', [[wo('The gurus sell')],[co('effortless posting.')]], 'Faceless clips, recycled quotes, ten minutes a day. The feed is drowning in it.', [co('And the feed ignores it.')], f"{M}/pitch.png", 1.0),
 ('THE CATCH', [[wo('Zero effort in')],[co('reads as zero value out.')]], 'Audiences smell templates. Recycled content gets recycled reach.', [co('The shortcut is the ceiling.')], f"{M}/catchg.png", 1.0),
 ('THE REFRAME', [[wo('Low effort is an')],[co('output, not an input.')]], 'The posting should be light. The system behind it should be heavy.', [co('Move the effort upstream.')], f"{M}/reframe2.png", 1.0),
 ('THE HEAVY', [[wo('Build once:')],[co('voice, bank, cadence.')]], 'Your voice sampled, your hook bank stocked, your calendar wired. That is the real work.', [co('One weekend, honestly spent.')], f"{M}/heavy.png", 1.0),
 ('THE LIGHT', [[wo('Then daily is')],[co('one line and one tap.')]], 'The desk plans, drafts to your bar, queues at 10:00. You approve on your phone.', [co('Ten minutes, for real now.')], f"{M}/light.png", 1.0),
 ('THE DIFFERENCE', [[wo('Guru low effort skips work.')],[co('System low effort front-loads it.')]], 'Same daily minutes, opposite outcomes. The system version compounds.', [co('Effort moved, not removed.')], f"{M}/difference.png", 1.0),
 ('THE RECEIPTS', [[wo('Fourteen posts a week')],[co('from one planning line.')]], 'In my voice, on my niche, each one passing the boring test before I see it.', [co('Light hands, heavy system.')], f"{M}/receipts.png", 1.0),
 ('THE VERDICT', [[wo('Work hard once.')],[co('Post easy forever.')]], 'That is the honest version of low effort. Everything else is a template farm.', [co('Front-load, then fly.')], f"{M}/verdictl.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save the honest version',l2='of low effort.',q='Where does your effort actually go?')
MARK2="strip"
