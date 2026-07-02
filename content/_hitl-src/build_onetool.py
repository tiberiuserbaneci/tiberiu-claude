#!/usr/bin/env python3
# FIVE ASSISTANTS, NO MEMORY - adaptare IG Scraped in context Ultron (generat de adapt_build.py)
import importlib.util
spec=importlib.util.spec_from_file_location("T2","/home/user/tiberiu-claude/content/_hitl-src/build_team_3d.py")
T2=importlib.util.module_from_spec(spec); spec.loader.exec_module(T2)
wo=lambda s:(s,T2.WHITE); co=lambda s:(s,T2.CORAL); mu=lambda s:(s,T2.MUTED)
M="/home/user/tiberiu-claude/content/_hitl-src/models_clay/onetool"; LIB=T2.LIB
PREMIUM=1
T2.ACCENT=(204, 120, 92); T2.CORAL=T2.ACCENT
T2.OBJ_THR=30
T2.COVER=dict(head=[[wo('You do not need five assistants.')],[co('You need one that remembers.')]])
T2.CONTENT=[
 ('THE LIST', [[wo('Inbox tool, calendar tool,')],[co('meeting tool, note tool.')]], 'The listicles sell you a specialist for every slice of your day.', [co('Five logins, five bills.')], f"{M}/list7.png", 1.0),
 ('THE SEAMS', [[wo('None of them')],[co('know the others exist.')]], 'The inbox tool cannot see the deal. The meeting tool never met your pipeline.', [co('You are the integration.')], f"{M}/seams.png", 1.0),
 ('THE COST', [[wo('Five memories')],[co('means no memory.')]], 'Your context lives nowhere, so you re-explain yourself to software all day.', [co('Amnesia at scale.')], f"{M}/cost7.png", 1.0),
 ('THE DESK', [[wo('One desk holds')],[co('inbox, calendar, pipeline.')]], 'Mail read, meetings booked, follow-ups drafted: one memory underneath all of it.', [co('One brain, many hands.')], f"{M}/desk7b.png", 1.0),
 ('THE COMPOUND', [[wo('Tool five forgets you.')],[co('The desk knows the thread.')]], 'The follow-up references the call, the call references the deal, the deal references the history.', [co('Context is the feature.')], f"{M}/compound7.png", 1.0),
 ('THE SLEEP', [[wo('It clears the inbox')],[co('while you sleep.')]], 'Triage at 23:00, drafts by 06:00, digest at 07:00. In your voice, parked for your tap.', [co('The night shift, unified.')], f"{M}/sleep7.png", 1.0),
 ('THE PRICE', [[wo('Five subscriptions')],[co('became one meter.')]], 'Cents per run instead of a stack of seats.', [co('The math got simple.')], f"{M}/price7.png", 1.0),
 ('THE RULE', [[wo('Never add a tool')],[co('that cannot share memory.')]], 'That single filter kills most of the listicle.', [co('Memory or nothing.')], f"{M}/rule7b.png", 1.0),
]
T2.CTA=("SAVE THIS", [[wo('Want the playbook?')],[co('comment FOUNDER.')]], f"{LIB}/cta3d-founder.png", 0.92)
T2.CLOSE=dict(l1='Save this before',l2='you add tool number six.',q='How many assistants do you juggle?')
MARK2="strip"
