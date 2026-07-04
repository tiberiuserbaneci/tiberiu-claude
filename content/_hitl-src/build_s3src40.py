#!/usr/bin/env python3
# ANATOMY OF A REPLY - adaptare IG Scraped (s3src40) in context Ultron. Angle: the outreach MESSAGE
# copy itself - what makes a cold message get a reply, SPECTER writing it in your voice.
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/s3src40"; LIB=T2.LIB
PREMIUM=1
TITLE="ANATOMY OF A REPLY"
T2.ACCENT=(212, 162, 127); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('One cold message.')],[co('One reply in an hour.')]])
T2.CONTENT=[
 ('THE DEAD DM', [[wo('"Hi, would love')],[co('to connect."')]], 'The template everyone sends reads like a template, so it dies unread in the request folder.', [co('Delete the opener.')], f"{M}/deadtemplate.png", 1.0),
 ('THE ANATOMY', [[wo('Four lines are')],[co('the whole message.')]], 'Trigger, one line of relevance, a question not a pitch, then stop. Nothing else earns a reply.', [co('Structure, not charm.')], f"{M}/anatomy.png", 1.0),
 ('THE TRIGGER', [[wo('Open on a real,')],[co('recent event.')]], 'A funding round, a hire, a launch from last week. Proof you looked, inside the first six words.', [co('No trigger, no send.')], f"{M}/trigger.png", 1.0),
 ('THE RELEVANCE', [[wo('One line ties')],[co('them to you.')]], 'Their event, then the single sentence that makes your reach out obvious. A bridge, not a brochure.', [co('One line, not ten.')], f"{M}/bridge.png", 1.0),
 ('THE ASK', [[wo('End on a question,')],[co('never a pitch.')]], 'A pitch asks them to work. A short question asks them to reply. The question wins every time.', [co('Ask, do not sell.')], f"{M}/ask.png", 1.0),
 ('THE LENGTH', [[wo('Forty words,')],[co('then stop typing.')]], 'Long messages read as a mass send. Under forty words reads like a person who actually wrote it.', [co('Short gets read.')], f"{M}/length.png", 1.0),
 ('THE WRITER', [[wo('SPECTER writes it')],[co('in your voice.')]], 'Trigger, relevance, question, short. Assembled from your real cadence, not a generic template.', [co('Your words, your reply.')], f"{M}/writer.png", 1.0),
 ('THE REPLY', [[wo('Sent once.')],[co('Answered in an hour.')]], 'The right four lines turn a cold name into a live thread. That is the entire outreach game.', [co('A reply, not a read.')], f"{M}/reply.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the four lines?')],[co('comment OPERATOR.')]], "/home/user/tiberiu-claude/content/_hitl-src/_templates/cta/cta-operator.png", 0.82)
T2.CLOSE=dict(l1='Save this and',l2='send the four lines.',q='When did a template ever get you a reply?')
MARK2="claude"
